# Local Delivery Roadmap

Date: 2026-05-03

This document records the local delivery route for `yao-geo-skills` after the
first remote alignment pass. It is intentionally local-first: the goal is to
keep the work reviewable and recoverable without rushing another upstream PR.

## Current Baseline

- Canonical upstream repository: `yaojingang/yao-geo-skills`
- Personal fork used for backup and staging: `hoho68/yao-geo-skills`
- Current local branch: `002-remote-align-yao-geoflow-template`
- Current candidate commit: `b6f20a3 align yao-geoflow-template package standardization`
- Closed draft PR: `https://github.com/yaojingang/yao-geo-skills/pull/1`
- Local branch is pushed to the fork and tracks
  `fork/002-remote-align-yao-geoflow-template`

The closed draft PR should be treated as a transport test and remote backup
checkpoint, not as a merge request that is ready for upstream review.

## Candidate Change Package

The current candidate package standardizes `yao-geoflow-template` around a
preview-first public package contract.

It contains:

- a self-contained Qiaomu editorial preview package with committed
  `package/tokens.json` and `package/mapping.json`
- explicit separation between preview readiness and production activation
  readiness
- package contract, guide, rubric, and failure-case updates
- a smoke validator for `yao-geoflow-template` package structure and ignored
  runtime output references
- CI wiring for the package smoke validator

It does not attempt to:

- activate any template in a production GEOFlow system
- change private runtime outputs into committed examples
- push directly to upstream `main`
- merge the old local Spec Kit baseline into the latest upstream branch

## Slice 2 Scope Review

Review date: 2026-05-03

The current candidate commit changes 21 files with 882 insertions and 29
deletions. The change is coherent as a local checkpoint, but it is larger than
the safest first upstream review unit.

### File Groups

| Group | Files | Review meaning |
| --- | --- | --- |
| Contract and skill behavior | `skills/yao-geoflow-template/SKILL.md`, `skills/yao-geoflow-template/README.md`, `skills/yao-geoflow-template/references/theme-package-contract.md`, `skills/yao-geoflow-template/evals/expected_artifacts.json`, `skills/yao-geoflow-template/evals/failure_cases.md`, `skills/yao-geoflow-template/evals/rubric.md` | Defines the new preview-first package contract and safety boundary. |
| Qiaomu public example | `skills/yao-geoflow-template/examples/qiaomu-editorial/README.md`, `skills/yao-geoflow-template/preview/qiaomu-editorial-20260418/assets/app.js`, `skills/yao-geoflow-template/preview/qiaomu-editorial-20260418/package/tokens.json`, `skills/yao-geoflow-template/preview/qiaomu-editorial-20260418/package/mapping.json` | Makes the committed preview self-contained and removes dependency on ignored runtime output paths. |
| Human-facing docs and inventory | `docs/skills/yao-geoflow-template.md`, `docs/skills/yao-geoflow-template.en.md`, `docs/CHANGELOG.md`, `docs/CHANGELOG.en.md`, `registry/skills.json`, `skills/yao-geoflow-template/manifest.json` | Keeps public docs and repository inventory aligned with the contract change. |
| CI and package validation | `.github/workflows/repository-checks.yml`, `scripts/smoke_yao_geoflow_template_package.py` | Enforces that the standardized package remains reviewable from a fresh checkout. |
| Repository-wide validation hardening | `.gitignore`, `docs/publishing-rules.md`, `scripts/validate_repository.py` | Adds broader repository safety checks, including `outputs-demo/` handling and manifest/registry date checks. |

### Scope Finding

The contract, public example, package metadata, docs, smoke validator, and CI
step all support one decision: `yao-geoflow-template` public preview packages
must be self-contained, preview-only, and safely reviewable.

The only scope-expansion risk is `scripts/validate_repository.py`. It does more
than support the template package:

- requires `manifest.json` and `agents/interface.yaml` for every skill
- validates manifest `updated_at` against registry `last_updated`
- rejects tracked `outputs/` and `outputs-demo/` paths globally

These checks currently pass, but they are repository-wide governance rules.
That makes them a better separate review topic if the upstream maintainer wants
minimal diffs.

### Decision

Keep `b6f20a3` as the local candidate checkpoint for now. Do not rewrite the
fork branch yet.

Before creating a new upstream PR, split the candidate into two review slices:

1. `yao-geoflow-template` package contract and Qiaomu example
   - include the skill contract, self-contained package metadata, example
     README, guide docs, eval updates, manifest/registry date updates, and
     changelog entries
   - goal: show the maintainer the actual product behavior and safety boundary

2. Validation and CI enforcement
   - include the smoke script, workflow step, `.gitignore`,
     `docs/publishing-rules.md`, and any repository-wide validation hardening
   - goal: make enforcement reviewable after the contract is accepted

If the maintainer explicitly asks for one PR, the current candidate can still
be used as the source package. The default local landing strategy should be
two review slices, because it separates product contract review from repository
governance review.

## Slice 3 Spec Kit Boundary Decision

Decision date: 2026-05-03

The active upstream-aligned branch does not contain `AGENTS.md`, `.agents/`,
`.specify/`, or `specs/`. The older local `main` and
`001-geoflow-template-standardization` branches do contain a complete Spec Kit
baseline and feature spec history, including:

- `AGENTS.md`
- `.agents/skills/speckit-*`
- `.specify/memory/constitution.md`
- `specs/000-project-baseline/`
- `specs/001-geoflow-template-standardization/`

Those files were useful for local brownfield planning, but they were created
before the remote alignment branch was rebuilt from the latest upstream
`origin/main`. They should not be mixed into the current
`yao-geoflow-template` package standardization candidate.

### Decision

Use Spec Kit as a local planning method for this project, but keep Spec Kit
configuration and generated specs out of the current upstream candidate branch.

Default path:

1. Keep using the old local Spec Kit baseline as planning evidence and workflow
   memory.
2. Keep upstream-facing product changes focused on `yao-geoflow-template`
   package behavior and documentation.
3. If the repository owner wants Spec Kit in the public repository, create a
   separate governance PR from a fresh `origin/main` branch.

### What Is Allowed Now

- Use the existing local Spec Kit constitution and specs as reference material
  when planning future slices.
- Continue recording delivery decisions in this local roadmap document.
- Keep fork branches as backup or staging points.
- Discuss Spec Kit adoption with the upstream maintainer after the package
  standardization path is clear.

### What Is Not Allowed In The Current Candidate

- Do not add `.specify/`, `.agents/`, `AGENTS.md`, or `specs/` to
  `002-remote-align-yao-geoflow-template`.
- Do not rerun `specify init` on the upstream-aligned branch without a separate
  adoption decision.
- Do not use `--force` for Spec Kit initialization unless the target branch is a
  dedicated governance branch and the exact overwrite risk has been reviewed.
- Do not bundle Spec Kit adoption with the template contract or CI enforcement
  slices.

### Future Governance PR Shape

If Spec Kit is later proposed upstream, the PR should be separate and small:

- base branch: latest `origin/main`
- purpose: repository governance and contribution workflow only
- include: constitution, baseline spec, context file, and minimal integration
  files required for Codex/Spec Kit workflow
- exclude: `yao-geoflow-template` implementation changes, Qiaomu preview
  metadata, smoke validator changes, and historical feature specs unless the
  maintainer explicitly wants them

That PR should explain why a public skill collection benefits from a
spec-first workflow and how it changes contributor expectations.

## Slice 4 Inherited Warning Strategy

Decision date: 2026-05-03

Current validation still passes with this inherited warning:

```text
WARN: Skill yao-geoflow-design has no examples/ directory
Repository validation passed.
```

The warning is present because `scripts/validate_repository.py` warns when a
skill has no `examples/` directory. `yao-geoflow-design` currently has
`preview/`, `reports/`, `references/`, `scripts/`, `templates/`, and `evals/`,
but no public `examples/` entry point.

### Finding

This warning should not block `yao-geoflow-template` standardization.

Reasons:

- it is inherited from the upstream baseline and is not introduced by the
  current template candidate
- `yao-geoflow-design` is a separate skill with a different job boundary
- creating a proper `examples/` entry would require deciding what sanitized
  design example contract should look like
- reusing the existing preview files without a clear example README would reduce
  the warning but not necessarily improve maintainability

### Decision

Track the warning as a known non-blocking repository quality issue. Do not fix
it inside the current `yao-geoflow-template` package standardization branch.

Create a separate future slice only when the project is ready to define a
sanitized `yao-geoflow-design` public example. That slice should decide whether
the existing `preview/qiaomu-editorial-20260418/` and related reports can be
promoted into:

- `skills/yao-geoflow-design/examples/qiaomu-editorial/README.md`
- a small example inventory that links to committed preview routes
- explicit public-safety notes for any report or preview asset reused by the
  example

### Future Slice Entry Criteria

Start the separate `yao-geoflow-design` example slice only when:

- the template standardization path is no longer competing for review attention
- the example can be sanitized without depending on private GEOFlow runtime
  outputs
- the example README can explain the design workflow, not only link to preview
  HTML
- validation expectations for design examples are clear enough to avoid
  creating a placeholder example

### Current Handling

For current validation summaries, report the warning explicitly as:

> Validation passes with an inherited warning: `yao-geoflow-design` has no
> `examples/` directory. This is tracked as a separate repository quality issue
> and is not a blocker for `yao-geoflow-template` package standardization.

## Slice 5 Maintainer PR Packet

Decision date: 2026-05-03

The maintainer-facing packet is recorded in:

- `docs/maintainer-pr-packet.md`

It prepares future upstream communication without reopening a PR. The packet
contains:

- current fork, branch, candidate commit, and closed draft PR context
- a recommended two-PR review strategy
- PR 1 packet for the `yao-geoflow-template` package contract and Qiaomu example
- PR 2 packet for validation and CI enforcement
- proposed titles, summaries, scope, non-goals, maintainer questions, and
  validation commands
- a short maintainer-facing message draft
- criteria for creating a fresh upstream PR later

Decision:

- Do not reopen the closed draft PR now.
- Do not create a new upstream PR now.
- Use `docs/maintainer-pr-packet.md` as the source material when the project is
  ready to open the first split PR.

## Validation Status

Already validated before the fork push:

- `python scripts\validate_repository.py`
- `python scripts\smoke_yao_geoflow_template_package.py`
- `git diff --check origin/main..HEAD`
- runtime output reference scan for
  `skills\yao-geoflow-template\preview\qiaomu-editorial-20260418`

Known residual issue:

- `python scripts\validate_repository.py` passes with an existing warning that
  `yao-geoflow-design` has no `examples/` directory. This warning is inherited
  from the upstream baseline and is not caused by the template standardization
  candidate.

## Delivery Principles

- Keep upstream `main` as the public stability boundary.
- Keep the fork branch as a recoverable staging area.
- Reopen a PR only after the candidate change is small, explainable, and useful
  to the upstream maintainer.
- Keep Spec Kit governance separate from the upstream alignment branch until
  the repository owner explicitly agrees to adopt it.
- Prefer one narrow PR per decision boundary: package contract, repository
  governance, validation hardening, and individual skill maturity work should
  not be bundled unless they are tightly coupled.

## Readiness Gates

| Gate | Status | Meaning |
| --- | --- | --- |
| Local branch clean | Passed | The candidate branch has no uncommitted implementation changes. |
| Fork backup exists | Passed | The branch has been pushed to `hoho68/yao-geo-skills`. |
| Draft PR closed | Passed | The upstream repository is not being asked to merge prematurely. |
| Candidate scope review | Completed | Keep `b6f20a3` as a local checkpoint, but split into two review slices before reopening an upstream PR. |
| Spec Kit adoption decision | Completed | Use Spec Kit locally for planning now; propose upstream adoption only through a separate future governance PR. |
| Inherited warning strategy | Completed | Track the `yao-geoflow-design` examples warning as a non-blocking known issue and handle it in a separate future slice. |
| Upstream maintainer context | Completed | Prepared `docs/maintainer-pr-packet.md`; do not reopen or create an upstream PR until a first slice is chosen. |

## MVP-First Next Slices

1. Document the local delivery route.
   - Outcome: this file exists and records the current branch, candidate commit,
     closed PR, validation status, and gates.

2. Review the candidate package size.
   - Outcome: decide whether `b6f20a3` should stay as one PR or be split into
     smaller reviewable commits.

3. Decide the Spec Kit boundary.
   - Outcome: choose one path:
     - keep Spec Kit local-only for planning
     - introduce Spec Kit in a separate governance PR
     - postpone Spec Kit adoption until after the template package lands
   - Decision: keep Spec Kit local-only for current work; consider a separate
     governance PR only after the upstream package path is clear.

4. Resolve or track inherited repository warnings.
   - Outcome: either add a sanitized `yao-geoflow-design` example in a separate
     slice or create a known-issue note so it does not block this package.
   - Decision: track it as a known non-blocking issue; do not create the example
     in the current template standardization branch.

5. Prepare the maintainer-facing PR packet.
   - Outcome: a short PR description, validation summary, and non-goals section
     are ready before reopening or creating a new PR.
   - Decision: packet created at `docs/maintainer-pr-packet.md`; upstream PR
     remains closed/not reopened.

## Reopen PR Criteria

Do not reopen or recreate an upstream PR until all of the following are true:

- the candidate scope has been reviewed locally
- the user confirms the branch is intended for upstream review
- the validation commands still pass on the latest branch state
- the PR description explains the safety boundary and non-goals
- no unrelated local or historical Spec Kit changes are mixed into the PR

When these criteria are met, prefer creating a fresh PR from the fork branch
instead of reopening the closed transport-test draft PR.

## Route Document Closure

Closure date: 2026-05-03

The local route-planning phase is complete for the current checkpoint.

Completed local decisions:

- keep `b6f20a3` as the current candidate checkpoint
- do not reopen the closed transport-test draft PR
- split future upstream review into package-contract and validation/CI slices
- keep Spec Kit local-only for current work
- track the `yao-geoflow-design` examples warning as a separate known issue
- use `docs/maintainer-pr-packet.md` as the source material for any future
  maintainer-facing message or PR description

Frozen actions until an explicit next decision:

- no upstream PR creation
- no force push
- no Spec Kit initialization on the upstream-aligned branch
- no `yao-geoflow-design` example work inside the template standardization
  branch
- no rewrite of `b6f20a3` until a specific split branch is chosen
- no commit of these local planning docs onto the current candidate branch
  unless a dedicated planning-doc branch or commit strategy is chosen

Safe next entry points:

1. Create a dedicated branch for PR 1: package contract and Qiaomu example.
2. Create a dedicated branch for PR 2: validation and CI enforcement.
3. Create a separate governance branch for Spec Kit adoption.
4. Create a separate quality branch for the `yao-geoflow-design` example
   warning.
5. Keep all planning docs local and continue discussion before changing git
   history.

Split-prep adjustment:

- `.gitignore` should travel with PR 1, because the package contract already
  names `outputs-demo/` as a runtime output path that public examples must not
  depend on.
- A minimal `scripts/validate_repository.py` UTF-8 registry read fix should
  travel with PR 1 so Windows validation can run after `registry/skills.json`
  is touched.
- Keep the rest of `scripts/validate_repository.py` hardening, the package
  smoke script, the GitHub Actions step, and publishing-rule enforcement in
  PR 2.

## Split Result Review

Review date: 2026-05-03

The split has been verified against the original complete checkpoint.

| Baseline | Commit | Role |
| --- | --- | --- |
| `origin/main` | `8774861` | latest upstream baseline used for split branches |
| PR 1 branch | `4c08b33` | `yao-geoflow-template` package contract and Qiaomu example |
| PR 2 branch | `8471713` | validation and CI enforcement stacked on PR 1 |
| old complete checkpoint | `b6f20a3` | original single-commit candidate before splitting |

Diff review:

| Comparison | Result |
| --- | --- |
| `origin/main..003-yao-geoflow-template-contract` | 18 files, 592 insertions, 28 deletions |
| `003-yao-geoflow-template-contract..004-yao-geoflow-template-validation` | 4 files, 290 insertions, 1 deletion |
| `origin/main..004-yao-geoflow-template-validation` | 21 files, 882 insertions, 29 deletions |
| `origin/main..002-remote-align-yao-geoflow-template` | 21 files, 882 insertions, 29 deletions |
| `002-remote-align-yao-geoflow-template..004-yao-geoflow-template-validation` | no diff |

Tree verification:

- `002-remote-align-yao-geoflow-template^{tree}`:
  `9a08fbb4ce6cd5f2e2f9c72b9785ab057202e297`
- `004-yao-geoflow-template-validation^{tree}`:
  `9a08fbb4ce6cd5f2e2f9c72b9785ab057202e297`

Conclusion:

- PR 1 plus PR 2 reconstructs the old complete candidate exactly.
- No implementation content was lost during the split.
- PR 2 remains stacked on PR 1 and should be reviewed only after PR 1 is
  accepted or otherwise rebased.
- Local planning docs remain outside both PR branches.

Final split-review validation:

```powershell
python scripts\validate_repository.py
python scripts\smoke_yao_geoflow_template_package.py
python -m py_compile scripts\validate_repository.py scripts\smoke_yao_geoflow_template_package.py
git diff --check origin/main..004-yao-geoflow-template-validation
git diff --check 003-yao-geoflow-template-contract..004-yao-geoflow-template-validation
```

Validation passes with the inherited warning that `yao-geoflow-design` has no
`examples/` directory.

## PR 1 Opening Decision

Decision date: 2026-05-03

Current facts:

- PR 1 branch: `003-yao-geoflow-template-contract`
- PR 1 commit: `4c08b33 standardize yao-geoflow-template package contract`
- PR 1 remote backup:
  `fork/003-yao-geoflow-template-contract`
- Upstream base: `origin/main` at `8774861`
- Old transport-test PR: `https://github.com/yaojingang/yao-geo-skills/pull/1`
  is closed and not merged.

Readiness:

- PR 1 is narrow enough for upstream review.
- PR 1 has a clean fork branch backup.
- PR 1 does not include the CI enforcement slice, Spec Kit files, local planning
  docs, or `yao-geoflow-design` example work.
- The inherited `yao-geoflow-design` warning must be disclosed, but it should
  not block the PR 1 decision.

Recommendation:

- It is safe to open PR 1 as a draft upstream PR when the user wants maintainer
  visibility.
- Do not open it automatically from this decision stage.
- Prefer a fresh PR from
  `hoho68:003-yao-geoflow-template-contract` to
  `yaojingang:main`; do not reopen the old transport-test PR.

Draft PR title:

```text
Standardize yao-geoflow-template preview package contract
```

Draft PR body source:

- use the PR 1 section in `docs/maintainer-pr-packet.md`
- include the non-goals and inherited-warning note
- explicitly say that validation/CI enforcement is prepared as a separate
  stacked follow-up branch

Decision status:

- PR 1 is eligible to open.
- No upstream PR has been created from this decision stage.
- Opening PR 1 requires an explicit next instruction from the user.

## Useful Local Commands

```powershell
git status -sb
git log --oneline --decorate -5
python scripts\validate_repository.py
python scripts\smoke_yao_geoflow_template_package.py
git diff --check origin/main..HEAD
git push -u fork 002-remote-align-yao-geoflow-template
```
