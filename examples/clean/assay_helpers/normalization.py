"""Normalization helpers extracted from duplicated notebook copies."""

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

    :param values: Measurements to normalize (may contain NaN from QC).
    :param control_mean: Reference level from control wells or library size.
    :param mode: ``ratio`` (divide), ``percent`` (×100), or ``cpm`` (counts per million).
    """
    if control_mean == 0:
        raise ValueError("control_mean must be non-zero")

    if mode == "ratio":
        return values / control_mean
    if mode == "percent":
        return 100.0 * values / control_mean
    return (values / control_mean) * 1_000_000.0
