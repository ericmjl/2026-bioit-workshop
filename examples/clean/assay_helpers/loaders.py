"""Shared assay table loading extracted from duplicated notebooks."""

from __future__ import annotations

from pathlib import Path
from typing import Literal

import pandas as pd

TableKind = Literal["plate", "dose_response", "expression_matrix"]


def load_assay_table(
    path: Path,
    *,
    kind: TableKind = "plate",
) -> pd.DataFrame:
    """Load an assay export and normalize column names.

    :param path: CSV path from plate reader, dose-response run, or LIMS export.
    :param kind: Expected table shape — selects parsing rules.
    """
    if kind == "expression_matrix":
        counts = pd.read_csv(path, index_col=0)
        counts.index = counts.index.astype(str)
        counts.columns = [c.strip() for c in counts.columns]
        return counts

    df = pd.read_csv(path)
    df.columns = [c.strip().lower() for c in df.columns]

    if kind == "plate" and "well" not in df.columns:
        raise ValueError("plate exports require a well column")

    if kind == "dose_response":
        df["concentration_um"] = pd.to_numeric(df["concentration_um"])
        df["signal"] = pd.to_numeric(df["signal"])
        return df.dropna(subset=["concentration_um", "signal"])

    if kind == "plate":
        df["well"] = df["well"].astype(str)

    return df
