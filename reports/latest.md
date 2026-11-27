# Daily Market Intelligence — 2026-11-27

- Generated: 2026-11-27 16:51 EST
- Purpose: educational market observation, not investment advice.
- Prices are daily adjusted OHLCV from the configured public data source.

## Watchlist overview

| Symbol | Last date | Close | Daily return | RSI (14) | RSI interpretation | SMA 20 | SMA 50 | Trend |
|---|---:|---:|---:|---:|---|---:|---:|---|
| AAPL | 2026-11-27 | 358.54 | 0.83% | 66.35 | Middle range (30-70) | 349.04 | 343.27 | Above both SMAs |
| MSFT | 2026-11-27 | 492.85 | 0.60% | 32.42 | Middle range (30-70) | 514.56 | 518.57 | Below both SMAs |
| QQQ | 2026-11-27 | 650.99 | 2.69% | 48.77 | Middle range (30-70) | 663.51 | 705.72 | Below both SMAs |
| RY.TO | 2026-11-27 | 267.95 | -0.26% | 24.36 | Low RSI (<30) | 279.76 | 279.75 | Below both SMAs |
| SHOP.TO | 2026-11-27 | 202.90 | 4.86% | 42.94 | Middle range (30-70) | 202.26 | 216.25 | Mixed / between SMAs |
| SPY | 2026-11-27 | 728.32 | 1.62% | 47.67 | Middle range (30-70) | 738.28 | 757.20 | Below both SMAs |
| VFV.TO | 2026-11-27 | 185.38 | 1.19% | 44.87 | Middle range (30-70) | 186.22 | 190.48 | Below both SMAs |
| XEQT.TO | 2026-11-27 | 43.98 | 1.13% | 40.79 | Middle range (30-70) | 44.32 | 45.10 | Below both SMAs |

### How to read the indicators

- **Above both SMAs:** the latest close is above both its 20-day and 50-day averages. This describes recent price positioning, not a guaranteed future direction.
- **Below both SMAs:** the latest close is below both averages.
- **Mixed / between SMAs:** the close is not above both or below both.
- **RSI below 30:** conventionally considered a low RSI reading. It does not guarantee a rebound.
- **RSI above 70:** conventionally considered a high RSI reading. It does not guarantee a reversal.
- **RSI 30-70:** the middle range under these simple thresholds.
- **Daily return:** the percentage price change for the latest bar; it can be negative even when the close is above both averages.

These labels describe historical data and are not standalone buy/sell signals.

## Baseline model experiment

- **AAPL:** accuracy 0.512; balanced accuracy 0.518; test samples 41; test positive-target rate 0.512.
- **MSFT:** accuracy 0.488; balanced accuracy 0.500; test samples 41; test positive-target rate 0.512.
- **QQQ:** accuracy 0.537; balanced accuracy 0.496; test samples 41; test positive-target rate 0.439.
- **RY.TO:** accuracy 0.561; balanced accuracy 0.479; test samples 41; test positive-target rate 0.415.
- **SHOP.TO:** accuracy 0.512; balanced accuracy 0.531; test samples 41; test positive-target rate 0.537.
- **SPY:** accuracy 0.415; balanced accuracy 0.404; test samples 41; test positive-target rate 0.463.
- **VFV.TO:** accuracy 0.439; balanced accuracy 0.433; test samples 41; test positive-target rate 0.488.
- **XEQT.TO:** accuracy 0.585; balanced accuracy 0.593; test samples 41; test positive-target rate 0.390.

Model metrics are historical holdout results, not a forecast guarantee or a buy/sell recommendation.

## Data retrieval issues

- None recorded.

## Notes

- Daily bars can be delayed or revised. Check timestamps and provider terms.
- Indicators summarize past prices and are not standalone decision rules.
- No transaction costs, taxes, slippage, or portfolio constraints are modeled.
