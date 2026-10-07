[CmdletBinding()]
param(
    [string]$RepositoryPath = (Get-Location).Path,
    [ValidateSet('Skip', 'Diff', 'Overwrite')]
    [string]$ExistingFileAction = 'Skip'
)

$ErrorActionPreference = 'Stop'
$templateRoot = Join-Path $PSScriptRoot '..\templates\repository'
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
    $targetRoot = (Resolve-Path -LiteralPath $RepositoryPath).Path
} catch {
    Write-Error "Repository path does not exist: $RepositoryPath"
    exit 1
}
if (-not (Test-Path -LiteralPath (Join-Path $targetRoot '.git'))) {
    Write-Error "Target is not a Git repository: $targetRoot"
    exit 1
}
if (-not (Test-Path -LiteralPath $templateRoot -PathType Container)) {
    Write-Error "Repository templates were not found: $templateRoot"
    exit 1
}

$created = 0
$preserved = 0
foreach ($relativePath in $requiredFiles) {
    $source = Join-Path $templateRoot ($relativePath -replace '/', '\\')
    $destination = Join-Path $targetRoot ($relativePath -replace '/', '\\')
    if (-not (Test-Path -LiteralPath $source -PathType Leaf)) {
        Write-Error "Required template is missing: $relativePath"
        exit 1
    }
    if ((Test-Path -LiteralPath $destination) -and -not (Test-Path -LiteralPath $destination -PathType Leaf)) {
        Write-Error "A directory blocks required file $relativePath; resolve it manually before initialization."
        exit 1
    }

    if (Test-Path -LiteralPath $destination) {
        switch ($ExistingFileAction) {
            'Skip' {
                Write-Host "PRESERVED existing file: $relativePath"
                $preserved++
            }
            'Diff' {
                $difference = Compare-Object (Get-Content -LiteralPath $source) (Get-Content -LiteralPath $destination)
                if ($difference) {
                    Write-Host "DIFFERENCES for $relativePath (<= template, => existing):"
                    $difference | Format-Table -AutoSize | Out-Host
                } else {
                    Write-Host "MATCH existing file: $relativePath"
                }
                $preserved++
            }
            'Overwrite' {
                Copy-Item -LiteralPath $source -Destination $destination -Force
                Write-Host "OVERWROTE existing file: $relativePath"
                $created++
            }
        }
    } else {
        $destinationDirectory = Split-Path -Parent $destination
        if (-not (Test-Path -LiteralPath $destinationDirectory)) {
            New-Item -ItemType Directory -Path $destinationDirectory -Force | Out-Null
        }
        Copy-Item -LiteralPath $source -Destination $destination
        Write-Host "CREATED $relativePath"
        $created++
    }
}

Write-Host "Applied templates: $created created/updated; $preserved preserved."
$powerShell = if (Get-Command pwsh -ErrorAction SilentlyContinue) { 'pwsh' } else { 'powershell' }
& $powerShell -NoProfile -ExecutionPolicy Bypass -File (Join-Path $PSScriptRoot 'verify-repository-bootstrap.ps1') -RepositoryPath $targetRoot
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

