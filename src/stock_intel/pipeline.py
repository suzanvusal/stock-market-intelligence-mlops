"""CLI entry point for daily market data, indicators, and report generation."""
from __future__ import annotations

import argparse
import json
import logging
from datetime import datetime
from pathlib import Path

import pandas as pd

from stock_intel.data_source import download_history
from stock_intel.features import add_indicators
from stock_intel.modeling import evaluate_baseline
from stock_intel.reporting import write_report

ROOT = Path(__file__).resolve().parents[2]
WATCHLIST_PATH = ROOT / "config" / "watchlist.json"
DATA_DIR = ROOT / "data" / "processed"
REPORTS_DIR = ROOT / "reports"

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
LOGGER = logging.getLogger(__name__)


def run_pipeline() -> int:
    config = json.loads(WATCHLIST_PATH.read_text(encoding="utf-8"))
    snapshots: dict[str, pd.DataFrame] = {}
    model_results: dict[str, dict] = {}
    errors: dict[str, str] = {}
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    for ticker in config["tickers"]:
        try:
            prices = download_history(ticker, config.get("period", "1y"))
            features = add_indicators(prices)
            features.to_csv(DATA_DIR / f"{ticker.replace('.', '_')}_latest.csv", index_label="Date")
            snapshots[ticker] = features
            model_results[ticker] = evaluate_baseline(features)
            LOGGER.info("%s: retrieved %s daily rows", ticker, len(features))
        
        except (ValueError, KeyError, OSError, RuntimeError) as exc:
            errors[ticker] = f"{type(exc).__name__}: {exc}"
            LOGGER.warning("%s failed: %s", ticker, errors[ticker])


    if not snapshots:
        LOGGER.error("No symbols returned valid data; refusing to publish an empty report.")
        return 1

    date_tag = datetime.now().astimezone().strftime("%Y-%m-%d")
    write_report(REPORTS_DIR / f"daily-{date_tag}.md", snapshots, model_results, errors)
    write_report(REPORTS_DIR / "latest.md", snapshots, model_results, errors)
    (DATA_DIR / "run_metadata.json").write_text(
        json.dumps(
            {
                "run_date": date_tag,
                "symbols_succeeded": sorted(snapshots),
                "symbols_failed": errors,
                "rows": {ticker: len(frame) for ticker, frame in snapshots.items()},
            },
            indent=2,
        ) + "\n",
        encoding="utf-8",
    )
    LOGGER.info("Report written. Success=%d Failure=%d", len(snapshots), len(errors))
    # Partial success is useful: publish valid symbols and record failed symbols in the report.
    # Return failure only when every symbol failed, which is handled above.
    return 0


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args()
    raise SystemExit(run_pipeline())


if __name__ == "__main__":
    main()
