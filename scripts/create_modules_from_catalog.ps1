Param(
  [string]$BaseDir = ".",
  [int]$Limit = 50,
  [int]$MinScore = 10,
  [string]$Framework = ""
)

Write-Host "Creating LaTeX modules from catalog..." -ForegroundColor Cyan

$argsList = @("--base-dir", $BaseDir, "--limit", $Limit, "--min-score", $MinScore)
if ($Framework -ne "") {
  $argsList += @("--framework", $Framework)
}

python scripts/auto_create_modules.py @argsList
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

Write-Host "Done. See synthesis/modules/modules_index_auto.tex" -ForegroundColor Green

