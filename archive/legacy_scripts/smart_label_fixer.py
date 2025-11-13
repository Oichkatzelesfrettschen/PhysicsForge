#!/usr/bin/env python3
"""
Smart label fixer that handles duplicate LaTeX labels intelligently.
Focuses on removing backup/expanded files and fixing remaining duplicates.
"""

import re
import shutil
import sys
from pathlib import Path
from collections import defaultdict
from typing import Dict, List, Tuple, Set

def find_tex_files(base_dir: Path, exclude_patterns: List[str] = None) -> List[Path]:
    """Recursively find all .tex files, optionally excluding patterns."""
    tex_files = []
    exclude_patterns = exclude_patterns or []

    for tex_file in base_dir.rglob('*.tex'):
        # Skip if matches any exclude pattern
        skip = False
        for pattern in exclude_patterns:
            if pattern in str(tex_file):
                skip = True
                break
        if not skip:
            tex_files.append(tex_file)

    return sorted(tex_files)

def extract_labels(file_path: Path) -> List[Tuple[str, int, str]]:
    """Extract all \label{} definitions from a file."""
    labels = []
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

def find_duplicates(base_dir: Path, exclude_patterns: List[str] = None) -> Dict[str, List[Tuple[Path, int, str]]]:
    """Find all duplicate labels in the project."""
    label_locations = defaultdict(list)

    # Find all tex files
    tex_files = find_tex_files(base_dir, exclude_patterns)
    print(f"Scanning {len(tex_files)} .tex files")

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

def identify_problem_files(duplicates: Dict) -> Set[Path]:
    """Identify backup and expanded files that should be removed/archived."""
    problem_files = set()

    for locations in duplicates.values():
        for file_path, _, _ in locations:
            file_str = str(file_path)
            if any(pattern in file_str for pattern in ['_backup', '_expanded', '_OLD', '_old', '_test']):
                problem_files.add(file_path)

    return problem_files

def fix_remaining_duplicates(base_dir: Path, duplicates: Dict, problem_files: Set[Path]) -> List[str]:
    """Generate sed commands to fix duplicates not in problem files."""
    fix_commands = []

    for label, locations in duplicates.items():
        # Filter out problem files
        valid_locations = [
            (path, line, content)
            for path, line, content in locations
            if path not in problem_files and not str(path).startswith('test_')
        ]

        if len(valid_locations) <= 1:
            continue  # No duplicates after filtering

        # Keep first occurrence, rename others
        for idx, (file_path, line_num, _) in enumerate(valid_locations[1:], 2):
            # Generate context-aware new label
            if 'chapters/' in str(file_path):
                match = re.search(r'ch(\d+)', str(file_path))
                if match:
                    ch_num = match.group(1)
                    new_label = f"{label}:ch{ch_num}"
                else:
                    new_label = f"{label}:v{idx}"
            elif 'modules/' in str(file_path):
                new_label = f"{label}:mod{idx}"
            else:
                new_label = f"{label}:v{idx}"

            # Generate sed command
            escaped_label = re.escape(label)
            sed_cmd = f"sed -i '{line_num}s/\\\\label{{{escaped_label}}}/\\\\label{{{new_label}}}/' {base_dir}/{file_path}"
            fix_commands.append(sed_cmd)

    return fix_commands

def main():
    """Main function."""
    base_dir = Path('/home/eirikr/Playground/PhysicsForge/synthesis')

    if not base_dir.exists():
        print(f"Error: {base_dir} does not exist")
        return 1

    print("=" * 80)
    print("SMART LABEL FIXER")
    print("=" * 80)

    # Step 1: Find all duplicates
    print("\n1. Finding duplicate labels...")
    duplicates = find_duplicates(base_dir)
    print(f"   Found {len(duplicates)} duplicate labels")

    if not duplicates:
        print("   No duplicates found! Nothing to fix.")
        return 0

    # Step 2: Identify problem files
    print("\n2. Identifying problem files...")
    problem_files = identify_problem_files(duplicates)
    print(f"   Found {len(problem_files)} backup/expanded files")

    if problem_files:
        print("\n   Files to archive/remove:")
        for file_path in sorted(problem_files):
            print(f"     - {file_path}")

    # Step 3: Archive problem files
    archive_dir = base_dir.parent / 'synthesis_archived_files'
    if problem_files and input("\n   Archive these files? (y/n): ").lower() == 'y':
        archive_dir.mkdir(exist_ok=True)
        for file_path in problem_files:
            src = base_dir / file_path
            dst = archive_dir / file_path
            dst.parent.mkdir(parents=True, exist_ok=True)
            print(f"     Moving {file_path} to archive...")
            shutil.move(str(src), str(dst))
        print(f"   Archived {len(problem_files)} files to {archive_dir}")

    # Step 4: Re-scan for remaining duplicates
    print("\n3. Re-scanning for remaining duplicates...")
    # Exclude archived files
    exclude_patterns = ['_backup', '_expanded', '_OLD', '_old'] if problem_files else []
    remaining_duplicates = find_duplicates(base_dir, exclude_patterns)

    # Filter out duplicates that only exist in test files
    filtered_duplicates = {}
    for label, locations in remaining_duplicates.items():
        non_test_locations = [
            loc for loc in locations
            if not str(loc[0]).startswith('test_')
        ]
        if len(non_test_locations) > 1:
            filtered_duplicates[label] = locations

    print(f"   Found {len(filtered_duplicates)} remaining duplicates (excluding test files)")

    if not filtered_duplicates:
        print("   No duplicates remain after archiving!")
        return 0

    # Step 5: Generate fix commands for remaining duplicates
    print("\n4. Generating fixes for remaining duplicates...")
    fix_commands = fix_remaining_duplicates(base_dir, filtered_duplicates, set())

    if fix_commands:
        print(f"   Generated {len(fix_commands)} fix commands")

        # Write fix script
        fix_script = base_dir.parent / 'fix_remaining_labels.sh'
        with open(fix_script, 'w') as f:
            f.write("#!/bin/bash\n")
            f.write("# Fix remaining duplicate labels\n")
            f.write("set -e\n\n")
            f.write(f"cd {base_dir}\n\n")
            f.write("echo 'Applying fixes...'\n")
            for cmd in fix_commands:
                f.write(f"{cmd}\n")
            f.write("\necho 'Done!'\n")

        fix_script.chmod(0o755)
        print(f"\n   Fix script written to: {fix_script}")
        print(f"   Run with: bash {fix_script}")

    # Step 6: Summary
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"Original duplicates: {len(duplicates)}")
    print(f"Files archived: {len(problem_files)}")
    print(f"Remaining duplicates: {len(filtered_duplicates)}")
    print(f"Fix commands generated: {len(fix_commands)}")

    print("\nNext steps:")
    print("1. Review archived files in:", archive_dir if problem_files else "N/A")
    print("2. Run fix script if needed:", f"bash {fix_script}" if fix_commands else "N/A")
    print("3. Test compilation: cd synthesis && pdflatex main.tex")
    print("4. Check for undefined references in main.log")

    return 0

if __name__ == "__main__":
    sys.exit(main())