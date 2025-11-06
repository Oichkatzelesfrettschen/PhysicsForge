import csv
import subprocess
from pathlib import Path


def test_framework_include_only_aether(tmp_path: Path):
    base = tmp_path
    notes = base / 'notes'
    notes.mkdir()
    (notes / 'alpha_dyn.md').write_text('E = m c^2', encoding='utf-8')  # -> Aether
    (notes / 'genesis_math.md').write_text('a = 1', encoding='utf-8')   # -> Genesis

    out = base / 'o.csv'
    script = Path(__file__).resolve().parents[1] / 'scripts' / 'equation_extractor.py'
    cmd = [
        'python', str(script), '--base-dir', str(base), '--scan-dir', '.', '--output', str(out),
        '--framework-include', 'Aether'
    ]
    subprocess.check_call(cmd, cwd=str(base))
    rows = list(csv.DictReader(out.read_text(encoding='utf-8').splitlines()))
    # Only Aether rows expected
    assert all(r['Framework'] == 'Aether' for r in rows)


def test_framework_exclude_genesis(tmp_path: Path):
    base = tmp_path
    notes = base / 'notes'
    notes.mkdir()
    (notes / 'genesis_math.md').write_text('a = 1', encoding='utf-8')   # -> Genesis
    (notes / 'unified_eq.md').write_text('F = m * a', encoding='utf-8') # -> Unified

    out = base / 'o.csv'
    script = Path(__file__).resolve().parents[1] / 'scripts' / 'equation_extractor.py'
    cmd = [
        'python', str(script), '--base-dir', str(base), '--scan-dir', '.', '--output', str(out),
        '--framework-exclude', 'Genesis'
    ]
    subprocess.check_call(cmd, cwd=str(base))
    rows = list(csv.DictReader(out.read_text(encoding='utf-8').splitlines()))
    assert all(r['Framework'] != 'Genesis' for r in rows)

