import json
import subprocess
from pathlib import Path


def test_metrics_timing_by_framework_present(tmp_path: Path):
    base = tmp_path
    notes = base / 'notes'
    notes.mkdir()

    # Filenames influence framework in extractor
    (notes / 'alpha_eq.md').write_text('E = m c^2', encoding='utf-8')  # -> Aether
    (notes / 'genesis_math.md').write_text('a = 1', encoding='utf-8')   # -> Genesis

    out_csv = base / 'o.csv'
    out_metrics = base / 'metrics.json'
    script = Path(__file__).resolve().parents[1] / 'scripts' / 'equation_extractor.py'
    cmd = [
        'python', str(script),
        '--base-dir', str(base),
        '--scan-dir', '.',
        '--output', str(out_csv),
        '--metrics-output', str(out_metrics),
        '--parallel-workers', '2',
    ]
    subprocess.check_call(cmd, cwd=str(base))

    data = json.loads(out_metrics.read_text(encoding='utf-8'))
    metrics = data['metrics']
    tbf = metrics.get('timing_by_framework', {})
    # Expect both frameworks present with non-negative elapsed
    assert 'Aether' in tbf and float(tbf['Aether']) >= 0.0
    assert 'Genesis' in tbf and float(tbf['Genesis']) >= 0.0
    # Timing totals present
    timing = metrics.get('timing', {})
    assert float(timing.get('read_s', 0.0)) >= 0.0
    assert float(timing.get('extract_s', 0.0)) >= 0.0
    assert float(timing.get('classify_s', 0.0)) >= 0.0
    # Per-framework breakdown exists
    tbf_break = metrics.get('timing_by_framework_breakdown', {})
    assert 'Aether' in tbf_break and all(k in tbf_break['Aether'] for k in ['read_s','extract_s','classify_s'])
    assert 'Genesis' in tbf_break and all(k in tbf_break['Genesis'] for k in ['read_s','extract_s','classify_s'])
