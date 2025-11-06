import os
import csv
import json
import yaml
from pathlib import Path

def get_csv_metadata(filepath: Path) -> tuple[list[str] | None, int | None]:
    try:
        with filepath.open('r', encoding='utf-8') as f:
            reader = csv.reader(f)
            headers = next(reader, None)
            row_count = sum(1 for row in reader)
            return headers, row_count
    except FileNotFoundError:
        print(f"Warning: CSV file not found: {filepath}")
        return None, None
    except IOError as e:
        print(f"Error reading CSV file {filepath}: {e}")
        return None, None
    except csv.Error as e:
        print(f"Error parsing CSV file {filepath}: {e}")
        return None, None
    except UnicodeDecodeError:
        print(f"Warning: Could not decode CSV file as UTF-8: {filepath}")
        return None, None

def get_json_metadata(filepath: Path) -> tuple[int | None, int | None]:
    try:
        with filepath.open('r', encoding='utf-8') as f:
            data = json.load(f)
            if isinstance(data, dict):
                return len(data.keys()), None # Number of top-level keys
            elif isinstance(data, list):
                return len(data), None # Number of items in list
            return None, None
    except FileNotFoundError:
        print(f"Warning: JSON file not found: {filepath}")
        return None, None
    except IOError as e:
        print(f"Error reading JSON file {filepath}: {e}")
        return None, None
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON file {filepath}: {e}")
        return None, None
    except UnicodeDecodeError:
        print(f"Warning: Could not decode JSON file as UTF-8: {filepath}")
        return None, None

def get_yaml_metadata(filepath: Path) -> tuple[int | None, int | None]:
    try:
        with filepath.open('r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
            if isinstance(data, dict):
                return len(data.keys()), None # Number of top-level keys
            elif isinstance(data, list):
                return len(data), None # Number of items in list
            return None, None
    except FileNotFoundError:
        print(f"Warning: YAML file not found: {filepath}")
        return None, None
    except IOError as e:
        print(f"Error reading YAML file {filepath}: {e}")
        return None, None
    except yaml.YAMLError as e:
        print(f"Error parsing YAML file {filepath}: {e}")
        return None, None
    except UnicodeDecodeError:
        print(f"Warning: Could not decode YAML file as UTF-8: {filepath}")
        return None, None

def update_data_readme(base_dir):
    data_dir = Path(base_dir) / 'data'
    readme_path = data_dir / 'README.md'

    # Read existing content to preserve the introductory text
    existing_content = ""
    if readme_path.exists():
        try:
            with readme_path.open('r', encoding='utf-8') as f:
                lines = f.readlines()
                # Find the end of the introductory text (before "Files:")
                intro_end_index = -1
                for i, line in enumerate(lines):
                    if line.strip() == "Files:":
                        intro_end_index = i
                        break
                if intro_end_index != -1:
                    existing_content = "".join(lines[:intro_end_index])
                else:
                    existing_content = "".join(lines) # If "Files:" not found, keep all
        except IOError as e:
            print(f"Error reading existing README.md: {e}")
            existing_content = "# Data Files\n\n"
        except UnicodeDecodeError:
            print(f"Warning: Could not decode existing README.md as UTF-8.")
            existing_content = "# Data Files\n\n"

    all_data_files = []
    total_size = 0
    for f_path in data_dir.iterdir():
        if f_path.is_file():
            try:
                total_size += f_path.stat().st_size
                all_data_files.append(f_path)
            except OSError as e:
                print(f"Warning: Could not get size of file {f_path}: {e}")

    csv_files = sorted([f for f in all_data_files if f.suffix.lower() == '.csv'])
    json_files = sorted([f for f in all_data_files if f.suffix.lower() == '.json'])
    yaml_files = sorted([f for f in all_data_files if f.suffix.lower() in ('.yaml', '.yml')])

    new_content = existing_content.strip() + "\n\n## Data Summary\n\n"
    new_content += f"- Total data files: {len(all_data_files)}\n"
    new_content += f"- Total size: {total_size / (1024*1024):.2f} MB\n\n"

    new_content += "## Current Data Files in `data/`\n\n"
    if csv_files or json_files or yaml_files:
        for f_path in csv_files:
            headers, row_count = get_csv_metadata(f_path)
            new_content += f"- `{f_path.name}` (CSV)"
            if headers:
                new_content += f" (Columns: {len(headers)}, Rows: {row_count})\n"
                new_content += f"  - Headers: {', '.join(headers)}\n"
            else:
                new_content += " (Metadata unavailable)\n"
        for f_path in json_files:
            num_keys, _ = get_json_metadata(f_path)
            new_content += f"- `{f_path.name}` (JSON)"
            if num_keys is not None:
                new_content += f" (Top-level keys/items: {num_keys})\n"
            else:
                new_content += " (Metadata unavailable)\n"
        for f_path in yaml_files:
            num_keys, _ = get_yaml_metadata(f_path)
            new_content += f"- `{f_path.name}` (YAML)"
            if num_keys is not None:
                new_content += f" (Top-level keys/items: {num_keys})\n"
            else:
                new_content += " (Metadata unavailable)\n"
    else:
        new_content += "No data files found in `data/`.\n"

    try:
        with readme_path.open('w', encoding='utf-8') as f:
            f.write(new_content)
    except IOError as e:
        print(f"Error writing README.md: {e}")

if __name__ == "__main__":
    base_dir = os.environ.get('BASE_DIR', os.getcwd())
    update_data_readme(base_dir)
