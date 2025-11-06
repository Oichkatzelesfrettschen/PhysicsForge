import argparse
import csv
from pathlib import Path

def generate_example_figure_data(output_dir: Path):
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / "example_figure_data.csv"
    
    data = [
        ["x", "y1", "y2"],
        [1, 10, 100],
        [2, 12, 110],
        [3, 15, 120],
        [4, 13, 115],
        [5, 18, 130],
    ]

    try:
        with open(output_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(data)
        print(f"Generated example figure data: {output_file}")
        return True
    except IOError as e:
        print(f"Error writing example figure data to {output_file}: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description="Generate example data and indicate figure generation.")
    parser.add_argument("--output-dir", type=str, default="output", help="Directory to save generated data.")
    args = parser.parse_args()

    output_path = Path(args.output_dir)
    
    had_errors = False
    if not generate_example_figure_data(output_path):
        had_errors = True

    print(f"Placeholder: A figure would be generated based on data in {output_path}.")

    if had_errors:
        raise SystemExit(1)

if __name__ == "__main__":
    main()