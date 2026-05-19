# Part 3 clean fallback

Pre-built refactor of the duplicated helpers in [`../messy/`](../messy/).
Generate during prep by running Matt Pocock's
[improve-codebase-architecture](https://github.com/mattpocock/skills/tree/main/skills/engineering/improve-codebase-architecture)
skill against the messy notebooks — or maintain this tree as the canonical
fallback if the live demo is slow.

## Layout

| Path | Role |
|------|------|
| `assay_helpers/loaders.py` | Unified `load_assay_table` with kind-specific parsing |
| `assay_helpers/qc.py` | Unified `remove_outliers` (z-score, MAD, log z-score) |
| `assay_helpers/normalization.py` | Unified `normalize_to_control` (ratio, percent, CPM) |
| `assay_helpers/cli.py` | Typer CLI stub |
| `tests/` | Smoke tests on core logic |

## Try it

```bash
cd examples/clean
pip install -e .
pip install pytest
pytest
assay-qc version
```

## In-room use

If the live agent refactor fails or runs long, open this directory and narrate:
"This is what the architecture skill proposes — shared module, tests, small CLI."
