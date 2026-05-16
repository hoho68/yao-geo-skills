# Codex Task: Set Up Yao GEO Skills On This Computer

You are operating on the second computer. Your job is to install and verify the Yao GEO Skills workspace from GitHub, then report the exact result.

## Goal

Set up this computer so it can work on the GEO project using the same repository, local skills, and project rules as the primary computer.

## Repository

- GitHub repository: `https://github.com/hoho68/yao-geo-skills.git`
- Branch: `007-local-landing-integration`
- Workspace root: `$HOME\GEO`
- Repository path: `$HOME\GEO\yao-geo-skills`

## Safety Rules

- Do not delete existing user files.
- Do not copy, create, or request secrets.
- Do not commit or push anything during setup.
- If a repository already exists and has local changes, stop and show `git status --short`.
- If Git, Python, or PowerShell is missing, stop and tell the user what to install.
- If Node.js is missing, warn the user but continue unless a later step requires it.

## Step 1: Check Required Tools

Run these in PowerShell:

```powershell
git --version
python --version
node --version
```

Expected:

- `git --version` succeeds.
- `python --version` succeeds and is Python 3.10 or newer.
- `node --version` is recommended. If it fails, warn only.

If `python` fails but `py -3 --version` works, use `py -3` where Python is needed.

## Step 2: Prepare Workspace

Run:

```powershell
$workspace = "$HOME\GEO"
$repo = "$workspace\yao-geo-skills"
New-Item -ItemType Directory -Force -Path $workspace | Out-Null
```

If `$repo` does not exist, clone it:

```powershell
git clone -b 007-local-landing-integration https://github.com/hoho68/yao-geo-skills.git "$repo"
cd "$repo"
```

If `$repo` already exists, enter it and inspect status:

```powershell
cd "$repo"
git status --short
```

If there are local changes, stop and report them to the user before pulling.

If there are no local changes, update it:

```powershell
git fetch --all --prune
git checkout 007-local-landing-integration
git pull --ff-only
```

## Step 3: Run Project Setup Script

Run:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\setup_workspace.ps1 -ForceSkillInstall
```

This should:

- install project skills into `$HOME\.codex\skills`
- create `docs\superpowers\specs\`
- create `docs\superpowers\plans\`
- run repository validation

## Step 4: Verify Repository Manually

Run:

```powershell
python scripts\validate_repository.py
```

If `python` does not work but `py -3` works, run:

```powershell
py -3 scripts\validate_repository.py
```

Expected output:

```text
Repository validation passed.
```

## Step 5: Verify Installed Skills

Run:

```powershell
Get-ChildItem "$HOME\.codex\skills" | Where-Object {
    $_.Name -like "yao-*"
} | Select-Object Name, FullName
```

Expected to include:

- `yao-geoflow-cli`
- `yao-geoflow-design`
- `yao-geoflow-template`
- `yao-geo-tracking`

## Step 6: Report Back

After running the setup, report:

- repository path
- current branch
- current commit
- whether repository validation passed
- whether project skills were installed
- any warnings, especially missing Node.js or local changes

Use these commands for the final report:

```powershell
git branch --show-current
git rev-parse --short HEAD
git status --short
```

## Success Criteria

Setup is complete only if:

- the repository exists at `$HOME\GEO\yao-geo-skills`
- branch is `007-local-landing-integration`
- `scripts\setup_workspace.ps1` ran successfully
- `python scripts\validate_repository.py` or `py -3 scripts\validate_repository.py` passed
- the `yao-*` skills exist under `$HOME\.codex\skills`

If any success criterion is not met, do not claim setup is complete. Show the failed command and its output.
