"""Marimo notebook: filter RNA-seq counts before downstream DE testing.

Prep artifact — copy into a pyds project's ``notebooks/`` for Part 3 demo.
"""

import marimo

__generated_with = "0.11.0"
app = marimo.App(width="medium")


@app.cell
def __():
    import marimo as mo
    import pandas as pd
    import numpy as np
    from pathlib import Path

    return Path, mo, np, pd


@app.cell
def __(Path, pd):
    def load_assay_table(file_path: Path) -> pd.DataFrame:
        """Load a gene x sample count matrix exported from the LIMS."""
        counts = pd.read_csv(file_path, index_col=0)
        counts.index = counts.index.astype(str)
        counts.columns = [c.strip() for c in counts.columns]
        return counts

    return (load_assay_table,)


@app.cell
def __(np):
    def remove_outliers(values: np.ndarray, z_thresh: float = 3.5) -> np.ndarray:
        """Flag sample-level library size outliers on log scale."""
        log_vals = np.log1p(values)
        mu = float(np.mean(log_vals))
        sigma = float(np.std(log_vals))
        if sigma == 0:
            return values
        z = np.abs((log_vals - mu) / sigma)
        cleaned = values.copy()
        cleaned[z > z_thresh] = np.nan
        return cleaned

    return (remove_outliers,)


@app.cell
def __(np):
    def normalize_to_control(values: np.ndarray, control_mean: float) -> np.ndarray:
        """CPM-style scaling against housekeeping control column mean."""
        return (values / control_mean) * 1_000_000.0

    return (normalize_to_control,)


@app.cell
def __(load_assay_table, mo, normalize_to_control, np, Path, pd, remove_outliers):
    rng = np.random.default_rng(3)
    genes = [f"GENE{i:04d}" for i in range(1, 51)]
    demo = pd.DataFrame(
        {
            "sample_ctrl": rng.integers(800, 1200, len(genes)),
            "sample_treat": rng.integers(600, 1400, len(genes)),
        },
        index=genes,
    )
    demo_path = Path("_demo_expression.csv")
    demo.to_csv(demo_path)

    matrix = load_assay_table(demo_path)
    library_sizes = matrix.sum(axis=0).to_numpy()
    cleaned_sizes = remove_outliers(library_sizes)
    control_mean = float(np.nanmean(cleaned_sizes))
    scaled = normalize_to_control(matrix["sample_treat"].to_numpy(), control_mean)

    mo.md(
        f"**Expression filter:** kept {len(genes)} genes; "
        f"control library size = {control_mean:,.0f}"
    )
    return demo_path, matrix, scaled


if __name__ == "__main__":
    app.run()
