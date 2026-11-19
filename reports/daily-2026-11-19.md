# Daily Market Intelligence — 2026-11-19

- Generated: 2026-11-19 16:14 EST
- Purpose: educational market observation, not investment advice.
- Prices are daily adjusted OHLCV from the configured public data source.

## Watchlist overview

| Symbol | Last date | Close | Daily return | RSI (14) | RSI interpretation | SMA 20 | SMA 50 | Trend |
|---|---:|---:|---:|---:|---|---:|---:|---|
| AAPL | 2026-11-19 | 349.21 | -0.92% | 53.72 | Middle range (30-70) | 347.55 | 341.37 | Above both SMAs |
| MSFT | 2026-11-19 | 498.30 | -1.97% | 42.61 | Middle range (30-70) | 524.96 | 520.06 | Below both SMAs |
| QQQ | 2026-11-19 | 645.04 | -2.19% | 36.48 | Middle range (30-70) | 683.33 | 713.00 | Below both SMAs |
| RY.TO | 2026-11-19 | 269.45 | -1.03% | 34.44 | Middle range (30-70) | 284.73 | 281.51 | Below both SMAs |
| SHOP.TO | 2026-11-19 | 189.35 | -5.22% | 33.89 | Middle range (30-70) | 214.75 | 215.00 | Below both SMAs |
| SPY | 2026-11-19 | 715.83 | -1.97% | 34.47 | Middle range (30-70) | 751.31 | 761.48 | Below both SMAs |
| VFV.TO | 2026-11-19 | 182.95 | -1.75% | 42.20 | Middle range (30-70) | 188.78 | 191.13 | Below both SMAs |
| XEQT.TO | 2026-11-19 | 43.28 | -1.66% | 40.20 | Middle range (30-70) | 44.90 | 45.32 | Below both SMAs |

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

- **AAPL:** accuracy 0.561; balanced accuracy 0.562; test samples 41; test positive-target rate 0.463.
- **MSFT:** accuracy 0.512; balanced accuracy 0.500; test samples 41; test positive-target rate 0.488.
- **QQQ:** accuracy 0.561; balanced accuracy 0.530; test samples 41; test positive-target rate 0.463.
- **RY.TO:** accuracy 0.561; balanced accuracy 0.500; test samples 41; test positive-target rate 0.439.
- **SHOP.TO:** accuracy 0.463; balanced accuracy 0.500; test samples 41; test positive-target rate 0.537.
- **SPY:** accuracy 0.463; balanced accuracy 0.431; test samples 41; test positive-target rate 0.439.
- **VFV.TO:** accuracy 0.537; balanced accuracy 0.529; test samples 41; test positive-target rate 0.488.
- **XEQT.TO:** accuracy 0.634; balanced accuracy 0.627; test samples 41; test positive-target rate 0.366.

Model metrics are historical holdout results, not a forecast guarantee or a buy/sell recommendation.

## Data retrieval issues

- None recorded.

## Notes

- Daily bars can be delayed or revised. Check timestamps and provider terms.
- Indicators summarize past prices and are not standalone decision rules.
- No transaction costs, taxes, slippage, or portfolio constraints are modeled.
