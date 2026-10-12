"""Deterministic technical feature calculations."""
from __future__ import annotations

import numpy as np
import pandas as pd


def add_indicators(prices: pd.DataFrame) -> pd.DataFrame:
    """Return OHLCV plus common indicators; early rows may contain NaN warm-up values."""
    if "Close" not in prices.columns:
        raise ValueError("prices must contain a Close column")
    out = prices.copy()
    close = pd.to_numeric(out["Close"], errors="coerce")
    out["daily_return"] = close.pct_change()
    out["sma_20"] = close.rolling(20, min_periods=20).mean()
    out["sma_50"] = close.rolling(50, min_periods=50).mean()

    delta = close.diff()
    gain = delta.clip(lower=0).rolling(14, min_periods=14).mean()
    loss = (-delta.clip(upper=0)).rolling(14, min_periods=14).mean()
    relative_strength = gain / loss.replace(0, np.nan)
    out["rsi_14"] = 100 - (100 / (1 + relative_strength))
    # A continuously rising series has no average losses; represent RSI as 100.
    out.loc[(loss == 0) & (gain > 0), "rsi_14"] = 100.0

    ema_12 = close.ewm(span=12, adjust=False, min_periods=12).mean()
    ema_26 = close.ewm(span=26, adjust=False, min_periods=26).mean()
    out["macd"] = ema_12 - ema_26
    out["macd_signal"] = out["macd"].ewm(span=9, adjust=False, min_periods=9).mean()
    out["volatility_20d_annualized"] = out["daily_return"].rolling(20, min_periods=20).std() * np.sqrt(252)
    return out


def build_model_frame(features: pd.DataFrame) -> pd.DataFrame:
    """Create next-session direction target with predictors available at current close."""
    out = features.copy()
    # Target on row t describes the return from close t to close t+1.
    out["target_up_next_session"] = (out["Close"].shift(-1) > out["Close"]).astype("int64")
    # The last row has no known future target and must be excluded.
    out.loc[out.index[-1], "target_up_next_session"] = np.nan
    return out
