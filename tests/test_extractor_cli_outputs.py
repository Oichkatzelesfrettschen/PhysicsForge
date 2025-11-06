import subprocess
from pathlib import Path


def test_cli_outputs_with_flags(tmp_path: Path):
    base = tmp_path
    # Create a simple notes file with an equation
    notes = base / 'notes'
    notes.mkdir()
    f = notes / 'sample.md'
    f.write_text('Energy relation: E = m c^2', encoding='utf-8')

    out_csv = base / 'out.csv'
    out_ndj = base / 'out.ndjson'
    out_metrics = base / 'metrics.json'

    script = Path(__file__).resolve().parents[1] / 'scripts' / 'equation_extractor.py'
    cmd = [
        'python', str(script),
        '--base-dir', str(base),
        '--scan-dir', '.',
        '--max-files', '10',
        '--output', str(out_csv),
        '--ndjson-output', str(out_ndj),
        '--metrics-output', str(out_metrics),
    ]
    subprocess.check_call(cmd, cwd=str(base))

    assert out_csv.exists() and out_csv.stat().st_size > 0
    assert out_ndj.exists() and out_ndj.stat().st_size > 0
    assert out_metrics.exists() and out_metrics.stat().st_size > 0


def test_exclude_dir(tmp_path: Path):
    base = tmp_path
    inc = base / 'include'
    exc = base / 'skipme'
    inc.mkdir()
    exc.mkdir()
    (inc / 'a.md').write_text('E = m c^2', encoding='utf-8')
    (exc / 'b.md').write_text('F = m a', encoding='utf-8')

    out_csv = base / 'o.csv'
    script = Path(__file__).resolve().parents[1] / 'scripts' / 'equation_extractor.py'
    cmd = [
        'python', str(script),
        '--base-dir', str(base),
        '--scan-dir', '.',
        '--exclude-dir', 'skipme',
        '--output', str(out_csv),
    ]
    subprocess.check_call(cmd, cwd=str(base))

    # Ensure only one equation extracted from included dir
    data = out_csv.read_text(encoding='utf-8')
    assert 'F = m a' not in data
    assert 'E = m c^2' in data

