# Daily Market Intelligence — 2026-11-20

- Generated: 2026-11-20 15:57 EST
- Purpose: educational market observation, not investment advice.
- Prices are daily adjusted OHLCV from the configured public data source.

## Watchlist overview

| Symbol | Last date | Close | Daily return | RSI (14) | RSI interpretation | SMA 20 | SMA 50 | Trend |
|---|---:|---:|---:|---:|---|---:|---:|---|
| AAPL | 2026-11-20 | 341.57 | -2.19% | 52.64 | Middle range (30-70) | 347.26 | 341.57 | Mixed / between SMAs |
| MSFT | 2026-11-20 | 482.61 | -3.15% | 42.62 | Middle range (30-70) | 521.95 | 518.83 | Below both SMAs |
| QQQ | 2026-11-20 | 607.60 | -5.80% | 31.27 | Middle range (30-70) | 678.49 | 710.87 | Below both SMAs |
| RY.TO | 2026-11-20 | 263.29 | -2.29% | 27.27 | Low RSI (<30) | 283.89 | 281.11 | Below both SMAs |
| SHOP.TO | 2026-11-20 | 177.10 | -6.47% | 30.84 | Middle range (30-70) | 211.79 | 215.04 | Below both SMAs |
| SPY | 2026-11-20 | 686.97 | -4.04% | 28.81 | Low RSI (<30) | 747.67 | 759.97 | Below both SMAs |
| VFV.TO | 2026-11-20 | 175.60 | -4.02% | 34.80 | Middle range (30-70) | 188.09 | 190.92 | Below both SMAs |
| XEQT.TO | 2026-11-20 | 41.85 | -3.30% | 32.93 | Middle range (30-70) | 44.75 | 45.26 | Below both SMAs |

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

- **AAPL:** accuracy 0.415; balanced accuracy 0.394; test samples 41; test positive-target rate 0.463.
- **MSFT:** accuracy 0.512; balanced accuracy 0.500; test samples 41; test positive-target rate 0.488.
- **QQQ:** accuracy 0.561; balanced accuracy 0.530; test samples 41; test positive-target rate 0.463.
- **RY.TO:** accuracy 0.561; balanced accuracy 0.500; test samples 41; test positive-target rate 0.439.
- **SHOP.TO:** accuracy 0.463; balanced accuracy 0.500; test samples 41; test positive-target rate 0.537.
- **SPY:** accuracy 0.439; balanced accuracy 0.409; test samples 41; test positive-target rate 0.439.
- **VFV.TO:** accuracy 0.537; balanced accuracy 0.529; test samples 41; test positive-target rate 0.488.
- **XEQT.TO:** accuracy 0.585; balanced accuracy 0.574; test samples 41; test positive-target rate 0.366.

Model metrics are historical holdout results, not a forecast guarantee or a buy/sell recommendation.

## Data retrieval issues

- None recorded.

## Notes

- Daily bars can be delayed or revised. Check timestamps and provider terms.
- Indicators summarize past prices and are not standalone decision rules.
- No transaction costs, taxes, slippage, or portfolio constraints are modeled.
