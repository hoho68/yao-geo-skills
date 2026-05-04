# Local Landing Trial Report

Date: 2026-05-04
Branch: `007-local-landing-integration`
Mode: local-only landing trial, no PR, no production activation

## Trial Goal

Validate whether the current local mainline can support a low-risk real workflow:

- `yao-geoflow-template` should provide a self-contained preview package contract.
- `yao-geoflow-design` should remain a preview-first design workflow example with its inherited runtime metadata warning clearly separated from the package contract.
- Repository-level validation should still pass after the integrated local landing branch is used as the working baseline.

## Trial Target

The trial used the committed Qiaomu public example because no separate GEOFlow Laravel or legacy PHP business workspace is present under `D:\GEO`.

Available local workspace scan:

- `D:\GEO\yao-geo-skills`: skills repository
- `D:\GEO`: no detected GEOFlow `artisan`, `resources/views/theme`, legacy `themes/`, or preview PHP system

This means the trial can validate public preview/package readiness, but cannot yet validate a live GEOFlow theme discovery/edit session against a real production codebase.

## Commands Run

```powershell
git status -sb
python scripts\validate_repository.py
python scripts\smoke_yao_geoflow_template_package.py
python skills\yao-geoflow-design\scripts\discover_themes.py D:\GEO\yao-geo-skills
python skills\yao-geoflow-design\scripts\discover_themes.py D:\GEO
```

An additional temporary local HTTP smoke check served each skill preview root and requested the Qiaomu preview pages, CSS, JavaScript, and metadata paths.

## Results

### Template Package

`yao-geoflow-template` passed the real preview/package readiness check.

The following committed paths returned HTTP 200 from a clean local static server:

- `preview/qiaomu-editorial-20260418/index.html`
- `preview/qiaomu-editorial-20260418/category.html`
- `preview/qiaomu-editorial-20260418/article.html`
- `preview/qiaomu-editorial-20260418/archive.html`
- `preview/qiaomu-editorial-20260418/assets/theme.css`
- `preview/qiaomu-editorial-20260418/assets/app.js`
- `preview/qiaomu-editorial-20260418/package/tokens.json`
- `preview/qiaomu-editorial-20260418/package/mapping.json`

The package metadata keeps `activation_status=preview-only`, so preview readiness is still separated from production activation readiness.

### Design Example

`yao-geoflow-design` passed as a public design workflow preview example, but not as a self-contained package metadata contract.

The committed preview pages and assets returned HTTP 200:

- `preview/qiaomu-editorial-20260418/index.html`
- `preview/qiaomu-editorial-20260418/category.html`
- `preview/qiaomu-editorial-20260418/article.html`
- `preview/qiaomu-editorial-20260418/archive.html`
- `preview/qiaomu-editorial-20260418/assets/theme.css`
- `preview/qiaomu-editorial-20260418/assets/app.js`

The inherited runtime metadata paths returned HTTP 404:

- `outputs/qiaomu-editorial-20260418/tokens.json`
- `outputs/qiaomu-editorial-20260418/mapping.json`

This is acceptable for the current landing baseline because the design example README explicitly documents this inherited warning and says the example is not the self-contained `yao-geoflow-template` package contract.

### Workspace Discovery

Running `discover_themes.py` against both `D:\GEO\yao-geo-skills` and `D:\GEO` returned:

- `framework=legacy_php`
- `theme_system_detected=false`
- `theme_count=0`

This confirms that a real GEOFlow theme edit session cannot begin until a real GEOFlow application workspace is supplied or cloned locally.

## Landing Judgment

The current branch is suitable as the local usable mainline for the skills repository.

Use it for:

- continuing package contract hardening
- public preview/package examples
- repository CI and publishing-rule validation
- preparing future GEOFlow theme work

Do not treat it as proof that a live GEOFlow application can be edited yet. That requires a separate acceptance pass against a real GEOFlow workspace with detected themes.

## Open Landing Items

1. Provide or clone a real GEOFlow application workspace for `yao-geoflow-design` discovery.
2. Run `discover_themes.py` against that application workspace.
3. Choose one low-risk target theme and create a preview edit session.
4. Keep activation out of scope until preview review passes.

## Recommended Next Step

Move into a real GEOFlow workspace onboarding stage:

- identify the actual GEOFlow application path
- confirm whether it is Laravel or legacy PHP
- run theme discovery
- only then decide the first preview edit slice
