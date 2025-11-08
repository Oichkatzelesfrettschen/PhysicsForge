#!/usr/bin/env python3
"""
Comprehensive duplicate label analysis for PhysicsForge LaTeX project.
Finds all duplicate labels and categorizes them by type and root cause.
"""

import re
import os
from pathlib import Path
from collections import defaultdict, Counter
from typing import Dict, List, Tuple, Set

def find_labels_in_file(filepath: Path) -> List[Tuple[str, int, str]]:
    """Extract all labels from a file with line numbers."""
    labels = []
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            for line_num, line in enumerate(f, 1):
                # Find all \label{...} patterns
                matches = re.findall(r'\\label\{([^}]+)\}', line)
                for label in matches:
                    labels.append((label, line_num, str(filepath)))
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
    return labels

def find_input_statements(filepath: Path) -> List[Tuple[str, int]]:
    """Find all \input statements in a file."""
    inputs = []
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            for line_num, line in enumerate(f, 1):
                matches = re.findall(r'\\input\{([^}]+)\}', line)
                for input_file in matches:
                    inputs.append((input_file, line_num))
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
    return inputs

def categorize_label(label: str) -> str:
    """Categorize label by its prefix."""
    if label.startswith('eq:'):
        return 'equation'
    elif label.startswith('fig:'):
        return 'figure'
    elif label.startswith('tab:'):
        return 'table'
    elif label.startswith('ch:'):
        return 'chapter'
    elif label.startswith('sec:') or label.startswith('subsec:'):
        return 'section'
    elif label.startswith('part:'):
        return 'part'
    else:
        return 'other'

def analyze_duplicates(base_path: Path):
    """Main analysis function."""
    print("Analyzing duplicate labels in PhysicsForge LaTeX project...")
    print("=" * 80)

    # Collect all labels
    all_labels = []
    tex_files = []

    # Find all .tex files
    for root, dirs, files in os.walk(base_path / 'synthesis'):
        # Skip backup directories and build artifacts
        dirs[:] = [d for d in dirs if d not in ['build', '.git', '__pycache__']]
        for file in files:
            if file.endswith('.tex') and not file.endswith('.bak'):
                filepath = Path(root) / file
                tex_files.append(filepath)
                labels = find_labels_in_file(filepath)
                all_labels.extend(labels)

    print(f"Found {len(tex_files)} .tex files")
    print(f"Found {len(all_labels)} total label definitions")

    # Count occurrences
    label_counts = Counter([label for label, _, _ in all_labels])
    duplicates = {label: count for label, count in label_counts.items() if count > 1}

    print(f"Found {len(duplicates)} duplicate labels")
    print()

    # Categorize duplicates
    categories = defaultdict(list)
    for label in duplicates:
        category = categorize_label(label)
        categories[category].append(label)

    # Create detailed report
    report = []
    report.append("# DUPLICATE LABELS ANALYSIS")
    report.append("")
    report.append("## Executive Summary")
    report.append("")
    report.append(f"- **Total .tex files analyzed:** {len(tex_files)}")
    report.append(f"- **Total label definitions found:** {len(all_labels)}")
    report.append(f"- **Unique labels:** {len(label_counts)}")
    report.append(f"- **Duplicate labels:** {len(duplicates)}")
    report.append("")
    report.append("### Duplicates by Category")
    report.append("")
    report.append("| Category | Count | Percentage |")
    report.append("|----------|-------|------------|")

    total_dups = len(duplicates)
    for cat in ['equation', 'figure', 'table', 'chapter', 'section', 'part', 'other']:
        count = len(categories.get(cat, []))
        pct = (count / total_dups * 100) if total_dups > 0 else 0
        report.append(f"| {cat.capitalize()} | {count} | {pct:.1f}% |")

    report.append("")
    report.append("## Detailed Duplicate Analysis")
    report.append("")

    # Analyze root causes
    module_reuse = []
    framework_collision = []
    copy_paste = []
    auto_manual = []

    for label, count in sorted(duplicates.items(), key=lambda x: x[1], reverse=True):
        locations = [(l, f) for l, _, f in all_labels if l == label]

        report.append(f"### Label: `{label}` (appears {count} times)")
        report.append("")
        report.append("**Category:** " + categorize_label(label))
        report.append("")
        report.append("**Locations:**")
        report.append("")

        # Get detailed locations
        for lbl, filepath in locations:
            matching_labels = [item for item in all_labels if item[0] == lbl and item[2] == filepath]
            for _, line_num, _ in matching_labels:
                relative_path = Path(filepath).relative_to(base_path)
                report.append(f"- `{relative_path}:{line_num}`")

        # Determine root cause
        files = list(set([f for _, f in locations]))
        if 'modules/equations' in str(files[0]) and len(files) == 1:
            # Check if module is included multiple times
            module_name = Path(files[0]).name
            includes = []
            for tex_file in tex_files:
                if 'chapters' in str(tex_file):
                    inputs = find_input_statements(tex_file)
                    for input_file, line in inputs:
                        if module_name.replace('.tex', '') in input_file:
                            includes.append((tex_file, line))

            if len(includes) > 1:
                module_reuse.append(label)
                report.append("")
                report.append("**Root Cause:** MODULE REUSE - Same equation module included in multiple chapters")
            else:
                # Labels within same module file
                if count > 1 and len(files) == 1:
                    copy_paste.append(label)
                    report.append("")
                    report.append("**Root Cause:** MULTIPLE LABELS IN SAME FILE - Multiple label definitions in single file")

        elif any('_auto' in str(f) for f in files):
            auto_manual.append(label)
            report.append("")
            report.append("**Root Cause:** AUTO-MANUAL CONFLICT - Auto-generated file conflicts with manual")

        elif label.startswith('eq:') and any(fw in label for fw in ['aether', 'genesis', 'pais']):
            framework_collision.append(label)
            report.append("")
            report.append("**Root Cause:** FRAMEWORK COLLISION - Same label used across framework boundaries")

        else:
            copy_paste.append(label)
            report.append("")
            report.append("**Root Cause:** COPY-PASTE ERROR - Simple duplication")

        report.append("")
        report.append("---")
        report.append("")

    # Resolution strategies
    report.append("## Resolution Strategy")
    report.append("")
    report.append("### Priority Order (Most Impactful First)")
    report.append("")
    report.append("1. **Fix Multiple Labels in Single File** ({} labels)".format(
        len([l for l in copy_paste if label_counts[l] > 1])))
    report.append("   - These are likely from multi-line align environments with repeated labels")
    report.append("   - Resolution: Keep only first label in align block")
    report.append("")

    report.append("2. **Module Reuse Issues** ({} labels)".format(len(module_reuse)))
    report.append("   - Resolution: Labels should be unique in modules, no action needed if properly used")
    report.append("   - Verify modules are not defining duplicate labels internally")
    report.append("")

    report.append("3. **Framework Collisions** ({} labels)".format(len(framework_collision)))
    report.append("   - Resolution: Add chapter prefix: `eq:chNN:framework:descriptor`")
    report.append("")

    report.append("4. **Auto-Manual Conflicts** ({} labels)".format(len(auto_manual)))
    report.append("   - Resolution: Rename auto labels with `:auto:` prefix")
    report.append("")

    report.append("5. **Copy-Paste Errors** ({} labels)".format(
        len([l for l in copy_paste if l not in module_reuse])))
    report.append("   - Resolution: Remove duplicate, keep first occurrence")
    report.append("")

    # Quick fixes
    report.append("## Quick Fix Commands")
    report.append("")
    report.append("### Find and review specific duplicates:")
    report.append("```bash")
    report.append("# Example: Fix eq:prelim:commutator-xx")
    report.append('grep -rn "\\\\label{eq:prelim:commutator-xx}" synthesis/')
    report.append("```")
    report.append("")

    report.append("### Check for labels in backup files:")
    report.append("```bash")
    report.append('find synthesis -name "*.bak" -exec grep -l "\\\\label{" {} \\;')
    report.append("```")
    report.append("")

    report.append("### Verify no duplicate labels after fixes:")
    report.append("```bash")
    report.append('grep -r "\\\\label{" synthesis --include="*.tex" | ')
    report.append('  grep -o "\\\\label{[^}]*}" | sort | uniq -d')
    report.append("```")
    report.append("")

    # Summary statistics
    report.append("## Statistics Summary")
    report.append("")
    report.append("| Metric | Value |")
    report.append("|--------|-------|")
    report.append(f"| Total Labels | {len(all_labels)} |")
    report.append(f"| Unique Labels | {len(label_counts)} |")
    report.append(f"| Duplicate Labels | {len(duplicates)} |")
    report.append(f"| Duplication Rate | {len(duplicates)/len(label_counts)*100:.1f}% |")
    report.append(f"| Most Duplicated | {max(duplicates.values()) if duplicates else 0} times |")

    return "\n".join(report)

if __name__ == "__main__":
    base_path = Path("/home/eirikr/Playground/PhysicsForge")
    report = analyze_duplicates(base_path)

    # Save report
    output_file = base_path / "DUPLICATE_LABELS_ANALYSIS.md"
    with open(output_file, 'w') as f:
        f.write(report)

    print(f"\nReport saved to: {output_file}")

    # Also print summary to console
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    lines = report.split('\n')
    for line in lines[4:20]:  # Print executive summary section
        print(line)