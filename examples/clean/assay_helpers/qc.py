"""Outlier detection extracted from duplicated notebook copies."""

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

    :param values: Raw measurements (well signals, replicates, library sizes).
    :param method: ``zscore`` (mean/std), ``mad`` (median/MAD), or ``log_zscore``.
    :param z_thresh: Threshold for flagging outliers.
    """
    cleaned = values.astype(float).copy()

    if method == "mad":
        med = float(np.median(cleaned))
        mad = float(np.median(np.abs(cleaned - med)))
        if mad == 0:
            return cleaned
        modified_z = 0.6745 * (cleaned - med) / mad
        cleaned[np.abs(modified_z) > z_thresh] = np.nan
        return cleaned

    working = cleaned
    if method == "log_zscore":
        working = np.log1p(cleaned)

    mu = float(np.nanmean(working))
    sigma = float(np.nanstd(working))
    if sigma == 0:
        return cleaned

    z = np.abs((working - mu) / sigma)
    cleaned[z > z_thresh] = np.nan
    return cleaned
