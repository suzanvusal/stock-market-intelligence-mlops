# Daily Market Intelligence — 2026-11-17

- Generated: 2026-11-17 16:34 EST
- Purpose: educational market observation, not investment advice.
- Prices are daily adjusted OHLCV from the configured public data source.

## Watchlist overview

| Symbol | Last date | Close | Daily return | RSI (14) | RSI interpretation | SMA 20 | SMA 50 | Trend |
|---|---:|---:|---:|---:|---|---:|---:|---|
| AAPL | 2026-11-17 | 351.91 | -0.25% | 55.90 | Middle range (30-70) | 347.05 | 340.17 | Above both SMAs |
| MSFT | 2026-11-17 | 506.24 | -2.27% | 42.10 | Middle range (30-70) | 527.33 | 519.61 | Below both SMAs |
| QQQ | 2026-11-17 | 656.95 | -0.73% | 31.56 | Middle range (30-70) | 689.58 | 715.38 | Below both SMAs |
| RY.TO | 2026-11-17 | 280.99 | -1.65% | 43.40 | Middle range (30-70) | 285.78 | 282.08 | Below both SMAs |
| SHOP.TO | 2026-11-17 | 202.83 | -4.07% | 33.33 | Middle range (30-70) | 219.36 | 214.42 | Below both SMAs |
| SPY | 2026-11-17 | 732.44 | -1.01% | 34.48 | Middle range (30-70) | 755.86 | 762.89 | Below both SMAs |
| VFV.TO | 2026-11-17 | 186.14 | -1.08% | 40.55 | Middle range (30-70) | 189.51 | 191.24 | Below both SMAs |
| XEQT.TO | 2026-11-17 | 44.34 | -1.16% | 41.77 | Middle range (30-70) | 45.07 | 45.38 | Below both SMAs |

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

- **AAPL:** accuracy 0.488; balanced accuracy 0.494; test samples 41; test positive-target rate 0.463.
- **MSFT:** accuracy 0.512; balanced accuracy 0.500; test samples 41; test positive-target rate 0.488.
- **QQQ:** accuracy 0.561; balanced accuracy 0.526; test samples 41; test positive-target rate 0.463.
- **RY.TO:** accuracy 0.537; balanced accuracy 0.500; test samples 41; test positive-target rate 0.463.
- **SHOP.TO:** accuracy 0.439; balanced accuracy 0.521; test samples 41; test positive-target rate 0.585.
- **SPY:** accuracy 0.512; balanced accuracy 0.475; test samples 41; test positive-target rate 0.439.
- **VFV.TO:** accuracy 0.561; balanced accuracy 0.570; test samples 41; test positive-target rate 0.512.
- **XEQT.TO:** accuracy 0.561; balanced accuracy 0.531; test samples 41; test positive-target rate 0.415.

Model metrics are historical holdout results, not a forecast guarantee or a buy/sell recommendation.

## Data retrieval issues

- None recorded.

## Notes

- Daily bars can be delayed or revised. Check timestamps and provider terms.
- Indicators summarize past prices and are not standalone decision rules.
- No transaction costs, taxes, slippage, or portfolio constraints are modeled.
