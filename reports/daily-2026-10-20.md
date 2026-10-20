# Daily Market Intelligence — 2026-10-20

- Generated: 2026-10-20 12:33 EDT
- Purpose: educational market observation, not investment advice.
- Prices are daily adjusted OHLCV from the configured public data source.

## Watchlist overview

| Symbol | Last date | Close | Daily return | RSI (14) | RSI interpretation | SMA 20 | SMA 50 | Trend |
|---|---:|---:|---:|---:|---|---:|---:|---|
| AAPL | 2026-10-20 | 340.69 | -0.66% | 62.92 | Middle range (30-70) | 337.67 | 326.94 | Above both SMAs |
| MSFT | 2026-10-20 | 532.02 | -0.28% | 62.42 | Middle range (30-70) | 523.52 | 506.59 | Above both SMAs |
| QQQ | 2026-10-20 | 719.09 | 0.10% | 38.03 | Middle range (30-70) | 739.94 | 726.23 | Below both SMAs |
| RY.TO | 2026-10-20 | 279.60 | 0.75% | 44.57 | Middle range (30-70) | 279.25 | 284.75 | Mixed / between SMAs |
| SHOP.TO | 2026-10-20 | 245.14 | 1.51% | 72.89 | High RSI (>70) | 225.98 | 209.65 | Above both SMAs |
| SPY | 2026-10-20 | 769.31 | 0.37% | 56.42 | Middle range (30-70) | 770.63 | 767.27 | Mixed / between SMAs |
| VFV.TO | 2026-10-20 | 192.32 | -0.09% | 48.18 | Middle range (30-70) | 194.43 | 191.15 | Mixed / between SMAs |
| XEQT.TO | 2026-10-20 | 45.45 | 0.22% | 47.16 | Middle range (30-70) | 45.79 | 45.64 | Below both SMAs |

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

- **AAPL:** accuracy 0.439; balanced accuracy 0.500; test samples 41; test positive-target rate 0.561.
- **MSFT:** accuracy 0.439; balanced accuracy 0.500; test samples 41; test positive-target rate 0.561.
- **QQQ:** accuracy 0.439; balanced accuracy 0.500; test samples 41; test positive-target rate 0.561.
- **RY.TO:** accuracy 0.561; balanced accuracy 0.500; test samples 41; test positive-target rate 0.439.
- **SHOP.TO:** accuracy 0.390; balanced accuracy 0.519; test samples 41; test positive-target rate 0.634.
- **SPY:** accuracy 0.610; balanced accuracy 0.556; test samples 41; test positive-target rate 0.439.
- **VFV.TO:** accuracy 0.439; balanced accuracy 0.521; test samples 41; test positive-target rate 0.585.
- **XEQT.TO:** accuracy 0.512; balanced accuracy 0.500; test samples 41; test positive-target rate 0.488.

Model metrics are historical holdout results, not a forecast guarantee or a buy/sell recommendation.

## Data retrieval issues

- None recorded.

## Notes

- Daily bars can be delayed or revised. Check timestamps and provider terms.
- Indicators summarize past prices and are not standalone decision rules.
- No transaction costs, taxes, slippage, or portfolio constraints are modeled.
