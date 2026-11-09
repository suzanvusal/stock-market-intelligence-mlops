# Daily Market Intelligence — 2026-11-09

- Generated: 2026-11-09 17:54 EST
- Purpose: educational market observation, not investment advice.
- Prices are daily adjusted OHLCV from the configured public data source.

## Watchlist overview

| Symbol | Last date | Close | Daily return | RSI (14) | RSI interpretation | SMA 20 | SMA 50 | Trend |
|---|---:|---:|---:|---:|---|---:|---:|---|
| AAPL | 2026-11-09 | 350.69 | 2.43% | 57.49 | Middle range (30-70) | 343.87 | 336.63 | Above both SMAs |
| MSFT | 2026-11-09 | 545.18 | 2.75% | 54.81 | Middle range (30-70) | 531.61 | 517.28 | Above both SMAs |
| QQQ | 2026-11-09 | 679.35 | 3.54% | 39.49 | Middle range (30-70) | 704.30 | 720.02 | Below both SMAs |
| RY.TO | 2026-11-09 | 288.32 | 1.46% | 62.21 | Middle range (30-70) | 282.66 | 281.87 | Above both SMAs |
| SHOP.TO | 2026-11-09 | 214.86 | 2.09% | 33.51 | Middle range (30-70) | 230.37 | 213.53 | Mixed / between SMAs |
| SPY | 2026-11-09 | 752.69 | 2.37% | 43.06 | Middle range (30-70) | 762.09 | 764.86 | Below both SMAs |
| VFV.TO | 2026-11-09 | 189.07 | 2.26% | 44.76 | Middle range (30-70) | 190.69 | 191.10 | Below both SMAs |
| XEQT.TO | 2026-11-09 | 45.36 | 2.36% | 49.39 | Middle range (30-70) | 45.19 | 45.42 | Mixed / between SMAs |

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

- **AAPL:** accuracy 0.439; balanced accuracy 0.450; test samples 41; test positive-target rate 0.512.
- **MSFT:** accuracy 0.488; balanced accuracy 0.500; test samples 41; test positive-target rate 0.512.
- **QQQ:** accuracy 0.463; balanced accuracy 0.500; test samples 41; test positive-target rate 0.537.
- **RY.TO:** accuracy 0.488; balanced accuracy 0.476; test samples 41; test positive-target rate 0.488.
- **SHOP.TO:** accuracy 0.415; balanced accuracy 0.500; test samples 41; test positive-target rate 0.585.
- **SPY:** accuracy 0.561; balanced accuracy 0.550; test samples 41; test positive-target rate 0.488.
- **VFV.TO:** accuracy 0.439; balanced accuracy 0.494; test samples 41; test positive-target rate 0.561.
- **XEQT.TO:** accuracy 0.585; balanced accuracy 0.556; test samples 41; test positive-target rate 0.463.

Model metrics are historical holdout results, not a forecast guarantee or a buy/sell recommendation.

## Data retrieval issues

- None recorded.

## Notes

- Daily bars can be delayed or revised. Check timestamps and provider terms.
- Indicators summarize past prices and are not standalone decision rules.
- No transaction costs, taxes, slippage, or portfolio constraints are modeled.
