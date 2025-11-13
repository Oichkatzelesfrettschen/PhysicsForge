#!/usr/bin/env python3
"""
Find duplicate LaTeX labels in a project and generate fix plan.
"""

import re
import sys
from pathlib import Path
from collections import defaultdict
from typing import Dict, List, Tuple

def find_tex_files(base_dir: Path) -> List[Path]:
    """Recursively find all .tex files."""
    tex_files = []
    for pattern in ['*.tex']:
        tex_files.extend(base_dir.rglob(pattern))
    return sorted(tex_files)

def extract_labels(file_path: Path) -> List[Tuple[str, int, str]]:
    """Extract all \label{} definitions from a file.
    Returns list of (label, line_number, line_content) tuples."""
    labels = []

    # Pattern to match \label{...} including multiline
    label_pattern = re.compile(r'\\label\{([^}]+)\}')

    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()

        for line_num, line in enumerate(lines, 1):
            matches = label_pattern.findall(line)
            for label in matches:
                labels.append((label.strip(), line_num, line.strip()))

    except Exception as e:
        print(f"Error reading {file_path}: {e}", file=sys.stderr)

    return labels

def find_duplicates(base_dir: Path) -> Dict[str, List[Tuple[Path, int, str]]]:
    """Find all duplicate labels in the project.
    Returns dict mapping label -> list of (file, line_num, line_content) tuples."""

    label_locations = defaultdict(list)

    # Find all tex files
    tex_files = find_tex_files(base_dir)
    print(f"Found {len(tex_files)} .tex files")

    # Extract labels from each file
    for tex_file in tex_files:
        rel_path = tex_file.relative_to(base_dir)
        labels = extract_labels(tex_file)

        for label, line_num, line_content in labels:
            label_locations[label].append((rel_path, line_num, line_content))

    # Filter to only duplicates
    duplicates = {
        label: locations
        for label, locations in label_locations.items()
        if len(locations) > 1
    }

    return duplicates

def categorize_label(label: str) -> str:
    """Categorize label by type."""
    if label.startswith('ch:'):
        return 'chapter'
    elif label.startswith('sec:'):
        return 'section'
    elif label.startswith('subsec:'):
        return 'subsection'
    elif label.startswith('eq:'):
        return 'equation'
    elif label.startswith('fig:'):
        return 'figure'
    elif label.startswith('tab:'):
        return 'table'
    elif label.startswith('thm:'):
        return 'theorem'
    elif label.startswith('lem:'):
        return 'lemma'
    elif label.startswith('def:'):
        return 'definition'
    elif label.startswith('prop:'):
        return 'proposition'
    elif label.startswith('cor:'):
        return 'corollary'
    elif label.startswith('rem:'):
        return 'remark'
    elif label.startswith('ex:'):
        return 'example'
    elif label.startswith('app:'):
        return 'appendix'
    else:
        return 'other'

def suggest_new_label(label: str, file_path: Path, occurrence: int) -> str:
    """Suggest a new label name for a duplicate."""
    category = categorize_label(label)

    # Extract chapter number if in chapters/ directory
    if 'chapters/' in str(file_path):
        # Try to extract chapter number
        match = re.search(r'ch(\d+)', str(file_path))
        if match:
            ch_num = match.group(1)
            if occurrence > 1:
                # For duplicates, append chapter number
                if category == 'equation':
                    # Special handling for equations
                    parts = label.split(':')
                    if len(parts) >= 2:
                        # Insert chapter number after framework prefix
                        return f"{parts[0]}:ch{ch_num}:{':'.join(parts[1:])}"
                return f"{label}:ch{ch_num}"

    # For modules, append module context
    if 'modules/' in str(file_path):
        if 'equations/' in str(file_path):
            # Extract equation module name
            match = re.search(r'eq_([^/]+)\.tex', str(file_path))
            if match and occurrence > 1:
                module_name = match.group(1)
                # Shorten module name if too long
                if len(module_name) > 15:
                    module_name = module_name[:15]
                return f"{label}:{module_name}"

    # Default: append occurrence number
    if occurrence > 1:
        return f"{label}:v{occurrence}"

    return label

def main():
    """Main function."""
    base_dir = Path('/home/eirikr/Playground/PhysicsForge/synthesis')

    if not base_dir.exists():
        print(f"Error: {base_dir} does not exist")
        return 1

    print(f"Scanning for duplicate labels in: {base_dir}")
    print("=" * 80)

    # Find all duplicates
    duplicates = find_duplicates(base_dir)

    if not duplicates:
        print("No duplicate labels found!")
        return 0

    print(f"\nFound {len(duplicates)} duplicate labels")
    print("=" * 80)

    # Categorize duplicates
    categories = defaultdict(list)
    for label in duplicates.keys():
        category = categorize_label(label)
        categories[category].append(label)

    # Print summary by category
    print("\nDuplicate labels by category:")
    for category in ['chapter', 'section', 'subsection', 'equation', 'figure', 'table',
                     'theorem', 'lemma', 'definition', 'proposition', 'corollary',
                     'remark', 'example', 'appendix', 'other']:
        if category in categories:
            print(f"  {category:15s}: {len(categories[category]):3d} duplicates")

    # Detailed analysis
    print("\n" + "=" * 80)
    print("DETAILED DUPLICATE ANALYSIS")
    print("=" * 80)

    # Sort by category priority
    priority_order = ['chapter', 'equation', 'section', 'figure', 'table',
                      'subsection', 'theorem', 'lemma', 'definition',
                      'proposition', 'corollary', 'remark', 'example',
                      'appendix', 'other']

    for category in priority_order:
        if category not in categories:
            continue

        print(f"\n{category.upper()} LABELS ({len(categories[category])} duplicates)")
        print("-" * 60)

        for label in sorted(categories[category]):
            locations = duplicates[label]
            print(f"\n  Label: \\label{{{label}}}")
            print(f"  Occurrences: {len(locations)}")

            for idx, (file_path, line_num, line_content) in enumerate(locations, 1):
                print(f"    [{idx}] {file_path}:{line_num}")
                print(f"        {line_content[:80]}{'...' if len(line_content) > 80 else ''}")

                # Suggest new name for duplicates
                if idx > 1:
                    new_label = suggest_new_label(label, file_path, idx)
                    if new_label != label:
                        print(f"        SUGGESTED: \\label{{{new_label}}}")

    return 0

if __name__ == "__main__":
    sys.exit(main())