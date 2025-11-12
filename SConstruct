# SConstruct
import os
import sys
import subprocess
from SCons.Script import *

# --- Help Target ---
Help("""
Usage: scons [target]

---------------------------------------------------------------------------
 PhysicsForge SCons Build System - Your portal to project automation.
---------------------------------------------------------------------------

 Core Commands:
   pipeline        - Full data extraction and catalog generation.
   quick_pipeline  - A faster, limited-scope pipeline for quick checks.
   test            - Run the full test suite.
   ci              - Continuous integration: all checks, tests, and build.

 Validation & Auditing:
   validate        - Validate the integrity of the equation catalog.
   audit           - Audit the repository for structural issues.
   parity          - Check for consistency between catalog and modules.
   gaps            - Identify TODOs and gaps in the research.
   lint            - Run all linting checks.

 LaTeX & Synthesis:
   latex           - Compile the main LaTeX document.
   latex_strict    - Compile LaTeX in strict mode (errors fail the build).
   link            - Link equation modules into the synthesis directory.

 Reporting & Metrics:
   reports         - Generate all project reports (dependencies, TODOs).
   quick_reports   - Generate a subset of faster reports.
   bench           - Benchmark the equation extraction process.
   metrics_only    - Generate extraction metrics without building catalog.
   plan            - Create an extraction plan without executing it.

 Maintenance:
   clean           - Remove temporary and generated files.
   distclean       - A more thorough cleaning, removing caches.
   ascii_guard     - Check for non-ASCII characters in the codebase.
   ascii_normalize - Normalize unicode characters to ASCII.
   update_data_readme - Regenerate the README for the data directory.

 GitHub Pages:
   svg             - Generate SVG figures from TikZ.
   web             - Build everything for web deployment.
   clean-svg       - Clean SVG build artifacts.
   serve           - Serve the site locally for testing.
---------------------------------------------------------------------------
""")

# Define a custom builder for running Python scripts
def run_python_script(target, source, env):
    script_path = str(source[0])
    command = [sys.executable, script_path]
    
    # Add generic script arguments
    script_args = env.get('SCRIPT_ARGS', [])
    command.extend(script_args)

    print(f"Running: {' '.join(command)}")
    return env.Execute(command)

# Define a custom builder for running shell scripts
def run_shell_script(target, source, env):
    script_path = str(source[0])
    command = [script_path] # Assuming the script is executable
    
    # Add generic script arguments
    script_args = env.get('SCRIPT_ARGS', [])
    command.extend(script_args)

    print(f"Running: {' '.join(command)}")
    return env.Execute(' '.join(command), shell=True) # Use shell=True for bash scripts

# Create a default environment
env = Environment()

# Add our custom builders
env.Append(BUILDERS={
    'PythonScriptBuilder': Builder(action=run_python_script),
    'ShellScriptBuilder': Builder(action=run_shell_script)
})

# --- SCons Variables for Makefile compatibility ---
# Allow BASE_DIR to be overridden from command line (e.g., scons BASE_DIR=/path/to/repo)
env['BASE_DIR'] = ARGUMENTS.get('BASE_DIR', os.getcwd())
# Allow SCANS to be overridden (e.g., scons SCANS="notes other_dir")
# Split by space if provided as a single string
scans_arg = ARGUMENTS.get('SCANS', 'notes .')
env['SCANS'] = scans_arg.split() if isinstance(scans_arg, str) else scans_arg

# --- Replicate 'pipeline' target --- 
pipeline_script = env.File('scripts/build_catalog_pipeline.py')
env.PythonScriptBuilder(target='pipeline_run', source=pipeline_script, 
                        SCRIPT_ARGS=['--base-dir', env['BASE_DIR']] + sum([['--scan-dir', s] for s in env['SCANS']], []))

Alias('pipeline', 'pipeline_run')

# --- Replicate 'audit' target ---
audit_script = env.File('scripts/repo_audit.py')
env.PythonScriptBuilder(target='audit_run', source=audit_script,
                        SCRIPT_ARGS=['--base-dir', env['BASE_DIR']])
Alias('audit', 'audit_run')

# --- Replicate 'parity' target ---
parity_script = env.File('scripts/catalog_parity.py')
env.PythonScriptBuilder(target='parity_run', source=parity_script,
                        SCRIPT_ARGS=['--base-dir', env['BASE_DIR']])
Alias('parity', 'parity_run')

# --- Replicate 'gaps' target ---
gaps_script = env.File('scripts/gap_todo.py')
env.PythonScriptBuilder(target='gaps_run', source=gaps_script,
                        SCRIPT_ARGS=['--base-dir', env['BASE_DIR']])
Alias('gaps', 'gaps_run')

# --- Replicate 'validate' target ---
validate_script = env.File('scripts/validate_catalog.py')
env.PythonScriptBuilder(target='validate_run', source=validate_script,
                        SCRIPT_ARGS=['--base-dir', env['BASE_DIR']])
Alias('validate', 'validate_run')

# --- Replicate 'bench' target ---
bench_script = env.File('scripts/benchmark_extraction.py')

def run_bench_ignore(target, source, env):
    cmd = [sys.executable, str(source[0]), '--base-dir', env['BASE_DIR']] + sum([['--scan-dir', s] for s in env['SCANS']], [])
    print('Running:', ' '.join(cmd))
    try:
        subprocess.call(cmd)
    except Exception:
        pass
    return 0

env.Command(target='bench_run', source=bench_script, action=run_bench_ignore)
Alias('bench', 'bench_run')

# --- Replicate 'smoke' target ---
smoke_script = env.File('scripts/test_extraction_smoke.py')
env.PythonScriptBuilder(target='smoke_run', source=smoke_script)
Alias('smoke', 'smoke_run')

# --- Replicate 'test' target ---
env.Command(target='test_run', action='pytest -q')
Alias('test', 'test_run')

# --- Replicate 'ascii_guard' target ---
ascii_guard_script = env.File('scripts/ascii_guard.py')
env.PythonScriptBuilder(target='ascii_guard_run', source=ascii_guard_script,
                        SCRIPT_ARGS=['--base-dir', env['BASE_DIR']])
Alias('ascii_guard', 'ascii_guard_run')

# --- Replicate 'latex_strict' target ---
latex_strict_script = env.File('synthesis/scripts/compile_strict.sh')
env.ShellScriptBuilder(target='latex_strict_run', source=latex_strict_script)
Alias('latex_strict', 'latex_strict_run')

# --- Replicate 'update_data_readme' target ---
update_data_readme_script = env.File('scripts/update_data_readme.py')
env.PythonScriptBuilder(target='update_data_readme_run', source=update_data_readme_script,
                        SCRIPT_ARGS=['--base-dir', env['BASE_DIR']])
Alias('update_data_readme', 'update_data_readme_run')

# --- Replicate 'dependency_audit' target ---
dependency_audit_script = env.File('scripts/dependency_audit.py')
env.PythonScriptBuilder(target='dependency_audit_run', source=dependency_audit_script,
                        SCRIPT_ARGS=['--base-dir', env['BASE_DIR']])
Alias('dependency_audit', 'dependency_audit_run')

# --- Replicate 'todowrite' target ---
todowrite_script = env.File('scripts/todowrite.py')
env.PythonScriptBuilder(target='todowrite_run', source=todowrite_script,
                        SCRIPT_ARGS=['--base-dir', env['BASE_DIR']])
Alias('todowrite', 'todowrite_run')

# --- Replicate 'reports' target ---
env.Alias('reports', ['dependency_audit_run', 'todowrite_run', 'audit_run', 'update_data_readme_run'])
env.AlwaysBuild('reports') # Ensure it always runs

# --- Replicate 'quick_pipeline' target ---
quick_pipeline_actions = [
    Action(f"{sys.executable} scripts/equation_extractor.py --base-dir {env['BASE_DIR']} --scan-dir notes --max-files 30 --max-lines 400 --parallel-workers 4"),
    Action(f"{sys.executable} scripts/merge_and_analyze_equations.py --base-dir {env['BASE_DIR']}"),
    Action(f"{sys.executable} scripts/catalog_parity.py --base-dir {env['BASE_DIR']}")
]
env.Command(target='quick_pipeline_run', action=quick_pipeline_actions)
Alias('quick_pipeline', 'quick_pipeline_run')

# --- Replicate 'quick_reports' target ---
quick_reports_actions = [
    Action(f"{sys.executable} scripts/dependency_audit.py --base-dir {env['BASE_DIR']}"),
    Action(f"{sys.executable} scripts/todowrite.py --base-dir {env['BASE_DIR']}")
]
env.Command(target='quick_reports_run', action=quick_reports_actions)
Alias('quick_reports', 'quick_reports_run')
env.AlwaysBuild('quick_reports') # Ensure it always runs

# --- Replicate 'ascii_normalize' target ---
ascii_normalize_script = env.File('scripts/ascii_normalize.py')
env.PythonScriptBuilder(target='ascii_normalize_run', source=ascii_normalize_script,
                        SCRIPT_ARGS=['--base-dir', env['BASE_DIR'], '--path', 'docs', '--path', 'synthesis'])
Alias('ascii_normalize', 'ascii_normalize_run')

# --- Replicate 'todo' target ---
Alias('todo', 'todowrite_run')

# --- Replicate 'ci' target ---
Alias('ci', ['ascii_guard_run', 'smoke_run', 'test_run', 'validate_run', 'audit_run', 'parity_run', 'gaps_run', 'latex_strict_run', 'reports'])

# --- Replicate 'link' target ---
link_script = env.File('scripts/link_modules.py')
env.PythonScriptBuilder(target='link_run', source=link_script,
                        SCRIPT_ARGS=['--base-dir', env['BASE_DIR']])
Alias('link', 'link_run')

# --- Replicate 'latex' target ---
latex_script = env.File('synthesis/scripts/compile.sh')
env.ShellScriptBuilder(target='latex_run', source=latex_script)
Alias('latex', 'latex_run')

# --- Replicate 'metrics_only' target ---
metrics_only_actions = [
    Action(f"{sys.executable} scripts/equation_extractor.py --base-dir {env['BASE_DIR']} " + " ".join([f"--scan-dir {s}" for s in env['SCANS']]) + " --max-files 50 --max-lines 400 --parallel-workers 4 --no-csv --no-ndjson --metrics-output metrics.json"),
    Action(f"{sys.executable} scripts/validate_metrics_schema.py metrics.json")
]
env.Command(target='metrics_only_run', action=metrics_only_actions)
Alias('metrics_only', 'metrics_only_run')

# --- Replicate 'plan' target ---
plan_actions = [
    Action(f"{sys.executable} scripts/equation_extractor.py --base-dir {env['BASE_DIR']} " + " ".join([f"--scan-dir {s}" for s in env['SCANS']]) + " --plan-only --plan-output plan.json"),
    Action(f"{sys.executable} scripts/validate_plan_schema.py plan.json")
]
env.Command(target='plan_run', action=plan_actions)
Alias('plan', 'plan_run')

# --- Replicate 'lint' target ---
Alias('lint', ['ascii_guard_run', 'plan_run', 'metrics_only_run'])

# --- Replicate 'clean' target ---
env.Clean(['plan.json', 'metrics.json', 'DEPS_REPORT.md', 'TODO_TRACKER.md', 'REPO_AUDIT.md', 'data/README.md'])
Alias('clean', ['plan.json', 'metrics.json', 'DEPS_REPORT.md', 'TODO_TRACKER.md', 'REPO_AUDIT.md', 'data/README.md'])


# --- Replicate 'distclean' target ---
distclean_targets = ['__pycache__', '.pytest_cache', 'scripts/__pycache__', 'tests/__pycache__']
env.Clean(distclean_targets + ['plan.json', 'metrics.json', 'DEPS_REPORT.md', 'TODO_TRACKER.md', 'REPO_AUDIT.md', 'data/README.md'])
Alias('distclean', distclean_targets)


# --- GitHub Pages Targets ---
env.Command('figures_run', None, 'mkdir -p build/xdv figures/svg && for f in figures/tikz/*.tex; do if [ -f "$$f" ]; then base=$$(basename "$$f" .tex); echo "Processing: $$base"; xelatex --no-pdf -interaction=nonstopmode -halt-on-error -output-directory=build/xdv "$$f" || echo "Warning: xelatex failed for $$f"; xdv_file=""; if [ -f "$${base}.xdv" ]; then xdv_file="$${base}.xdv"; mv "$${base}.xdv" "build/xdv/$${base}.xdv" 2>/dev/null || true; elif [ -f "build/xdv/$${base}.xdv" ]; then xdv_file="build/xdv/$${base}.xdv"; fi; if [ -n "$$xdv_file" ] && [ -f "build/xdv/$${base}.xdv" ]; then dvisvgm --exact --font-format=woff2 -n -a -o "figures/svg/$${base}.svg" "build/xdv/$${base}.xdv" || echo "Warning: dvisvgm failed for $$base"; fi; fi; done && echo "=== Copying SVGs to site ===" && mkdir -p site/figs && cp figures/svg/*.svg site/figs/ 2>/dev/null || echo "No SVGs to copy" && echo "=== Figure generation complete ==="')
Alias('figures', 'figures_run')
Alias('svg', 'figures')

env.Command('web_run', None, 'mkdir -p site/pdf && cp synthesis/main.pdf site/pdf/ 2>/dev/null || cp build/main.pdf site/pdf/ || echo "Warning: PDF not found"')
Alias('web', ['latex_run', 'svg', 'web_run'])

env.Clean(['build/xdv', 'figures/svg', 'site/figs'])
Alias('clean-svg', ['build/xdv', 'figures/svg', 'site/figs'])

def serve_site(target, source, env):
    print("=== Starting local server at http://localhost:8000 ===")
    subprocess.run(["python3", "-m", "http.server", "8000"], cwd='site')

env.Command('serve_run', None, serve_site)
Alias('serve', 'serve_run')


# Default target
Default('pipeline')
