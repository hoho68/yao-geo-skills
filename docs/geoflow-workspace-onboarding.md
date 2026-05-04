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

## Path Clarification Pass

On 2026-05-04, the operator clarified that the project path is the current
project path. The workspace was checked again at both levels:

- `D:\GEO`
- `D:\GEO\yao-geo-skills`

The result did not change:

- `D:\GEO` is not a Git worktree.
- `D:\GEO\yao-geo-skills` is the Git worktree root.
- The Git remotes point to `yao-geo-skills`, which is the Skill repository.
- `.trae/specs/analyze-yao-geo-skills/spec.md` and `README.md` describe this
  repository as a GEO workflow Skill repository, not a GEOFlow application.
- No Laravel or legacy PHP GEOFlow application signals were found in either
  path.

This means the current project path can remain the local Skill landing
baseline, but it should not be treated as the real GEOFlow application
workspace for theme editing.

## Source Location Correction Pass

On 2026-05-04, a broader read-only source location pass checked whether the real
GEOFlow application might be elsewhere on the local machine.

Checked areas:

- `D:\GEO`
- `D:\GEO.claude`
- `D:\Downloads`
- `D:\Documents`
- `D:\BaiduNetdiskDownload`
- `D:\下载收集`
- `D:\文档`
- common user folders under `C:\Users\Administrator`
- likely workspace directories under `D:\跨境龙虾会`, `D:\致盛龙虾会`, and
  `D:\MyLocalBot`

The scan looked for:

- Laravel signals: `artisan`, `routes/web.php`, `resources/views/site`,
  `resources/views/theme`, `composer.json`
- legacy PHP signals: `index.php`, `article.php`, `category.php`,
  `archive.php`, `includes/header.php`, `themes`
- Git repositories with names or remotes related to `geo`, `geoflow`, `yao`,
  `flow`, or `skills`
- likely compressed source archives with names related to `geo`, `geoflow`,
  `yao`, `laravel`, `theme`, `源码`, or `项目`

Findings:

- No directory had the Laravel or legacy PHP GEOFlow signal set.
- No matching source archive was found in the checked download/document paths.
- `D:\Downloads\i4Tools9\themes` was a false positive from a third-party tool.
- `D:\GEO\yao-geo-skills` and
  `D:\跨境龙虾会\金算盘\workspace\_yao-geo-skills` are Skill repository copies,
  not GEOFlow applications.
- Workspace-like directories such as `D:\跨境龙虾会\金算盘\workspace`,
  `D:\致盛龙虾会\小红虾\workspace`, and `D:\MyLocalBot\moltbot\workspace`
  returned `theme_system_detected=false` and `theme_count=0`.

This pass reinforces the current correction: the real GEOFlow application source
is not currently present in the checked local paths.

## Landing Reroute

Because no real GEOFlow application source was found locally, the landing path
now uses a fixture-only workspace for workflow validation:

- fixture: `fixtures/geoflow-laravel-minimal`
- report: `docs/landing-reroute-fixture-report.md`

The fixture is suitable for testing discovery and preview edit-session scripts.
It is not a replacement for a real application acceptance pass.

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

For the detailed intake gate, use
`docs/geoflow-app-handoff-checklist.md`.

## Recommended Next Step

Place or clone the real GEOFlow application under `D:\GEO`, then run theme
discovery against that application path before creating any preview edit
session.
