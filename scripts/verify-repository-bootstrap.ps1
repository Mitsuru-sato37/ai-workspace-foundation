[CmdletBinding()]
param(
    [string]$RepositoryPath = (Get-Location).Path
)

$ErrorActionPreference = 'Stop'
$requiredFiles = @(
    'AGENTS.md',
    'docs/SPEC.md',
    'docs/STATUS.md',
    'docs/DEBUG_STANDARD.md',
    'docs/DEBUG_MATRIX.md',
    'git-status.cmd',
    'scripts/git-sync-status.ps1'
)

try {
    $root = (Resolve-Path -LiteralPath $RepositoryPath).Path
} catch {
    Write-Error "Repository path does not exist: $RepositoryPath"
    exit 1
}

$missing = @($requiredFiles | Where-Object {
    $candidate = Join-Path $root ($_ -replace '/', '\\')
    -not (Test-Path -LiteralPath $candidate -PathType Leaf)
})

if ($missing.Count -gt 0) {
    Write-Host 'Repository bootstrap is incomplete. Missing required files:'
    foreach ($path in $missing) { Write-Host " - $path" }
    exit 1
}

Write-Host "Repository bootstrap check passed ($($requiredFiles.Count) required files)."
exit 0

