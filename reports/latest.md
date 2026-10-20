# Daily Market Intelligence — 2026-10-20

- Generated: 2026-10-20 09:35 EDT
- Purpose: educational market observation, not investment advice.
- Prices are daily adjusted OHLCV from the configured public data source.

## Watchlist overview

| Symbol | Last date | Close | Daily return | RSI (14) | RSI interpretation | SMA 20 | SMA 50 | Trend |
|---|---:|---:|---:|---:|---|---:|---:|---|
| AAPL | 2026-10-20 | 342.85 | -0.03% | 67.84 | Middle range (30-70) | 337.78 | 326.98 | Above both SMAs |
| MSFT | 2026-10-20 | 532.80 | -0.13% | 63.07 | Middle range (30-70) | 523.56 | 506.61 | Above both SMAs |
| QQQ | 2026-10-20 | 713.29 | -0.71% | 35.41 | Middle range (30-70) | 739.66 | 726.11 | Below both SMAs |
| RY.TO | 2026-10-20 | 277.27 | -0.09% | 40.62 | Middle range (30-70) | 279.13 | 284.70 | Below both SMAs |
| SHOP.TO | 2026-10-20 | 243.60 | 0.87% | 72.34 | High RSI (>70) | 225.91 | 209.62 | Above both SMAs |
| SPY | 2026-10-20 | 765.59 | -0.12% | 52.96 | Middle range (30-70) | 770.44 | 767.19 | Below both SMAs |
| VFV.TO | 2026-10-20 | 191.30 | -0.62% | 44.85 | Middle range (30-70) | 194.38 | 191.13 | Mixed / between SMAs |
| XEQT.TO | 2026-10-20 | 45.16 | -0.42% | 43.02 | Middle range (30-70) | 45.78 | 45.64 | Below both SMAs |

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
- **QQQ:** accuracy 0.463; balanced accuracy 0.500; test samples 41; test positive-target rate 0.537.
- **RY.TO:** accuracy 0.585; balanced accuracy 0.500; test samples 41; test positive-target rate 0.415.
- **SHOP.TO:** accuracy 0.390; balanced accuracy 0.519; test samples 41; test positive-target rate 0.634.
- **SPY:** accuracy 0.634; balanced accuracy 0.559; test samples 41; test positive-target rate 0.415.
- **VFV.TO:** accuracy 0.439; balanced accuracy 0.521; test samples 41; test positive-target rate 0.585.
- **XEQT.TO:** accuracy 0.537; balanced accuracy 0.500; test samples 41; test positive-target rate 0.463.

Model metrics are historical holdout results, not a forecast guarantee or a buy/sell recommendation.

## Data retrieval issues

- None recorded.

## Notes

- Daily bars can be delayed or revised. Check timestamps and provider terms.
- Indicators summarize past prices and are not standalone decision rules.
- No transaction costs, taxes, slippage, or portfolio constraints are modeled.
