import subprocess
import json
from pathlib import Path


def test_metrics_schema_validator(tmp_path: Path):
    base = tmp_path
    notes = base / 'notes'
    notes.mkdir()
    (notes / 's.md').write_text('E = m c^2', encoding='utf-8')

    out_csv = base / 'o.csv'
    out_metrics = base / 'metrics.json'
    extractor = Path(__file__).resolve().parents[1] / 'scripts' / 'equation_extractor.py'
    validator = Path(__file__).resolve().parents[1] / 'scripts' / 'validate_metrics_schema.py'

    subprocess.check_call([
        'python', str(extractor), '--base-dir', str(base), '--scan-dir', '.', '--output', str(out_csv), '--metrics-output', str(out_metrics)
    ], cwd=str(base))

    # Validate
    subprocess.check_call(['python', str(validator), str(out_metrics)], cwd=str(base))

