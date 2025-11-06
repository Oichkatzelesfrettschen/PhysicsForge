import csv
import subprocess
from pathlib import Path


def test_domain_config_override_sample(tmp_path: Path):
    base = tmp_path
    notes = base / 'notes'
    notes.mkdir()
    # Include the keyword "pythagoras" so the custom domain matches
    (notes / 'n1.md').write_text('pythagoras: a^2 + b^2 = c^2', encoding='utf-8')

    out_csv = base / 'out.csv'
    script = Path(__file__).resolve().parents[1] / 'scripts' / 'equation_extractor.py'
    # Use the sample domain config committed to the repo
    sample_cfg = Path(__file__).resolve().parents[1] / 'data' / 'fixtures' / 'domain_config.sample.json'

    cmd = [
        'python', str(script),
        '--base-dir', str(base),
        '--scan-dir', '.',
        '--output', str(out_csv),
        '--domain-config', str(sample_cfg),
    ]
    subprocess.check_call(cmd, cwd=str(base))

    assert out_csv.exists() and out_csv.stat().st_size > 0

    # Verify that at least one row (the pythagoras equation) is classified as Custom
    rows = list(csv.DictReader(out_csv.read_text(encoding='utf-8').splitlines()))
    assert any('pythagoras' in r['Equation'].lower() and r['Domain'] == 'Custom' for r in rows)


def test_domain_config_override_list_form(tmp_path: Path):
    base = tmp_path
    notes = base / 'notes'
    notes.mkdir()
    (notes / 'n2.md').write_text(r'qubit: H = \omega', encoding='utf-8')

    # List-of-dicts form
    cfg = base / 'cfg.json'
    cfg.write_text(
        (
            '[\n'
            '  {"name": "Quantum", "keywords": ["qubit", "hamiltonian"]},\n'
            '  {"name": "General", "keywords": ["misc"]}\n'
            ']\n'
        ),
        encoding='utf-8'
    )

    out_csv = base / 'out.csv'
    script = Path(__file__).resolve().parents[1] / 'scripts' / 'equation_extractor.py'
    cmd = [
        'python', str(script),
        '--base-dir', str(base),
        '--scan-dir', '.',
        '--output', str(out_csv),
        '--domain-config', str(cfg),
    ]
    subprocess.check_call(cmd, cwd=str(base))

    rows = list(csv.DictReader(out_csv.read_text(encoding='utf-8').splitlines()))
    assert any('qubit' in r['Equation'].lower() and r['Domain'] == 'Quantum' for r in rows)
