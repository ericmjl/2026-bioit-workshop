"""Shared assay table loading for messy notebook refactors."""

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
    :param kind: Expected table shape, used to select parser rules.
    """
    if kind == "expression_matrix":
        counts = pd.read_csv(path, index_col=0)
        counts.index = counts.index.astype(str)
        counts.columns = [column.strip() for column in counts.columns]
        return counts

    table = pd.read_csv(path)
    table.columns = [column.strip().lower() for column in table.columns]

    if kind == "plate":
        if "well" not in table.columns:
            raise ValueError("expected a well column")
        table["well"] = table["well"].astype(str)
        return table

    table["concentration_um"] = pd.to_numeric(table["concentration_um"])
    table["signal"] = pd.to_numeric(table["signal"])
    return table.dropna(subset=["concentration_um", "signal"])
