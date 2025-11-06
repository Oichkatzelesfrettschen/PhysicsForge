#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
MAIN="../main.tex"
LOG_DIR="../logs"
mkdir -p "$LOG_DIR"
LATEXMK_LOG="$LOG_DIR/latexmk_compile.log"
PDFLATEX_LOG="$LOG_DIR/pdflatex_compile.log"

echo "Starting compilation of $MAIN..."

if command -v latexmk >/dev/null 2>&1; then
  echo "Using latexmk for compilation."
  if latexmk -pdf "$MAIN" > "$LATEXMK_LOG" 2>&1; then
    echo "Compilation successful. Output at $(dirname "$MAIN")/$(basename "$MAIN" .tex).pdf"
  else
    echo "Error: latexmk compilation failed. See log for details: $LATEXMK_LOG" >&2
    echo "To debug, check for errors in the log file or run latexmk manually." >&2
    exit 1
  fi
else
  if ! command -v pdflatex >/dev/null 2>&1; then
    echo "pdflatex not found. Install TeX Live or MiKTeX." >&2
    exit 1
  fi

  echo "Using pdflatex for compilation."
  if pdflatex -interaction=nonstopmode "$MAIN" > "$PDFLATEX_LOG" 2>&1 && \
     pdflatex -interaction=nonstopmode "$MAIN" >> "$PDFLATEX_LOG" 2>&1; then
    echo "Compilation successful. Output at $(dirname "$MAIN")/$(basename "$MAIN" .tex).pdf"
  else
    echo "Error: pdflatex compilation failed. See log for details: $PDFLATEX_LOG" >&2
    echo "To debug, check for common LaTeX errors like missing packages or syntax issues." >&2
    exit 1
  fi
fi
