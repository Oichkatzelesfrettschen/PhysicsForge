Param(
  [Parameter(Mandatory=$true)][string]$Command,
  [string]$Arguments = ""
)

# Relaunch the specified command with elevation (UAC prompt)
$psi = New-Object System.Diagnostics.ProcessStartInfo
$psi.FileName = $Command
if ($Arguments -ne "") { $psi.Arguments = $Arguments }
$psi.Verb = "runas"
try {
  $p = [System.Diagnostics.Process]::Start($psi)
  $p.WaitForExit()
  exit $p.ExitCode
} catch {
  Write-Error "Elevation cancelled or failed: $_"
  exit 1
}

