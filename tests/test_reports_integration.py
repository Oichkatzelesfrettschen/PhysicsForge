import subprocess
from pathlib import Path


def test_reports_generation(tmp_path):
    base = Path(__file__).resolve().parents[1]
    deps = base / 'DEPS_REPORT.md'
    todo = base / 'TODO_TRACKER.md'
    repo = base / 'REPO_AUDIT.md'

    # Run scripts individually to avoid depending on 'make' in test env
    subprocess.check_call(['python', str(base / 'scripts' / 'dependency_audit.py'), '--base-dir', str(base)])
    subprocess.check_call(['python', str(base / 'scripts' / 'todowrite.py'), '--base-dir', str(base)])
    subprocess.check_call(['python', str(base / 'scripts' / 'repo_audit.py'), '--base-dir', str(base)])

    assert deps.exists(), 'DEPS_REPORT.md should exist after report generation'
    assert todo.exists(), 'TODO_TRACKER.md should exist after report generation'
    assert repo.exists(), 'REPO_AUDIT.md should exist after report generation'

