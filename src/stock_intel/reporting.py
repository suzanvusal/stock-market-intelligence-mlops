"""Human-readable report generation."""
from __future__ import annotations

from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import pandas as pd


def _fmt(value: object, digits: int = 2) -> str:
    """Format a numeric value, handling missing data."""
    if pd.isna(value):
        return "n/a"
    return f"{value:.{digits}f}"


def _trend_label(close: object, sma_20: object, sma_50: object) -> str:
    """Describe the latest close relative to its moving averages."""
    values = (close, sma_20, sma_50)
    if any(pd.isna(value) for value in values):
        return "Insufficient data"
    if close > sma_20 and close > sma_50:
        return "Above both SMAs"
    if close < sma_20 and close < sma_50:
        return "Below both SMAs"
    return "Mixed / between SMAs"


def _rsi_label(rsi: object) -> str:
    """Give a simple educational interpretation of RSI."""
    if pd.isna(rsi):
        return "Unavailable"
    if rsi < 30:
        return "Low RSI (<30)"
    if rsi > 70:
        return "High RSI (>70)"
    return "Middle range (30-70)"


def write_report(
    output_path: Path,
    snapshots: dict[str, pd.DataFrame],
    model_results: dict[str, dict],
    errors: dict[str, str],
) -> None:
    now = datetime.now(ZoneInfo("America/Toronto"))
    lines = [
        f"# Daily Market Intelligence — {now:%Y-%m-%d}",
        "",
        f"- Generated: {now:%Y-%m-%d %H:%M %Z}",
        "- Purpose: educational market observation, not investment advice.",
        "- Prices are daily adjusted OHLCV from the configured public data source.",
        "",
        "## Watchlist overview",
        "",
        "| Symbol | Last date | Close | Daily return | RSI (14) | RSI interpretation | SMA 20 | SMA 50 | Trend |",
        "|---|---:|---:|---:|---:|---|---:|---:|---|",
    ]

    for ticker, frame in sorted(snapshots.items()):
        if frame.empty:
            continue

        last = frame.iloc[-1]
        date_label = pd.Timestamp(frame.index[-1]).strftime("%Y-%m-%d")
        daily_return = last.get("daily_return")
        return_label = (
            "n/a" if pd.isna(daily_return)
            else f"{daily_return * 100:.2f}%"
        )
        close = last.get("Close")
        sma_20 = last.get("sma_20")
        sma_50 = last.get("sma_50")
        rsi = last.get("rsi_14")

        lines.append(
            f"| {ticker} | {date_label} | {_fmt(close)} | {return_label} | "
            f"{_fmt(rsi)} | {_rsi_label(rsi)} | {_fmt(sma_20)} | "
            f"{_fmt(sma_50)} | {_trend_label(close, sma_20, sma_50)} |"
        )

    lines += [
        "",
        "### How to read the indicators",
        "",
        (
            "- **Above both SMAs:** the latest close is above both its 20-day "
            "and 50-day averages. This describes recent price positioning, "
            "not a guaranteed future direction."
        ),
        "- **Below both SMAs:** the latest close is below both averages.",
        "- **Mixed / between SMAs:** the close is not above both or below both.",
        (
            "- **RSI below 30:** conventionally considered a low RSI reading. "
            "It does not guarantee a rebound."
        ),
        (
            "- **RSI above 70:** conventionally considered a high RSI reading. "
            "It does not guarantee a reversal."
        ),
        "- **RSI 30-70:** the middle range under these simple thresholds.",
        (
            "- **Daily return:** the percentage price change for the latest bar; "
            "it can be negative even when the close is above both averages."
        ),
        "",
        (
            "These labels describe historical data and are not standalone "
            "buy/sell signals."
        ),
        "",
        "## Baseline model experiment",
        "",
    ]

    for ticker, result in sorted(model_results.items()):
        if result.get("status") == "ok":
            lines.append(
                f"- **{ticker}:** accuracy {result['accuracy']:.3f}; "
                f"balanced accuracy {result['balanced_accuracy']:.3f}; "
                f"test samples {result['test_samples']}; "
                f"test positive-target rate {result['baseline_up_rate']:.3f}."
            )
        else:
            lines.append(
                f"- **{ticker}:** "
                f"{result.get('status', 'not available')} "
                f"({result.get('samples', 0)} samples)."
            )

    lines += [
        "",
        (
            "Model metrics are historical holdout results, not a forecast "
            "guarantee or a buy/sell recommendation."
        ),
        "",
        "## Data retrieval issues",
        "",
    ]

    if errors:
        lines.extend(
            f"- **{ticker}:** {message}"
            for ticker, message in sorted(errors.items())
        )
    else:
        lines.append("- None recorded.")

    lines += [
        "",
        "## Notes",
        "",
        "- Daily bars can be delayed or revised. Check timestamps and provider terms.",
        "- Indicators summarize past prices and are not standalone decision rules.",
        "- No transaction costs, taxes, slippage, or portfolio constraints are modeled.",
        "",
    ]

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(lines), encoding="utf-8")
