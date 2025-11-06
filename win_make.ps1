param(
  [Parameter(Position=0)][string]$Target = "pipeline",
  [string]$BaseDir = ".",
  [string[]]$Scans = @("notes", ".")
)

function Invoke-Py {
  param([string[]]$Args)
  Write-Host "> python $($Args -join ' ')"
  $p = Start-Process -FilePath "python" -ArgumentList $Args -NoNewWindow -Wait -PassThru
  if ($p.ExitCode -ne 0) { throw "Command failed: python $($Args -join ' ') (code=$($p.ExitCode))" }
}

$scanArgs = @()
foreach ($s in $Scans) { $scanArgs += @('--scan-dir', $s) }

switch ($Target.ToLowerInvariant()) {
  'pipeline' {
    Invoke-Py @('scripts/build_catalog_pipeline.py', '--base-dir', $BaseDir) + $scanArgs
  }
  'audit' { Invoke-Py @('scripts/repo_audit.py', '--base-dir', $BaseDir) }
  'parity' { Invoke-Py @('scripts/catalog_parity.py', '--base-dir', $BaseDir) }
  'gaps' { Invoke-Py @('scripts/gap_todo.py', '--base-dir', $BaseDir) }
  'validate' { Invoke-Py @('scripts/validate_catalog.py', '--base-dir', $BaseDir) }
  'bench' {
    try { Invoke-Py @('scripts/benchmark_extraction.py', '--base-dir', $BaseDir) + $scanArgs } catch { Write-Warning $_.Exception.Message }
  }
  'smoke' { Invoke-Py @('scripts/test_extraction_smoke.py') }
  'test' { Invoke-Expression 'pytest -q' }
  'ascii_guard' { Invoke-Py @('scripts/ascii_guard.py', '--base-dir', $BaseDir) }
  'ascii_normalize' { Invoke-Py @('scripts/ascii_normalize.py', '--base-dir', $BaseDir, '--path', 'docs', '--path', 'synthesis') }
  'todo' { Invoke-Py @('scripts/todowrite.py', '--base-dir', $BaseDir) }
  'reports' {
    Invoke-Py @('scripts/dependency_audit.py', '--base-dir', $BaseDir)
    Invoke-Py @('scripts/todowrite.py', '--base-dir', $BaseDir)
    Invoke-Py @('scripts/repo_audit.py', '--base-dir', $BaseDir)
    Invoke-Py @('scripts/update_data_readme.py', '--base-dir', $BaseDir)
    Write-Host 'Reports generated: DEPS_REPORT.md, TODO_TRACKER.md, REPO_AUDIT.md, data/README.md'
  }
  'quick_pipeline' {
    Invoke-Py @('scripts/equation_extractor.py', '--base-dir', $BaseDir, '--scan-dir', 'notes', '--max-files', '30', '--max-lines', '400', '--parallel-workers', '4')
    Invoke-Py @('scripts/merge_and_analyze_equations.py', '--base-dir', $BaseDir)
    Invoke-Py @('scripts/catalog_parity.py', '--base-dir', $BaseDir)
  }
  'quick_reports' {
    Invoke-Py @('scripts/dependency_audit.py', '--base-dir', $BaseDir)
    Invoke-Py @('scripts/todowrite.py', '--base-dir', $BaseDir)
    Write-Host 'Quick reports generated: DEPS_REPORT.md, TODO_TRACKER.md'
  }
  'plan' {
    Invoke-Py @('scripts/equation_extractor.py', '--base-dir', $BaseDir) + $scanArgs + @('--plan-only', '--plan-output', 'plan.json')
    Invoke-Py @('scripts/validate_plan_schema.py', 'plan.json')
    Write-Host 'Plan generated and validated: plan.json'
  }
  'metrics_only' {
    Invoke-Py @('scripts/equation_extractor.py', '--base-dir', $BaseDir) + $scanArgs + @('--max-files', '50', '--max-lines', '400', '--parallel-workers', '4', '--no-csv', '--no-ndjson', '--metrics-output', 'metrics.json')
    Invoke-Py @('scripts/validate_metrics_schema.py', 'metrics.json')
  }
  'lint' {
    Invoke-Py @('scripts/ascii_guard.py', '--base-dir', $BaseDir)
    Invoke-Py @('scripts/equation_extractor.py', '--base-dir', $BaseDir) + @('--scan-dir', 'notes', '--scan-dir', '.') + @('--plan-only', '--plan-output', 'plan.json')
    Invoke-Py @('scripts/validate_plan_schema.py', 'plan.json')
    Invoke-Py @('scripts/equation_extractor.py', '--base-dir', $BaseDir) + @('--scan-dir', 'notes', '--scan-dir', '.') + @('--max-files', '50', '--max-lines', '400', '--parallel-workers', '4', '--no-csv', '--no-ndjson', '--metrics-output', 'metrics.json')
    Invoke-Py @('scripts/validate_metrics_schema.py', 'metrics.json')
    Write-Host 'Lint OK: ASCII guard, plan.json, metrics.json validated'
  }
  'clean' {
    foreach ($f in @('plan.json','metrics.json','DEPS_REPORT.md','TODO_TRACKER.md','REPO_AUDIT.md','data/README.md')) {
      if (Test-Path $f) { Remove-Item -Force $f }
    }
    foreach ($d in @('__pycache__','.pytest_cache','scripts/__pycache__','tests/__pycache__')) {
      if (Test-Path $d) { Remove-Item -Recurse -Force $d }
    }
    Write-Host 'Cleaned ephemeral artifacts.'
  }
  'latex' { Write-Warning 'LaTeX builds are Linux/WSL only in this repo. Use WSL or run on Linux.' }
  'latex_strict' { Write-Warning 'LaTeX strict is Linux/WSL only. Use WSL or run on Linux CI.' }
  Default { throw "Unknown target: $Target" }
}
