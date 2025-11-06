import csv
import subprocess
from pathlib import Path


def test_parallel_vs_serial_determinism(tmp_path: Path):
    base = tmp_path
    notes = base / 'notes'
    notes.mkdir()

    # Create several files with overlapping equations
    (notes / 'f1.md').write_text('E = m c^2\nF = m * a', encoding='utf-8')
    (notes / 'f2.md').write_text('H = T + V\nE = m c^2', encoding='utf-8')
    (notes / 'f3.md').write_text('F = m * a\nH = T + V', encoding='utf-8')

    script = Path(__file__).resolve().parents[1] / 'scripts' / 'equation_extractor.py'

    out1 = base / 'o1.csv'
    cmd1 = [
        'python', str(script), '--base-dir', str(base), '--scan-dir', '.',
        '--output', str(out1), '--parallel-workers', '1'
    ]
    subprocess.check_call(cmd1, cwd=str(base))

    out2 = base / 'o2.csv'
    cmd2 = [
        'python', str(script), '--base-dir', str(base), '--scan-dir', '.',
        '--output', str(out2), '--parallel-workers', '4'
    ]
    subprocess.check_call(cmd2, cwd=str(base))

    # Exact CSV content must match deterministically
    c1 = out1.read_text(encoding='utf-8')
    c2 = out2.read_text(encoding='utf-8')
    assert c1 == c2

