"""Tests for assay helper modules extracted from messy notebooks."""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from assay_helpers.loaders import load_assay_table
from assay_helpers.normalization import normalize_to_control
from assay_helpers.qc import remove_outliers


def test_load_assay_table_plate_requires_well(tmp_path: Path) -> None:
    """Plate parser should validate required ``well`` column."""
    csv_path = tmp_path / "plate.csv"
    pd.DataFrame({"signal": [100.0]}).to_csv(csv_path, index=False)

    with pytest.raises(ValueError, match="well"):
        load_assay_table(csv_path, kind="plate")


def test_load_assay_table_expression_matrix_keeps_gene_ids(tmp_path: Path) -> None:
    """Expression parser should preserve matrix shape and string index."""
    csv_path = tmp_path / "expression.csv"
    matrix = pd.DataFrame(
        {
            "sample_ctrl": [100, 120],
            "sample_treat": [80, 140],
        },
        index=["GENE0001", "GENE0002"],
    )
    matrix.to_csv(csv_path)

    loaded = load_assay_table(csv_path, kind="expression_matrix")
    assert list(loaded.index) == ["GENE0001", "GENE0002"]
    assert list(loaded.columns) == ["sample_ctrl", "sample_treat"]


def test_remove_outliers_mad_masks_extreme_value() -> None:
    """MAD mode should replace an extreme observation with ``NaN``."""
    values = np.array([10.0, 11.0, 12.0, 13.0, 500.0])
    cleaned = remove_outliers(values, method="mad", z_thresh=2.5)
    assert np.isnan(cleaned[-1])


def test_remove_outliers_log_zscore_masks_large_library_size() -> None:
    """Log z-score mode should flag implausibly large library size."""
    values = np.array([1000.0, 1020.0, 980.0, 1010.0, 100000.0])
    cleaned = remove_outliers(values, method="log_zscore", z_thresh=1.9)
    assert np.isnan(cleaned[-1])


def test_normalize_to_control_supports_percent_ratio_and_cpm() -> None:
    """Normalization modes should apply expected control-relative scales."""
    values = np.array([50.0])
    assert normalize_to_control(values, 100.0, mode="ratio")[0] == pytest.approx(0.5)
    assert normalize_to_control(values, 100.0, mode="percent")[0] == pytest.approx(50.0)
    assert normalize_to_control(values, 100.0, mode="cpm")[0] == pytest.approx(500000.0)
