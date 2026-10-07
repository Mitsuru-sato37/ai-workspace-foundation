$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent $PSScriptRoot
$source = Join-Path $root 'templates\repository'
$initializer = Join-Path $PSScriptRoot 'initialize-repository.ps1'
$checker = Join-Path $PSScriptRoot 'verify-repository-bootstrap.ps1'
$required = @(
    'AGENTS.md',
    'docs/SPEC.md',
    'docs/STATUS.md',
    'docs/DEBUG_STANDARD.md',
    'docs/DEBUG_MATRIX.md',
    'git-status.cmd',
    'scripts/git-sync-status.ps1'
)
$temp = Join-Path ([IO.Path]::GetTempPath()) ('repository-bootstrap-test-' + [guid]::NewGuid().ToString('N'))

function Assert($condition, $message) {
    if (-not $condition) { throw $message }
}

try {
    New-Item -ItemType Directory -Path $temp -Force | Out-Null
    New-Item -ItemType Directory -Path (Join-Path $temp '.git') -Force | Out-Null
    $missingOutput = & powershell -NoProfile -ExecutionPolicy Bypass -File $checker -RepositoryPath $temp 2>&1
    $missingExit = $LASTEXITCODE
    Assert ($missingExit -ne 0) 'Checker accepted a repository with all required files missing.'
    foreach ($path in $required) {
        Assert (($missingOutput -join "`n") -match [regex]::Escape($path)) "Missing-file output did not name $path."
    }

    & powershell -NoProfile -ExecutionPolicy Bypass -File $initializer -RepositoryPath $temp
    Assert ($LASTEXITCODE -eq 0) 'Initializer failed on an empty Git repository.'

    foreach ($path in $required) {
        $target = Join-Path $temp ($path -replace '/', '\\')
        $template = Join-Path $source ($path -replace '/', '\\')
        Assert ((Get-FileHash -LiteralPath $target -Algorithm SHA256).Hash -eq (Get-FileHash -LiteralPath $template -Algorithm SHA256).Hash) "Applied file differs from template: $path"
    }

    $preserved = Join-Path $temp 'AGENTS.md'
    Set-Content -LiteralPath $preserved -Value 'user-owned content' -NoNewline
    $diffOutput = & powershell -NoProfile -ExecutionPolicy Bypass -File $initializer -RepositoryPath $temp -ExistingFileAction Diff 2>&1
    Assert ($LASTEXITCODE -eq 0) 'Diff mode failed on an existing file.'
    Assert (($diffOutput -join "`n") -match 'DIFFERENCES for AGENTS\.md') 'Diff mode did not report the pre-existing difference.'
    Assert ((Get-Content -LiteralPath $preserved -Raw) -eq 'user-owned content') 'Diff mode changed an existing file.'
    & powershell -NoProfile -ExecutionPolicy Bypass -File $initializer -RepositoryPath $temp
    Assert ($LASTEXITCODE -eq 0) 'Default skip mode failed on an existing file.'
    Assert ((Get-Content -LiteralPath $preserved -Raw) -eq 'user-owned content') 'Default mode overwrote an existing file.'

    & powershell -NoProfile -ExecutionPolicy Bypass -File $initializer -RepositoryPath $temp -ExistingFileAction Overwrite
    Assert ($LASTEXITCODE -eq 0) 'Explicit overwrite mode failed.'
    Assert ((Get-FileHash -LiteralPath $preserved -Algorithm SHA256).Hash -eq (Get-FileHash -LiteralPath (Join-Path $source 'AGENTS.md') -Algorithm SHA256).Hash) 'Explicit overwrite did not apply the template.'

    $okOutput = & powershell -NoProfile -ExecutionPolicy Bypass -File $checker -RepositoryPath $temp 2>&1
    Assert ($LASTEXITCODE -eq 0) "Checker rejected a completed repository: $($okOutput -join ' ')"

    Write-Host 'PASS: missing files fail with names; complete repository passes; all seven files match templates; skip/diff preserve existing files; explicit overwrite applies template.'
} finally {
    if (Test-Path -LiteralPath $temp) { Remove-Item -LiteralPath $temp -Recurse -Force }
}

