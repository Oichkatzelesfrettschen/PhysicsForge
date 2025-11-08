#!/usr/bin/env python3
"""Find all locations where balance drops (excess closing braces)."""

import sys
from pathlib import Path

def find_excess_braces(filepath):
    """Find all lines where cumulative balance decreases."""
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    balance = 0
    balance_drops = []

    for i, line in enumerate(lines, start=1):
        # Skip comments
        clean_line = line
        if '%' in line:
            idx = 0
            while idx < len(line):
                if line[idx] == '%' and (idx == 0 or line[idx-1] != '\\'):
                    clean_line = line[:idx]
                    break
                idx += 1

        open_count = clean_line.count('{')
        close_count = clean_line.count('}')

        prev_balance = balance
        balance += open_count - close_count

        # Record when balance decreases
        if balance < prev_balance:
            balance_drops.append((i, line.rstrip(), prev_balance, balance, close_count - open_count))

    return balance, balance_drops

if __name__ == '__main__':
    filepath = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('chapters/unification/ch19_master_equation.tex')

    final_balance, drops = find_excess_braces(filepath)

    print(f"File: {filepath}")
    print(f"Final balance: {final_balance}")
    print(f"\nLines where balance decreased (potential excess closing braces):")
    print(f"{'Line':<7} {'Prev Bal':<10} {'New Bal':<10} {'Excess':<8} Content")
    print("-" * 80)

    for line_num, content, prev, new, excess in drops:
        if excess > 0:  # More closing than opening
            print(f"{line_num:<7} {prev:<10} {new:<10} {excess:<8} {content[:50]}")
