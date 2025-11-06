import json
import subprocess
from pathlib import Path


def test_plan_only_outputs_candidates_and_skips(tmp_path: Path):
    base = tmp_path
    notes = base / 'notes'
    notes.mkdir()
    (notes / 'keep.md').write_text('E = m c^2', encoding='utf-8')
    (notes / 'drop.md').write_text('F = m * a', encoding='utf-8')

    script = Path(__file__).resolve().parents[1] / 'scripts' / 'equation_extractor.py'
    plan_path = base / 'plan.json'
    cmd = [
        'python', str(script), '--base-dir', str(base), '--scan-dir', '.', '--plan-only', '--plan-output', str(plan_path), '--exclude-glob', 'notes/drop.md'
    ]
    subprocess.check_call(cmd, cwd=str(base))

    data = json.loads(plan_path.read_text(encoding='utf-8'))
    items = data['items']
    assert any(i['action'] == 'scan' and i['rel'].endswith('keep.md') for i in items)
    assert any(i['action'] == 'skip' and i['reason'] == 'glob_exclude' and i['rel'].endswith('drop.md') for i in items)

