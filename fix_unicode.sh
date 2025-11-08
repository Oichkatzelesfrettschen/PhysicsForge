#!/bin/bash
# fix_unicode.sh - Fix unicode characters and missing LaTeX environments
# Created: 2025-11-07

echo "==============================================="
echo "LaTeX Unicode and Environment Fix Script"
echo "==============================================="

BASE_DIR="/home/eirikr/Playground/PhysicsForge"
cd "$BASE_DIR" || exit 1

# Function to check for unicode characters
check_unicode() {
    echo ""
    echo "1. Checking for problematic unicode characters in .tex files..."

    # Common problematic unicode characters
    UNICODE_CHARS=(
        "✓" "✗" "×" "→" "←" "↔" "⇒" "⇐" "⇔"
        "≈" "≠" "≥" "≤" "≡" "≢" "∈" "∉" "⊂" "⊃"
        "∞" "∀" "∃" "∴" "∵" "•" "·" "…" "—"
        "α" "β" "γ" "δ" "ε" "θ" "λ" "μ" "π" "σ" "φ" "ψ" "ω"
        "Α" "Β" "Γ" "Δ" "Θ" "Λ" "Π" "Σ" "Φ" "Ψ" "Ω"
    )

    FOUND_UNICODE=false

    for char in "${UNICODE_CHARS[@]}"; do
        results=$(find synthesis -name "*.tex" -exec grep -l "$char" {} \; 2>/dev/null)
        if [ -n "$results" ]; then
            echo "   Found '$char' in:"
            echo "$results" | sed 's/^/      /'
            FOUND_UNICODE=true
        fi
    done

    if [ "$FOUND_UNICODE" = false ]; then
        echo "   ✓ No problematic unicode characters found in .tex files"
    fi
}

# Function to fix shadedbox environment
fix_shadedbox() {
    echo ""
    echo "2. Fixing shadedbox environment definition..."

    PREAMBLE="synthesis/preamble.tex"

    # Check if shadedbox is already defined
    if grep -q "newenvironment{shadedbox}" "$PREAMBLE" 2>/dev/null; then
        echo "   ✓ shadedbox environment already defined in preamble.tex"
    else
        echo "   Adding shadedbox environment to preamble.tex..."

        # Create backup
        cp "$PREAMBLE" "${PREAMBLE}.backup.$(date +%Y%m%d_%H%M%S)"

        # Add shadedbox definition before \endinput
        sed -i '/^\\endinput/i \
% Shaded box environment for highlighting important content\
\\usepackage{framed}\
\\usepackage{xcolor}\
\\definecolor{shadecolor}{gray}{0.95}\
\\newenvironment{shadedbox}%\
  {\\begin{shaded}\\begin{quote}}%\
  {\\end{quote}\\end{shaded}}%\
' "$PREAMBLE"

        echo "   ✓ Added shadedbox environment definition"
    fi
}

# Function to replace unicode characters
replace_unicode() {
    echo ""
    echo "3. Replacing unicode characters with LaTeX equivalents..."

    # Define replacements
    declare -A REPLACEMENTS=(
        ["✓"]="\\checkmark"
        ["✗"]="\\times"
        ["×"]="\\times"
        ["→"]="\\rightarrow"
        ["←"]="\\leftarrow"
        ["↔"]="\\leftrightarrow"
        ["⇒"]="\\Rightarrow"
        ["⇐"]="\\Leftarrow"
        ["⇔"]="\\Leftrightarrow"
        ["≈"]="\\approx"
        ["≠"]="\\neq"
        ["≥"]="\\geq"
        ["≤"]="\\leq"
        ["≡"]="\\equiv"
        ["≢"]="\\not\\equiv"
        ["∈"]="\\in"
        ["∉"]="\\notin"
        ["⊂"]="\\subset"
        ["⊃"]="\\supset"
        ["∞"]="\\infty"
        ["∀"]="\\forall"
        ["∃"]="\\exists"
        ["∴"]="\\therefore"
        ["∵"]="\\because"
        ["•"]="\\bullet"
        ["·"]="\\cdot"
        ["…"]="\\ldots"
        ["—"]="---"
    )

    # Greek letters in text mode (outside math mode)
    declare -A GREEK_REPLACEMENTS=(
        ["α"]="\\(\\alpha\\)"
        ["β"]="\\(\\beta\\)"
        ["γ"]="\\(\\gamma\\)"
        ["δ"]="\\(\\delta\\)"
        ["ε"]="\\(\\epsilon\\)"
        ["θ"]="\\(\\theta\\)"
        ["λ"]="\\(\\lambda\\)"
        ["μ"]="\\(\\mu\\)"
        ["π"]="\\(\\pi\\)"
        ["σ"]="\\(\\sigma\\)"
        ["φ"]="\\(\\phi\\)"
        ["ψ"]="\\(\\psi\\)"
        ["ω"]="\\(\\omega\\)"
    )

    FILES_MODIFIED=0

    # Process each .tex file
    while IFS= read -r -d '' file; do
        MODIFIED=false

        # Check if file contains any unicode
        for char in "${!REPLACEMENTS[@]}"; do
            if grep -q "$char" "$file" 2>/dev/null; then
                sed -i "s/$char/${REPLACEMENTS[$char]}/g" "$file"
                echo "   Replaced '$char' in $file"
                MODIFIED=true
            fi
        done

        # Greek letters need special handling (only outside math mode)
        for char in "${!GREEK_REPLACEMENTS[@]}"; do
            if grep -q "$char" "$file" 2>/dev/null; then
                # This is a simplified replacement - ideally would parse context
                echo "   Warning: Found Greek letter '$char' in $file - manual review recommended"
                MODIFIED=true
            fi
        done

        if [ "$MODIFIED" = true ]; then
            ((FILES_MODIFIED++))
        fi
    done < <(find synthesis -name "*.tex" -print0)

    echo "   Modified $FILES_MODIFIED files"
}

# Function to clean build artifacts
clean_build() {
    echo ""
    echo "4. Cleaning LaTeX build artifacts..."

    cd synthesis || exit 1
    rm -f main.aux main.log main.pdf main.toc main.lof main.lot
    rm -f main.idx main.ind main.ilg main.bbl main.blg
    rm -f main.fls main.fdb_latexmk main.synctex.gz main.out
    rm -f *.aux *.log *.toc *.lof *.lot *.idx *.ind *.ilg

    echo "   ✓ Cleaned build artifacts"
    cd ..
}

# Function to verify compilation
verify_compilation() {
    echo ""
    echo "5. Attempting compilation to verify fixes..."

    cd synthesis || exit 1

    # Try a quick compilation
    timeout 30 pdflatex -interaction=nonstopmode main.tex > /dev/null 2>&1

    if [ $? -eq 0 ]; then
        echo "   ✓ LaTeX compilation succeeded!"
    else
        echo "   ⚠ LaTeX compilation still has issues. Check main.log for details."

        # Extract first error from log
        if [ -f main.log ]; then
            echo ""
            echo "   First error in main.log:"
            grep -m1 "! LaTeX Error\|! Emergency stop" main.log | head -5
        fi
    fi

    cd ..
}

# Main execution
main() {
    echo "Starting at: $(date)"
    echo "Working directory: $BASE_DIR"

    check_unicode
    fix_shadedbox
    replace_unicode
    clean_build
    verify_compilation

    echo ""
    echo "==============================================="
    echo "Script completed at: $(date)"
    echo "==============================================="
    echo ""
    echo "Next steps:"
    echo "1. Review any warnings above"
    echo "2. Run 'make latex' to perform full compilation"
    echo "3. Check logs/latexmk_compile.log for any remaining errors"
}

# Run main function
main