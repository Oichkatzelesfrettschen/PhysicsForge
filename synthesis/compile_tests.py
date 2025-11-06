#!/usr/bin/env python3
"""
Comprehensive test compilation script
Compiles all 35 test files and generates detailed report
"""

import subprocess
import os
import re
from pathlib import Path

SYNTHESIS_DIR = Path(r"C:\Users\ericj\Git-Projects\Math_Science\synthesis")
os.chdir(SYNTHESIS_DIR)

# List of all test files
TEST_FILES = [
    f'test_ch{i:02d}.tex' for i in range(1, 31)
] + [
    'test_part1_foundations.tex',
    'test_part2_frameworks.tex',
    'test_part3.tex',
    'test_part4.tex',
    'test_part5.tex'
]

def compile_test(tex_file):
    """Compile a test file and return results"""
    basename = tex_file.replace('.tex', '')

    print(f"Compiling {tex_file}...", end=' ')

    # Clean previous outputs
    for ext in ['.aux', '.log', '.pdf', '.bbl', '.blg', '.out', '.toc']:
        aux_file = f"{basename}{ext}"
        if os.path.exists(aux_file):
            try:
                os.remove(aux_file)
            except:
                pass

    # First pdflatex pass
    subprocess.run(['pdflatex', '-interaction=nonstopmode', tex_file],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # BibTeX pass
    if os.path.exists(f"{basename}.aux"):
        subprocess.run(['bibtex', basename],
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # Second pdflatex pass
    subprocess.run(['pdflatex', '-interaction=nonstopmode', tex_file],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # Third pdflatex pass
    subprocess.run(['pdflatex', '-interaction=nonstopmode', tex_file],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # Check results
    pdf_file = f"{basename}.pdf"
    log_file = f"{basename}.log"

    if os.path.exists(pdf_file):
        # Get PDF size
        size_bytes = os.path.getsize(pdf_file)
        size_kb = size_bytes / 1024

        # Extract page count from log
        pages = "?"
        errors = 0
        warnings = 0

        if os.path.exists(log_file):
            with open(log_file, 'r', encoding='latin-1', errors='ignore') as f:
                log_content = f.read()

                # Find page count
                match = re.search(r'Output written.*?\((\d+) page', log_content)
                if match:
                    pages = match.group(1)

                # Count errors
                errors = len(re.findall(r'^!', log_content, re.MULTILINE))

                # Count warnings
                warnings = log_content.count('Warning')

        print(f"SUCCESS ({pages} pages, {size_kb:.1f} KB)")
        return {
            'file': tex_file,
            'status': 'SUCCESS',
            'pages': pages,
            'size_kb': f"{size_kb:.1f}",
            'errors': errors,
            'warnings': warnings
        }
    else:
        print("FAILED")
        return {
            'file': tex_file,
            'status': 'FAILED',
            'pages': '0',
            'size_kb': '0',
            'errors': 'N/A',
            'warnings': 'N/A'
        }

def main():
    print("=" * 70)
    print("COMPREHENSIVE TEST COMPILATION")
    print("=" * 70)
    print()

    results = []
    success_count = 0
    failed_count = 0

    # Compile all test files
    for test_file in TEST_FILES:
        result = compile_test(test_file)
        results.append(result)

        if result['status'] == 'SUCCESS':
            success_count += 1
        else:
            failed_count += 1

    print()
    print("=" * 70)
    print("RESULTS TABLE")
    print("=" * 70)
    print()

    # Print table header
    print(f"{'Filename':<35} {'Status':<10} {'Pages':<8} {'Size':<12} {'Errors':<8} {'Warnings':<8}")
    print("-" * 90)

    # Print results
    for r in results:
        print(f"{r['file']:<35} {r['status']:<10} {r['pages']:<8} {r['size_kb']:<12} {r['errors']:<8} {r['warnings']:<8}")

    print()
    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(f"Total tests:     {len(TEST_FILES)}")
    print(f"Successful:      {success_count}")
    print(f"Failed:          {failed_count}")
    print(f"Success rate:    {success_count/len(TEST_FILES)*100:.1f}%")
    print()

    # Save to CSV
    csv_file = 'test_compilation_results.csv'
    with open(csv_file, 'w') as f:
        f.write("Filename,Status,Pages,Size_KB,Errors,Warnings\n")
        for r in results:
            f.write(f"{r['file']},{r['status']},{r['pages']},{r['size_kb']},{r['errors']},{r['warnings']}\n")

    print(f"Results saved to {csv_file}")

    return success_count, failed_count

if __name__ == '__main__':
    main()
