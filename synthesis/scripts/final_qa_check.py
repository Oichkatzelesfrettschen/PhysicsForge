#!/usr/bin/env python3
"""
Final Quality Assurance Check for v1.0 release.
Comprehensive verification of all deliverables.
"""

import re
from pathlib import Path

def check_file_exists(filepath, description):
    """Check if a file exists and return status."""
    exists = filepath.exists()
    if exists:
        size = filepath.stat().st_size
        return True, f"{description}: EXISTS ({size:,} bytes)"
    else:
        return False, f"{description}: MISSING"

def verify_bibliography(bib_path):
    """Verify bibliography quality."""
    if not bib_path.exists():
        return False, "Bibliography file not found"

    with open(bib_path, 'r', encoding='utf-8') as f:
        content = f.read()

    entries = len(re.findall(r'@\w+\{', content))
    duplicates = check_for_duplicates(content)

    if entries < 200:
        return False, f"Bibliography has only {entries} entries (< 200 target)"
    elif duplicates:
        return False, f"Found {len(duplicates)} potential duplicate entries"
    else:
        return True, f"Bibliography verified: {entries} entries, no duplicates"

def check_for_duplicates(bib_content):
    """Quick check for obvious duplicate keys."""
    keys = re.findall(r'@\w+\{([^,]+),', bib_content)
    seen = set()
    duplicates = []
    for key in keys:
        if key in seen:
            duplicates.append(key)
        seen.add(key)
    return duplicates

def verify_pdf_compilation(log_path):
    """Verify PDF was compiled successfully."""
    if not log_path.exists():
        return False, "Log file not found"

    with open(log_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # Check for successful output
    if 'Output written on main.pdf' not in content:
        return False, "PDF compilation failed"

    # Extract page count
    match = re.search(r'Output written on main.pdf \((\d+) pages', content)
    if not match:
        return False, "Could not determine page count"

    pages = int(match.group(1))
    if pages < 500:
        return False, f"Page count too low: {pages} < 500"

    # Check for critical errors
    critical_errors = len(re.findall(r'! .*Error', content))
    undefined_cites = 'undefined citations' in content.lower()

    if undefined_cites:
        return False, "Undefined citations found"

    return True, f"Compilation successful: {pages} pages, {critical_errors} formatting errors"

def main():
    repo_root = Path(__file__).parent.parent.parent
    synthesis_dir = repo_root / 'synthesis'

    print("="*80)
    print("FINAL QUALITY ASSURANCE CHECK - VERSION 1.0")
    print("="*80)

    checks = []

    # 1. Core deliverables
    print("\n[1] CORE DELIVERABLES")

    files_to_check = [
        (synthesis_dir / 'main.pdf', "Main PDF"),
        (repo_root / 'RELEASE_NOTES_v1.0.md', "Release Notes"),
        (repo_root / 'STATISTICS_REPORT_v1.0.md', "Statistics Report"),
        (synthesis_dir / 'README_v1.0.md', "Synthesis README"),
        (synthesis_dir / 'bibliography.bib', "Bibliography"),
        (synthesis_dir / 'main.tex', "Main LaTeX source"),
        (synthesis_dir / 'preamble.tex', "LaTeX preamble"),
    ]

    for filepath, description in files_to_check:
        passed, message = check_file_exists(filepath, description)
        checks.append((description, passed))
        status = "PASS" if passed else "FAIL"
        print(f"  [{status}] {message}")

    # 2. Bibliography quality
    print("\n[2] BIBLIOGRAPHY QUALITY")
    bib_path = synthesis_dir / 'bibliography.bib'
    passed, message = verify_bibliography(bib_path)
    checks.append(("Bibliography Quality", passed))
    status = "PASS" if passed else "FAIL"
    print(f"  [{status}] {message}")

    # 3. PDF compilation
    print("\n[3] PDF COMPILATION")
    log_path = synthesis_dir / 'main.log'
    passed, message = verify_pdf_compilation(log_path)
    checks.append(("PDF Compilation", passed))
    status = "PASS" if passed else "FAIL"
    print(f"  [{status}] {message}")

    # 4. Chapter files
    print("\n[4] CHAPTER FILES")
    chapter_dirs = [
        'foundations', 'frameworks', 'unification', 'experiments', 'applications'
    ]
    total_chapters = 0
    for dirname in chapter_dirs:
        chapter_dir = synthesis_dir / 'chapters' / dirname
        if chapter_dir.exists():
            chapters = list(chapter_dir.glob('ch*.tex'))
            total_chapters += len(chapters)

    passed = total_chapters >= 30
    checks.append(("Chapter Files", passed))
    status = "PASS" if passed else "FAIL"
    print(f"  [{status}] Found {total_chapters} chapter files (target: >= 30)")

    # 5. Frontmatter and backmatter
    print("\n[5] FRONTMATTER/BACKMATTER")

    frontmatter_files = [
        'titlepage.tex', 'abstract.tex', 'notation.tex', 'acknowledgments.tex'
    ]
    fm_dir = synthesis_dir / 'frontmatter'
    fm_found = sum(1 for f in frontmatter_files if (fm_dir / f).exists())

    backmatter_dir = synthesis_dir / 'backmatter'
    bm_exists = backmatter_dir.exists()

    passed = fm_found >= 3 and bm_exists
    checks.append(("Front/Backmatter", passed))
    status = "PASS" if passed else "FAIL"
    print(f"  [{status}] Frontmatter: {fm_found}/4 files, Backmatter: {'EXISTS' if bm_exists else 'MISSING'}")

    # 6. Scripts
    print("\n[6] SUPPORT SCRIPTS")
    scripts_dir = synthesis_dir / 'scripts'
    if scripts_dir.exists():
        py_scripts = list(scripts_dir.glob('*.py'))
        passed = len(py_scripts) >= 5
        checks.append(("Support Scripts", passed))
        status = "PASS" if passed else "FAIL"
        print(f"  [{status}] Found {len(py_scripts)} Python scripts")
    else:
        checks.append(("Support Scripts", False))
        print(f"  [FAIL] Scripts directory not found")

    # Summary
    print("\n" + "="*80)
    print("QA SUMMARY")
    print("="*80)

    passed_count = sum(1 for _, passed in checks if passed)
    total_count = len(checks)
    pass_rate = (passed_count / total_count) * 100

    print(f"\nChecks passed: {passed_count}/{total_count} ({pass_rate:.1f}%)")

    print("\nDetailed results:")
    for check_name, passed in checks:
        status = "PASS" if passed else "FAIL"
        print(f"  [{status}] {check_name}")

    # Final verdict
    print("\n" + "="*80)
    print("FINAL VERDICT")
    print("="*80)

    if pass_rate >= 90:
        verdict = "EXCELLENT - Ready for v1.0 release"
        grade = "A"
    elif pass_rate >= 80:
        verdict = "GOOD - Ready for v1.0 release with minor notes"
        grade = "B"
    elif pass_rate >= 70:
        verdict = "ACCEPTABLE - Can proceed with caution"
        grade = "C"
    else:
        verdict = "NEEDS IMPROVEMENT - Address failures before release"
        grade = "F"

    print(f"  Grade: {grade}")
    print(f"  Verdict: {verdict}")

    if pass_rate >= 70:
        print("\n  Repository status: READY FOR v1.0 RELEASE")
    else:
        print("\n  Repository status: NOT READY - FIX FAILURES")

    return 0 if pass_rate >= 70 else 1

if __name__ == '__main__':
    exit(main())
