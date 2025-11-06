# MiKTeX Admin Repair Script
# Fixes user/administrator sync issues and rebuilds format files

Write-Host "=== MiKTeX Admin Repair ===" -ForegroundColor Cyan
Write-Host ""

Write-Host "[1/4] Synchronizing user/admin links..." -ForegroundColor Yellow
initexmf --admin --mklinks
if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: mklinks failed" -ForegroundColor Red
    pause
    exit 1
}
Write-Host "  ✓ Complete" -ForegroundColor Green

Write-Host "[2/4] Updating file name database (admin)..." -ForegroundColor Yellow
initexmf --admin --update-fndb
if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: admin fndb update failed" -ForegroundColor Red
    pause
    exit 1
}
Write-Host "  ✓ Complete" -ForegroundColor Green

Write-Host "[3/4] Updating file name database (user)..." -ForegroundColor Yellow
initexmf --update-fndb
if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: user fndb update failed" -ForegroundColor Red
    pause
    exit 1
}
Write-Host "  ✓ Complete" -ForegroundColor Green

Write-Host "[4/4] Rebuilding pdflatex format file..." -ForegroundColor Yellow
initexmf --admin --dump=pdflatex
if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: format rebuild failed" -ForegroundColor Red
    pause
    exit 1
}
Write-Host "  ✓ Complete" -ForegroundColor Green

Write-Host ""
Write-Host "=== Verification ===" -ForegroundColor Cyan
pdflatex --version

Write-Host ""
Write-Host "=== MiKTeX repair complete! ===" -ForegroundColor Green
Write-Host "Press any key to close..." -ForegroundColor Gray
pause
