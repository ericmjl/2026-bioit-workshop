# Part 3 messy notebooks (prep staging)

Duplicated Marimo notebooks for the Part 3 agent refactor demo. They live in the
workshop materials repo so presenters can rehearse and version them; during the
session, copy them into the **live pyds project** from Part 1.

## Copy into live demo project

From the workshop materials repo (adjust paths to your Part 1 project):

```bash
cp examples/messy/*.py /path/to/live-pyds-project/notebooks/
```

Then open the copied notebooks inside the pyds project and point the
architecture improvement skill at `notebooks/`.

## Notebooks

| File | Scenario |
|------|----------|
| `screen_hit_qc.py` | Primary screening hit QC |
| `dose_response_fit.py` | Dose-response curve prep |
| `expression_filter.py` | RNA-seq count filtering |

Each notebook reimplements `load_assay_table`, `remove_outliers`, and
`normalize_to_control` with slightly different logic — realistic duplication for
the refactor demo.

## Open locally (optional)

```bash
marimo edit examples/messy/screen_hit_qc.py
```

Requires `marimo`, `pandas`, and `numpy` in your environment.
