"""Market data retrieval and basic validation."""
from __future__ import annotations

import pandas as pd
import yfinance as yf

REQUIRED_COLUMNS = ["Open", "High", "Low", "Close", "Volume"]


def download_history(ticker: str, period: str = "1y") -> pd.DataFrame:
    """Download daily history for one symbol. Raises when no valid data is returned."""
    frame = yf.Ticker(ticker).history(period=period, interval="1d", auto_adjust=True)
    if frame is None or frame.empty:
        raise ValueError(f"No history returned for {ticker}")
    missing = [column for column in REQUIRED_COLUMNS if column not in frame.columns]
    if missing:
        raise ValueError(f"{ticker} is missing required columns: {missing}")

    result = frame[REQUIRED_COLUMNS].copy()
    result.index = pd.to_datetime(result.index).tz_localize(None)
    result.index.name = "Date"
    result = result[~result.index.duplicated(keep="last")].sort_index()
    result = result.dropna(subset=["Open", "High", "Low", "Close"])
    if result.empty:
        raise ValueError(f"No valid OHLC rows remain for {ticker}")
    return result
