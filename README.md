# Stock Market Intelligence & MLOps

An educational, automated market-data pipeline for US and Canadian stocks/ETFs. It downloads daily OHLCV data, computes technical indicators, runs a simple time-ordered baseline experiment, produces a dated Markdown report, and validates the pipeline with tests.

> **Research/education only.** This repository does not provide personalized financial advice or reliable predictions. Indicators and historical models do not guarantee future results. `yfinance` uses Yahoo Finance's publicly available interfaces and is intended for personal/research use; review the provider's terms before broader use.

## Initial watchlist

Edit `config/watchlist.json` to change symbols.

- US: `AAPL`, `MSFT`, `SPY`, `QQQ`
- Canada: `SHOP.TO`, `VFV.TO`, `XEQT.TO`, `RY.TO`

Canadian symbols commonly use the `.TO` suffix on Yahoo Finance. Symbols, availability, and data completeness can change.

## Features

- Daily historical data download with no API key required initially (`yfinance`)
- CSV data snapshots and computed features
- SMA 20/50, RSI 14, MACD, annualized rolling volatility, daily return
- A simple logistic-regression experiment with a chronological split and next-session direction target
- Dated Markdown report with data-quality notes and model metrics
- `pytest` tests, Ruff linting, and GitHub Actions automation
- Scheduled weekday run at **8:00 a.m. Toronto time**; manual `workflow_dispatch` is also available

## Local setup (macOS/Linux)

Requires Python 3.11+.

```bash
git clone https://github.com/YOUR-USERNAME/stock-market-intelligence-mlops.git
cd stock-market-intelligence-mlops

python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt

# Run automated tests without calling a market-data provider
pytest

# Run the live pipeline (internet/provider availability required)
python -m stock_intel.pipeline
```

Outputs are written to `data/processed/` and `reports/`. These output folders are intentionally versioned so the scheduled workflow can commit useful daily artifacts.

## Run the workflow

1. Create a GitHub repository named `stock-market-intelligence-mlops`.
2. Upload/push this project to its default branch (`main`).
3. In GitHub, open **Settings → Actions → General → Workflow permissions** and select **Read and write permissions**.
4. Open **Actions → Daily Market Intelligence** and choose **Run workflow** for the first live run.
5. Review the run logs and generated report. The workflow commits outputs only when tests and pipeline succeed and there are changes.

Scheduled workflows run from the default branch. GitHub may delay scheduled starts during high load; a scheduled workflow is not guaranteed to start at the exact minute. See [GitHub Actions schedule documentation](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#schedule).

## What the model does (and doesn't)

The baseline experiment uses technical features available at close on session t to classify whether the next observed daily close-to-close return is positive. The target is the next session's close direction, so no future-session feature is used. It uses a chronological holdout, not a random split. This is a learning exercise, not a trading signal; it does not account for transaction costs, taxes, slippage, survivorship bias, or portfolio constraints.

## Data source caveat

`yfinance` is an open-source tool that accesses Yahoo Finance's publicly available interfaces. It is not affiliated with or endorsed by Yahoo. Data availability, adjustments, rate limits, and terms can change. This initial setup is suitable for personal educational research, not a guaranteed production market-data service.

## Project layout

```text
.
├── .github/workflows/daily-market-intelligence.yml
├── config/watchlist.json
├── data/processed/.gitkeep
├── reports/.gitkeep
├── src/stock_intel/
│   ├── __init__.py
│   ├── data_source.py
│   ├── features.py
│   ├── modeling.py
│   ├── reporting.py
│   └── pipeline.py
├── tests/
├── requirements.txt
└── pyproject.toml
```

## Suggested 30-day progression

1–5: data ingestion, configuration, validation, and tests  
6–10: indicators, watchlist comparisons, and anomaly flags  
11–15: baseline model, time-aware evaluation, and experiment tracking  
16–20: report improvements and optional Streamlit dashboard  
21–25: monitoring, data-quality checks, and workflow reliability  
26–30: documentation, charts, demo artifacts, and portfolio polish

## License

MIT; see `LICENSE`.
