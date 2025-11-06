import csv
import subprocess
from pathlib import Path


def test_default_excludes_skip_data_without_flag(tmp_path: Path):
    base = tmp_path
    data_dir = base / 'data'
    data_dir.mkdir()
    (data_dir / 's.md').write_text('E = m c^2', encoding='utf-8')

    out_csv = base / 'o.csv'
    script = Path(__file__).resolve().parents[1] / 'scripts' / 'equation_extractor.py'
    cmd = [
        'python', str(script), '--base-dir', str(base), '--scan-dir', '.', '--output', str(out_csv)
    ]
    subprocess.check_call(cmd, cwd=str(base))

    rows = list(csv.DictReader(out_csv.read_text(encoding='utf-8').splitlines()))
    # Default excludes applied at repo root: data/ skipped
    assert all('E = m c^2' not in r['Equation'] for r in rows)


def test_no_default_excludes_includes_data_with_flag(tmp_path: Path):
    base = tmp_path
    data_dir = base / 'data'
    data_dir.mkdir()
    (data_dir / 's.md').write_text('E = m c^2', encoding='utf-8')

    out_csv = base / 'o.csv'
    script = Path(__file__).resolve().parents[1] / 'scripts' / 'equation_extractor.py'
    cmd = [
        'python', str(script), '--base-dir', str(base), '--scan-dir', '.', '--no-default-excludes', '--output', str(out_csv)
    ]
    subprocess.check_call(cmd, cwd=str(base))

    rows = list(csv.DictReader(out_csv.read_text(encoding='utf-8').splitlines()))
    assert any('E = m c^2' in r['Equation'] for r in rows)

