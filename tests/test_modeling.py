import numpy as np
import pandas as pd

from stock_intel.features import add_indicators
from stock_intel.modeling import evaluate_baseline


def test_model_returns_valid_status_or_metrics():
    idx = pd.date_range("2022-01-01", periods=300, freq="B")
    rng = np.random.default_rng(7)
    returns = rng.normal(0.0003, 0.012, size=len(idx))
    close = 100 * np.cumprod(1 + returns)
    prices = pd.DataFrame({
        "Open": close * 0.999,
        "High": close * 1.01,
        "Low": close * 0.99,
        "Close": close,
        "Volume": 1000,
    }, index=idx)
    result = evaluate_baseline(add_indicators(prices))
    assert result["status"] in {"ok", "insufficient_data", "insufficient_class_balance"}
    if result["status"] == "ok":
        assert 0 <= result["accuracy"] <= 1
        assert 0 <= result["balanced_accuracy"] <= 1
