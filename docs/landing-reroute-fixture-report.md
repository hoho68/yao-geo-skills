# Landing Reroute Fixture Report

Date: 2026-05-04
Branch: `007-local-landing-integration`
Mode: local-only fixture drill, no PR, no production activation

## Why This Reroute Exists

The real GEOFlow application source is not present in the checked local paths.
To keep the project landing work moving without pretending the Skill repository
is a production application, the workflow now uses a minimal non-production
fixture.

The fixture is intentionally small and explicit:

- path: `fixtures/geoflow-laravel-minimal`
- framework signal: Laravel-style GEOFlow theme workspace
- purpose: exercise discovery and preview edit-session scripts
- status: fixture-only, not deployable

## Fixture Boundary

The fixture contains only the signals required for safe local workflow testing:

- `artisan`
- `routes/web.php`
- `resources/views/site`
- `resources/views/theme`
- `app/Support/Site/SiteThemeViewResolver.php`
- one baseline theme: `default`

The fixture does not include:

- database configuration
- controllers
- production `.env`
- admin activation settings
- customer content
- live deployment path

## Commands Run

```powershell
python skills\yao-geoflow-design\scripts\discover_themes.py fixtures\geoflow-laravel-minimal

python skills\yao-geoflow-design\scripts\prepare_theme_edit_session.py `
  fixtures\geoflow-laravel-minimal `
  --base-theme default `
  --new-theme-id qiaomu-preview `
  --new-name "Qiaomu Preview Fixture" `
  --change-request "Fixture-only landing reroute drill; keep preview separate from activation."

python skills\yao-geoflow-design\scripts\discover_themes.py fixtures\geoflow-laravel-minimal
```

## Discovery Result

Before creating the preview fork:

- `framework=laravel`
- `theme_system_detected=true`
- `theme_count=1`
- discovered baseline theme: `default`

After creating the preview fork:

- `framework=laravel`
- `theme_system_detected=true`
- `theme_count=2`
- discovered baseline theme: `default`
- discovered preview theme: `qiaomu-preview`

The preview theme is marked with:

- `base_theme_id=default`
- `target_theme_id=default`
- `mode=edit_theme`
- `session_state=preview`

## Landing Judgment

The reroute is successful for local workflow validation.

This gives the project a safe, repeatable way to test:

- GEOFlow workspace detection
- Laravel theme inventory
- preview fork creation
- editable-file listing
- preview-vs-activation separation

This does not replace testing against a real GEOFlow application. It only keeps
the workflow moving until real application source is available.

## Next Gate

Use the fixture for one MVP preview edit slice:

1. modify only `qiaomu-preview` theme files
2. keep `default` unchanged
3. update `change-plan.md` and `preview-notes.md`
4. rerun discovery and repository validation
5. do not run `finalize_theme_edit_session.py` unless the goal is explicitly to
   test publish/replace mechanics inside the fixture

## Fixture Quality Gate

The fixture workflow is guarded by:

```powershell
python scripts\smoke_geoflow_laravel_fixture.py
```

The smoke test verifies:

- `discover_themes.py` recognizes the fixture as Laravel
- the fixture exposes exactly `default` and `qiaomu-preview`
- `default` remains a baseline theme
- `qiaomu-preview` remains an `edit_theme` preview session
- preview Blade files do not reference `theme.default`
- preview metadata keeps `activation_status=preview-only`
- no `.theme-backups` directory is committed under the fixture
