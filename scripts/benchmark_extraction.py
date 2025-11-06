"""
Benchmark extraction and merge steps without external deps.
Writes BENCHMARK.md with durations and basic throughput metrics.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
import time
from pathlib import Path


def run(cmd: list[str]) -> tuple[float, bool]:
    t0 = time.perf_counter()
    rc = subprocess.call(cmd)
    t1 = time.perf_counter()
    success = rc == 0
    if not success:
        print('Command failed:', ' '.join(cmd))
    return t1 - t0, success


def main() -> None:
    ap = argparse.ArgumentParser(description='Benchmark extraction/merge steps')
    ap.add_argument('--base-dir', type=str, default='.', help='Repository root')
    ap.add_argument('--scan-dir', action='append', help='Directories to scan (repeatable)')
    args = ap.parse_args()

    base = str(Path(args.base_dir).resolve())
    scans = args.scan_dir or ['notes', '.']

    had_errors = False
    timings: dict[str, float | str] = {}
    time_taken, success = run([sys.executable, 'scripts/equation_extractor.py', '--base-dir', base, *sum((["--scan-dir", s] for s in scans), [])])
    if not success:
        had_errors = True
        timings['extract_text'] = "FAILED"
    else:
        timings['extract_text'] = time_taken
    time_taken, success = run([sys.executable, 'scripts/pdf_equation_extractor.py', '--base-dir', base])
    if not success:
        had_errors = True
        timings['extract_pdf'] = "FAILED"
    else:
        timings['extract_pdf'] = time_taken
    time_taken, success = run([sys.executable, 'scripts/merge_and_analyze_equations.py', '--base-dir', base])
    if not success:
        had_errors = True
        timings['merge'] = "FAILED"
    else:
        timings['merge'] = time_taken

    out = Path(base) / 'BENCHMARK.md'
    try:
        with out.open('w', encoding='utf-8') as f:
            f.write('# Extraction Benchmark\n\n')
            total_time = 0.0
            for k, v in timings.items():
                if isinstance(v, float):
                    total_time += v
                    f.write(f'- {k}: {v:.2f}s\n')
                else:
                    f.write(f'- {k}: {v}\n')
            f.write(f'\nTotal: {total_time:.2f}s\n')
        print(f'Benchmark written: {out}')
    except IOError as e:
        print(f"Error writing benchmark file {out}: {e}")
        had_errors = True

    if had_errors:
        raise SystemExit(1)

if __name__ == '__main__':
    main()

