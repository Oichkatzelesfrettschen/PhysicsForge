Param(
  [string]$BaseDir = ".",
  [string[]]$ScanDir = @("notes", "."),
  [switch]$AutoModules,
  [int]$Limit = 50,
  [int]$MinScore = 10,
  [switch]$Elevated
)

Write-Host "Phase 2/3 synthesis pipeline starting..." -ForegroundColor Cyan

# Run catalog pipeline
python scripts/build_catalog_pipeline.py --base-dir $BaseDir @("--scan-dir") + $ScanDir
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

if ($AutoModules) {
  python scripts/auto_create_modules.py --base-dir $BaseDir --limit $Limit --min-score $MinScore
  if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
}

# Try LaTeX compilation if known scripts exist
$paths = @(
  Join-Path $BaseDir "synthesis/scripts/compile_enhanced.ps1" ,
  Join-Path $BaseDir "synthesis/scripts/compile.ps1"
)

foreach ($p in $paths) {
  if (Test-Path $p) {
    Write-Host "Found compile script: $p" -ForegroundColor Green
    if ($Elevated) {
      # Some TeX installations require elevated package installs
      powershell -ExecutionPolicy Bypass -File scripts/uac_run.ps1 -Command $p
    } else {
      & $p
    }
    break
  }
}

Write-Host "Synthesis pipeline complete." -ForegroundColor Green

