#!/usr/bin/env python3
"""Remove specific lines from a file."""

import sys
from pathlib import Path

def remove_lines(filepath, lines_to_remove):
    """Remove specific line numbers from file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        all_lines = f.readlines()

    # Convert to set for O(1) lookup
    remove_set = set(lines_to_remove)

    # Keep only lines not in the removal set
    kept_lines = [line for i, line in enumerate(all_lines, start=1) if i not in remove_set]

    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(kept_lines)

    print(f"Removed {len(lines_to_remove)} lines from {filepath}")
    print(f"Lines removed: {sorted(lines_to_remove)}")

if __name__ == '__main__':
    filepath = Path(sys.argv[1])
    lines = [int(x) for x in sys.argv[2:]]

    remove_lines(filepath, lines)
