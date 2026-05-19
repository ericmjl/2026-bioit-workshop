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

    return Path, mo, np, pd


@app.cell
def __(Path, pd):
    def load_assay_table(path: Path) -> pd.DataFrame:
        """Load a 384-well plate export from the CDD vault."""
        df = pd.read_csv(path)
        df.columns = [c.strip().lower() for c in df.columns]
        if "well" not in df.columns:
            raise ValueError("expected a well column")
        df["well"] = df["well"].astype(str)
        return df

    return (load_assay_table,)


@app.cell
def __(np):
    def remove_outliers(values: np.ndarray, z_thresh: float = 3.0) -> np.ndarray:
        """Drop wells more than z_thresh standard deviations from the plate mean."""
        mu = float(np.mean(values))
        sigma = float(np.std(values))
        if sigma == 0:
            return values
        z = np.abs((values - mu) / sigma)
        cleaned = values.copy()
        cleaned[z > z_thresh] = np.nan
        return cleaned

    return (remove_outliers,)


@app.cell
def __(np):
    def normalize_to_control(values: np.ndarray, control_mean: float) -> np.ndarray:
        """Express signal relative to DMSO control wells."""
        if control_mean == 0:
            raise ValueError("control mean must be non-zero")
        return values / control_mean

    return (normalize_to_control,)


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

    raw = load_assay_table(demo_path)
    cleaned = remove_outliers(raw["signal"].to_numpy())
    control_mean = float(np.nanmean(cleaned[:3]))
    normalized = normalize_to_control(cleaned, control_mean)

    mo.md(
        f"**QC summary:** {np.isnan(cleaned).sum()} outliers flagged; "
        f"control mean = {control_mean:.1f}"
    )
    return demo_path, normalized, raw


if __name__ == "__main__":
    app.run()
