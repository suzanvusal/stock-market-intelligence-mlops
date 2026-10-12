"""Human-readable report generation."""
from __future__ import annotations

from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import pandas as pd


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
        "| Symbol | Last date | Close | Daily return | RSI (14) | SMA 20 | SMA 50 |",
        "|---|---:|---:|---:|---:|---:|---:|",
    ]
    for ticker, frame in sorted(snapshots.items()):
        last = frame.iloc[-1]
        date_label = pd.Timestamp(frame.index[-1]).strftime("%Y-%m-%d")
        def fmt(value, digits=2):
            return "n/a" if pd.isna(value) else f"{value:.{digits}f}"
        daily_return = last.get("daily_return")
        return_label = "n/a" if pd.isna(daily_return) else f"{daily_return * 100:.2f}%"
        lines.append(
            f"| {ticker} | {date_label} | {fmt(last.get('Close'))} | {return_label} | "
            f"{fmt(last.get('rsi_14'))} | {fmt(last.get('sma_20'))} | {fmt(last.get('sma_50'))} |"
        )
    lines += ["", "## Baseline model experiment", ""]
    for ticker, result in sorted(model_results.items()):
        if result.get("status") == "ok":
            lines.append(
                f"- **{ticker}:** accuracy {result['accuracy']:.3f}; "
                f"balanced accuracy {result['balanced_accuracy']:.3f}; "
                f"test samples {result['test_samples']}; "
                f"test positive-target rate {result['baseline_up_rate']:.3f}."
            )
        else:
            lines.append(f"- **{ticker}:** {result.get('status', 'not available')} ({result.get('samples', 0)} samples).")
    lines += [
        "",
        "Model metrics are historical holdout results, not a forecast guarantee or a buy/sell recommendation.",
        "",
        "## Data retrieval issues",
        "",
    ]
    if errors:
        lines.extend(f"- **{ticker}:** {message}" for ticker, message in sorted(errors.items()))
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
