# GEOFlow Workspace Onboarding

Date: 2026-05-04
Branch: `007-local-landing-integration`
Mode: local-only workspace discovery, no PR, no production activation

## Purpose

This note records the first real GEOFlow workspace onboarding pass. The goal was
to find a local GEOFlow application workspace that can be used for
`yao-geoflow-design` theme discovery and a future preview edit session.

## Local Scan Scope

Scanned root:

- `D:\GEO`

Observed top-level content:

- `yao-geo-skills`
- `.trae`
- several small JSON field files

## GEOFlow Detection Signals

The scan looked for Laravel GEOFlow signals:

- `artisan`
- `routes/web.php`
- `resources/views/site`
- `resources/views/theme`
- `app/Support/Site/SiteThemeViewResolver.php`

The scan also looked for legacy PHP GEOFlow signals:

- `index.php`
- `article.php`
- `category.php`
- `archive.php`
- `includes/header.php`
- `theme-preview.php`
- `includes/theme_preview.php`
- `themes`

No matching application workspace was found under `D:\GEO`.

## Discovery Commands

```powershell
python skills\yao-geoflow-design\scripts\discover_themes.py D:\GEO
python skills\yao-geoflow-design\scripts\discover_themes.py D:\GEO\yao-geo-skills
```

Both commands completed successfully and reported:

- `theme_system_detected=false`
- `theme_count=0`

For `D:\GEO`, the script reported:

- `framework=legacy_php`
- `themes_root=D:\GEO\themes`
- missing legacy theme-system signals

For `D:\GEO\yao-geo-skills`, the script reported:

- `framework=legacy_php`
- `themes_root=D:\GEO\yao-geo-skills\themes`
- missing legacy theme-system signals

These are negative discovery results, not validation failures.

## Onboarding Conclusion

The skills repository is ready as a local working baseline, but a real GEOFlow
application workspace has not been connected yet.

`yao-geoflow-design` cannot safely enter a true preview edit session until the
actual application code is available locally. The next workspace should be a
GEOFlow app directory, not this skills repository.

## Ready Criteria For The Next Workspace

Use one of the following acceptable inputs:

- a local path to the actual GEOFlow application
- a Git repository URL that can be cloned locally
- a ZIP/archive of the GEOFlow application that can be extracted into `D:\GEO`

The workspace is ready for theme discovery when one of these signal sets exists:

- Laravel: `artisan`, `routes/web.php`, `resources/views/site`, and
  `resources/views/theme`
- legacy PHP: `index.php`, `article.php`, `category.php`, `archive.php`,
  `includes/header.php`, and `themes`

## Recommended Next Step

Place or clone the real GEOFlow application under `D:\GEO`, then run theme
discovery against that application path before creating any preview edit
session.
