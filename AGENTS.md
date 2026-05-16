# AGENTS.md

This repository is the working home for reusable GEO skills, GEOFlow operations, and public-safe delivery templates.

## Core Workflow

- Treat `registry/skills.json` as the source of truth for published skills.
- For new capabilities, write a spec before implementation and keep specs under `docs/superpowers/specs/`.
- For approved specs, write implementation plans under `docs/superpowers/plans/`.
- Keep each skill focused on one repeatable job with clear inputs, outputs, boundaries, and evals.
- Prefer small, reviewable changes. Normal feature work should happen on `codex/<topic>` branches.

## Safety Rules

- Do not commit customer secrets, API keys, backend credentials, `.env` files, private URLs, or unsanitized client data.
- Do not commit runtime outputs from real client work. Use sanitized `examples/` only when an artifact is meant to be public.
- Do not directly modify a customer's production GEOFlow theme. Use preview-first workflows.
- Do not activate production changes without explicit human confirmation and a rollback plan.
- When a workspace has unrelated local changes, leave them alone.

## Skill Package Rules

- Public skills live in `skills/<skill-id>/`.
- Every public skill must include `SKILL.md`, `templates/brief-template.md`, `evals/trigger_cases.json`, and `evals/expected_artifacts.json`.
- Every published public skill needs a human-facing guide at `docs/skills/<skill-id>.md`.
- Any new or renamed public skill must update `registry/skills.json` in the same change set.
- Detailed methods should live in `references/`, reusable deterministic logic in `scripts/`, and public sample artifacts in `examples/`.

## Verification

Run repository validation before pushing:

```powershell
python scripts/validate_repository.py
```

For template or fixture changes, also run the relevant smoke checks from `scripts/`.

## Second Machine Setup

Use `docs/second-machine-setup.md` and `scripts/setup_workspace.ps1` to initialize another computer. The setup script installs project skills into the local Codex skills directory, but local secrets and machine-specific settings must still be configured separately.
