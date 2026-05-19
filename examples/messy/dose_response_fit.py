# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "marimo>=0.23.6",
#     "numpy==2.4.6",
#     "pandas==3.0.3",
#     "plotly==6.7.0",
# ]
# ///
"""Marimo notebook: fit log-logistic curves to dose-response replicates.

Prep artifact — copy into a pyds project's ``notebooks/`` for Part 3 demo.
"""

import marimo

__generated_with = "0.23.6"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Dose-Response Preprocessing Walkthrough

    This notebook is organized as a small pipeline.

    You should expect to see:
    - setup imports first,
    - then focused helper functions for loading, cleaning, and normalization,
    - and finally a demo cell that runs the whole flow and reports a summary metric.
    """)
    return


@app.cell
def _():
    import marimo as mo
    import pandas as pd
    import numpy as np
    from pathlib import Path

    return Path, mo, np, pd


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Step 1: Environment and Core Dependencies

    This section only defines imports and shared types.

    What to expect next: a data-loading helper that standardizes assay table columns and ensures numeric concentration/signal fields.
    """)
    return


@app.cell
def _():
    from assay_helpers.loaders import load_assay_table

    return (load_assay_table,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Step 2: Load and Standardize Assay Data

    The next code cell defines a loader function that:
    - reads a CSV export,
    - normalizes column names,
    - coerces key columns to numeric values,
    - and drops unusable rows.

    What to expect after that: an outlier-filtering helper for replicate cleanup.
    """)
    return


@app.cell
def _():
    from assay_helpers.qc import remove_outliers

    return (remove_outliers,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Step 3: Remove Replicate Outliers

    The upcoming function uses a median-absolute-deviation (MAD) rule to mark extreme replicate values as missing (`NaN`).

    What to expect next: a normalization step that converts cleaned signal to percent activity relative to control.
    """)
    return


@app.cell
def _():
    from assay_helpers.normalization import normalize_to_control

    return (normalize_to_control,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Step 4: Normalize to Control and Run End-to-End Demo

    The normalization helper expresses signal as percent activity versus the control mean.

    The final code cell then creates a synthetic dataset, runs the full preprocessing pipeline, and displays a short markdown summary statistic.
    """)
    return


@app.cell
def _(
    Path,
    load_assay_table,
    mo,
    normalize_to_control,
    np,
    pd,
    remove_outliers,
):
    rng = np.random.default_rng(11)
    conc = np.array([0, 0.01, 0.1, 1, 10, 100], dtype=float)

    demo = pd.DataFrame(
        {
            "concentration_um": np.repeat(conc, 3),
            "replicate_id": np.tile(np.arange(1, 4), conc.size),
        }
    )
    demo["signal"] = rng.normal(np.repeat(900 - conc * 4, 3), 40)
    demo["replicate_label"] = demo["replicate_id"].map(lambda r: f"Replicate {r}")

    demo_path = Path("_demo_dose_response.csv")
    demo.to_csv(demo_path, index=False)

    table = load_assay_table(demo_path, kind="dose_response")
    cleaned = remove_outliers(
        table["signal"].to_numpy(), method="mad", z_thresh=2.5
    )
    control_mean = float(np.nanmean(cleaned[:3]))
    activity = normalize_to_control(cleaned, control_mean, mode="percent")

    demo_for_plot = table.copy()
    demo_for_plot["cleaned_signal"] = cleaned
    demo_for_plot["activity_pct"] = activity
    demo_for_plot["replicate_label"] = demo_for_plot["replicate_id"].map(
        lambda r: f"Replicate {int(r)}"
    )

    mo.md(
        f"**Dose-response prep:** minimum activity at top dose = "
        f"{np.nanmin(activity):.1f}%"
    )
    return demo, demo_for_plot


@app.cell
def _(demo):
    demo
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Step 5: Plot Individual Replicate Curves (Plotly)

    This plot shows one curve per replicate across concentrations.

    Each point is labeled by replicate number, and hover details include raw and cleaned signal values.
    """)
    return


@app.cell(hide_code=True)
def _(demo_for_plot):
    import plotly.express as px

    plot_df = demo_for_plot.dropna(subset=["activity_pct"]).copy()

    fig = px.line(
        plot_df,
        x="concentration_um",
        y="activity_pct",
        color="replicate_label",
        line_group="replicate_label",
        markers=True,
        text="replicate_id",
        hover_data={
            "replicate_label": True,
            "signal": ":.2f",
            "cleaned_signal": ":.2f",
            "activity_pct": ":.2f",
        },
        title="Individual Dose-Response Curves by Replicate",
    )

    fig.update_xaxes(type="log", title="Concentration (uM)")
    fig.update_yaxes(title="Activity (% of control)")
    fig.update_layout(legend_title_text="Replicate")
    fig.update_traces(textposition="top center")

    fig
    return


if __name__ == "__main__":
    app.run()
