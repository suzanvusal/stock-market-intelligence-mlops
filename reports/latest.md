# Daily Market Intelligence — 2026-11-13

- Generated: 2026-11-13 15:23 EST
- Purpose: educational market observation, not investment advice.
- Prices are daily adjusted OHLCV from the configured public data source.

## Watchlist overview

| Symbol | Last date | Close | Daily return | RSI (14) | RSI interpretation | SMA 20 | SMA 50 | Trend |
|---|---:|---:|---:|---:|---|---:|---:|---|
| AAPL | 2026-11-13 | 356.82 | 0.55% | 58.99 | Middle range (30-70) | 345.94 | 338.80 | Above both SMAs |
| MSFT | 2026-11-13 | 524.89 | 0.36% | 47.28 | Middle range (30-70) | 529.44 | 519.02 | Mixed / between SMAs |
| QQQ | 2026-11-13 | 679.64 | -1.24% | 40.80 | Middle range (30-70) | 695.44 | 717.71 | Below both SMAs |
| RY.TO | 2026-11-13 | 288.24 | -0.40% | 55.53 | Middle range (30-70) | 285.15 | 282.35 | Above both SMAs |
| SHOP.TO | 2026-11-13 | 210.43 | 0.49% | 36.41 | Middle range (30-70) | 222.96 | 214.18 | Below both SMAs |
| SPY | 2026-11-13 | 753.51 | -0.48% | 44.81 | Middle range (30-70) | 758.98 | 764.07 | Below both SMAs |
| VFV.TO | 2026-11-13 | 191.27 | -0.41% | 50.65 | Middle range (30-70) | 190.02 | 191.31 | Mixed / between SMAs |
| XEQT.TO | 2026-11-13 | 45.51 | -0.15% | 53.41 | Middle range (30-70) | 45.15 | 45.43 | Above both SMAs |

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

- **AAPL:** accuracy 0.512; balanced accuracy 0.514; test samples 41; test positive-target rate 0.488.
- **MSFT:** accuracy 0.488; balanced accuracy 0.500; test samples 41; test positive-target rate 0.512.
- **QQQ:** accuracy 0.488; balanced accuracy 0.500; test samples 41; test positive-target rate 0.512.
- **RY.TO:** accuracy 0.512; balanced accuracy 0.500; test samples 41; test positive-target rate 0.488.
- **SHOP.TO:** accuracy 0.439; balanced accuracy 0.488; test samples 41; test positive-target rate 0.561.
- **SPY:** accuracy 0.512; balanced accuracy 0.504; test samples 41; test positive-target rate 0.488.
- **VFV.TO:** accuracy 0.463; balanced accuracy 0.516; test samples 41; test positive-target rate 0.561.
- **XEQT.TO:** accuracy 0.610; balanced accuracy 0.586; test samples 41; test positive-target rate 0.439.

Model metrics are historical holdout results, not a forecast guarantee or a buy/sell recommendation.

## Data retrieval issues

- None recorded.

## Notes

- Daily bars can be delayed or revised. Check timestamps and provider terms.
- Indicators summarize past prices and are not standalone decision rules.
- No transaction costs, taxes, slippage, or portfolio constraints are modeled.
