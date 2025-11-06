param(
  [string]$MainTex = "../main.tex"
)

Write-Host "=== Strict LaTeX Compile ===" -ForegroundColor Cyan

if (-not (Get-Command pdflatex -ErrorAction SilentlyContinue) -and -not (Get-Command latexmk -ErrorAction SilentlyContinue)) {
  Write-Error "pdflatex/latexmk not found. Install TeX Live or MiKTeX."
  exit 2
}

if (Get-Command latexmk -ErrorAction SilentlyContinue) {
  latexmk -pdf -interaction=nonstopmode $MainTex
} else {
  pdflatex -interaction=nonstopmode $MainTex
  pdflatex -interaction=nonstopmode $MainTex
}

$log = (Split-Path $MainTex -Parent) + "/" + (Split-Path $MainTex -Leaf).Replace('.tex','.log')
if (Test-Path $log) {
  $warns = Select-String -Path $log -Pattern '^(\!)|LaTeX Warning|Package .* Warning' -SimpleMatch
  if ($warns) {
    Write-Error "Strict compile failed due to warnings/errors. See $log"
    exit 3
  }
}

Write-Host "Strict compile passed (no warnings)." -ForegroundColor Green
