# Daily Market Intelligence — 2026-10-22

- Generated: 2026-10-22 12:50 EDT
- Purpose: educational market observation, not investment advice.
- Prices are daily adjusted OHLCV from the configured public data source.

## Watchlist overview

| Symbol | Last date | Close | Daily return | RSI (14) | RSI interpretation | SMA 20 | SMA 50 | Trend |
|---|---:|---:|---:|---:|---|---:|---:|---|
| AAPL | 2026-10-22 | 345.14 | 0.33% | 68.80 | Middle range (30-70) | 338.42 | 328.56 | Above both SMAs |
| MSFT | 2026-10-22 | 523.93 | -1.69% | 53.89 | Middle range (30-70) | 526.43 | 507.84 | Mixed / between SMAs |
| QQQ | 2026-10-22 | 704.69 | -2.83% | 28.56 | Low RSI (<30) | 737.25 | 725.98 | Below both SMAs |
| RY.TO | 2026-10-22 | 282.80 | -0.29% | 57.41 | Middle range (30-70) | 279.17 | 284.35 | Mixed / between SMAs |
| SHOP.TO | 2026-10-22 | 234.88 | -4.10% | 63.49 | Middle range (30-70) | 229.51 | 210.66 | Above both SMAs |
| SPY | 2026-10-22 | 762.23 | -1.40% | 43.79 | Middle range (30-70) | 770.63 | 767.18 | Below both SMAs |
| VFV.TO | 2026-10-22 | 190.13 | -1.63% | 40.93 | Middle range (30-70) | 194.28 | 191.18 | Below both SMAs |
| XEQT.TO | 2026-10-22 | 45.00 | -1.43% | 44.29 | Middle range (30-70) | 45.73 | 45.62 | Below both SMAs |

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

- **AAPL:** accuracy 0.415; balanced accuracy 0.500; test samples 41; test positive-target rate 0.585.
- **MSFT:** accuracy 0.512; balanced accuracy 0.545; test samples 41; test positive-target rate 0.537.
- **QQQ:** accuracy 0.463; balanced accuracy 0.500; test samples 41; test positive-target rate 0.537.
- **RY.TO:** accuracy 0.561; balanced accuracy 0.500; test samples 41; test positive-target rate 0.439.
- **SHOP.TO:** accuracy 0.415; balanced accuracy 0.509; test samples 41; test positive-target rate 0.610.
- **SPY:** accuracy 0.585; balanced accuracy 0.528; test samples 41; test positive-target rate 0.439.
- **VFV.TO:** accuracy 0.463; balanced accuracy 0.522; test samples 41; test positive-target rate 0.561.
- **XEQT.TO:** accuracy 0.561; balanced accuracy 0.526; test samples 41; test positive-target rate 0.463.

Model metrics are historical holdout results, not a forecast guarantee or a buy/sell recommendation.

## Data retrieval issues

- None recorded.

## Notes

- Daily bars can be delayed or revised. Check timestamps and provider terms.
- Indicators summarize past prices and are not standalone decision rules.
- No transaction costs, taxes, slippage, or portfolio constraints are modeled.
