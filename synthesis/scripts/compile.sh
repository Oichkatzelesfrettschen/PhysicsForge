#!/usr/bin/env bash
set -euo pipefail

# --- Start Harmonized Block ---

# 1. Use the 'feature' branch logic to cd to the project root (up one level).
#    This is cleaner as all build files (.aux, .log, etc.) will be
#    created in the project root, not in the script directory.
cd "$(dirname "$0")/.."

# We are now in synthesis/; MAIN is in this directory
MAIN="main.tex"

# Write logs to project root logs/ as tests expect
LOG_DIR="../logs"
mkdir -p "$LOG_DIR"
LATEXMK_LOG="$LOG_DIR/latexmk_compile.log"
PDFLATEX_LOG="$LOG_DIR/pdflatex_compile.log"

echo "Starting compilation of $MAIN..."

# Pre-clean potentially stale aux files that can carry bad encodings
rm -f main.{aux,idx,ind,ilg,out,toc,lot,lof,nav,snm,bbl,blg} 2>/dev/null || true

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
  # Strip stray BOM and NUL bytes anywhere in file (robust against mid-file BOM)
  find "$root" -type f -name "*.tex" -print0 | while IFS= read -r -d '' g; do
    if grep -Ua -q $'\x00' "$g" || grep -Ua -q $'\xFE\xFF' "$g" || grep -Ua -q $'\xFF\xFE' "$g"; then
      perl -0777 -pe 's/\x{FEFF}//g; s/\x00//g' "$g" > "$g".utf8 && mv "$g".utf8 "$g"
    fi
  done
done

# --- End Harmonized Block ---

if command -v latexmk >/dev/null 2>&1; then
  echo "Using latexmk for compilation."
  # Pre-pass: emit aux/out/toc to scrub encoding artifacts before latexmk
  if command -v pdflatex >/dev/null 2>&1; then
    pdflatex -interaction=nonstopmode "$MAIN" >/dev/null 2>&1 || true
    for ext in aux out toc ind ilg idx lot lof nav snm; do
      f="${MAIN%.tex}.$ext"
      if [ -f "$f" ]; then
        perl -0777 -pe 's/\x{FEFF}//g; s/\x00//g' "$f" > "$f".clean && mv "$f".clean "$f"
      fi
    done
  fi
  # Note: Redirecting both stdout and stderr to the log file
  if latexmk -pdf "$MAIN" > "$LATEXMK_LOG" 2>&1; then
    echo "Compilation successful. Output at $(dirname "$MAIN")/$(basename "$MAIN" .tex).pdf"
  else
    # Attempt one automatic scrub-and-rerun to handle stray BOM/NUL in aux files
    echo "latexmk failed; attempting aux scrub and one retry..." >&2
    for ext in aux out toc ind ilg idx lot lof nav snm; do
      f="${MAIN%.tex}.$ext"
      if [ -f "$f" ]; then
        perl -0777 -pe 's/\x{FEFF}//g; s/\x00//g' "$f" > "$f".clean && mv "$f".clean "$f"
      fi
    done
    if latexmk -pdf "$MAIN" >> "$LATEXMK_LOG" 2>&1; then
      echo "Compilation successful after scrub retry. Output at $(dirname "$MAIN")/$(basename "$MAIN" .tex).pdf"
    else
      echo "Error: latexmk compilation failed. See log for details: $LATEXMK_LOG" >&2
      echo "To debug, check for errors in the log file or run latexmk manually." >&2
      exit 1
    fi
  fi
else
  if ! command -v pdflatex >/dev/null 2>&1; then
    echo "pdflatex not found. Install TeX Live or MiKTeX." >&2
    exit 1
  fi

  echo "Using pdflatex for compilation."
  # Note: Redirecting both stdout and stderr to the log file.
  # Running pdflatex twice is necessary to resolve references/TOC.
  if pdflatex -interaction=nonstopmode "$MAIN" > "$PDFLATEX_LOG" 2>&1 && \
     pdflatex -interaction=nonstopmode "$MAIN" >> "$PDFLATEX_LOG" 2>&1; then
    echo "Compilation successful. Output at $(dirname "$MAIN")/$(basename "$MAIN" .tex).pdf"
  else
    echo "Error: pdflatex compilation failed. See log for details: $PDFLATEX_LOG" >&2
    echo "To debug, check for common LaTeX errors like missing packages or syntax issues." >&2
    exit 1
  fi
fi