#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Extract a range of text delimited by headings from a Markdown file."
    )
    parser.add_argument("--source", type=Path, required=True, help="Path to source Markdown document")
    parser.add_argument("--start", type=str, required=True, help="Heading text signalling the start of the section")
    parser.add_argument("--end", type=str, help="Heading text signalling the end of the section (exclusive)")
    parser.add_argument("--dest", type=Path, required=True, help="Path of the destination file")
    parser.add_argument("--strip-heading", action="store_true", help="Remove the start heading line from the output")
    return parser.parse_args()


def extract_section(text: str, start: str, end: str | None, strip_heading: bool) -> str:
    start_idx = text.find(start)
    if start_idx == -1:
        raise SystemExit(f"Start marker '{start}' not found")
    if end:
        end_idx = text.find(end, start_idx + len(start))
        if end_idx == -1:
            end_idx = len(text)
    else:
        end_idx = len(text)
    snippet = text[start_idx:end_idx]

    if strip_heading:
        lines = snippet.splitlines()
        if lines and start in lines[0]:
            lines = lines[1:]
        snippet = "\n".join(lines)

    return snippet.strip() + "\n"


def main() -> None:
    args = parse_args()
    source_text = args.source.read_text(encoding="utf-8")
    section = extract_section(source_text, args.start, args.end, args.strip_heading)
    args.dest.parent.mkdir(parents=True, exist_ok=True)
    args.dest.write_text(section, encoding="utf-8")


if __name__ == "__main__":
    main()
