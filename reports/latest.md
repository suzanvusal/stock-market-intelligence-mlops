# Daily Market Intelligence — 2026-11-18

- Generated: 2026-11-18 16:10 EST
- Purpose: educational market observation, not investment advice.
- Prices are daily adjusted OHLCV from the configured public data source.

## Watchlist overview

| Symbol | Last date | Close | Daily return | RSI (14) | RSI interpretation | SMA 20 | SMA 50 | Trend |
|---|---:|---:|---:|---:|---|---:|---:|---|
| AAPL | 2026-11-18 | 352.45 | 0.15% | 52.88 | Middle range (30-70) | 347.49 | 340.92 | Above both SMAs |
| MSFT | 2026-11-18 | 508.29 | 0.40% | 43.08 | Middle range (30-70) | 526.09 | 519.94 | Below both SMAs |
| QQQ | 2026-11-18 | 659.51 | 0.39% | 34.36 | Middle range (30-70) | 686.30 | 714.26 | Below both SMAs |
| RY.TO | 2026-11-18 | 272.26 | -3.11% | 33.39 | Middle range (30-70) | 285.30 | 281.80 | Below both SMAs |
| SHOP.TO | 2026-11-18 | 199.78 | -1.50% | 32.90 | Middle range (30-70) | 217.10 | 214.71 | Below both SMAs |
| SPY | 2026-11-18 | 730.25 | -0.30% | 34.69 | Middle range (30-70) | 753.72 | 762.28 | Below both SMAs |
| VFV.TO | 2026-11-18 | 186.20 | 0.03% | 41.56 | Middle range (30-70) | 189.15 | 191.21 | Below both SMAs |
| XEQT.TO | 2026-11-18 | 44.01 | -0.74% | 39.91 | Middle range (30-70) | 44.99 | 45.36 | Below both SMAs |

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

- **AAPL:** accuracy 0.488; balanced accuracy 0.523; test samples 41; test positive-target rate 0.463.
- **MSFT:** accuracy 0.488; balanced accuracy 0.500; test samples 41; test positive-target rate 0.512.
- **QQQ:** accuracy 0.561; balanced accuracy 0.530; test samples 41; test positive-target rate 0.463.
- **RY.TO:** accuracy 0.537; balanced accuracy 0.478; test samples 41; test positive-target rate 0.439.
- **SHOP.TO:** accuracy 0.439; balanced accuracy 0.500; test samples 41; test positive-target rate 0.561.
- **SPY:** accuracy 0.488; balanced accuracy 0.453; test samples 41; test positive-target rate 0.439.
- **VFV.TO:** accuracy 0.537; balanced accuracy 0.545; test samples 41; test positive-target rate 0.512.
- **XEQT.TO:** accuracy 0.585; balanced accuracy 0.559; test samples 41; test positive-target rate 0.390.

Model metrics are historical holdout results, not a forecast guarantee or a buy/sell recommendation.

## Data retrieval issues

- None recorded.

## Notes

- Daily bars can be delayed or revised. Check timestamps and provider terms.
- Indicators summarize past prices and are not standalone decision rules.
- No transaction costs, taxes, slippage, or portfolio constraints are modeled.
