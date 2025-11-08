#!/usr/bin/env python3
"""
Generate a comprehensive plan to fix duplicate LaTeX labels with automated sed commands.
"""

import re
import sys
from pathlib import Path
from collections import defaultdict, OrderedDict
from typing import Dict, List, Tuple

def find_tex_files(base_dir: Path) -> List[Path]:
    """Recursively find all .tex files."""
    tex_files = []
    for pattern in ['*.tex']:
        tex_files.extend(base_dir.rglob(pattern))
    return sorted(tex_files)

def extract_labels_and_refs(file_path: Path) -> Tuple[List[Tuple[str, int, str]], List[Tuple[str, int, str]]]:
    """Extract all \label{} and \ref{} from a file.
    Returns (labels, refs) where each is a list of (label, line_number, line_content) tuples."""
    labels = []
    refs = []

    # Patterns to match \label{...} and \ref{...}
    label_pattern = re.compile(r'\\label\{([^}]+)\}')
    ref_patterns = [
        re.compile(r'\\ref\{([^}]+)\}'),
        re.compile(r'\\eqref\{([^}]+)\}'),
        re.compile(r'\\cref\{([^}]+)\}'),
        re.compile(r'\\Cref\{([^}]+)\}'),
        re.compile(r'\\pageref\{([^}]+)\}'),
        re.compile(r'\\autoref\{([^}]+)\}'),
        re.compile(r'\\nameref\{([^}]+)\}'),
    ]

    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()

        for line_num, line in enumerate(lines, 1):
            # Find labels
            matches = label_pattern.findall(line)
            for label in matches:
                labels.append((label.strip(), line_num, line.strip()))

            # Find refs
            for ref_pattern in ref_patterns:
                matches = ref_pattern.findall(line)
                for ref in matches:
                    refs.append((ref.strip(), line_num, line.strip()))

    except Exception as e:
        print(f"Error reading {file_path}: {e}", file=sys.stderr)

    return labels, refs

def find_duplicates_and_refs(base_dir: Path) -> Tuple[Dict[str, List[Tuple[Path, int, str]]], Dict[str, List[Tuple[Path, int, str]]]]:
    """Find all duplicate labels and all references in the project.
    Returns (duplicates, all_refs)."""

    label_locations = defaultdict(list)
    ref_locations = defaultdict(list)

    # Find all tex files
    tex_files = find_tex_files(base_dir)

    # Extract labels and refs from each file
    for tex_file in tex_files:
        rel_path = tex_file.relative_to(base_dir)
        labels, refs = extract_labels_and_refs(tex_file)

        for label, line_num, line_content in labels:
            label_locations[label].append((rel_path, line_num, line_content))

        for ref, line_num, line_content in refs:
            ref_locations[ref].append((rel_path, line_num, line_content))

    # Filter to only duplicates
    duplicates = {
        label: locations
        for label, locations in label_locations.items()
        if len(locations) > 1
    }

    return duplicates, ref_locations

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
    else:
        return 'other'

def suggest_new_label(label: str, file_path: Path, occurrence: int) -> str:
    """Suggest a new label name for a duplicate based on context."""

    # Special handling for backup and expanded files
    if '_backup' in str(file_path) or '_expanded' in str(file_path):
        # These are alternative versions - should be deleted or renamed significantly
        suffix = 'backup' if '_backup' in str(file_path) else 'expanded'
        return f"{label}:{suffix}"

    # For test files, don't rename (they're just including the main content)
    if str(file_path).startswith('test_'):
        return label  # Keep original

    # Extract chapter number if in chapters/ directory
    if 'chapters/' in str(file_path):
        match = re.search(r'ch(\d+)', str(file_path))
        if match:
            ch_num = match.group(1)
            # Only rename if it's the second+ occurrence
            if occurrence > 1:
                # Insert chapter number contextually
                if label.startswith('eq:'):
                    parts = label.split(':', 2)
                    if len(parts) >= 3:
                        # eq:framework:descriptor -> eq:framework:ch##:descriptor
                        return f"{parts[0]}:{parts[1]}:ch{ch_num}:{parts[2]}"
                    elif len(parts) == 2:
                        # eq:descriptor -> eq:ch##:descriptor
                        return f"{parts[0]}:ch{ch_num}:{parts[1]}"
                else:
                    # Other labels: append :ch##
                    return f"{label}:ch{ch_num}"

    # For modules, use module name
    if 'modules/' in str(file_path):
        if 'equations/' in str(file_path):
            match = re.search(r'eq_([^/]+)\.tex', str(file_path))
            if match and occurrence > 1:
                module_name = match.group(1)
                # Shorten if needed
                if len(module_name) > 20:
                    # Take first and last parts
                    parts = module_name.split('_')
                    if len(parts) > 2:
                        module_name = f"{parts[0]}_{parts[-1]}"
                return f"{label}:mod_{module_name}"

    # Default for other duplicates
    if occurrence > 1:
        return f"{label}:alt{occurrence}"

    return label

def generate_fix_commands(duplicates: Dict, ref_locations: Dict, base_dir: Path) -> List[Dict]:
    """Generate sed commands to fix duplicates."""

    fix_commands = []
    label_renames = {}  # Track what we're renaming labels to

    # Sort duplicates by priority
    priority_order = ['chapter', 'equation', 'section', 'figure', 'table', 'subsection', 'other']
    sorted_labels = sorted(duplicates.keys(),
                          key=lambda x: (priority_order.index(categorize_label(x))
                                        if categorize_label(x) in priority_order else 999, x))

    for label in sorted_labels:
        locations = duplicates[label]

        # Determine which file should keep the original label
        # Priority: main chapter files > modules > backup/expanded files
        primary_idx = 0
        for idx, (file_path, _, _) in enumerate(locations):
            file_str = str(file_path)
            # Skip test files
            if file_str.startswith('test_'):
                continue
            # Deprioritize backup and expanded files
            if '_backup' in file_str or '_expanded' in file_str:
                continue
            # This is a good candidate for primary
            primary_idx = idx
            break

        # Generate rename commands for non-primary occurrences
        for idx, (file_path, line_num, _) in enumerate(locations):
            if str(file_path).startswith('test_'):
                continue  # Don't modify test files

            if idx != primary_idx:
                new_label = suggest_new_label(label, file_path, idx + 1)
                if new_label != label:
                    label_renames[label] = label_renames.get(label, [])
                    label_renames[label].append((file_path, new_label))

                    # Generate sed command for label
                    fix_commands.append({
                        'type': 'rename_label',
                        'file': file_path,
                        'line': line_num,
                        'old_label': label,
                        'new_label': new_label,
                        'sed_cmd': f"sed -i '{line_num}s/\\\\label{{{re.escape(label)}}}/\\\\label{{{new_label}}}/' {base_dir}/{file_path}"
                    })

                    # Check if this label has references that need updating
                    if label in ref_locations:
                        refs_in_same_file = [
                            (ref_line, ref_content)
                            for ref_file, ref_line, ref_content in ref_locations[label]
                            if ref_file == file_path
                        ]

                        for ref_line, _ in refs_in_same_file:
                            fix_commands.append({
                                'type': 'update_ref',
                                'file': file_path,
                                'line': ref_line,
                                'old_ref': label,
                                'new_ref': new_label,
                                'sed_cmd': f"sed -i '{ref_line}s/\\(\\\\[a-z]*ref\\){{{re.escape(label)}}}/\\1{{{new_label}}}/' {base_dir}/{file_path}"
                            })

    return fix_commands

def main():
    """Main function."""
    base_dir = Path('/home/eirikr/Playground/PhysicsForge/synthesis')
    output_file = Path('/home/eirikr/Playground/PhysicsForge/DUPLICATE_LABEL_FIX_PLAN.md')

    if not base_dir.exists():
        print(f"Error: {base_dir} does not exist")
        return 1

    print(f"Analyzing duplicate labels in: {base_dir}")

    # Find all duplicates and references
    duplicates, ref_locations = find_duplicates_and_refs(base_dir)

    if not duplicates:
        print("No duplicate labels found!")
        return 0

    print(f"Found {len(duplicates)} duplicate labels")

    # Generate fix commands
    fix_commands = generate_fix_commands(duplicates, ref_locations, base_dir)

    # Write fix plan
    with open(output_file, 'w') as f:
        f.write("# DUPLICATE LABEL FIX PLAN\n")
        f.write(f"Generated: {Path.cwd()}\n")
        f.write(f"Total duplicates found: {len(duplicates)}\n")
        f.write(f"Total fix commands: {len(fix_commands)}\n\n")

        # Summary by category
        f.write("## Summary by Category\n\n")
        categories = defaultdict(list)
        for label in duplicates.keys():
            category = categorize_label(label)
            categories[category].append(label)

        for category in ['chapter', 'equation', 'section', 'figure', 'table', 'subsection', 'other']:
            if category in categories:
                f.write(f"- **{category}**: {len(categories[category])} duplicates\n")

        f.write("\n## Fix Strategy\n\n")
        f.write("1. **Backup files** (`*_backup.tex`, `*_expanded.tex`): Rename labels with `:backup` or `:expanded` suffix\n")
        f.write("2. **Chapter duplicates**: Add `:ch##` suffix where ## is chapter number\n")
        f.write("3. **Equation duplicates**: Insert `:ch##:` after framework prefix\n")
        f.write("4. **Module duplicates**: Add `:mod_<module_name>` suffix\n")
        f.write("5. **Test files**: Not modified (they include the main content)\n\n")

        # Detailed fixes by category
        f.write("## Detailed Fix Commands\n\n")

        # Group commands by file for efficiency
        commands_by_file = defaultdict(list)
        for cmd in fix_commands:
            commands_by_file[cmd['file']].append(cmd)

        # Write fix script
        f.write("### Automated Fix Script\n\n")
        f.write("Save the following as `fix_duplicate_labels.sh` and run with `bash fix_duplicate_labels.sh`:\n\n")
        f.write("```bash\n")
        f.write("#!/bin/bash\n")
        f.write("# Fix duplicate LaTeX labels\n")
        f.write("set -e\n\n")
        f.write("cd /home/eirikr/Playground/PhysicsForge/synthesis\n\n")
        f.write("echo 'Creating backup...'\n")
        f.write("tar -czf ../synthesis_backup_$(date +%Y%m%d_%H%M%S).tar.gz .\n\n")

        for file_path, commands in sorted(commands_by_file.items()):
            f.write(f"\n# Fixing {file_path} ({len(commands)} changes)\n")
            f.write(f"echo 'Fixing {file_path}...'\n")

            # Sort by line number (descending) to avoid line number shifts
            commands_sorted = sorted(commands, key=lambda x: x['line'], reverse=True)

            for cmd in commands_sorted:
                if cmd['type'] == 'rename_label':
                    f.write(f"# Line {cmd['line']}: {cmd['old_label']} -> {cmd['new_label']}\n")
                    f.write(f"{cmd['sed_cmd']}\n")

        f.write("\necho 'All fixes applied!'\n")
        f.write("```\n\n")

        # List of all duplicates with details
        f.write("## Complete Duplicate List\n\n")

        for category in ['chapter', 'equation', 'section', 'figure', 'table', 'subsection', 'other']:
            if category not in categories:
                continue

            f.write(f"### {category.upper()} Labels\n\n")

            for label in sorted(categories[category]):
                locations = duplicates[label]
                f.write(f"#### `\\label{{{label}}}`\n")
                f.write(f"Occurrences: {len(locations)}\n\n")

                for idx, (file_path, line_num, line_content) in enumerate(locations):
                    f.write(f"{idx + 1}. `{file_path}:{line_num}`\n")

                    # Show suggested rename
                    if not str(file_path).startswith('test_'):
                        new_label = suggest_new_label(label, file_path, idx + 1)
                        if new_label != label and idx > 0:
                            f.write(f"   - **Rename to**: `\\label{{{new_label}}}`\n")

                f.write("\n")

        # Validation steps
        f.write("## Validation Steps\n\n")
        f.write("After running the fix script:\n\n")
        f.write("1. **Re-run duplicate finder**:\n")
        f.write("   ```bash\n")
        f.write("   python /home/eirikr/Playground/PhysicsForge/find_duplicate_labels.py\n")
        f.write("   ```\n\n")
        f.write("2. **Test compilation**:\n")
        f.write("   ```bash\n")
        f.write("   cd /home/eirikr/Playground/PhysicsForge/synthesis\n")
        f.write("   pdflatex main.tex\n")
        f.write("   ```\n\n")
        f.write("3. **Check for undefined references**:\n")
        f.write("   ```bash\n")
        f.write("   grep -n 'Undefined' main.log\n")
        f.write("   ```\n\n")
        f.write("4. **Verify no new duplicates introduced**:\n")
        f.write("   ```bash\n")
        f.write("   grep -rn '\\\\label{' . | sort | uniq -d\n")
        f.write("   ```\n\n")

        f.write("## Files to Consider Removing\n\n")
        f.write("The following backup/expanded files contain duplicates and should be reviewed:\n\n")

        backup_files = set()
        for locations in duplicates.values():
            for file_path, _, _ in locations:
                file_str = str(file_path)
                if '_backup' in file_str or '_expanded' in file_str:
                    backup_files.add(file_path)

        for file_path in sorted(backup_files):
            f.write(f"- `{file_path}`\n")

        f.write("\nConsider removing these files or moving them to an archive directory.\n")

    print(f"\nFix plan written to: {output_file}")
    print(f"Total fix commands generated: {len(fix_commands)}")

    return 0

if __name__ == "__main__":
    sys.exit(main())