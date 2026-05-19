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
    from assay_helpers.loaders import load_assay_table
    from assay_helpers.normalization import normalize_to_control
    from assay_helpers.qc import remove_outliers

    return (
        Path,
        load_assay_table,
        mo,
        normalize_to_control,
        np,
        pd,
        remove_outliers,
    )


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

    matrix = load_assay_table(demo_path, kind="expression_matrix")
    library_sizes = matrix.sum(axis=0).to_numpy()
    cleaned_sizes = remove_outliers(
        library_sizes,
        method="log_zscore",
        z_thresh=3.5,
    )
    control_mean = float(np.nanmean(cleaned_sizes))
    scaled = normalize_to_control(
        matrix["sample_treat"].to_numpy(),
        control_mean,
        mode="cpm",
    )

    mo.md(
        f"**Expression filter:** kept {len(genes)} genes; "
        f"control library size = {control_mean:,.0f}"
    )
    return demo_path, matrix, scaled


if __name__ == "__main__":
    app.run()
