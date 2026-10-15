# Daily Market Intelligence — 2026-10-15

- Generated: 2026-10-15 09:52 EDT
- Purpose: educational market observation, not investment advice.
- Prices are daily adjusted OHLCV from the configured public data source.

## Watchlist overview

| Symbol | Last date | Close | Daily return | RSI (14) | RSI interpretation | SMA 20 | SMA 50 | Trend |
|---|---:|---:|---:|---:|---|---:|---:|---|
| AAPL | 2026-10-15 | 346.01 | 0.89% | 55.77 | Middle range (30-70) | 337.26 | 325.15 | Above both SMAs |
| MSFT | 2026-10-15 | 535.19 | 0.28% | 64.10 | Middle range (30-70) | 518.24 | 504.68 | Above both SMAs |
| QQQ | 2026-10-15 | 717.41 | -1.58% | 33.22 | Middle range (30-70) | 742.53 | 726.20 | Below both SMAs |
| RY.TO | 2026-10-15 | 276.00 | -0.01% | 40.21 | Middle range (30-70) | 280.19 | 285.69 | Below both SMAs |
| SHOP.TO | 2026-10-15 | 241.81 | -1.50% | 76.86 | High RSI (>70) | 216.77 | 207.30 | Above both SMAs |
| SPY | 2026-10-15 | 765.68 | -0.51% | 44.08 | Middle range (30-70) | 770.80 | 767.35 | Below both SMAs |
| VFV.TO | 2026-10-15 | 193.50 | -0.71% | 51.37 | Middle range (30-70) | 194.13 | 191.07 | Mixed / between SMAs |
| XEQT.TO | 2026-10-15 | 45.36 | -0.57% | 44.81 | Middle range (30-70) | 45.79 | 45.66 | Below both SMAs |

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

- **AAPL:** accuracy 0.463; balanced accuracy 0.516; test samples 41; test positive-target rate 0.585.
- **MSFT:** accuracy 0.415; balanced accuracy 0.500; test samples 41; test positive-target rate 0.585.
- **QQQ:** accuracy 0.463; balanced accuracy 0.500; test samples 41; test positive-target rate 0.537.
- **RY.TO:** accuracy 0.366; balanced accuracy 0.500; test samples 41; test positive-target rate 0.366.
- **SHOP.TO:** accuracy 0.439; balanced accuracy 0.521; test samples 41; test positive-target rate 0.585.
- **SPY:** accuracy 0.634; balanced accuracy 0.559; test samples 41; test positive-target rate 0.415.
- **VFV.TO:** accuracy 0.463; balanced accuracy 0.522; test samples 41; test positive-target rate 0.561.
- **XEQT.TO:** accuracy 0.537; balanced accuracy 0.484; test samples 41; test positive-target rate 0.439.

Model metrics are historical holdout results, not a forecast guarantee or a buy/sell recommendation.

## Data retrieval issues

- None recorded.

## Notes

- Daily bars can be delayed or revised. Check timestamps and provider terms.
- Indicators summarize past prices and are not standalone decision rules.
- No transaction costs, taxes, slippage, or portfolio constraints are modeled.
