 = Join-Path C:\Users\ericj\AppData\Local 'Pandoc\\pandoc.exe'
if (-not (Test-Path )) {
    Write-Error "pandoc.exe not found"
    exit 1
}
 = @(
    "--from=markdown"
    "--to=latex"
    "--output=synthesis/modules/narrative/genesis_phase4_draft.tex"
    "math5GenesisFrameworkUnveiled.md"
)
Start-Process -FilePath  -ArgumentList  -Wait
