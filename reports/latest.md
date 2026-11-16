# Daily Market Intelligence — 2026-11-16

- Generated: 2026-11-16 17:46 EST
- Purpose: educational market observation, not investment advice.
- Prices are daily adjusted OHLCV from the configured public data source.

## Watchlist overview

| Symbol | Last date | Close | Daily return | RSI (14) | RSI interpretation | SMA 20 | SMA 50 | Trend |
|---|---:|---:|---:|---:|---|---:|---:|---|
| AAPL | 2026-11-16 | 352.78 | -0.98% | 54.07 | Middle range (30-70) | 346.42 | 339.45 | Above both SMAs |
| MSFT | 2026-11-16 | 517.99 | -1.12% | 45.41 | Middle range (30-70) | 528.61 | 519.36 | Below both SMAs |
| QQQ | 2026-11-16 | 661.75 | -2.67% | 33.99 | Middle range (30-70) | 692.62 | 716.59 | Below both SMAs |
| RY.TO | 2026-11-16 | 285.69 | -0.93% | 50.31 | Middle range (30-70) | 285.66 | 282.25 | Above both SMAs |
| SHOP.TO | 2026-11-16 | 211.43 | 0.81% | 38.29 | Middle range (30-70) | 221.42 | 214.38 | Below both SMAs |
| SPY | 2026-11-16 | 739.95 | -1.91% | 37.98 | Middle range (30-70) | 757.69 | 763.52 | Below both SMAs |
| VFV.TO | 2026-11-16 | 188.17 | -1.69% | 43.03 | Middle range (30-70) | 189.81 | 191.30 | Below both SMAs |
| XEQT.TO | 2026-11-16 | 44.86 | -1.45% | 45.22 | Middle range (30-70) | 45.13 | 45.41 | Below both SMAs |

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

- **AAPL:** accuracy 0.512; balanced accuracy 0.507; test samples 41; test positive-target rate 0.488.
- **MSFT:** accuracy 0.488; balanced accuracy 0.500; test samples 41; test positive-target rate 0.512.
- **QQQ:** accuracy 0.512; balanced accuracy 0.500; test samples 41; test positive-target rate 0.488.
- **RY.TO:** accuracy 0.537; balanced accuracy 0.500; test samples 41; test positive-target rate 0.463.
- **SHOP.TO:** accuracy 0.415; balanced accuracy 0.491; test samples 41; test positive-target rate 0.585.
- **SPY:** accuracy 0.512; balanced accuracy 0.488; test samples 41; test positive-target rate 0.463.
- **VFV.TO:** accuracy 0.488; balanced accuracy 0.519; test samples 41; test positive-target rate 0.537.
- **XEQT.TO:** accuracy 0.610; balanced accuracy 0.581; test samples 41; test positive-target rate 0.415.

Model metrics are historical holdout results, not a forecast guarantee or a buy/sell recommendation.

## Data retrieval issues

- None recorded.

## Notes

- Daily bars can be delayed or revised. Check timestamps and provider terms.
- Indicators summarize past prices and are not standalone decision rules.
- No transaction costs, taxes, slippage, or portfolio constraints are modeled.
