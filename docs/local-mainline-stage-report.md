# Local Mainline Stage Report

Date: 2026-05-04
Branch: `007-local-landing-integration`
Fork backup: `hoho68/yao-geo-skills:007-local-landing-integration`
Latest verified commit: `921da3d`
Mode: local landing mainline, no upstream PR, no production activation

## Stage Summary

`007-local-landing-integration` is now the usable local mainline for this
repository. It integrates the `yao-geoflow-template` package contract work, the
`yao-geoflow-design` public example work, local landing documentation, and a
fixture-based reroute for testing the design workflow while the real GEOFlow
application source is unavailable.

The branch is backed up to the user's fork and is aligned with the remote fork
branch.

This branch should be used as the working baseline for continued local landing
work. Do not open an upstream PR from it unless collaboration with the upstream
maintainer becomes necessary.

## Integrated Outcomes

### Template Package Contract

`yao-geoflow-template` now has a self-contained public Qiaomu preview package:

- committed preview pages for home, category, article, and archive
- committed `package/tokens.json`
- committed `package/mapping.json`
- example README
- contract documentation
- smoke validation for preview routes, metadata, runtime-output boundaries, and
  preview-only activation status

The template package is the strongest current evidence that the skills
repository can support preview-first package delivery.

### Preview Vs Activation Boundary

The branch documents and validates that preview readiness is separate from
production activation readiness.

The current rule is:

- preview packages may be reviewable from committed metadata and preview routes
- production activation requires a separate activation request, spec, or
  operator-approved implementation step
- public examples must not claim production readiness by default

### Design Workflow Example

`yao-geoflow-design` now includes a public Qiaomu design example. It is useful as
a design workflow and preview-review example, but it is intentionally not
treated as the same self-contained package contract as `yao-geoflow-template`.

The inherited runtime metadata warning remains documented and accepted for this
stage.

### Real Application Source Correction

Local scans did not find a real GEOFlow application workspace. The checked
machine paths did not contain a Laravel GEOFlow application or a legacy PHP
GEOFlow application.

This means the current branch proves the skills repository workflow and fixture
workflow, not live production application editing.

### Fixture Reroute

Because the real application source is unavailable, the branch adds:

- `fixtures/geoflow-laravel-minimal`
- a baseline `default` theme
- a `qiaomu-preview` preview edit session
- fixture discovery and preview isolation smoke validation

The fixture is explicitly non-production. It exists to keep the workflow moving
and to test the design scripts safely.

## Quality Gates

The current local mainline is expected to pass:

```powershell
python scripts\validate_repository.py
python scripts\smoke_yao_geoflow_template_package.py
python scripts\smoke_geoflow_laravel_fixture.py
python -m py_compile scripts\validate_repository.py scripts\smoke_yao_geoflow_template_package.py scripts\smoke_geoflow_laravel_fixture.py skills\yao-geoflow-design\scripts\discover_themes.py skills\yao-geoflow-design\scripts\prepare_theme_edit_session.py skills\yao-geoflow-design\scripts\finalize_theme_edit_session.py
git diff --check
```

The GitHub Actions workflow also runs:

- repository contract validation
- `yao-geoflow-template` package smoke validation
- GEOFlow Laravel fixture smoke validation

## Current Branch State

Relative to `origin/main`, this local mainline contains these landing commits:

- `452204a standardize yao-geoflow-template package contract`
- `9ac4e78 add yao-geoflow-template package validation`
- `be70a0c add yao-geoflow-design public example`
- `84c0e30 document local landing trial results`
- `d908083 document geoflow workspace onboarding status`
- `0627299 clarify current path is not geoflow app workspace`
- `6d3566e document geoflow source location correction`
- `a21d70e add geoflow laravel fixture for landing reroute`
- `f784986 edit qiaomu preview fixture slice`
- `921da3d add geoflow fixture smoke gate`

The branch was backed up to:

```text
https://github.com/hoho68/yao-geo-skills/tree/007-local-landing-integration
```

## Known Gaps

1. A real GEOFlow application workspace is still not available locally.
2. The fixture cannot prove production theme rendering, admin activation, route
   behavior, database-backed content, or controller integration.
3. `yao-geoflow-design` still needs a real application acceptance pass before it
   should be used for live theme editing.
4. No upstream PR is currently necessary because the user's goal is local
   landing speed, not upstream collaboration.

## Recommended Operating Rule

Use `007-local-landing-integration` as the local baseline.

For new work:

1. keep changes small and slice-based
2. run the three smoke/validation commands before committing
3. push to the user's fork when local commits become worth backing up
4. avoid upstream PRs unless collaboration or review becomes necessary
5. do not treat fixture success as live application success

## Next Landing Move

The next practical move is to define a repeatable "real application handoff
checklist" for the moment the actual GEOFlow application source becomes
available.

That checklist should say exactly what path to provide, what files must exist,
which command to run first, and what conditions must be true before any preview
edit session is created.

The handoff checklist now lives at:

```text
docs/geoflow-app-handoff-checklist.md
```
