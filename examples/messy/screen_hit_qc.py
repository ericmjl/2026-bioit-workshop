# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo>=0.23.6",
#     "numpy==2.4.6",
#     "pandas==3.0.3",
# ]
# ///
"""Marimo notebook: QC pass on primary screening hits.

Prep artifact — copy into a pyds project's ``notebooks/`` for Part 3 demo.
"""

import marimo

__generated_with = "0.11.0"
app = marimo.App(width="medium")


@app.cell
def __():
    from pathlib import Path

    import marimo as mo
    import numpy as np
    import pandas as pd
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
    # Demo data — replace with a real export during follow-along
    demo = pd.DataFrame(
        {
            "well": [f"A{i}" for i in range(1, 13)],
            "signal": np.random.default_rng(7).normal(1200, 180, 12),
        }
    )
    demo_path = Path("_demo_screen_hits.csv")
    demo.to_csv(demo_path, index=False)

    raw = load_assay_table(demo_path, kind="plate")
    cleaned = remove_outliers(raw["signal"].to_numpy(), method="zscore", z_thresh=3.0)
    control_mean = float(np.nanmean(cleaned[:3]))
    normalized = normalize_to_control(cleaned, control_mean, mode="ratio")

    mo.md(
        f"**QC summary:** {np.isnan(cleaned).sum()} outliers flagged; "
        f"control mean = {control_mean:.1f}"
    )
    return demo_path, normalized, raw


if __name__ == "__main__":
    app.run()
