import subprocess
from pathlib import Path


def test_plan_schema_validator(tmp_path: Path):
    base = tmp_path
    notes = base / 'notes'
    notes.mkdir()
    (notes / 'keep.md').write_text('E = m c^2', encoding='utf-8')
    (notes / 'drop.md').write_text('F = m * a', encoding='utf-8')

    plan = base / 'plan.json'
    extractor = Path(__file__).resolve().parents[1] / 'scripts' / 'equation_extractor.py'
    validator = Path(__file__).resolve().parents[1] / 'scripts' / 'validate_plan_schema.py'

    subprocess.check_call([
        'python', str(extractor), '--base-dir', str(base), '--scan-dir', '.', '--plan-only', '--plan-output', str(plan), '--exclude-glob', 'notes/drop.md'
    ], cwd=str(base))

    subprocess.check_call(['python', str(validator), str(plan)], cwd=str(base))

