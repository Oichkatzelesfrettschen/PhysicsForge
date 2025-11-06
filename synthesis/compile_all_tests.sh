#!/bin/bash
# Comprehensive test compilation script
# Compiles all 35 test files and generates report

SYNTHESIS_DIR="C:/Users/ericj/Git-Projects/Math_Science/synthesis"
cd "$SYNTHESIS_DIR"

# Output file for results
RESULTS_FILE="test_compilation_results.txt"
echo "=== TEST COMPILATION RESULTS ===" > "$RESULTS_FILE"
echo "Date: $(date)" >> "$RESULTS_FILE"
echo "" >> "$RESULTS_FILE"

# Arrays to track results
declare -a TEST_FILES
declare -a STATUSES
declare -a PAGES
declare -a SIZES
declare -a ERRORS

# List of all test files
TEST_FILES=(
    test_ch01.tex test_ch02.tex test_ch03.tex test_ch04.tex test_ch05.tex
    test_ch06.tex test_ch07.tex test_ch08.tex test_ch09.tex test_ch10.tex
    test_ch11.tex test_ch12.tex test_ch13.tex test_ch14.tex test_ch15.tex
    test_ch16.tex test_ch17.tex test_ch18.tex test_ch19.tex test_ch20.tex
    test_ch21.tex test_ch22.tex test_ch23.tex test_ch24.tex test_ch25.tex
    test_ch26.tex test_ch27.tex test_ch28.tex test_ch29.tex test_ch30.tex
    test_part1_foundations.tex test_part2_frameworks.tex test_part3.tex
    test_part4.tex test_part5.tex
)

# Function to compile a test file
compile_test() {
    local testfile=$1
    local basename="${testfile%.tex}"

    echo "Compiling $testfile..."

    # Clean previous outputs
    rm -f "${basename}.aux" "${basename}.log" "${basename}.pdf" "${basename}.bbl" "${basename}.blg"

    # First pass
    pdflatex -interaction=nonstopmode "$testfile" > /dev/null 2>&1
    local status1=$?

    # BibTeX if needed
    if [ -f "${basename}.aux" ]; then
        bibtex "$basename" > /dev/null 2>&1
    fi

    # Second pass
    pdflatex -interaction=nonstopmode "$testfile" > /dev/null 2>&1
    local status2=$?

    # Third pass for cross-references
    pdflatex -interaction=nonstopmode "$testfile" > /dev/null 2>&1
    local status3=$?

    # Check results
    if [ -f "${basename}.pdf" ]; then
        # Count pages using pdfinfo
        local pages=$(pdfinfo "${basename}.pdf" 2>/dev/null | grep "Pages:" | awk '{print $2}')
        [ -z "$pages" ] && pages="?"

        # Get file size
        local size=$(ls -lh "${basename}.pdf" | awk '{print $5}')

        # Count errors in log
        local errors=0
        if [ -f "${basename}.log" ]; then
            errors=$(grep -c "^!" "${basename}.log" 2>/dev/null || echo 0)
        fi

        echo "$testfile|SUCCESS|$pages|$size|$errors"
        return 0
    else
        echo "$testfile|FAILED|0|0|N/A"
        return 1
    fi
}

# Compile all test files
success_count=0
failed_count=0

for testfile in "${TEST_FILES[@]}"; do
    result=$(compile_test "$testfile")
    echo "$result" >> "$RESULTS_FILE"

    if [[ $result == *"SUCCESS"* ]]; then
        ((success_count++))
    else
        ((failed_count++))
    fi
done

# Summary
echo "" >> "$RESULTS_FILE"
echo "=== SUMMARY ===" >> "$RESULTS_FILE"
echo "Total tests: ${#TEST_FILES[@]}" >> "$RESULTS_FILE"
echo "Successful: $success_count" >> "$RESULTS_FILE"
echo "Failed: $failed_count" >> "$RESULTS_FILE"
echo "Success rate: $(echo "scale=2; $success_count * 100 / ${#TEST_FILES[@]}" | bc)%" >> "$RESULTS_FILE"

cat "$RESULTS_FILE"
