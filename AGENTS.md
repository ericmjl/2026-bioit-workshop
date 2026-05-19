# Agent Preferences For This Repo

## Architecture For Messy Notebook Refactors

- Prefer an assay-operation split over a technical split.
- Shared code should live in modules named by assay operations (for example: `loaders`, `qc`, `normalization`), not generic `io_utils`/`stats_utils`.
- Keep notebook-specific behavior at call sites via explicit parameters (for example `kind=`, `method=`, `mode=`) rather than duplicating helper implementations.

## Notebook Code Style

- Do not introduce wrapper functions around imported helpers when a direct call is sufficient.
- Do not use underscore-prefixed alias imports (for example `from x import y as _y`) to create wrapper indirection.
- Import shared functions directly and call them directly.

## Live Marimo Pairing Workflow

- After refactors that move notebook helper code into shared modules, re-import and re-run affected cells in the live marimo notebook session.
- Use the `marimo-pair` skill workflow for live notebook updates.
