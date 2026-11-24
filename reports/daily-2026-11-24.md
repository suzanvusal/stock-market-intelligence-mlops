# Daily Market Intelligence — 2026-11-23

- Generated: 2026-11-23 19:38 EST
- Purpose: educational market observation, not investment advice.
- Prices are daily adjusted OHLCV from the configured public data source.

## Watchlist overview

| Symbol | Last date | Close | Daily return | RSI (14) | RSI interpretation | SMA 20 | SMA 50 | Trend |
|---|---:|---:|---:|---:|---|---:|---:|---|
| AAPL | 2026-11-23 | 349.08 | 1.90% | 63.30 | Middle range (30-70) | 347.58 | 341.91 | Above both SMAs |
| MSFT | 2026-11-23 | 492.50 | 1.65% | 40.93 | Middle range (30-70) | 520.09 | 518.63 | Below both SMAs |
| QQQ | 2026-11-23 | 651.03 | 7.00% | 42.67 | Middle range (30-70) | 675.47 | 709.73 | Below both SMAs |
| RY.TO | 2026-11-23 | 270.29 | 2.75% | 36.75 | Middle range (30-70) | 283.18 | 280.84 | Below both SMAs |
| SHOP.TO | 2026-11-23 | 192.96 | 8.96% | 46.53 | Middle range (30-70) | 209.64 | 215.33 | Below both SMAs |
| SPY | 2026-11-23 | 722.29 | 4.71% | 41.15 | Middle range (30-70) | 745.65 | 759.30 | Below both SMAs |
| VFV.TO | 2026-11-23 | 184.72 | 4.78% | 46.27 | Middle range (30-70) | 187.82 | 190.87 | Below both SMAs |
| XEQT.TO | 2026-11-23 | 43.58 | 3.84% | 44.52 | Middle range (30-70) | 44.68 | 45.23 | Below both SMAs |

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

- **AAPL:** accuracy 0.488; balanced accuracy 0.487; test samples 41; test positive-target rate 0.463.
- **MSFT:** accuracy 0.512; balanced accuracy 0.500; test samples 41; test positive-target rate 0.488.
- **QQQ:** accuracy 0.561; balanced accuracy 0.530; test samples 41; test positive-target rate 0.463.
- **RY.TO:** accuracy 0.561; balanced accuracy 0.500; test samples 41; test positive-target rate 0.439.
- **SHOP.TO:** accuracy 0.463; balanced accuracy 0.500; test samples 41; test positive-target rate 0.537.
- **SPY:** accuracy 0.463; balanced accuracy 0.437; test samples 41; test positive-target rate 0.439.
- **VFV.TO:** accuracy 0.512; balanced accuracy 0.505; test samples 41; test positive-target rate 0.488.
- **XEQT.TO:** accuracy 0.610; balanced accuracy 0.622; test samples 41; test positive-target rate 0.366.

Model metrics are historical holdout results, not a forecast guarantee or a buy/sell recommendation.

## Data retrieval issues

- None recorded.

## Notes

- Daily bars can be delayed or revised. Check timestamps and provider terms.
- Indicators summarize past prices and are not standalone decision rules.
- No transaction costs, taxes, slippage, or portfolio constraints are modeled.
