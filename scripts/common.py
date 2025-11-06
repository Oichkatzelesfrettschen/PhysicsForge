"""
Shared helpers for scripts: path resolution, PDF discovery, and regex safety.
"""

from __future__ import annotations

import os
import re
from pathlib import Path
from typing import Iterable


def resolve_base_dir(cli_base_dir: str | None, env_var: str = "MATH_SCIENCE_BASE_DIR", fallback: Path | None = None) -> str:
    if cli_base_dir:
        return str(Path(cli_base_dir).resolve())
    env = os.environ.get(env_var)
    if env:
        return str(Path(env).resolve())
    if fallback is None:
        fallback = Path(__file__).resolve().parents[1]
    return str(fallback)


def resolve_papers_dir(base_dir: str, override: str | None, candidates: Iterable[str] = ("source_materials/pdfs", "papers")) -> Path:
    base = Path(base_dir)
    if override:
        cand = Path(override)
        return cand if cand.is_absolute() else (base / cand)
    for rel in candidates:
        cand = base / rel
        if cand.exists():
            return cand
    return base


def build_pdf_list(papers_dir: Path, specific: list[str] | None) -> list[Path]:
    if specific:
        out: list[Path] = []
        for name in specific:
            p = (papers_dir / name) if not os.path.isabs(name) else Path(name)
            if p.exists():
                out.append(p)
        return out
    return sorted(papers_dir.glob('*.pdf'))


def safe_finditer(pattern: str, text: str, flags: int = 0):
    try:
        return re.finditer(pattern, text, flags)
    except re.error:
        return []

