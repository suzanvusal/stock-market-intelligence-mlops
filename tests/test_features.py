import numpy as np
import pandas as pd
import pytest

from stock_intel.features import add_indicators


def sample_prices(n=100):
    idx = pd.date_range("2024-01-01", periods=n, freq="B")
    close = pd.Series(np.linspace(100, 150, n), index=idx)
    return pd.DataFrame({
        "Open": close - 0.5,
        "High": close + 1,
        "Low": close - 1,
        "Close": close,
        "Volume": 1000,
    }, index=idx)


def test_indicators_are_created():
    result = add_indicators(sample_prices())
    for column in ["daily_return", "sma_20", "sma_50", "rsi_14", "macd", "macd_signal", "volatility_20d_annualized"]:
        assert column in result.columns
    assert result["sma_20"].notna().any()
    assert result["sma_50"].notna().any()


def test_missing_close_fails():
    with pytest.raises(ValueError, match="Close"):
        add_indicators(pd.DataFrame({"Open": [1]}))
