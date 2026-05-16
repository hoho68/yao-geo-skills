# Second Machine Setup

This guide explains how to operate the GEO project from another Windows computer while keeping the same repository structure, skills, and project rules.

## What Syncs

These items should sync through Git:

- GEO skill packages under `skills/`
- public documentation under `docs/`
- repository validation and setup scripts under `scripts/`
- shared templates, schemas, and rubrics under `shared/`
- project rules in `AGENTS.md`
- specs and plans under `docs/superpowers/`

These items should stay local to each computer:

- `.env` and `.env.*`
- API keys and platform tokens
- customer backend credentials
- private customer source packages
- unsanitized customer outputs
- local caches and temporary files

## Prerequisites

Install these on the second computer:

- Git
- Python 3.10 or newer
- Node.js, recommended for skills tooling and future automation
- Codex Desktop or the Codex environment you plan to use

## One-Time Setup

Open PowerShell and run:

```powershell
$workspace = "$HOME\GEO"
New-Item -ItemType Directory -Force -Path $workspace | Out-Null

git clone https://github.com/yaojingang/yao-geo-skills.git "$workspace\yao-geo-skills"
cd "$workspace\yao-geo-skills"

.\scripts\setup_workspace.ps1
```

If you want another Codex session to perform the setup automatically, copy the full contents of
`docs/second-machine-codex-task.md` into Codex on the second computer and ask it to execute the task.

If the repository already exists, run the script from inside the repository:

```powershell
cd "$HOME\GEO\yao-geo-skills"
.\scripts\setup_workspace.ps1
```

## What The Script Does

The setup script:

- checks that Git is available
- checks that Python is available
- warns if Node.js is missing
- pulls the latest repository changes only when the working tree is clean
- creates `docs/superpowers/specs/` and `docs/superpowers/plans/`
- copies project skills into the local Codex skills directory
- runs `python scripts/validate_repository.py`

It does not:

- delete local files
- overwrite existing installed skills unless you pass `-ForceSkillInstall`
- copy private credentials
- configure customer-specific platform accounts

## Updating The Second Machine

For normal updates:

```powershell
cd "$HOME\GEO\yao-geo-skills"
git pull --ff-only
.\scripts\setup_workspace.ps1 -ForceSkillInstall
```

If `git pull --ff-only` fails because the second computer has local changes, review them first:

```powershell
git status --short
```

Commit, stash, or move the local changes before pulling.

## Working Rules On Both Machines

Both computers should follow the same project rules:

- new capabilities start with a spec in `docs/superpowers/specs/`
- approved specs get plans in `docs/superpowers/plans/`
- reusable GEO work becomes a skill package under `skills/`
- public skill changes update `registry/skills.json`
- validation runs before pushing
- secrets and unsanitized customer material stay out of Git

See `AGENTS.md` for the agent-facing version of these rules.

## Troubleshooting

If Codex does not show the project skills, rerun:

```powershell
.\scripts\setup_workspace.ps1 -ForceSkillInstall
```

If validation fails, fix the reported repository contract issue before pushing.

If another machine needs a different Codex home directory, pass it explicitly:

```powershell
.\scripts\setup_workspace.ps1 -CodexHome "D:\CodexHome"
```
