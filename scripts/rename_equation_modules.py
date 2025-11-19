#!/usr/bin/env python3
"""
Rename equation module files from branded terms to standard physics terms.
Part of PhysicsForge Framework Unification Phase 2.
"""

import argparse
import csv
import re
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Tuple


def get_rename_mapping() -> Dict[str, str]:
    """Define the comprehensive rename mapping."""
    return {
        # Full word replacements
        "aether": "scalar",
        "genesis": "symm",
        "pais": "gem",
        "unified": "physforge",

        # Auto-generated prefixes
        "eq_ae": "eq_sc",
        "eq_ge": "eq_sx",
        "eq_pe": "eq_gm",
        "eq_ue": "eq_pf",
    }


def find_equation_files(base_dir: Path) -> List[Path]:
    """Find all equation module files."""
    equations_dir = base_dir / "synthesis" / "modules" / "equations"
    if not equations_dir.exists():
        raise FileNotFoundError(f"Equations directory not found: {equations_dir}")

    return sorted(equations_dir.glob("eq_*.tex"))


def determine_new_name(file_path: Path, mapping: Dict[str, str]) -> str:
    """Determine the new name for a file based on mapping rules."""
    filename = file_path.name
    new_name = filename

    # First check auto-generated patterns (more specific)
    for old_prefix, new_prefix in mapping.items():
        if old_prefix.startswith("eq_") and filename.startswith(old_prefix):
            # Handle auto-generated files (eq_ae001_auto.tex -> eq_sc001_auto.tex)
            if re.match(rf"^{re.escape(old_prefix)}\d", filename):
                new_name = filename.replace(old_prefix, new_prefix, 1)
                return new_name

    # Then check full word replacements
    for old_term, new_term in mapping.items():
        if not old_term.startswith("eq_"):  # Skip prefix patterns
            if f"_{old_term}_" in filename or filename.startswith(f"eq_{old_term}_"):
                new_name = filename.replace(f"_{old_term}_", f"_{new_term}_")
                new_name = new_name.replace(f"eq_{old_term}_", f"eq_{new_term}_")

    return new_name


def find_files_to_rename(base_dir: Path) -> List[Tuple[Path, str]]:
    """Find all files that need renaming."""
    mapping = get_rename_mapping()
    files = find_equation_files(base_dir)
    to_rename = []

    for file_path in files:
        new_name = determine_new_name(file_path, mapping)
        if new_name != file_path.name:
            to_rename.append((file_path, new_name))

    return to_rename


def find_chapter_files(base_dir: Path) -> List[Path]:
    """Find all chapter files that might contain references."""
    chapters_dir = base_dir / "synthesis" / "chapters"
    chapter_files = []

    if chapters_dir.exists():
        for subdir in chapters_dir.iterdir():
            if subdir.is_dir():
                chapter_files.extend(subdir.glob("*.tex"))

    # Also check unification equations subdirectory
    unif_eq_dir = base_dir / "synthesis" / "chapters" / "unification" / "equations"
    if unif_eq_dir.exists():
        chapter_files.extend(unif_eq_dir.glob("*.tex"))

    return sorted(chapter_files)


def update_references_in_file(file_path: Path, renames: List[Tuple[str, str]],
                             dry_run: bool = True) -> int:
    r"""Update \input references in a file."""
    if not file_path.exists():
        return 0

    content = file_path.read_text(encoding='utf-8')
    changes = 0

    for old_name, new_name in renames:
        # Check with .tex extension (which is what the files actually use)
        pattern = f'\\input{{modules/equations/{old_name}}}'
        replacement = f'\\input{{modules/equations/{new_name}}}'

        if pattern in content:
            occurrences = content.count(pattern)
            content = content.replace(pattern, replacement)
            changes += occurrences

    if changes > 0 and not dry_run:
        file_path.write_text(content, encoding='utf-8')

    return changes


def perform_renames(base_dir: Path, dry_run: bool = True) -> None:
    """Perform the renaming operation."""
    timestamp = datetime.now().isoformat()

    # Find files to rename
    print("\n" + "="*70)
    print("PHASE 2: EQUATION MODULE RENAMING")
    print("="*70)

    to_rename = find_files_to_rename(base_dir)

    if not to_rename:
        print("\nNo files need renaming.")
        return

    # Display summary
    print(f"\nFound {len(to_rename)} files to rename:")

    # Count by category
    categories = {
        'aether': 0,
        'genesis': 0,
        'pais': 0,
        'unified': 0,
        'ae': 0,
        'ge': 0,
        'pe': 0,
        'ue': 0,
    }

    for old_path, new_name in to_rename:
        old_name = old_path.name
        if 'aether' in old_name:
            categories['aether'] += 1
        elif 'genesis' in old_name:
            categories['genesis'] += 1
        elif 'pais' in old_name:
            categories['pais'] += 1
        elif 'unified' in old_name:
            categories['unified'] += 1
        elif old_name.startswith('eq_ae'):
            categories['ae'] += 1
        elif old_name.startswith('eq_ge'):
            categories['ge'] += 1
        elif old_name.startswith('eq_pe'):
            categories['pe'] += 1
        elif old_name.startswith('eq_ue'):
            categories['ue'] += 1

    print("\nBreakdown by category:")
    print(f"  - Aether -> Scalar: {categories['aether']} files")
    print(f"  - Genesis -> Symmetry: {categories['genesis']} files")
    print(f"  - Pais -> GEM: {categories['pais']} files")
    print(f"  - Unified -> PhysicsForge: {categories['unified']} files")
    print(f"  - Auto AE -> SC: {categories['ae']} files")
    print(f"  - Auto GE -> SX: {categories['ge']} files")
    print(f"  - Auto PE -> GM: {categories['pe']} files")
    print(f"  - Auto UE -> PF: {categories['ue']} files")

    if dry_run:
        print("\n" + "="*70)
        print("DRY RUN MODE - No changes will be made")
        print("="*70)

        # Show sample renames
        print("\nSample renames (first 20):")
        for i, (old_path, new_name) in enumerate(to_rename[:20]):
            print(f"  {old_path.name}")
            print(f"    -> {new_name}")

        if len(to_rename) > 20:
            print(f"\n  ... and {len(to_rename) - 20} more files")
    else:
        print("\n" + "="*70)
        print("EXECUTE MODE - Performing renames")
        print("="*70)

        # Create CSV log
        log_file = base_dir / "EQUATION_RENAME_LOG.csv"
        with open(log_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['old_name', 'new_name', 'timestamp'])

            # Perform renames
            renamed_files = []
            for old_path, new_name in to_rename:
                new_path = old_path.parent / new_name

                # Check for conflicts
                if new_path.exists():
                    print(f"WARNING: Target exists, skipping: {new_name}")
                    continue

                # Rename the file
                old_path.rename(new_path)
                renamed_files.append((old_path.name, new_name))
                writer.writerow([old_path.name, new_name, timestamp])
                print(f"  Renamed: {old_path.name} -> {new_name}")

        print(f"\nRenamed {len(renamed_files)} files successfully")
        print(f"Log saved to: {log_file}")

    # Find and update references
    print("\n" + "="*70)
    print("UPDATING REFERENCES IN CHAPTERS")
    print("="*70)

    chapter_files = find_chapter_files(base_dir)
    print(f"\nFound {len(chapter_files)} chapter files to check")

    # Prepare rename list for reference updates
    rename_list = [(old_path.name, new_name) for old_path, new_name in to_rename]

    total_updates = 0
    updated_files = []

    for chapter_file in chapter_files:
        updates = update_references_in_file(chapter_file, rename_list, dry_run)
        if updates > 0:
            total_updates += updates
            updated_files.append((chapter_file.relative_to(base_dir), updates))
            if not dry_run:
                print(f"  Updated {updates} references in: {chapter_file.name}")

    print(f"\nTotal references to update: {total_updates} in {len(updated_files)} files")

    if dry_run:
        print("\nFiles that would be updated:")
        for file_path, count in updated_files[:10]:
            print(f"  {file_path}: {count} references")
        if len(updated_files) > 10:
            print(f"  ... and {len(updated_files) - 10} more files")

    # Final summary
    print("\n" + "="*70)
    print("SUMMARY")
    print("="*70)
    print(f"Files to rename: {len(to_rename)}")
    print(f"References to update: {total_updates}")
    print(f"Chapter files affected: {len(updated_files)}")

    if dry_run:
        print("\nTo execute these changes, run with --execute flag")
    else:
        print("\nRenaming completed successfully!")


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Rename equation modules from branded to standard terms"
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        '--dry-run',
        action='store_true',
        help='Show what would be renamed without making changes'
    )
    group.add_argument(
        '--execute',
        action='store_true',
        help='Perform actual renames'
    )
    parser.add_argument(
        '--base-dir',
        type=Path,
        default=Path.cwd(),
        help='Base directory of the repository (default: current directory)'
    )

    args = parser.parse_args()

    # Verify we're in the right location
    if not (args.base_dir / "synthesis" / "modules" / "equations").exists():
        print(f"ERROR: Cannot find synthesis/modules/equations in {args.base_dir}")
        print("Please run from the repository root or specify --base-dir")
        return 1

    try:
        perform_renames(args.base_dir, dry_run=args.dry_run)
        return 0
    except Exception as e:
        print(f"ERROR: {e}")
        return 1


if __name__ == "__main__":
    exit(main())