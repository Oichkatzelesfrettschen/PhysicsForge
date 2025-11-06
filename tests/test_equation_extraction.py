import subprocess
import os
import csv
from pathlib import Path

def test_equation_extraction_smoke():
    """
    Smoke test for the equation_extractor.py script.
    Ensures the script runs without error and produces a non-empty CSV.
    """
    # Define paths
    base_dir = Path(__file__).resolve().parents[1]
    script_path = base_dir / "scripts" / "equation_extractor.py"
    output_csv_path = base_dir / "data" / "catalogs" / "equation_catalog_preliminary.csv"

    # Ensure the output directory exists
    output_csv_path.parent.mkdir(parents=True, exist_ok=True)

    # Run the extractor script
    print(f"Running equation extractor: {script_path}")
    result = subprocess.run(
        ["python", str(script_path)],
        capture_output=True,
        text=True,
        cwd=str(base_dir),
        check=False # Do not raise an exception for non-zero exit codes
    )

    # Print stdout and stderr for debugging if the test fails
    print("Extractor stdout:")
    print(result.stdout)
    print("Extractor stderr:")
    print(result.stderr)

    # Assert the script ran successfully
    assert result.returncode == 0, f"Extractor script failed with error: {result.stderr}"

    # Assert the output CSV file was created
    assert output_csv_path.exists(), f"Output CSV file not found: {output_csv_path}"

    # Assert the CSV file is not empty and contains some data
    with open(output_csv_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader, None) # Read header
        assert header is not None, "CSV file is empty (no header)"
        
        # Count data rows
        data_rows = 0
        for row in reader:
            data_rows += 1
        
        assert data_rows > 0, "No equations extracted into the CSV file."

    print(f"Smoke test passed: {data_rows} equations extracted.")
