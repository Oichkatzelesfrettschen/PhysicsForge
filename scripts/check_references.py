"""
Validate cross-references, equation labels, and bibliography usage across the
LaTeX synthesis tree.
"""

from __future__ import annotations

import argparse
import re
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Sequence

try:
    from scripts.common import resolve_base_dir
except ImportError:  # pragma: no cover
    from common import resolve_base_dir  # type: ignore


LABEL_PATTERN = re.compile(r"\\label\{([^}]+)\}")
REF_PATTERN = re.compile(r"\\(?:[cC]?[Rr]ef|eqref)\{([^}]+)\}")
CITE_PATTERN = re.compile(r"\\(?:[Tt]ext)?cite[a-zA-Z]*\{([^}]+)\}")
INPUT_PATTERN = re.compile(r"\\(?:input|include)\{([^}]+)\}")


@dataclass
class Occurrence:
    file: Path
    line: int

    def __str__(self) -> str:
        return f"{self.file}:{self.line}"


def _matches_skip(path: Path, skip_tokens: Sequence[str]) -> bool:
    lowered = str(path).lower()
    return any(token in lowered for token in skip_tokens)


def _collect_tex_files(root: Path, include_modules: bool, skip_tokens: Sequence[str]) -> list[Path]:
    patterns = ("*.tex", "*.ltx") if include_modules else ("*.tex",)
    tex_files: list[Path] = []
    for pattern in patterns:
        for candidate in root.rglob(pattern):
            if _matches_skip(candidate, skip_tokens):
                continue
            tex_files.append(candidate)
    return sorted({p.resolve() for p in tex_files})


def _split_keys(raw: str) -> Iterable[str]:
    for part in raw.split(","):
        key = part.strip()
        if key:
            yield key


def _scan_labels(path: Path) -> set[str]:
    text = path.read_text(encoding="utf-8", errors="strict")
    return set(LABEL_PATTERN.findall(text))


def _scan_references(path: Path) -> dict[str, list[Occurrence]]:
    references: dict[str, list[Occurrence]] = defaultdict(list)
    for idx, line in enumerate(path.read_text(encoding="utf-8", errors="strict").splitlines(), start=1):
        for match in REF_PATTERN.findall(line):
            for key in _split_keys(match):
                references[key].append(Occurrence(path, idx))
    return references


def _scan_citations(path: Path) -> dict[str, list[Occurrence]]:
    citations: dict[str, list[Occurrence]] = defaultdict(list)
    for idx, line in enumerate(path.read_text(encoding="utf-8", errors="strict").splitlines(), start=1):
        for match in CITE_PATTERN.findall(line):
            for key in _split_keys(match):
                citations[key].append(Occurrence(path, idx))
    return citations


def _scan_inputs(path: Path) -> dict[str, list[Occurrence]]:
    includes: dict[str, list[Occurrence]] = defaultdict(list)
    for idx, line in enumerate(path.read_text(encoding="utf-8", errors="strict").splitlines(), start=1):
        for match in INPUT_PATTERN.findall(line):
            includes[match.strip()].append(Occurrence(path, idx))
    return includes


def _load_bibliography_keys(bib_path: Path) -> set[str]:
    if not bib_path.exists():
        return set()
    keys: set[str] = set()
    pattern = re.compile(r"@\w+\{([^,]+),")
    for line in bib_path.read_text(encoding="utf-8", errors="strict").splitlines():
        match = pattern.search(line)
        if match:
            keys.add(match.group(1).strip())
    return keys


def validate_references(
    tex_root: Path,
    bib_path: Path,
    include_modules: bool,
    ignore_missing_inputs: Sequence[str],
    skip_tokens: Sequence[str],
) -> int:
    files = _collect_tex_files(tex_root, include_modules, skip_tokens)
    labels: dict[str, Path] = {}
    duplicates: dict[str, list[Path]] = defaultdict(list)
    references: dict[str, list[Occurrence]] = defaultdict(list)
    citations: dict[str, list[Occurrence]] = defaultdict(list)
    includes: dict[str, list[Occurrence]] = defaultdict(list)

    for tex in files:
        file_labels = _scan_labels(tex)
        for label in file_labels:
            if label in labels:
                duplicates[label].extend([labels[label], tex])
            else:
                labels[label] = tex
        for key, occs in _scan_references(tex).items():
            references[key].extend(occs)
        for key, occs in _scan_citations(tex).items():
            citations[key].extend(occs)
        for key, occs in _scan_inputs(tex).items():
            includes[key].extend(occs)

    bib_keys = _load_bibliography_keys(bib_path)

    status = 0

    undefined_refs = sorted(set(references) - set(labels))
    if undefined_refs:
        status = 1
        print("[ERROR] Undefined references:")
        for ref in undefined_refs:
            locations = ", ".join(str(o) for o in references[ref])
            print(f"  {ref} -> {locations}")

    duplicate_entries = {key: paths for key, paths in duplicates.items() if len(paths) > 1}
    if duplicate_entries:
        status = 1
        print("\n[ERROR] Duplicate labels:")
        for label, paths in duplicate_entries.items():
            unique = sorted({str(p) for p in paths})
            print(f"  {label} defined in: {', '.join(unique)}")

    if bib_keys:
        missing_cites = sorted(set(citations) - bib_keys)
    else:
        missing_cites = sorted(set(citations))
    if missing_cites:
        status = 1
        header = "[ERROR] Missing bibliography entries:" if bib_keys else "[ERROR] bibliography.bib not found; unable to resolve citations:"
        print(f"\n{header}")
        for cite in missing_cites:
            locations = ", ".join(str(o) for o in citations[cite])
            print(f"  {cite} -> {locations}")

    unused_labels = sorted(set(labels) - set(references))
    if unused_labels:
        print(f"\n[WARNING] {len(unused_labels)} unused labels (informational)")

    missing_inputs = []
    for include_key, occs in includes.items():
        candidate = (tex_root / include_key).with_suffix(".tex")
        if candidate.exists():
            continue
        normalized = include_key.replace("\\", "/")
        if any(normalized.startswith(prefix) for prefix in ignore_missing_inputs):
            continue
        missing_inputs.append((include_key, occs))
    if missing_inputs:
        status = 1
        print("\n[ERROR] Missing inputs/includes:")
        for include_key, occs in missing_inputs:
            locations = ", ".join(str(o) for o in occs)
            print(f"  {include_key} -> {locations}")

    print(
        "\nSummary:"
        f"\n  Files analyzed : {len(files)}"
        f"\n  Labels defined : {len(labels)}"
        f"\n  References used: {len(references)}"
        f"\n  Citations used : {len(citations)}"
    )

    return status


def main(argv: Sequence[str] | None = None) -> None:
    ap = argparse.ArgumentParser(description="Validate LaTeX cross-references and citations.")
    ap.add_argument("--base-dir", type=str, default=".", help="Repository root.")
    ap.add_argument(
        "--tex-root",
        type=str,
        default="synthesis",
        help="Path (relative to base) containing LaTeX sources.",
    )
    ap.add_argument(
        "--bib",
        type=str,
        default="synthesis/bibliography.bib",
        help="Bibliography file to validate against.",
    )
    ap.add_argument(
        "--ignore-missing-input",
        action="append",
        default=[],
        help="Prefix to ignore when checking \\input/\\include availability.",
    )
    ap.add_argument(
        "--include-modules",
        action="store_true",
        help="Scan modules directory (tex/ltx files) in addition to chapters.",
    )
    ap.add_argument(
        "--skip-token",
        action="append",
        default=["backup", "expanded", "archive", "test_compile"],
        help="Substring token to skip when scanning paths (repeatable).",
    )
    args = ap.parse_args(argv)

    base_dir = Path(resolve_base_dir(args.base_dir)).resolve()
    tex_root = (base_dir / args.tex_root).resolve()
    bib_path = (base_dir / args.bib).resolve()

    if not tex_root.exists():
        raise SystemExit(f"Tex root not found: {tex_root}")

    status = validate_references(
        tex_root=tex_root,
        bib_path=bib_path,
        include_modules=args.include_modules,
        ignore_missing_inputs=args.ignore_missing_input or [],
        skip_tokens=args.skip_token or [],
    )
    raise SystemExit(status)


if __name__ == "__main__":
    main()
