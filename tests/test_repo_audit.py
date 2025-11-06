import pytest
import os
from pathlib import Path
from unittest.mock import patch, mock_open

from scripts.repo_audit import human_size, audit_repo, write_report

def test_human_size():
    assert human_size(0) == "0.0 B"
    assert human_size(100) == "100.0 B"
    assert human_size(1023) == "1023.0 B"
    assert human_size(1024) == "1.0 KB"
    assert human_size(1024 * 1024 - 1) == "1023.9 KB"
    assert human_size(1024 * 1024) == "1.0 MB"
    assert human_size(1024 * 1024 * 1024 - 1) == "1023.9 MB"
    assert human_size(1024 * 1024 * 1024) == "1.0 GB"
    assert human_size(1024 * 1024 * 1024 * 1024 - 1) == "1023.9 GB"
    assert human_size(1024 * 1024 * 1024 * 1024) == "1.0 TB"

@pytest.fixture
def mock_repo_structure(tmp_path):
    # Create a mock repository structure
    (tmp_path / "scripts").mkdir()
    (tmp_path / "docs").mkdir()
    (tmp_path / "data").mkdir()
    (tmp_path / "synthesis").mkdir()

    (tmp_path / "scripts" / "script1.py").write_text("print('hello')")
    (tmp_path / "scripts" / "script2.py").write_text("import os\n# SYNTHESIS_ROADMAP.md")
    (tmp_path / "docs" / "doc1.md").write_text("# Document 1")
    (tmp_path / "data" / "file.csv").write_text("a,b,c\n1,2,3")
    (tmp_path / "synthesis" / "main.tex").write_text("\\documentclass{article}")
    (tmp_path / "SYNTHESIS_ROADMAP.md").write_text("# Roadmap")
    (tmp_path / "large_file.bin").write_bytes(b'\x00' * 2000)

    return tmp_path

def test_audit_repo_basic(mock_repo_structure):
    base_dir = mock_repo_structure
    data, had_errors = audit_repo(base_dir)

    assert not had_errors
    assert data['total_size'] > 0
    assert data['exts']['.py'] == 2
    assert data['exts']['.md'] == 2
    assert data['exts']['.csv'] == 1
    assert data['exts']['.tex'] == 1
    assert data['exts']['.bin'] == 1

    assert len(data['top_dirs']) > 0
    assert len(data['top_files']) > 0
    assert 'SYNTHESIS_ROADMAP.md' in [Path(p).name for p in data['key_docs']]

def test_audit_repo_permission_error(tmp_path):
    # Simulate a permission error by creating an inaccessible directory
    inaccessible_dir = tmp_path / "inaccessible"
    inaccessible_dir.mkdir()
    os.chmod(inaccessible_dir, 0o000)  # No permissions

    data, had_errors = audit_repo(tmp_path)
    os.chmod(inaccessible_dir, 0o755) # Restore permissions for cleanup

    assert had_errors
    # The audit should still collect data from accessible parts
    assert data['total_size'] >= 0

def test_write_report(mock_repo_structure):
    base_dir = mock_repo_structure
    data, _ = audit_repo(base_dir)

    report_path, success = write_report(base_dir, data)
    assert success
    assert report_path.exists()

    content = report_path.read_text()
    assert "# Repository Audit" in content
    assert "## Key Documents" in content
    assert "## Top Directories by Size" in content
    assert "## Largest Files" in content
    assert "## File Type Counts" in content
    assert "SYNTHESIS_ROADMAP.md" in content
    assert ".py: 2" in content

def test_write_report_io_error(tmp_path):
    # Simulate an IOError by trying to write to a read-only location
    read_only_dir = tmp_path / "read_only"
    read_only_dir.mkdir()
    os.chmod(read_only_dir, 0o444) # Read-only permissions

    data = {'total_size': 100, 'exts': {'.txt': 1}, 'top_dirs': [], 'top_files': [], 'key_docs': []}
    report_path, success = write_report(read_only_dir, data)
    os.chmod(read_only_dir, 0o755) # Restore permissions for cleanup

    assert not success
    assert report_path is None
