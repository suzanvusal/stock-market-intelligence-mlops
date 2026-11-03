# Daily Market Intelligence — 2026-11-03

- Generated: 2026-11-03 14:59 EST
- Purpose: educational market observation, not investment advice.
- Prices are daily adjusted OHLCV from the configured public data source.

## Watchlist overview

| Symbol | Last date | Close | Daily return | RSI (14) | RSI interpretation | SMA 20 | SMA 50 | Trend |
|---|---:|---:|---:|---:|---|---:|---:|---|
| AAPL | 2026-11-03 | 329.95 | -2.47% | 36.97 | Middle range (30-70) | 342.17 | 334.01 | Below both SMAs |
| MSFT | 2026-11-03 | 522.40 | 3.01% | 43.54 | Middle range (30-70) | 529.73 | 514.09 | Mixed / between SMAs |
| QQQ | 2026-11-03 | 684.48 | 0.50% | 32.34 | Middle range (30-70) | 720.67 | 723.65 | Below both SMAs |
| RY.TO | 2026-11-03 | 284.87 | -0.47% | 67.36 | Middle range (30-70) | 279.58 | 281.52 | Above both SMAs |
| SHOP.TO | 2026-11-03 | 201.92 | -7.22% | 20.24 | Low RSI (<30) | 235.91 | 213.63 | Below both SMAs |
| SPY | 2026-11-03 | 754.04 | 0.26% | 38.59 | Middle range (30-70) | 768.08 | 766.39 | Below both SMAs |
| VFV.TO | 2026-11-03 | 187.82 | 0.35% | 29.64 | Low RSI (<30) | 192.70 | 191.24 | Below both SMAs |
| XEQT.TO | 2026-11-03 | 44.62 | -0.16% | 35.25 | Middle range (30-70) | 45.43 | 45.50 | Below both SMAs |

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

- **AAPL:** accuracy 0.488; balanced accuracy 0.500; test samples 41; test positive-target rate 0.512.
- **MSFT:** accuracy 0.488; balanced accuracy 0.500; test samples 41; test positive-target rate 0.512.
- **QQQ:** accuracy 0.512; balanced accuracy 0.500; test samples 41; test positive-target rate 0.488.
- **RY.TO:** accuracy 0.512; balanced accuracy 0.493; test samples 41; test positive-target rate 0.439.
- **SHOP.TO:** accuracy 0.463; balanced accuracy 0.500; test samples 41; test positive-target rate 0.537.
- **SPY:** accuracy 0.561; balanced accuracy 0.500; test samples 41; test positive-target rate 0.439.
- **VFV.TO:** accuracy 0.512; balanced accuracy 0.501; test samples 41; test positive-target rate 0.488.
- **XEQT.TO:** accuracy 0.585; balanced accuracy 0.517; test samples 41; test positive-target rate 0.415.

Model metrics are historical holdout results, not a forecast guarantee or a buy/sell recommendation.

## Data retrieval issues

- None recorded.

## Notes

- Daily bars can be delayed or revised. Check timestamps and provider terms.
- Indicators summarize past prices and are not standalone decision rules.
- No transaction costs, taxes, slippage, or portfolio constraints are modeled.
