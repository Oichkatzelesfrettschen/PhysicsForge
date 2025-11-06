import json
import subprocess
from pathlib import Path


def test_metrics_json_content_and_invariants(tmp_path: Path):
    base = tmp_path
    notes = base / 'notes'
    notes.mkdir()
    # Create a small file with multiple equations to exercise stats/metrics
    f = notes / 'sample.md'
    f.write_text(
        '\n'.join([
            'Energy relation: E = m c^2',
            'H = T + V',
            'F = m * a',
        ]),
        encoding='utf-8',
    )

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

    assert out_metrics.exists() and out_metrics.stat().st_size > 0

    data = json.loads(out_metrics.read_text(encoding='utf-8'))
    # Top-level keys
    assert 'stats' in data and 'metrics' in data

    stats = data['stats']
    metrics = data['metrics']

    # Stats keys
    assert 'total' in stats
    assert 'by_framework' in stats
    assert 'by_domain' in stats
    assert 'by_source' in stats

    # Basic invariants
    total = int(stats['total'])
    sum_by_domain = sum(int(v) for v in stats['by_domain'].values())
    assert sum_by_domain == total

    # Metrics keys
    for k in ['files_scanned', 'bytes_scanned', 'candidate_equations', 'unique_equations', 'elapsed_s']:
        assert k in metrics

    # Relationships and ranges
    assert int(metrics['unique_equations']) <= int(metrics['candidate_equations'])
    assert float(metrics['elapsed_s']) >= 0.0

    # Per-domain counts mirrored in metrics
    assert 'by_domain' in metrics
    assert sum(int(v) for v in metrics['by_domain'].values()) == total

    # Timing struct present with total elapsed
    assert 'timing' in metrics and 'total_elapsed_s' in metrics['timing']
    assert float(metrics['timing']['total_elapsed_s']) == float(metrics['elapsed_s'])
    # Optional details present
    assert 'read_s' in metrics['timing'] and 'extract_s' in metrics['timing'] and 'classify_s' in metrics['timing']
