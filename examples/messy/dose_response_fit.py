"""Marimo notebook: fit log-logistic curves to dose-response replicates.

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
    def load_assay_table(csv_path: Path) -> pd.DataFrame:
        """Read dose-response plate reader export."""
        table = pd.read_csv(csv_path)
        table = table.rename(columns={c: c.strip().lower() for c in table.columns})
        table["concentration_um"] = pd.to_numeric(table["concentration_um"])
        table["signal"] = pd.to_numeric(table["signal"])
        return table.dropna(subset=["concentration_um", "signal"])

    return (load_assay_table,)


@app.cell
def __(np):
    def remove_outliers(values: np.ndarray, z_thresh: float = 2.5) -> np.ndarray:
        """Mask replicate outliers using median absolute deviation."""
        med = float(np.median(values))
        mad = float(np.median(np.abs(values - med)))
        if mad == 0:
            return values
        modified_z = 0.6745 * (values - med) / mad
        cleaned = values.copy()
        cleaned[np.abs(modified_z) > z_thresh] = np.nan
        return cleaned

    return (remove_outliers,)


@app.cell
def __(np):
    def normalize_to_control(values: np.ndarray, control_mean: float) -> np.ndarray:
        """Percent activity relative to high control."""
        return 100.0 * values / control_mean

    return (normalize_to_control,)


@app.cell
def __(load_assay_table, mo, normalize_to_control, np, Path, pd, remove_outliers):
    rng = np.random.default_rng(11)
    conc = np.array([0, 0.01, 0.1, 1, 10, 100], dtype=float)
    demo = pd.DataFrame(
        {
            "concentration_um": np.repeat(conc, 3),
            "signal": rng.normal(900 - conc * 4, 40, len(conc) * 3),
        }
    )
    demo_path = Path("_demo_dose_response.csv")
    demo.to_csv(demo_path, index=False)

    table = load_assay_table(demo_path)
    cleaned = remove_outliers(table["signal"].to_numpy())
    control_mean = float(np.nanmean(cleaned[:3]))
    activity = normalize_to_control(cleaned, control_mean)

    mo.md(
        f"**Dose-response prep:** median activity at top dose = "
        f"{np.nanmin(activity):.1f}%"
    )
    return activity, demo_path, table


if __name__ == "__main__":
    app.run()
