## Enfield — AI contributor quick instructions

This file gives essential, repository-specific guidance to help an AI coding agent be immediately productive.

1) Project purpose
- Small Python library for player/team entities, match management and a custom rating algorithm.
- Core packages: `enfield/base_entities`, `enfield/match`, `enfield/rating`, `enfield/settings`, `enfield/messages`.

2) Quick start (what to run)
- Python requirement: >= 3.13 (declared in `pyproject.toml`).
- Dependencies are declared in `pyproject.toml`. README mentions the `uv` dependency manager; if `uv` is not available, install in editable mode:
  - python -m pip install -e .
- Minimal smoke test used in repo: run `python match_test.py` from the project root — it demonstrates basic `BaseMatch` usage.

3) High-level architecture and responsibilities
- `enfield/base_entities/*` — entity models (players, teams). Uses Pydantic models and Extra Types (country, timezone).
- `enfield/match/*` — match model and basic match logic (scoring, end_match, player management).
- `enfield/rating/*` — rating calculation logic. Uses NumPy and the shared `settings` object for weighting/scaling.
- `enfield/settings/*` — pydantic-settings based configuration; a single `settings` instance is created in `enfield/settings/__init__.py` and imported across modules.
- `enfield/messages/*` — tiny PR-style success/error helpers used across code (e.g. `GenericSuccess`, `GenericError`).

4) Common code patterns to follow (project-specific)
- Pydantic-first: most domain objects are `pydantic.BaseModel` and rely on `Annotated[...]`, `Strict*` types and `Field()`.
  - Fields frequently use `alias=` (for example `BaseEntity.entity_name` has alias `name`) — read fields using their model attribute names, and accept aliases when parsing input.
- Settings are centralized: modify default behavior by changing `enfield/settings/*.py` (e.g. `rating_settings.py` contains `rating_weighting` / `rating_scaling_multiplier`). Import the package-level `settings` when needed.
- Use strict typing: many models use `StrictInt`/`StrictFloat`. Preserve these types in new API surfaces unless there is a clear reason to relax them.
- Pattern matching: code uses modern `match/case` constructs — keep compatibility with declared Python version.

5) Notable entrypoints & examples (explicit references)
- Package-level exports: `enfield/__init__.py` exposes `BasePlayer`, `BaseMatch`, `BaseRating`, and `UserSettings` (alias for settings). Useful for quick imports.
- Example test (root `match_test.py`): initializes two `BaseMatch` instances and calls `score()` — use it as a canonical minimal example of how the API is used.
- `BaseMatch.score(p1=..., p2=..., override=False)` updates `match_score`; `end_match()` sets `match_winner`, `match_draw` and `match_complete` flags.
- `BaseEntity` uses `Field(alias=...)` extensively — when generating serializers or tests, prefer passing alias names to mimic user input.

6) Integration points & external libs
- pydantic (v2), pydantic-settings, pydantic-extra-types (country, timezone), numpy. See `pyproject.toml` for pinned dependencies.
- Settings object is imported and used directly (e.g. `UserSettings.rating_weighting` in rating code) — changes to settings immediately affect runtime behavior.

7) Known small pitfalls to watch for (discovered by reading code)
- `BaseMatch._validate_player_slot` has a logical bug in the slot check (uses `slot_value == (1 or 2)` which does not test both values). When authoring tests or fixes, add unit tests to cover player slot validation before changing behavior.
- `enfield/rating/base_rating.py` contains in-source notes and an informal algorithm; if changing rating logic, preserve current defaults in `enfield/settings/rating_settings.py` and add tests that mirror expected numeric behaviour.

8) How to extend or change behavior safely
- To change defaults: update the `RatingSettings`/`PlayerSettings`/`EntitySettings` classes under `enfield/settings` and the `settings = Settings(...)` initializer in `enfield/settings/__init__.py`.
- To add new fields to models, follow the existing pattern: `Annotated[...]` with `Strict*` types and `Field(alias=...)` where appropriate.
- For any change touching runtime behavior, add a small test (following `match_test.py` style) and run it from the repository root.

9) When merging or replacing this file
- If a repository-level `.github/copilot-instructions.md` already exists, merge by preserving any project-specific examples and the Quick start section. Replace generic or outdated references (e.g., Python versions) with values from `pyproject.toml`.

If anything here is unclear or you'd like me to include more examples (e.g., unit-test templates, a suggested patch to fix the `slot` bug, or an automated check command), tell me which area to expand. 
