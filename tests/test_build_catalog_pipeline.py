import pytest
from unittest.mock import patch, MagicMock
from pathlib import Path
import sys

from scripts.build_catalog_pipeline import run, main

@patch('subprocess.call')
def test_run_success(mock_call):
    mock_call.return_value = 0
    cmd = ['echo', 'hello']
    result = run(cmd)
    mock_call.assert_called_once_with(cmd)
    assert result == 0

@patch('subprocess.call')
def test_run_failure(mock_call):
    mock_call.return_value = 1
    cmd = ['false']
    result = run(cmd)
    mock_call.assert_called_once_with(cmd)
    assert result == 1

@patch('scripts.build_catalog_pipeline.run')
@patch('argparse.ArgumentParser.parse_args')
@patch('pathlib.Path.resolve')
def test_main_success(mock_resolve, mock_parse_args, mock_run):
    # Mock arguments
    mock_parse_args.return_value = MagicMock(
        base_dir='.',
        scan_dir=['notes', '.']
    )
    mock_resolve.return_value = Path('/mock/base')

    # Mock all subprocess calls to succeed
    mock_run.return_value = 0

    # Run main function
    with pytest.raises(SystemExit) as excinfo:
        main()
    assert excinfo.value.code == 0

    # Verify all expected scripts were run
    expected_calls = [
        ([sys.executable, 'scripts/equation_extractor.py', '--base-dir', '/mock/base', '--scan-dir', 'notes', '--scan-dir', '.'],),
        ([sys.executable, 'scripts/pdf_equation_extractor.py', '--base-dir', '/mock/base'],),
        ([sys.executable, 'scripts/pdf_image_equation_extractor.py', '--base-dir', '/mock/base'],),
        ([sys.executable, 'scripts/merge_and_analyze_equations.py', '--base-dir', '/mock/base'],),
        ([sys.executable, 'scripts/catalog_parity.py', '--base-dir', '/mock/base'],),
    ]
    assert mock_run.call_args_list == expected_calls

@patch('scripts.build_catalog_pipeline.run')
@patch('argparse.ArgumentParser.parse_args')
@patch('pathlib.Path.resolve')
def test_main_required_script_failure(mock_resolve, mock_parse_args, mock_run):
    # Mock arguments
    mock_parse_args.return_value = MagicMock(
        base_dir='.',
        scan_dir=['notes', '.']
    )
    mock_resolve.return_value = Path('/mock/base')

    # Simulate failure of a required script (e.g., equation_extractor.py)
    mock_run.side_effect = [1, 0, 0, 0, 0] # First call fails

    # Run main function
    with pytest.raises(SystemExit) as excinfo:
        main()
    assert excinfo.value.code == 1 # Should exit with 1 (rc |= rc_text)

@patch('scripts.build_catalog_pipeline.run')
@patch('argparse.ArgumentParser.parse_args')
@patch('pathlib.Path.resolve')
def test_main_optional_script_failure(mock_resolve, mock_parse_args, mock_run):
    # Mock arguments
    mock_parse_args.return_value = MagicMock(
        base_dir='.',
        scan_dir=['notes', '.']
    )
    mock_resolve.return_value = Path('/mock/base')

    # Simulate failure of an optional script (e.g., pdf_equation_extractor.py)
    mock_run.side_effect = [0, 1, 0, 0, 0] # Second call fails

    # Run main function
    with pytest.raises(SystemExit) as excinfo:
        main()
    assert excinfo.value.code == 1 # Should exit with 1 (rc |= 1 for optional failure)
