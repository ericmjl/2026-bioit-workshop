"""Outlier detection helpers for assay preprocessing."""

from __future__ import annotations

from typing import Literal

import numpy as np

OutlierMethod = Literal["zscore", "mad", "log_zscore"]


def remove_outliers(
    values: np.ndarray,
    *,
    method: OutlierMethod = "zscore",
    z_thresh: float = 3.0,
) -> np.ndarray:
    """Return a copy of values with outliers masked as NaN.

    :param values: Raw measurements such as plate signals or library sizes.
    :param method: Outlier strategy, one of ``zscore``, ``mad``, or ``log_zscore``.
    :param z_thresh: Threshold used by the selected outlier strategy.
    """
    cleaned = values.astype(float).copy()

    if method == "mad":
        median = float(np.median(cleaned))
        mad = float(np.median(np.abs(cleaned - median)))
        if mad == 0:
            return cleaned
        modified_z = 0.6745 * (cleaned - median) / mad
        cleaned[np.abs(modified_z) > z_thresh] = np.nan
        return cleaned

    transformed = cleaned
    if method == "log_zscore":
        transformed = np.log1p(cleaned)

    mu = float(np.nanmean(transformed))
    sigma = float(np.nanstd(transformed))
    if sigma == 0:
        return cleaned

    z_scores = np.abs((transformed - mu) / sigma)
    cleaned[z_scores > z_thresh] = np.nan
    return cleaned
