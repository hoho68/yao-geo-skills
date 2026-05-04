# GEOFlow Application Handoff Checklist

Date: 2026-05-04
Branch baseline: `007-local-landing-integration`
Mode: real application intake, preview-first, no production activation

## Purpose

Use this checklist when the real GEOFlow application source becomes available.
It prevents the team from treating the Skill repository or fixture workspace as
the production application and defines the exact gate before a preview edit
session can be created.

## Inputs To Provide

Provide one of:

- a local application path
- a Git repository URL that can be cloned locally
- a ZIP/archive that can be extracted into `D:\GEO`

Recommended local target path:

```text
D:\GEO\geoflow-app
```

Do not place the real application inside:

- `D:\GEO\yao-geo-skills`
- `D:\GEO\yao-geo-skills\skills`
- `D:\GEO\yao-geo-skills\fixtures`

## Initial Safety Rules

Before any theme edit:

- do not run production activation
- do not edit the active/base theme directly
- do not change backend queries, routes, controllers, database schema, SEO
  contracts, or admin settings
- do not copy customer secrets, `.env`, private URLs, or credentials into this
  Skill repository
- keep any experimental output inside the application workspace or a preview
  branch, not in public examples

## Step 1: Confirm The Path

Run:

```powershell
$app = "D:\GEO\geoflow-app"
Test-Path -LiteralPath $app
Get-ChildItem -LiteralPath $app -Force | Select-Object Mode,Name
```

Pass condition:

- the path exists
- the directory is the application root, not a nested docs/export folder

Stop if:

- the path points to `yao-geo-skills`
- the path only contains documents, screenshots, or exported static files
- the path is a package archive that has not been extracted

## Step 2: Identify Framework Signals

For Laravel GEOFlow, these files/directories should exist:

```text
artisan
routes/web.php
resources/views/site
resources/views/theme
```

Preferred extra Laravel signal:

```text
app/Support/Site/SiteThemeViewResolver.php
```

For legacy PHP GEOFlow, these files/directories should exist:

```text
index.php
article.php
category.php
archive.php
includes/header.php
themes
```

Pass condition:

- one full signal set is present

Stop if:

- neither signal set is present
- only generic files like `README.md`, `package.json`, or `composer.json` are
  present
- the directory is another Skill repository copy

## Step 3: Inspect Git State

If the application is a Git repository, run:

```powershell
git -C $app status -sb
git -C $app remote -v
git -C $app branch --show-current
```

Pass condition:

- the branch is known
- dirty changes are understood
- the remote origin is the expected application repository

Stop if:

- there are unexplained dirty business changes
- the remote points to `yao-geo-skills`
- the current branch is unknown and production-related

## Step 4: Run Theme Discovery

From the Skill repository root:

```powershell
python skills\yao-geoflow-design\scripts\discover_themes.py $app
```

Pass condition:

- `theme_system_detected=true`
- `theme_count` is greater than `0`
- at least one theme has editable files

Stop if:

- `theme_system_detected=false`
- `theme_count=0`
- discovery reports the wrong framework
- the only discovered themes are generated or backup directories

## Step 5: Choose A Low-Risk Target Theme

Pick a target theme only after discovery passes.

Prefer:

- an inactive theme
- a duplicate/staging theme
- a theme explicitly selected by the operator

Avoid:

- the active production theme unless a preview fork will be created first
- backup directories
- generated temp themes
- themes with unclear ownership

Record:

```text
target_theme_id=<theme-id>
reason=<why this is safe enough for preview>
operator_confirmation=<who approved the target>
```

## Step 6: Create Preview Edit Session

Only after Steps 1-5 pass, run:

```powershell
python skills\yao-geoflow-design\scripts\prepare_theme_edit_session.py `
  $app `
  --base-theme <target_theme_id> `
  --new-theme-id <preview_theme_id> `
  --new-name "<preview display name>" `
  --change-request "<small preview-only change>"
```

Pass condition:

- a new preview theme is created
- `session_state=preview`
- `base_theme_id` points to the selected target theme
- editable files are listed
- the base theme remains unchanged

Stop if:

- the script would overwrite an existing theme
- preview theme creation fails
- the output suggests direct activation

## Step 7: First Preview Edit Slice

The first real edit slice should be tiny.

Allowed first-slice changes:

- preview theme CSS
- preview theme Blade view markup
- preview `tokens.json`
- preview `mapping.json`
- preview `change-plan.md`
- preview `preview-notes.md`

Not allowed in the first slice:

- controllers
- routes
- migrations
- database changes
- admin settings
- activation/finalization
- base theme edits

Pass condition:

- only preview theme files changed
- discovery still detects both base and preview themes
- preview remains marked `session_state=preview`

## Step 8: Validation Before Any Commit

From the Skill repository root:

```powershell
python scripts\validate_repository.py
python scripts\smoke_yao_geoflow_template_package.py
python scripts\smoke_geoflow_laravel_fixture.py
git diff --check
```

From the application repository root, run project-specific checks if available.
Examples:

```powershell
php artisan test
npm test
npm run build
```

Only run commands that are safe for the local environment and do not mutate
production data.

## Required Acceptance Note

Before committing real application work, write a short note with:

- application path
- framework detected
- discovery command output summary
- chosen target theme
- preview theme id
- files changed
- validation commands run
- explicit statement that production activation did not happen

Recommended location inside this Skill repository:

```text
docs/geoflow-real-app-acceptance-YYYYMMDD.md
```

## Hard Stop Conditions

Stop and ask before continuing if:

- the application path is uncertain
- the application has production credentials in the working tree
- the base theme appears to be active and no preview fork exists
- discovery cannot identify a theme system
- the requested change requires backend logic
- the operator asks for activation before preview review
- any command would overwrite or delete application files outside a preview
  theme

## Next Action Template

When the real application source is ready, the first message should provide:

```text
Application path:
Expected framework: Laravel | legacy PHP | unknown
Target outcome: discovery only | create preview fork | first preview edit
Activation allowed: no
```

Default target outcome should be `discovery only`.
