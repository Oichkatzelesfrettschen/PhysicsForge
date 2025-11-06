#!/usr/bin/env python3
"""
Verify final PDF quality - Phase 5D.
Checks: compilation, file size, page count, bibliography, cross-references.
"""

import os
import re
import subprocess
from pathlib import Path

def check_pdf_exists(pdf_path):
    """Check if PDF exists and get stats."""
    if not pdf_path.exists():
        return False, "PDF not found"

    size = pdf_path.stat().st_size
    size_mb = size / (1024 * 1024)

    return True, f"Size: {size_mb:.2f} MB"

def count_pdf_pages(pdf_path):
    """Count pages in PDF using pdfinfo if available."""
    try:
        result = subprocess.run(
            ['pdfinfo', str(pdf_path)],
            capture_output=True,
            text=True,
            timeout=10
        )
        for line in result.stdout.split('\n'):
            if line.startswith('Pages:'):
                return int(line.split(':')[1].strip())
    except:
        pass

    # Fallback: estimate from log file
    return None

def analyze_log_file(log_path):
    """Analyze LaTeX log file for errors and warnings."""
    if not log_path.exists():
        return None

    with open(log_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # Count different types of issues
    errors = len(re.findall(r'! .*Error', content))
    warnings = len(re.findall(r'Warning', content))
    undefined_refs = len(re.findall(r'undefined references', content, re.IGNORECASE))
    undefined_cites = len(re.findall(r'undefined citations', content, re.IGNORECASE))

    # Extract page count
    page_match = re.search(r'Output written on main.pdf \((\d+) pages', content)
    pages = int(page_match.group(1)) if page_match else 0

    return {
        'errors': errors,
        'warnings': warnings,
        'undefined_refs': undefined_refs,
        'undefined_cites': undefined_cites,
        'pages': pages
    }

def check_bibliography(bib_path):
    """Check bibliography statistics."""
    if not bib_path.exists():
        return None

    with open(bib_path, 'r', encoding='utf-8') as f:
        content = f.read()

    entries = len(re.findall(r'@\w+\{', content))
    lines = len(content.splitlines())

    return {
        'entries': entries,
        'lines': lines
    }

def check_aux_files(synthesis_dir):
    """Check auxiliary files generated."""
    files = {
        'main.aux': 'Auxiliary file',
        'main.bbl': 'Bibliography',
        'main.blg': 'BibTeX log',
        'main.idx': 'Index input',
        'main.ind': 'Index output',
        'main.toc': 'Table of contents',
        'main.lof': 'List of figures',
        'main.lot': 'List of tables',
    }

    results = {}
    for filename, description in files.items():
        filepath = synthesis_dir / filename
        results[filename] = filepath.exists()

    return results

def main():
    synthesis_dir = Path(__file__).parent.parent
    pdf_path = synthesis_dir / 'main.pdf'
    log_path = synthesis_dir / 'main.log'
    bib_path = synthesis_dir / 'bibliography.bib'

    print("="*80)
    print("PDF QUALITY VERIFICATION - PHASE 5D")
    print("="*80)

    # 1. Check PDF exists
    print("\n[1] PDF File Check")
    exists, info = check_pdf_exists(pdf_path)
    if exists:
        print(f"  PDF exists: {pdf_path}")
        print(f"  {info}")
    else:
        print(f"  ERROR: {info}")
        return 1

    # 2. Analyze log file
    print("\n[2] Compilation Analysis")
    log_stats = analyze_log_file(log_path)
    if log_stats:
        print(f"  Pages: {log_stats['pages']}")
        print(f"  LaTeX errors: {log_stats['errors']}")
        print(f"  Warnings: {log_stats['warnings']}")
        print(f"  Undefined references: {log_stats['undefined_refs']}")
        print(f"  Undefined citations: {log_stats['undefined_cites']}")

        # Status
        if log_stats['pages'] >= 500:
            print("  Status: Page count GOOD (>= 500)")
        else:
            print(f"  Status: Page count LOW ({log_stats['pages']} < 500)")

    # 3. Bibliography check
    print("\n[3] Bibliography Check")
    bib_stats = check_bibliography(bib_path)
    if bib_stats:
        print(f"  Entries: {bib_stats['entries']}")
        print(f"  Lines: {bib_stats['lines']}")

        if bib_stats['entries'] >= 200:
            print("  Status: Entry count GOOD (>= 200)")
        else:
            print(f"  Status: Entry count LOW ({bib_stats['entries']} < 200)")

    # 4. Auxiliary files
    print("\n[4] Auxiliary Files Check")
    aux_files = check_aux_files(synthesis_dir)
    for filename, exists in aux_files.items():
        status = "EXISTS" if exists else "MISSING"
        print(f"  {filename}: {status}")

    # 5. Overall quality score
    print("\n" + "="*80)
    print("OVERALL QUALITY ASSESSMENT")
    print("="*80)

    score = 0
    max_score = 100

    # PDF exists (20 points)
    if exists:
        score += 20

    # Page count (20 points)
    if log_stats and log_stats['pages'] >= 500:
        score += 20
    elif log_stats and log_stats['pages'] >= 400:
        score += 15

    # Minimal errors (20 points)
    if log_stats:
        if log_stats['errors'] < 10:
            score += 20
        elif log_stats['errors'] < 50:
            score += 15
        elif log_stats['errors'] < 100:
            score += 10

    # No undefined refs/cites (20 points)
    if log_stats:
        if log_stats['undefined_refs'] == 0 and log_stats['undefined_cites'] == 0:
            score += 20
        elif log_stats['undefined_refs'] < 5 and log_stats['undefined_cites'] < 5:
            score += 15
        elif log_stats['undefined_refs'] < 20:
            score += 10

    # Bibliography (10 points)
    if bib_stats and bib_stats['entries'] >= 200:
        score += 10
    elif bib_stats and bib_stats['entries'] >= 150:
        score += 7

    # Auxiliary files (10 points)
    aux_count = sum(1 for exists in aux_files.values() if exists)
    score += int((aux_count / len(aux_files)) * 10)

    print(f"\nQuality Score: {score}/{max_score}")

    if score >= 90:
        grade = "A (Excellent)"
    elif score >= 80:
        grade = "B (Good)"
    elif score >= 70:
        grade = "C (Acceptable)"
    elif score >= 60:
        grade = "D (Needs Improvement)"
    else:
        grade = "F (Poor)"

    print(f"Grade: {grade}")

    # Verdict
    print("\n" + "="*80)
    if score >= 80:
        print("VERDICT: PDF ready for v1.0 release")
    elif score >= 70:
        print("VERDICT: PDF acceptable with minor issues")
    else:
        print("VERDICT: PDF needs significant improvement")

    return 0 if score >= 70 else 1

if __name__ == '__main__':
    exit(main())
