"""Normalization helpers for assay preprocessing."""

from __future__ import annotations

from typing import Literal

import numpy as np

NormalizeMode = Literal["ratio", "percent", "cpm"]


def normalize_to_control(
    values: np.ndarray,
    control_mean: float,
    *,
    mode: NormalizeMode = "ratio",
) -> np.ndarray:
    """Scale values relative to a control reference.

    :param values: Measurements to normalize, potentially containing NaN values.
    :param control_mean: Reference level from control wells or library size.
    :param mode: Normalization mode, one of ``ratio``, ``percent``, or ``cpm``.
    """
    if control_mean == 0:
        raise ValueError("control mean must be non-zero")

    if mode == "ratio":
        return values / control_mean
    if mode == "percent":
        return 100.0 * values / control_mean
    return (values / control_mean) * 1_000_000.0
