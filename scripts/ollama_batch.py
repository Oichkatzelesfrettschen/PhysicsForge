"""
Batch-run local Ollama models on text inputs and save outputs under extracted_data/reports/.

Usage examples:
  python scripts/ollama_batch.py --model llama3 --input notes --glob "*.md"
  python scripts/ollama_batch.py --model mistral --file docs/PROJECT_ROADMAP.md
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
from pathlib import Path


def run_ollama(model: str, prompt: str) -> str:
    if not shutil.which('ollama'):
        raise RuntimeError('ollama CLI not found. Install from https://ollama.com and ensure it is in PATH.')
    proc = subprocess.run(['ollama', 'run', model], input=prompt.encode('utf-8'), capture_output=True)
    if proc.returncode != 0:
        try:
            stderr_output = proc.stderr.decode("utf-8", errors="strict")
        except UnicodeDecodeError:
            stderr_output = "<Undecodable stderr>"
        raise RuntimeError(f'ollama run failed: {stderr_output}')
    try:
        stdout_output = proc.stdout.decode('utf-8', errors='strict')
    except UnicodeDecodeError:
        stdout_output = "<Undecodable stdout>"
    return stdout_output


def iter_inputs(input_path: Path, glob: str | None) -> tuple[list[Path], bool]:
    had_errors_local = False
    if not input_path.exists():
        print(f"Error: Input path not found: {input_path}")
        return [], True
    if input_path.is_file():
        return [input_path], had_errors_local
    if not input_path.is_dir():
        print(f"Error: Input path is not a file or directory: {input_path}")
        return [], True

    pattern = glob or '*.md'
    found_paths = []
    for p in input_path.rglob(pattern):
        if p.is_file():
            found_paths.append(p)
    return found_paths, had_errors_local


def main() -> None:
    ap = argparse.ArgumentParser(description='Batch invoke Ollama on files and save outputs')
    ap.add_argument('--model', type=str, default='llama3', help='Ollama model name (e.g., llama3, mistral)')
    ap.add_argument('--input', type=str, default='notes', help='Input directory to scan (or file via --file)')
    ap.add_argument('--glob', type=str, help='Glob pattern for files under input dir (default: *.md)')
    ap.add_argument('--file', type=str, help='Specific input file (overrides --input)')
    ap.add_argument('--base-dir', type=str, default='.', help='Repository base directory')
    args = ap.parse_args()

    base = Path(args.base_dir).resolve()
    out_dir = base / 'extracted_data' / 'reports' / 'ollama'
    had_errors = False
    try:
        out_dir.mkdir(parents=True, exist_ok=True)
    except OSError as e:
        print(f"Error creating output directory {out_dir}: {e}")
        had_errors = True

    if args.file:
        inputs = [Path(args.file)]
    else:
        inputs, inputs_had_errors = iter_inputs((base / args.input).resolve(), args.glob)
        if inputs_had_errors:
            had_errors = True

    for src in inputs:
        try:
            text = src.read_text(encoding='utf-8', errors='strict')
        except UnicodeDecodeError:
            print(f"Warning: Could not decode input file as UTF-8 (non-ASCII content?): {src}")
            had_errors = True
            continue
        except IOError as e:
            print(f"Error reading input file {src}: {e}")
            had_errors = True
            continue
        prompt = f"Summarize the following file with citations if present and propose next actions.\n\nFILE: {src}\n\n{text}"
        try:
            out = run_ollama(args.model, prompt)
        except Exception as e:
            out = f"ERROR: {e}"
            had_errors = True
        dst = out_dir / (src.stem + '_ollama_out.md')
        try:
            dst.write_text(out, encoding='utf-8')
            print(f'Wrote: {dst}')
        except IOError as e:
            print(f"Error writing output file {dst}: {e}")
            had_errors = True

    if had_errors:
        raise SystemExit(1)


if __name__ == '__main__':
    main()

