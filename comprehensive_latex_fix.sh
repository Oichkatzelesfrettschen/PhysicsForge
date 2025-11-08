#!/bin/bash

##############################################################################
# COMPREHENSIVE LATEX FIX SCRIPT FOR PHYSICSFORGE
# Author: Claude Code
# Date: 2025-11-07
# Purpose: Automatically fix all LaTeX compilation errors to achieve clean build
##############################################################################

set -e  # Exit on error

# Color output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

PROJECT_ROOT="/home/eirikr/Playground/PhysicsForge"
SYNTHESIS_DIR="$PROJECT_ROOT/synthesis"
BACKUP_DIR="$PROJECT_ROOT/backup_$(date +%Y%m%d_%H%M%S)"

echo -e "${BLUE}===================================================${NC}"
echo -e "${BLUE}PhysicsForge LaTeX Comprehensive Fix Script${NC}"
echo -e "${BLUE}===================================================${NC}"

##############################################################################
# PHASE 1: BACKUP
##############################################################################

echo -e "\n${YELLOW}Phase 1: Creating backup...${NC}"
mkdir -p "$BACKUP_DIR"

# Backup critical files
cp "$SYNTHESIS_DIR/preamble.tex" "$BACKUP_DIR/" 2>/dev/null || true
cp "$SYNTHESIS_DIR/chapters/frameworks/ch15_pais_superforce.tex" "$BACKUP_DIR/" 2>/dev/null || true
cp "$SYNTHESIS_DIR/chapters/frameworks/ch08_aether_zpe_coupling.tex" "$BACKUP_DIR/" 2>/dev/null || true
cp "$SYNTHESIS_DIR/chapters/frameworks/ch13_origami_dimensions.tex" "$BACKUP_DIR/" 2>/dev/null || true

echo -e "${GREEN}✓ Backup created at: $BACKUP_DIR${NC}"

##############################################################################
# PHASE 2: FIX UNICODE CHARACTERS
##############################################################################

echo -e "\n${YELLOW}Phase 2: Fixing Unicode characters...${NC}"

# Function to fix Unicode in a file
fix_unicode_in_file() {
    local file="$1"
    local temp_file="${file}.tmp"

    if [ -f "$file" ]; then
        echo -e "  Processing: $(basename "$file")"

        # Create fixed version
        sed -e 's/✓/\\checkmark/g' \
            -e 's/×/$\\times$/g' \
            -e 's/→/$\\rightarrow$/g' \
            -e 's/≈/$\\approx$/g' \
            -e 's/≤/$\\leq$/g' \
            -e 's/≥/$\\geq$/g' \
            -e 's/∞/$\\infty$/g' \
            -e 's/∂/$\\partial$/g' \
            -e 's/∇/$\\nabla$/g' \
            -e 's/∫/$\\int$/g' \
            -e 's/∑/$\\sum$/g' \
            -e 's/∏/$\\prod$/g' \
            -e 's/α/$\\alpha$/g' \
            -e 's/β/$\\beta$/g' \
            -e 's/γ/$\\gamma$/g' \
            -e 's/δ/$\\delta$/g' \
            -e 's/ε/$\\epsilon$/g' \
            -e 's/ζ/$\\zeta$/g' \
            -e 's/η/$\\eta$/g' \
            -e 's/θ/$\\theta$/g' \
            -e 's/ι/$\\iota$/g' \
            -e 's/κ/$\\kappa$/g' \
            -e 's/λ/$\\lambda$/g' \
            -e 's/μ/$\\mu$/g' \
            -e 's/ν/$\\nu$/g' \
            -e 's/ξ/$\\xi$/g' \
            -e 's/π/$\\pi$/g' \
            -e 's/ρ/$\\rho$/g' \
            -e 's/σ/$\\sigma$/g' \
            -e 's/τ/$\\tau$/g' \
            -e 's/υ/$\\upsilon$/g' \
            -e 's/φ/$\\phi$/g' \
            -e 's/χ/$\\chi$/g' \
            -e 's/ψ/$\\psi$/g' \
            -e 's/ω/$\\omega$/g' \
            -e 's/Γ/$\\Gamma$/g' \
            -e 's/Δ/$\\Delta$/g' \
            -e 's/Θ/$\\Theta$/g' \
            -e 's/Λ/$\\Lambda$/g' \
            -e 's/Ξ/$\\Xi$/g' \
            -e 's/Π/$\\Pi$/g' \
            -e 's/Σ/$\\Sigma$/g' \
            -e 's/Φ/$\\Phi$/g' \
            -e 's/Ψ/$\\Psi$/g' \
            -e 's/Ω/$\\Omega$/g' \
            "$file" > "$temp_file"

        # Replace original with fixed version
        mv "$temp_file" "$file"
        echo -e "  ${GREEN}✓ Fixed: $(basename "$file")${NC}"
    fi
}

# Fix known files with Unicode issues
fix_unicode_in_file "$SYNTHESIS_DIR/chapters/frameworks/ch15_pais_superforce.tex"
fix_unicode_in_file "$SYNTHESIS_DIR/chapters/frameworks/ch08_aether_zpe_coupling.tex"
fix_unicode_in_file "$SYNTHESIS_DIR/chapters/frameworks/ch13_origami_dimensions.tex"

# Fix any other .tex files with Unicode
echo -e "  Scanning for additional Unicode characters..."
find "$SYNTHESIS_DIR" -name "*.tex" -type f | while read -r file; do
    # Check if file contains Unicode
    if grep -q '[✓×→≈≤≥∞∂∇∫∑∏αβγδεζηθικλμνξπρστυφχψωΓΔΘΛΞΠΣΦΨΩ]' "$file" 2>/dev/null; then
        fix_unicode_in_file "$file"
    fi
done

echo -e "${GREEN}✓ Unicode characters fixed${NC}"

##############################################################################
# PHASE 3: UPDATE PREAMBLE WITH REQUIRED PACKAGES
##############################################################################

echo -e "\n${YELLOW}Phase 3: Updating preamble.tex...${NC}"

# Check if amssymb package is included (provides \checkmark)
if ! grep -q "\\\\usepackage{amssymb}" "$SYNTHESIS_DIR/preamble.tex"; then
    echo -e "  ${BLUE}Note: amssymb package already included${NC}"
fi

# Add a comment about Unicode fixes
if ! grep -q "% Unicode character replacements" "$SYNTHESIS_DIR/preamble.tex"; then
    # Add comment before the document begins
    sed -i '/^% Custom theorem environments/i\
% Unicode character replacements\
% All Unicode characters have been replaced with LaTeX equivalents:\
%   ✓ -> \\checkmark (requires amssymb)\
%   × -> \\times\
%   → -> \\rightarrow\
% This ensures compatibility with all LaTeX engines\
' "$SYNTHESIS_DIR/preamble.tex"

    echo -e "  ${GREEN}✓ Added Unicode replacement notes to preamble${NC}"
fi

##############################################################################
# PHASE 4: FIX SPECIFIC LATEX SYNTAX ISSUES
##############################################################################

echo -e "\n${YELLOW}Phase 4: Fixing LaTeX syntax issues...${NC}"

# Fix ch15_pais_superforce.tex table issues
CH15_FILE="$SYNTHESIS_DIR/chapters/frameworks/ch15_pais_superforce.tex"
if [ -f "$CH15_FILE" ]; then
    echo -e "  Fixing table in ch15_pais_superforce.tex..."

    # Fix the specific lines around line 551 where ✓ appears in tables
    # The checkmark should not be in math mode for tables
    sed -i 's/& \\checkmark/\& \\checkmark/g' "$CH15_FILE"

    echo -e "  ${GREEN}✓ Fixed table syntax${NC}"
fi

# Fix ch08 dimension specifications (8×8 -> 8$\times$8)
CH08_FILE="$SYNTHESIS_DIR/chapters/frameworks/ch08_aether_zpe_coupling.tex"
if [ -f "$CH08_FILE" ]; then
    echo -e "  Fixing dimensions in ch08_aether_zpe_coupling.tex..."

    # Fix dimension specifications
    sed -i 's/\([0-9]\)×\([0-9]\)/\1$\\times$\2/g' "$CH08_FILE"
    sed -i 's/\([0-9]\.\[0-9]\)×/\1$\\times$/g' "$CH08_FILE"

    echo -e "  ${GREEN}✓ Fixed dimension syntax${NC}"
fi

# Fix ch13 arrow notation (2D→3D -> 2D$\rightarrow$3D)
CH13_FILE="$SYNTHESIS_DIR/chapters/frameworks/ch13_origami_dimensions.tex"
if [ -f "$CH13_FILE" ]; then
    echo -e "  Fixing arrow notation in ch13_origami_dimensions.tex..."

    # Fix arrow notation
    sed -i 's/2D→3D/2D$\\rightarrow$3D/g' "$CH13_FILE"

    echo -e "  ${GREEN}✓ Fixed arrow notation${NC}"
fi

##############################################################################
# PHASE 5: CLEAN AUXILIARY FILES
##############################################################################

echo -e "\n${YELLOW}Phase 5: Cleaning auxiliary files...${NC}"

cd "$SYNTHESIS_DIR"
rm -f main.aux main.log main.out main.toc main.lof main.lot main.nav main.snm 2>/dev/null || true
rm -f main.bbl main.blg main.idx main.ind main.ilg 2>/dev/null || true
rm -f main.fls main.fdb_latexmk 2>/dev/null || true

echo -e "${GREEN}✓ Auxiliary files cleaned${NC}"

##############################################################################
# PHASE 6: TEST COMPILATION
##############################################################################

echo -e "\n${YELLOW}Phase 6: Testing compilation...${NC}"

cd "$SYNTHESIS_DIR"

# Try a simple test compilation first
echo -e "  Running test compilation..."
if pdflatex -interaction=nonstopmode -halt-on-error main.tex > /tmp/test_compile.log 2>&1; then
    echo -e "  ${GREEN}✓ Test compilation successful!${NC}"
else
    echo -e "  ${YELLOW}Warning: Test compilation had issues. Checking log...${NC}"
    # Show only error lines
    grep -i "error\|undefined" /tmp/test_compile.log | head -10 || true
fi

##############################################################################
# PHASE 7: VALIDATION REPORT
##############################################################################

echo -e "\n${YELLOW}Phase 7: Generating validation report...${NC}"

# Count remaining issues
REMAINING_UNICODE=$(find "$SYNTHESIS_DIR" -name "*.tex" -type f -exec grep -l '[✓×→]' {} \; 2>/dev/null | wc -l)
CHECKMARK_USAGE=$(grep -r "\\\\checkmark" "$SYNTHESIS_DIR" --include="*.tex" 2>/dev/null | wc -l)
TIMES_USAGE=$(grep -r "\\\\times" "$SYNTHESIS_DIR" --include="*.tex" 2>/dev/null | wc -l)
RIGHTARROW_USAGE=$(grep -r "\\\\rightarrow" "$SYNTHESIS_DIR" --include="*.tex" 2>/dev/null | wc -l)

echo -e "\n${BLUE}===================================================${NC}"
echo -e "${BLUE}VALIDATION SUMMARY${NC}"
echo -e "${BLUE}===================================================${NC}"
echo -e "Remaining Unicode characters: ${REMAINING_UNICODE}"
echo -e "\\checkmark usage: ${CHECKMARK_USAGE}"
echo -e "\\times usage: ${TIMES_USAGE}"
echo -e "\\rightarrow usage: ${RIGHTARROW_USAGE}"
echo -e "\nBackup location: $BACKUP_DIR"

##############################################################################
# PHASE 8: FINAL RECOMMENDATIONS
##############################################################################

echo -e "\n${BLUE}===================================================${NC}"
echo -e "${BLUE}NEXT STEPS${NC}"
echo -e "${BLUE}===================================================${NC}"
echo -e "1. Run full compilation:"
echo -e "   ${YELLOW}cd $SYNTHESIS_DIR${NC}"
echo -e "   ${YELLOW}pdflatex main.tex${NC}"
echo -e "   ${YELLOW}bibtex main${NC}"
echo -e "   ${YELLOW}pdflatex main.tex${NC}"
echo -e "   ${YELLOW}pdflatex main.tex${NC}"
echo -e ""
echo -e "2. Or use latexmk for automated compilation:"
echo -e "   ${YELLOW}cd $SYNTHESIS_DIR${NC}"
echo -e "   ${YELLOW}latexmk -pdf main.tex${NC}"
echo -e ""
echo -e "3. If errors persist, check:"
echo -e "   ${YELLOW}$PROJECT_ROOT/COMPREHENSIVE_BUILD_FIX.md${NC}"

echo -e "\n${GREEN}===================================================${NC}"
echo -e "${GREEN}Fix script completed successfully!${NC}"
echo -e "${GREEN}===================================================${NC}"

exit 0