#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
MAIN="../main.tex"
if command -v latexmk >/dev/null 2>&1; then
  latexmk -pdf "$MAIN"
else
  if ! command -v pdflatex >/dev/null 2>&1; then
    echo "pdflatex not found. Install TeX Live or MiKTeX." >&2
    exit 1
  fi
  pdflatex "$MAIN"
  pdflatex "$MAIN"
fi

