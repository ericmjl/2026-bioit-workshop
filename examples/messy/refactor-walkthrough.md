# Refactor Walkthrough: From Duplicated Notebooks to Assay Helpers

This document captures the agent-assisted refactor session that consolidated
duplicated logic across the three Part 3 messy notebooks into shared
`assay_helpers` modules.

## Starting point

Three Marimo notebooks each reimplemented the same three helper names with
**different behavior**:

| Notebook | `load_assay_table` | `remove_outliers` | `normalize_to_control` |
|----------|-------------------|-------------------|------------------------|
| `screen_hit_qc.py` | Plate CSV, requires `well` | Raw z-score (3.0) | Ratio (divide by control) |
| `dose_response_fit.py` | Dose-response CSV, numeric coercion | MAD (2.5) | Percent activity (×100) |
| `expression_filter.py` | Gene × sample matrix | Log z-score (3.5) | CPM-style (×1e6) |

All three followed the same pipeline shape:

1. Generate demo CSV
2. Load via `load_assay_table`
3. Clean via `remove_outliers`
4. Normalize via `normalize_to_control` against a control mean
5. Print a markdown summary

The duplication was not just copy-paste boilerplate — **same function names,
different semantics**. That is the realistic mess the Part 3 demo is meant to
surface.

## Architecture review: two candidate splits

### Candidate A — technical split (rejected as end state)

```
common/io_utils.py      # read CSV, strip columns, coerce types
common/stats_utils.py   # outlier masking, normalization
```

**Pros:** Small, obvious extraction.

**Cons:** Shallow seams. Callers still need to know `kind`, `method`, and
`mode`; a `stats_utils` junk drawer is easy to grow. The split follows file I/O
vs numerics, not assay concepts.

### Candidate B — assay-operation split (chosen)

```
assay_helpers/
  loaders.py        # load_assay_table(path, *, kind=...)
  qc.py             # remove_outliers(values, *, method=..., z_thresh=...)
  normalization.py  # normalize_to_control(values, control_mean, *, mode=...)
```

**Pros:** Deep modules at real seams. One implementation pays back across all
three notebooks. Tests map 1:1 to the interface. Aligns with
`examples/clean/assay_helpers/`.

**Cons:** Slightly more files than two utility modules — worth it for clarity
and maintainability.

## What we built

### Shared modules

- **`loaders.py`** — `load_assay_table(path, *, kind)` with
  `kind="plate" | "dose_response" | "expression_matrix"`.
- **`qc.py`** — `remove_outliers(values, *, method, z_thresh)` with
  `method="zscore" | "mad" | "log_zscore"`.
- **`normalization.py`** — `normalize_to_control(values, control_mean, *,
  mode)` with `mode="ratio" | "percent" | "cpm"`.

### Notebook adapters (explicit parameters at call sites)

Each notebook imports the shared functions directly and pins domain behavior
via keyword arguments — no wrapper functions, no underscore-prefixed alias
imports.

**Screen hit QC:**

```python
raw = load_assay_table(demo_path, kind="plate")
cleaned = remove_outliers(raw["signal"].to_numpy(), method="zscore", z_thresh=3.0)
normalized = normalize_to_control(cleaned, control_mean, mode="ratio")
```

**Dose-response:**

```python
table = load_assay_table(demo_path, kind="dose_response")
cleaned = remove_outliers(table["signal"].to_numpy(), method="mad", z_thresh=2.5)
activity = normalize_to_control(cleaned, control_mean, mode="percent")
```

**Expression filter:**

```python
matrix = load_assay_table(demo_path, kind="expression_matrix")
cleaned_sizes = remove_outliers(library_sizes, method="log_zscore", z_thresh=3.5)
scaled = normalize_to_control(treat_counts, control_mean, mode="cpm")
```

### Tests

`examples/messy/tests/test_assay_helpers.py` covers loader validation, each
outlier method, and all three normalization modes.

Run:

```bash
pixi run pytest examples/messy/tests/test_assay_helpers.py
```

## Live Marimo pairing

After the file refactor, the dose-response notebook was updated in a **running**
Marimo session (port 2720) using the `marimo-pair` skill:

1. Discover the server (`discover-servers.sh`).
2. Edit cells in-kernel via `marimo._code_mode` — **not** by writing the `.py`
   file while the session is open (the kernel overwrites disk edits on save).
3. Replace wrapper cells with direct imports.
4. Re-run downstream cells so the UI reflects the new imports.

## Style rules we settled on

These preferences are recorded in the repo root [`AGENTS.md`](../../AGENTS.md):

- Prefer assay-operation module names (`loaders`, `qc`, `normalization`) over
  generic `io_utils` / `stats_utils`.
- Keep notebook-specific behavior at call sites via `kind=`, `method=`, `mode=`.
- **Do not** add wrapper functions around imported helpers.
- **Do not** use `from x import y as _y` indirection.
- After moving code into shared modules, re-import and re-run affected cells in
  any live Marimo session.

### Anti-pattern (removed)

```python
from assay_helpers.normalization import normalize_to_control as _normalize_to_control


def normalize_to_control(values, control_mean):
    return _normalize_to_control(values, control_mean, mode="percent")
```

### Preferred pattern

```python
from assay_helpers.normalization import normalize_to_control

activity = normalize_to_control(cleaned, control_mean, mode="percent")
```

## File map after refactor

```
examples/messy/
├── assay_helpers/
│   ├── __init__.py
│   ├── loaders.py
│   ├── qc.py
│   └── normalization.py
├── tests/
│   └── test_assay_helpers.py
├── dose_response_fit.py      # imports assay_helpers; direct calls
├── expression_filter.py
├── screen_hit_qc.py
├── README.md
└── REFACTOR-WALKTHROUGH.md   # this file
```

## Related clean fallback

The same assay-operation layout already exists under
`examples/clean/assay_helpers/` as the polished fallback if a live demo runs
slow. The messy tree now mirrors that structure while keeping the workshop
narrative intact.

## Suggested next deepening steps

Not done in this session, but natural follow-ups:

- Extract repeated `control_mean = float(np.nanmean(cleaned[:3]))` into a
  small control-reference helper.
- Add golden CSV fixtures per notebook kind for loader tests.
- Wire `assay_helpers` into the pyds project package when copied for Part 3.
