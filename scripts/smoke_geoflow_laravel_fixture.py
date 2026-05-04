#!/usr/bin/env python3

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
FIXTURE_ROOT = ROOT / "fixtures" / "geoflow-laravel-minimal"
DISCOVER_THEMES = ROOT / "skills" / "yao-geoflow-design" / "scripts" / "discover_themes.py"
THEMES_ROOT = FIXTURE_ROOT / "resources" / "views" / "theme"
DEFAULT_THEME = THEMES_ROOT / "default"
PREVIEW_THEME = THEMES_ROOT / "qiaomu-preview"

REQUIRED_FIXTURE_SIGNALS = [
    FIXTURE_ROOT / "artisan",
    FIXTURE_ROOT / "routes" / "web.php",
    FIXTURE_ROOT / "resources" / "views" / "site",
    THEMES_ROOT,
    FIXTURE_ROOT / "app" / "Support" / "Site" / "SiteThemeViewResolver.php",
]

EXPECTED_PAGE_TEMPLATES = [
    "home.blade.php",
    "category.blade.php",
    "article.blade.php",
    "archive.blade.php",
]

EXPECTED_EDITABLE_FILES = {
    "home.blade.php",
    "category.blade.php",
    "article.blade.php",
    "archive.blade.php",
    "partials/header.blade.php",
    "partials/footer.blade.php",
    "assets/theme.css",
    "manifest.json",
    "tokens.json",
    "mapping.json",
}


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    sys.exit(1)


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        fail(f"Missing JSON file: {rel(path)}")
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(f"{rel(path)} is invalid JSON: {exc}")
    if not isinstance(data, dict):
        fail(f"{rel(path)} must contain a JSON object")
    return data


def require_paths(paths: list[Path]) -> None:
    missing = [rel(path) for path in paths if not path.exists()]
    if missing:
        fail(f"Missing fixture files: {', '.join(missing)}")


def run_discovery() -> dict[str, Any]:
    result = subprocess.run(
        [sys.executable, str(DISCOVER_THEMES), str(FIXTURE_ROOT)],
        cwd=ROOT,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    if result.returncode != 0:
        fail(f"discover_themes.py failed: {result.stderr.strip() or result.stdout.strip()}")
    try:
        report = json.loads(result.stdout)
    except json.JSONDecodeError as exc:
        fail(f"discover_themes.py did not return JSON: {exc}")
    if not isinstance(report, dict):
        fail("discover_themes.py must return a JSON object")
    return report


def theme_by_id(report: dict[str, Any]) -> dict[str, dict[str, Any]]:
    themes = report.get("themes")
    if not isinstance(themes, list):
        fail("Discovery report must include a themes list")
    by_id: dict[str, dict[str, Any]] = {}
    for theme in themes:
        if not isinstance(theme, dict) or not isinstance(theme.get("id"), str):
            fail("Every discovered theme must be an object with a string id")
        by_id[theme["id"]] = theme
    return by_id


def validate_discovery(report: dict[str, Any]) -> dict[str, dict[str, Any]]:
    if report.get("framework") != "laravel":
        fail("Fixture discovery must report framework=laravel")
    if report.get("theme_system_detected") is not True:
        fail("Fixture discovery must report theme_system_detected=true")

    signals = report.get("theme_system_signals")
    if not isinstance(signals, dict):
        fail("Fixture discovery must include theme_system_signals")
    missing_signals = [name for name, value in signals.items() if value is not True]
    if missing_signals:
        fail(f"Fixture discovery signals are not all true: {', '.join(sorted(missing_signals))}")

    themes = theme_by_id(report)
    expected_ids = {"default", "qiaomu-preview"}
    actual_ids = set(themes)
    if actual_ids != expected_ids:
        fail(f"Fixture must expose exactly {sorted(expected_ids)}, got {sorted(actual_ids)}")
    if report.get("theme_count") != len(expected_ids):
        fail("Fixture discovery theme_count must match the expected fixture themes")

    default = themes["default"]
    if default.get("is_preview_session") is not False:
        fail("default theme must not be marked as a preview session")
    if default.get("session_state") != "baseline":
        fail("default theme session_state must remain baseline")
    if default.get("mode") != "theme":
        fail("default theme mode must remain theme")

    preview = themes["qiaomu-preview"]
    if preview.get("is_preview_session") is not True:
        fail("qiaomu-preview must be marked as a preview session")
    if preview.get("session_state") != "preview":
        fail("qiaomu-preview session_state must remain preview")
    if preview.get("mode") != "edit_theme":
        fail("qiaomu-preview mode must remain edit_theme")
    if preview.get("base_theme_id") != "default":
        fail("qiaomu-preview base_theme_id must remain default")

    editable = set(preview.get("editable_files", []))
    expected_preview_files = EXPECTED_EDITABLE_FILES | {
        "edit-session.json",
        "change-plan.md",
        "preview-notes.md",
    }
    missing_editable = sorted(expected_preview_files - editable)
    if missing_editable:
        fail(f"qiaomu-preview editable_files is missing: {', '.join(missing_editable)}")

    return themes


def validate_default_isolation() -> None:
    for path in DEFAULT_THEME.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in {".php", ".json", ".css", ".md"}:
            continue
        text = path.read_text(encoding="utf-8")
        forbidden = [marker for marker in ("qiaomu-preview", "Qiaomu Preview") if marker in text]
        if forbidden:
            fail(f"{rel(path)} contains preview-only marker(s): {', '.join(forbidden)}")

    default_manifest = load_json(DEFAULT_THEME / "manifest.json")
    if default_manifest.get("session_state") != "baseline":
        fail("default manifest session_state must remain baseline")


def validate_preview_isolation() -> None:
    for template in EXPECTED_PAGE_TEMPLATES:
        path = PREVIEW_THEME / template
        text = path.read_text(encoding="utf-8")
        if "theme.default.partials" in text:
            fail(f"{rel(path)} still references default partials")
        for include in (
            "theme.qiaomu-preview.partials.header",
            "theme.qiaomu-preview.partials.footer",
        ):
            if include not in text:
                fail(f"{rel(path)} is missing isolated preview include: {include}")

    for path in PREVIEW_THEME.rglob("*.blade.php"):
        text = path.read_text(encoding="utf-8")
        if "theme.default" in text:
            fail(f"{rel(path)} still references theme.default")


def validate_preview_metadata() -> None:
    manifest = load_json(PREVIEW_THEME / "manifest.json")
    if manifest.get("session_state") != "preview":
        fail("qiaomu-preview manifest session_state must remain preview")
    if manifest.get("base_theme_id") != "default":
        fail("qiaomu-preview manifest base_theme_id must remain default")
    if manifest.get("target_theme_id") != "default":
        fail("qiaomu-preview manifest target_theme_id must remain default")

    edit_session = load_json(PREVIEW_THEME / "edit-session.json")
    if edit_session.get("session_state") != "preview":
        fail("qiaomu-preview edit-session session_state must remain preview")
    if edit_session.get("base_theme_id") != "default":
        fail("qiaomu-preview edit-session base_theme_id must remain default")
    if edit_session.get("preview_theme_id") != "qiaomu-preview":
        fail("qiaomu-preview edit-session preview_theme_id must remain qiaomu-preview")

    mapping = load_json(PREVIEW_THEME / "mapping.json")
    if mapping.get("activation_status") != "preview-only":
        fail("qiaomu-preview mapping activation_status must remain preview-only")
    boundaries = " ".join(str(item).lower() for item in mapping.get("safe_boundaries", []))
    for term in ("qiaomu-preview", "default", "activation"):
        if term not in boundaries:
            fail(f"qiaomu-preview mapping safe_boundaries must mention {term}")

    tokens = load_json(PREVIEW_THEME / "tokens.json")
    if tokens.get("id") != "qiaomu-preview-fixture":
        fail("qiaomu-preview tokens id must remain qiaomu-preview-fixture")
    style_direction = tokens.get("style_direction")
    if not isinstance(style_direction, list) or "preview-only" not in style_direction:
        fail("qiaomu-preview tokens style_direction must include preview-only")

    change_plan = (PREVIEW_THEME / "change-plan.md").read_text(encoding="utf-8")
    preview_notes = (PREVIEW_THEME / "preview-notes.md").read_text(encoding="utf-8")
    for required in ("qiaomu-preview", "production activation"):
        if required not in change_plan and required not in preview_notes:
            fail(f"Preview documentation must mention {required!r}")


def validate_no_fixture_backups() -> None:
    backups = sorted(FIXTURE_ROOT.rglob(".theme-backups"))
    if backups:
        fail(f"Fixture must not contain theme backups: {', '.join(rel(path) for path in backups)}")


def main() -> None:
    require_paths(REQUIRED_FIXTURE_SIGNALS)
    require_paths([DEFAULT_THEME, PREVIEW_THEME])
    require_paths([PREVIEW_THEME / path for path in EXPECTED_PAGE_TEMPLATES])

    report = run_discovery()
    validate_discovery(report)
    validate_default_isolation()
    validate_preview_isolation()
    validate_preview_metadata()
    validate_no_fixture_backups()
    print("GEOFlow Laravel fixture smoke test passed.")


if __name__ == "__main__":
    main()
