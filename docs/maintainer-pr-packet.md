# Maintainer PR Packet

Date: 2026-05-03

This packet prepares the upstream-facing explanation for the
`yao-geoflow-template` standardization work. It is not an open pull request and
should not be treated as a request to merge yet.

Status: local planning packet only. Use this file when the project explicitly
chooses a future PR slice.

Split verification status: PR 1 plus PR 2 reconstructs the old complete
checkpoint exactly. `004-yao-geoflow-template-validation` and
`002-remote-align-yao-geoflow-template` have the same tree hash:
`9a08fbb4ce6cd5f2e2f9c72b9785ab057202e297`.

PR 1 opening decision: eligible to open as a fresh draft PR from
`hoho68:003-yao-geoflow-template-contract` to `yaojingang:main`, but no PR
should be created until the user explicitly confirms.

## Current State

- Upstream repository: `yaojingang/yao-geo-skills`
- Staging fork: `hoho68/yao-geo-skills`
- Local branch: `002-remote-align-yao-geoflow-template`
- Candidate checkpoint: `b6f20a3 align yao-geoflow-template package standardization`
- Prior draft PR: `https://github.com/yaojingang/yao-geo-skills/pull/1`
- Prior draft PR status: closed, not merged

The prior draft PR was used to validate the fork and PR route. A future
upstream review should use a fresh PR after the candidate scope is split or
explicitly approved as one package.

## Recommended Review Strategy

Default recommendation: split the candidate checkpoint into two PRs.

Reason:

- the package contract and Qiaomu example are one product decision
- CI and repository-wide validation hardening are a governance/enforcement
  decision
- splitting keeps the first maintainer review focused on behavior and safety
  boundaries instead of repository policy

## PR 1 Packet: Template Package Contract

### Proposed Title

Standardize `yao-geoflow-template` preview package contract

### Maintainer Summary

This PR standardizes how committed public `yao-geoflow-template` examples should
represent preview-first theme packages. It makes the Qiaomu editorial preview
self-contained, documents the minimum `tokens.json` and `mapping.json` metadata
contract, and separates preview readiness from production activation readiness.

### Why This Change

The current preview was useful but depended on runtime output-style package
metadata. A fresh checkout should be able to inspect the public example without
generating local `outputs/` files. The standard contract also reduces ambiguity
for future theme mappings by making required metadata, preview routes, and safe
activation boundaries explicit.

### Proposed Scope

Include:

- `skills/yao-geoflow-template/SKILL.md`
- `skills/yao-geoflow-template/README.md`
- `skills/yao-geoflow-template/references/theme-package-contract.md`
- `skills/yao-geoflow-template/evals/expected_artifacts.json`
- `skills/yao-geoflow-template/evals/failure_cases.md`
- `skills/yao-geoflow-template/evals/rubric.md`
- `skills/yao-geoflow-template/examples/qiaomu-editorial/README.md`
- `skills/yao-geoflow-template/preview/qiaomu-editorial-20260418/assets/app.js`
- `skills/yao-geoflow-template/preview/qiaomu-editorial-20260418/package/tokens.json`
- `skills/yao-geoflow-template/preview/qiaomu-editorial-20260418/package/mapping.json`
- `docs/skills/yao-geoflow-template.md`
- `docs/skills/yao-geoflow-template.en.md`
- `docs/CHANGELOG.md`
- `docs/CHANGELOG.en.md`
- `.gitignore`
- `scripts/validate_repository.py` with only the UTF-8 registry read fix needed
  for Windows validation
- `registry/skills.json`
- `skills/yao-geoflow-template/manifest.json`

### Non-Goals

- no production template activation
- no live routing, SEO, sitemap, canonical, or structured-data changes
- no backend schema, controller, query, or data-fetching changes
- no private runtime output promotion
- no Spec Kit adoption or repository governance change
- no changes to `yao-geoflow-design`

### Maintainer Review Questions

- Is `preview-only` the right default activation state for committed public
  examples?
- Are `tokens.json` and `mapping.json` the right minimum metadata files?
- Should the Qiaomu editorial example remain the first standardized example?
- Are the documented production activation exclusions clear enough?

### Validation To Report

```powershell
python scripts\validate_repository.py
git diff --check origin/main..HEAD
```

Expected validation note:

```text
Validation passes with an inherited warning: `yao-geoflow-design` has no
`examples/` directory. This warning is not introduced by this package contract
change and is tracked separately.
```

## PR 2 Packet: Validation And CI Enforcement

### Proposed Title

Add smoke validation for `yao-geoflow-template` preview packages

### Maintainer Summary

This PR adds enforcement for the standardized `yao-geoflow-template` package
contract after the contract itself is accepted. It adds a smoke validator for
the Qiaomu package shape, rejects committed runtime output paths, and wires the
package smoke check into repository CI.

### Why This Change

A written contract is useful only when future examples can be checked from a
fresh checkout. The smoke validator catches missing metadata files, mismatched
package ids, invalid preview routes, unsafe activation-state claims, and
references to ignored runtime output paths.

### Proposed Scope

Include:

- `scripts/smoke_yao_geoflow_template_package.py`
- `.github/workflows/repository-checks.yml`
- `docs/publishing-rules.md`
- additional `scripts/validate_repository.py` hardening beyond the UTF-8 read
  fix, such as manifest/registry date checks and tracked `outputs-demo/`
  rejection

### Non-Goals

- no new package contract semantics beyond what PR 1 accepts
- no production activation
- no change to the upstream repository's Spec Kit posture
- no attempt to fix the inherited `yao-geoflow-design` examples warning

### Maintainer Review Questions

- Should package smoke validation be specific to Qiaomu first, or generalized
  immediately for all future template examples?
- Should `outputs-demo/` be globally rejected in tracked files, or only for
  `yao-geoflow-template` examples?
- Should manifest and registry `updated_at` / `last_updated` alignment be
  enforced repository-wide now?

### Validation To Report

```powershell
python scripts\validate_repository.py
python scripts\smoke_yao_geoflow_template_package.py
git diff --check origin/main..HEAD
```

Expected validation note:

```text
`python scripts\validate_repository.py` passes with the inherited
`yao-geoflow-design` examples warning.
`python scripts\smoke_yao_geoflow_template_package.py` passes for
`qiaomu-editorial-20260418`.
```

## Maintainer-Facing Message Draft

```markdown
Hi, I prepared a small standardization path for `yao-geoflow-template`.

The main goal is to make committed public preview packages reviewable from a
fresh checkout: package metadata is committed under the preview example, preview
readiness remains separate from production activation readiness, and ignored
runtime output paths are not required for the public example to render.

I recommend reviewing this in two steps:

1. accept or adjust the `yao-geoflow-template` package contract and the Qiaomu
   example shape
2. separately review the CI and repository-wide validation enforcement

This does not activate any production template, change routing/SEO/backend
behavior, or introduce Spec Kit governance into the upstream repository.
```

## Reopen Criteria

Create a fresh upstream PR only after:

- the user confirms which PR slice to open first
- the branch is rebuilt or split cleanly from latest `origin/main`
- validation is rerun on the exact branch being proposed
- the inherited `yao-geoflow-design` examples warning is disclosed as
  non-blocking
- the PR description includes non-goals and activation safety boundaries
