#!/usr/bin/env bash
set -euo pipefail

# Change to the synthesis directory
cd "$(dirname "$0")/.."
MAIN="main.tex"
LOG_DIR="logs"
mkdir -p "$LOG_DIR"
LATEXMK_LOG="$LOG_DIR/latexmk_strict_compile.log"
PDFLATEX_LOG="$LOG_DIR/pdflatex_strict_compile.log"
MAIN_LOG="main.log"

echo "Starting strict compilation of $MAIN..."

# Convert any UTF-16 .tex files to UTF-8 to avoid hyperref bookmark crashes
for root in . ../modules; do
  [ -d "$root" ] || continue
  find "$root" -type f -name "*.tex" -print0 | while IFS= read -r -d '' f; do
    enc=$(file -bi "$f" || true)
    bom=$(xxd -p -l 2 "$f" 2>/dev/null || echo "")
    if [[ "$enc" == *"charset=utf-16"* ]] || [[ "$bom" == "feff" ]] || [[ "$bom" == "fffe" ]]; then
      iconv -f utf-16 -t utf-8 "$f" > "$f".utf8 && mv "$f".utf8 "$f"
    fi
  done
done

if ! command -v pdflatex >/dev/null 2>&1 && ! command -v latexmk >/dev/null 2>&1; then
  echo "pdflatex/latexmk not found. Install TeX Live or MiKTeX." >&2
  exit 2
fi

COMPILED_SUCCESSFULLY=false
if command -v latexmk >/dev/null 2>&1; then
  echo "Using latexmk for strict compilation."
  if latexmk -pdf -interaction=nonstopmode "$MAIN" > "$LATEXMK_LOG" 2>&1; then
    COMPILED_SUCCESSFULLY=true
  else
    echo "Error: latexmk strict compilation failed. See log for details: $LATEXMK_LOG" >&2
    echo "To debug, check for fatal errors in the log file." >&2
    exit 3
  fi
else
  echo "Using pdflatex for strict compilation."
  if pdflatex -interaction=nonstopmode "$MAIN" > "$PDFLATEX_LOG" 2>&1 && \
     pdflatex -interaction=nonstopmode "$MAIN" >> "$PDFLATEX_LOG" 2>&1; then
    COMPILED_SUCCESSFULLY=true
  else
    echo "Error: pdflatex strict compilation failed. See log for details: $PDFLATEX_LOG" >&2
    echo "To debug, check for fatal errors in the log file." >&2
    exit 3
  fi
fi

if [ "$COMPILED_SUCCESSFULLY" = true ]; then
  if [ ! -f "$MAIN_LOG" ]; then
    echo "Error: Main log file not found at $MAIN_LOG" >&2
    exit 4
  fi
  WARNINGS=$(grep -Ein "^!|LaTeX Warning|Package .* Warning|Undefined references|Missing character" "$MAIN_LOG" || true)
  if [ -n "$WARNINGS" ]; then
    echo "Strict compilation failed due to the following warnings/errors:" >&2
    echo "$WARNINGS" >&2
    echo "See the full log for details: $MAIN_LOG" >&2
    exit 3
  else
    echo "Strict compilation successful. No warnings or errors found."
  fi
fi
