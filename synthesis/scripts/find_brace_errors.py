#!/usr/bin/env python3
"""Find brace mismatch locations in LaTeX files."""

import sys
from pathlib import Path

def analyze_braces(filepath):
    """Analyze brace balance line by line."""
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    balance = 0
    problematic_lines = []

    for i, line in enumerate(lines, start=1):
        # Skip comments
        if '%' in line:
            # Find first % not escaped
            idx = 0
            while idx < len(line):
                if line[idx] == '%' and (idx == 0 or line[idx-1] != '\\'):
                    line = line[:idx]
                    break
                idx += 1

        open_count = line.count('{')
        close_count = line.count('}')

        prev_balance = balance
        balance += open_count - close_count

        # Track lines that go negative (excess closing braces)
        if balance < prev_balance and balance < 0:
            problematic_lines.append((i, line.strip(), balance, open_count, close_count))
        elif balance < 0:
            problematic_lines.append((i, line.strip(), balance, open_count, close_count))

    return balance, problematic_lines

if __name__ == '__main__':
    filepath = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('chapters/unification/ch19_master_equation.tex')

    balance, problematic = analyze_braces(filepath)

    print(f"File: {filepath}")
    print(f"Final balance: {balance} ({'excess closing' if balance < 0 else 'unclosed opening'} braces)")
    print(f"\nProblematic lines (negative balance):")

    for line_num, content, bal, open_br, close_br in problematic:
        print(f"  Line {line_num}: balance={bal} (open={open_br}, close={close_br})")
        print(f"    {content[:100]}")
