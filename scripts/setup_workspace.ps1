param(
    [string]$RepoUrl = "https://github.com/yaojingang/yao-geo-skills.git",
    [string]$WorkspaceRoot = "",
    [string]$CodexHome = "",
    [switch]$SkipPull,
    [switch]$SkipSkillInstall,
    [switch]$ForceSkillInstall
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

function Write-Step {
    param([string]$Message)
    Write-Host ""
    Write-Host "==> $Message" -ForegroundColor Cyan
}

function Write-Warn {
    param([string]$Message)
    Write-Host "WARN: $Message" -ForegroundColor Yellow
}

function Test-Command {
    param([string]$Name)
    return $null -ne (Get-Command $Name -ErrorAction SilentlyContinue)
}

function Get-PythonCommand {
    if (Test-Command "python") {
        return "python"
    }

    if (Test-Command "py") {
        return "py -3"
    }

    return ""
}

function Invoke-Python {
    param(
        [string]$PythonCommand,
        [string[]]$Arguments
    )

    if ($PythonCommand -eq "py -3") {
        & py -3 @Arguments
    } else {
        & $PythonCommand @Arguments
    }
}

function Get-RepoRoot {
    try {
        $root = git rev-parse --show-toplevel 2>$null
        if ($LASTEXITCODE -eq 0 -and $root) {
            return $root.Trim()
        }
    } catch {
        return ""
    }

    return ""
}

Write-Step "Checking required tools"

if (-not (Test-Command "git")) {
    throw "Git is required. Install Git, then rerun this script."
}

$pythonCommand = Get-PythonCommand
if (-not $pythonCommand) {
    throw "Python 3 is required. Install Python 3.10 or newer, then rerun this script."
}

if (-not (Test-Command "node")) {
    Write-Warn "Node.js was not found. The repository can validate without it, but future skills tooling may need Node."
}

Write-Host "Git: available"
Write-Host "Python: $pythonCommand"

if (-not $WorkspaceRoot) {
    $WorkspaceRoot = Join-Path $HOME "GEO"
}

if (-not $CodexHome) {
    if ($env:CODEX_HOME) {
        $CodexHome = $env:CODEX_HOME
    } else {
        $CodexHome = Join-Path $HOME ".codex"
    }
}

$expectedRepoPath = Join-Path $WorkspaceRoot "yao-geo-skills"
$currentRepoRoot = Get-RepoRoot

if (-not $currentRepoRoot) {
    Write-Step "Preparing workspace repository"
    New-Item -ItemType Directory -Force -Path $WorkspaceRoot | Out-Null

    if (Test-Path $expectedRepoPath) {
        throw "Repository path already exists but is not a Git repository: $expectedRepoPath"
    }

    git clone $RepoUrl $expectedRepoPath
    if ($LASTEXITCODE -ne 0) {
        throw "git clone failed."
    }

    Set-Location $expectedRepoPath
    $currentRepoRoot = Get-RepoRoot
} else {
    Set-Location $currentRepoRoot
}

Write-Host "Repository: $currentRepoRoot"

if (-not $SkipPull) {
    Write-Step "Checking repository update status"
    $status = git status --porcelain

    if ($status) {
        Write-Warn "Working tree has local changes. Skipping git pull to avoid mixing changes."
        Write-Host "Run git status --short to review local changes."
    } else {
        git pull --ff-only
        if ($LASTEXITCODE -ne 0) {
            throw "git pull --ff-only failed. Resolve branch state manually, then rerun this script."
        }
    }
}

Write-Step "Ensuring project workflow directories"
$specDir = Join-Path $currentRepoRoot "docs\superpowers\specs"
$planDir = Join-Path $currentRepoRoot "docs\superpowers\plans"
New-Item -ItemType Directory -Force -Path $specDir | Out-Null
New-Item -ItemType Directory -Force -Path $planDir | Out-Null

if (-not $SkipSkillInstall) {
    Write-Step "Installing project skills into Codex skills directory"
    $sourceSkillsDir = Join-Path $currentRepoRoot "skills"
    $targetSkillsDir = Join-Path $CodexHome "skills"

    if (-not (Test-Path $sourceSkillsDir)) {
        throw "Source skills directory not found: $sourceSkillsDir"
    }

    New-Item -ItemType Directory -Force -Path $targetSkillsDir | Out-Null

    Get-ChildItem -Path $sourceSkillsDir -Directory | ForEach-Object {
        $source = $_.FullName
        $target = Join-Path $targetSkillsDir $_.Name

        if ((Test-Path $target) -and (-not $ForceSkillInstall)) {
            Write-Warn "Skill already exists, skipping: $($_.Name). Use -ForceSkillInstall to refresh it."
        } else {
            Copy-Item -Path $source -Destination $targetSkillsDir -Recurse -Force
            Write-Host "Installed skill: $($_.Name)"
        }
    }
}

Write-Step "Running repository validation"
$validationScript = Join-Path $currentRepoRoot "scripts\validate_repository.py"
Invoke-Python -PythonCommand $pythonCommand -Arguments @($validationScript)

if ($LASTEXITCODE -ne 0) {
    throw "Repository validation failed."
}

Write-Step "Setup complete"
Write-Host "Repository root: $currentRepoRoot"
Write-Host "Codex home: $CodexHome"
Write-Host "Next step: open this repository on the second computer and follow AGENTS.md."
