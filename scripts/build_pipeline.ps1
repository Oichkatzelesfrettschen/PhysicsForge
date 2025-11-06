Param(
  [string]$BaseDir = ".",
  [string[]]$ScanDir = @("notes", ".")
)

Write-Host "Running catalog pipeline..." -ForegroundColor Cyan

foreach ($d in $ScanDir) {
  python scripts/equation_extractor.py --base-dir $BaseDir --scan-dir $d
  if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
}
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

python scripts/pdf_equation_extractor.py --base-dir $BaseDir
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

python scripts/merge_and_analyze_equations.py --base-dir $BaseDir
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

python scripts/catalog_parity.py --base-dir $BaseDir
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

python scripts/gap_todo.py --base-dir $BaseDir
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

Write-Host "Pipeline completed." -ForegroundColor Green

