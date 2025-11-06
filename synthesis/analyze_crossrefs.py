#!/usr/bin/env python3
"""
Comprehensive cross-reference analysis script
Analyzes all labels and references across the entire LaTeX project
"""

import re
from pathlib import Path
from collections import defaultdict, Counter

SYNTHESIS_DIR = Path(r"C:\Users\ericj\Git-Projects\Math_Science\synthesis")

def extract_labels(tex_files):
    """Extract all \\label{} commands from TeX files"""
    labels = defaultdict(list)

    for tex_file in tex_files:
        try:
            with open(tex_file, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()

            # Find all labels
            label_pattern = r'\\label\{([^}]+)\}'
            matches = re.finditer(label_pattern, content)

            for match in matches:
                label = match.group(1).strip()
                labels[label].append(str(tex_file.relative_to(SYNTHESIS_DIR)))

        except Exception as e:
            print(f"Warning: Could not read {tex_file}: {e}")

    return labels

def extract_references(tex_files):
    """Extract all \\ref{} and \\eqref{} commands from TeX files"""
    references = []

    for tex_file in tex_files:
        try:
            with open(tex_file, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()

            # Find all references
            ref_pattern = r'\\(?:ref|eqref)\{([^}]+)\}'
            matches = re.finditer(ref_pattern, content)

            for match in matches:
                ref = match.group(1).strip()
                references.append(ref)

        except Exception as e:
            print(f"Warning: Could not read {tex_file}: {e}")

    return references

def categorize_labels(labels):
    """Categorize labels by prefix"""
    categories = defaultdict(list)

    for label in labels:
        if ':' in label:
            prefix = label.split(':')[0]
            categories[prefix].append(label)
        else:
            categories['other'].append(label)

    return categories

def check_framework_tagging(labels):
    """Check equation labels for framework tagging compliance"""
    eq_labels = [l for l in labels if l.startswith('eq:')]
    framework_tags = ['aether', 'genesis', 'pais', 'unified']

    tagged = 0
    untagged = []

    for label in eq_labels:
        parts = label.split(':')
        if len(parts) >= 2 and parts[1] in framework_tags:
            tagged += 1
        else:
            untagged.append(label)

    compliance = tagged / len(eq_labels) * 100 if eq_labels else 0
    return compliance, untagged

def find_duplicate_labels(labels):
    """Find labels that are defined multiple times"""
    duplicates = []

    for label, files in labels.items():
        if len(files) > 1:
            duplicates.append((label, files))

    return duplicates

def check_reference_validity(references, labels):
    """Check if all references point to existing labels"""
    undefined = []
    ref_counts = Counter(references)

    for ref in ref_counts:
        if ref not in labels:
            undefined.append(ref)

    return undefined, ref_counts

def analyze_chapter_references(tex_files):
    """Analyze forward/backward references between chapters"""
    forward_refs = []
    isolated_chapters = []

    # Extract chapter numbers from files
    chapter_pattern = r'ch(\d+)_'

    for tex_file in tex_files:
        if 'chapters' not in str(tex_file):
            continue

        match = re.search(chapter_pattern, tex_file.name)
        if not match:
            continue

        current_ch = int(match.group(1))

        try:
            with open(tex_file, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()

            # Find references to other chapters
            ref_pattern = r'\\(?:ref|eqref)\{(?:ch|eq|sec):(?:chapter)?(\d+)'
            matches = re.finditer(ref_pattern, content)

            for match in matches:
                ref_ch = int(match.group(1))
                if ref_ch > current_ch:
                    forward_refs.append((current_ch, ref_ch))

        except Exception as e:
            pass

    return forward_refs

def main():
    print("=" * 80)
    print("CROSS-REFERENCE ANALYSIS")
    print("=" * 80)
    print()

    # Get all TeX files
    all_tex_files = list(SYNTHESIS_DIR.rglob("*.tex"))
    chapter_files = list((SYNTHESIS_DIR / "chapters").rglob("*.tex"))

    print(f"Scanning {len(all_tex_files)} TeX files...")
    print()

    # Extract labels
    print("=" * 80)
    print("LABEL EXTRACTION")
    print("=" * 80)
    labels = extract_labels(all_tex_files)
    print(f"Found {len(labels)} unique labels")

    # Categorize labels
    categories = categorize_labels(labels)
    print("\nLabel categories:")
    for cat, labs in sorted(categories.items()):
        print(f"  {cat:15s}: {len(labs):4d} labels")
    print()

    # Check for duplicate labels
    print("=" * 80)
    print("DUPLICATE LABELS")
    print("=" * 80)
    duplicates = find_duplicate_labels(labels)
    if duplicates:
        print(f"Found {len(duplicates)} duplicate labels:")
        for label, files in duplicates[:20]:
            print(f"  {label}")
            for f in files:
                print(f"    - {f}")
    else:
        print("No duplicate labels found")
    print()

    # Extract references
    print("=" * 80)
    print("REFERENCE EXTRACTION")
    print("=" * 80)
    references = extract_references(all_tex_files)
    print(f"Found {len(references)} total references ({len(set(references))} unique)")
    print()

    # Check reference validity
    print("=" * 80)
    print("REFERENCE VALIDATION")
    print("=" * 80)
    undefined, ref_counts = check_reference_validity(references, labels)
    if undefined:
        print(f"Found {len(undefined)} undefined references:")
        for ref in undefined[:30]:
            print(f"  {ref}")
    else:
        print("All references are defined")
    print()

    # Framework tagging compliance
    print("=" * 80)
    print("FRAMEWORK TAGGING COMPLIANCE")
    print("=" * 80)
    compliance, untagged = check_framework_tagging(labels)
    print(f"Framework tagging compliance: {compliance:.1f}%")
    if untagged:
        print(f"\nFirst 20 untagged equation labels:")
        for label in untagged[:20]:
            print(f"  {label}")
    print()

    # Chapter reference analysis
    print("=" * 80)
    print("CHAPTER REFERENCE ANALYSIS")
    print("=" * 80)
    forward_refs = analyze_chapter_references(chapter_files)
    if forward_refs:
        print(f"Found {len(forward_refs)} forward references:")
        for src, dst in forward_refs[:20]:
            print(f"  Ch{src:02d} -> Ch{dst:02d}")
    else:
        print("No forward references found")
    print()

    # Summary
    print("=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"Total labels:              {len(labels)}")
    print(f"Total references:          {len(set(references))}")
    print(f"Undefined references:      {len(undefined)}")
    print(f"Duplicate labels:          {len(duplicates)}")
    print(f"Framework tagging:         {compliance:.1f}%")
    print(f"Forward references:        {len(forward_refs)}")
    print()

    # Save results
    with open(SYNTHESIS_DIR / 'crossref_analysis.txt', 'w') as f:
        f.write("CROSS-REFERENCE ANALYSIS REPORT\n")
        f.write("=" * 80 + "\n\n")
        f.write(f"Total labels: {len(labels)}\n")
        f.write(f"Total references: {len(set(references))}\n")
        f.write(f"Undefined references: {len(undefined)}\n")
        if undefined:
            f.write("\nUndefined references:\n")
            for ref in undefined:
                f.write(f"  {ref}\n")
        f.write(f"\nDuplicate labels: {len(duplicates)}\n")
        if duplicates:
            f.write("\nDuplicate labels:\n")
            for label, files in duplicates:
                f.write(f"  {label}\n")
                for file in files:
                    f.write(f"    - {file}\n")

    print("Results saved to crossref_analysis.txt")

if __name__ == '__main__':
    main()
