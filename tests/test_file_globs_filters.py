import csv
import subprocess
from pathlib import Path


def test_include_glob_limits_to_matching_files(tmp_path: Path):
    base = tmp_path
    notes = base / 'notes'
    notes.mkdir()
    (notes / 'keep_alpha.md').write_text('E = m c^2', encoding='utf-8')
    (notes / 'drop_beta.md').write_text('F = m * a', encoding='utf-8')

    out = base / 'o.csv'
    script = Path(__file__).resolve().parents[1] / 'scripts' / 'equation_extractor.py'
    subprocess.check_call([
        'python', str(script), '--base-dir', str(base), '--scan-dir', '.', '--output', str(out), '--include-glob', 'notes/*alpha*.md'
    ], cwd=str(base))

    rows = list(csv.DictReader(out.read_text(encoding='utf-8').splitlines()))
    assert any('keep_alpha.md' in r['SourceDoc'] for r in rows)
    assert all('drop_beta.md' not in r['SourceDoc'] for r in rows)


def test_exclude_glob_filters_out_files(tmp_path: Path):
    base = tmp_path
    notes = base / 'notes'
    notes.mkdir()
    (notes / 'alpha.md').write_text('E = m c^2', encoding='utf-8')
    (notes / 'genesis.md').write_text('a = 1', encoding='utf-8')

    out = base / 'o.csv'
    script = Path(__file__).resolve().parents[1] / 'scripts' / 'equation_extractor.py'
    subprocess.check_call([
        'python', str(script), '--base-dir', str(base), '--scan-dir', '.', '--output', str(out), '--exclude-glob', 'notes/genesis*.md'
    ], cwd=str(base))

    rows = list(csv.DictReader(out.read_text(encoding='utf-8').splitlines()))
    assert any('alpha.md' in r['SourceDoc'] for r in rows)
    assert all('genesis.md' not in r['SourceDoc'] for r in rows)

