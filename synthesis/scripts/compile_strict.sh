#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")"
MAIN="../main.tex"

if ! command -v pdflatex >/dev/null 2>&1 && ! command -v latexmk >/dev/null 2>&1; then
  echo "pdflatex/latexmk not found. Install TeX Live or MiKTeX." >&2
  exit 2
fi

if command -v latexmk >/dev/null 2>&1; then
  latexmk -pdf -interaction=nonstopmode "$MAIN"
else
  pdflatex -interaction=nonstopmode "$MAIN"
  pdflatex -interaction=nonstopmode "$MAIN"
fi

LOG="../main.log"
if [[ -f "$LOG" ]];
then
  if grep -Eqi "^!|LaTeX Warning|Package .* Warning" "$LOG"; then
    echo "Strict compile failed due to warnings/errors. See $LOG" >&2
    exit 3
  fi
fi

echo "Strict compile passed (no warnings)."
