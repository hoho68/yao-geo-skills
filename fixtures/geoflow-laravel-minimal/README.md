# Minimal GEOFlow Laravel Fixture

This fixture is a non-production workspace for exercising
`yao-geoflow-design` discovery and preview edit-session scripts when a real
GEOFlow application is not available locally.

It intentionally contains only the smallest signal set needed by the current
workflow:

- `artisan`
- `routes/web.php`
- `resources/views/site`
- `resources/views/theme`
- one editable theme: `default`

Do not treat this fixture as a deployable GEOFlow application. It has no
database, controllers, production configuration, admin settings, or live
activation path.

## Safe Use

Use this fixture for:

- validating `discover_themes.py`
- validating `prepare_theme_edit_session.py`
- checking preview-first workflow shape
- documenting what a real GEOFlow workspace must provide

Do not use this fixture for:

- production activation
- backend feature work
- data contract changes
- customer-specific content
