"""Tests for refactored assay helpers."""

import numpy as np
import pandas as pd
import pytest
from pathlib import Path

from assay_helpers import load_assay_table, normalize_to_control, remove_outliers


def test_load_assay_table_plate(tmp_path: Path) -> None:
    csv = tmp_path / "plate.csv"
    pd.DataFrame({"well": ["A1"], "signal": [100.0]}).to_csv(csv, index=False)
    table = load_assay_table(csv, kind="plate")
    assert list(table.columns) == ["well", "signal"]


def test_remove_outliers_zscore() -> None:
    values = np.array([10.0, 10.0, 10.0, 10.0, 500.0])
    cleaned = remove_outliers(values, method="zscore", z_thresh=1.5)
    assert np.isnan(cleaned[-1])


def test_normalize_to_control_percent() -> None:
    result = normalize_to_control(np.array([50.0]), 100.0, mode="percent")
    assert result[0] == pytest.approx(50.0)
