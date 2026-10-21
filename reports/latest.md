# Daily Market Intelligence — 2026-10-21

- Generated: 2026-10-21 12:50 EDT
- Purpose: educational market observation, not investment advice.
- Prices are daily adjusted OHLCV from the configured public data source.

## Watchlist overview

| Symbol | Last date | Close | Daily return | RSI (14) | RSI interpretation | SMA 20 | SMA 50 | Trend |
|---|---:|---:|---:|---:|---|---:|---:|---|
| AAPL | 2026-10-21 | 343.93 | 1.30% | 70.87 | High RSI (>70) | 337.96 | 327.70 | Above both SMAs |
| MSFT | 2026-10-21 | 532.31 | 0.08% | 62.60 | Middle range (30-70) | 525.10 | 507.18 | Above both SMAs |
| QQQ | 2026-10-21 | 726.51 | 1.24% | 41.66 | Middle range (30-70) | 739.14 | 726.37 | Mixed / between SMAs |
| RY.TO | 2026-10-21 | 283.68 | 1.25% | 55.40 | Middle range (30-70) | 279.10 | 284.55 | Mixed / between SMAs |
| SHOP.TO | 2026-10-21 | 249.57 | 2.28% | 74.09 | High RSI (>70) | 228.02 | 210.30 | Above both SMAs |
| SPY | 2026-10-21 | 773.02 | 0.52% | 58.30 | Middle range (30-70) | 770.88 | 767.35 | Above both SMAs |
| VFV.TO | 2026-10-21 | 193.33 | 0.55% | 50.72 | Middle range (30-70) | 194.41 | 191.19 | Mixed / between SMAs |
| XEQT.TO | 2026-10-21 | 45.71 | 0.61% | 51.98 | Middle range (30-70) | 45.77 | 45.64 | Mixed / between SMAs |

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

- **AAPL:** accuracy 0.488; balanced accuracy 0.537; test samples 41; test positive-target rate 0.561.
- **MSFT:** accuracy 0.439; balanced accuracy 0.500; test samples 41; test positive-target rate 0.561.
- **QQQ:** accuracy 0.439; balanced accuracy 0.500; test samples 41; test positive-target rate 0.561.
- **RY.TO:** accuracy 0.537; balanced accuracy 0.500; test samples 41; test positive-target rate 0.463.
- **SHOP.TO:** accuracy 0.415; balanced accuracy 0.538; test samples 41; test positive-target rate 0.634.
- **SPY:** accuracy 0.585; balanced accuracy 0.553; test samples 41; test positive-target rate 0.463.
- **VFV.TO:** accuracy 0.439; balanced accuracy 0.521; test samples 41; test positive-target rate 0.585.
- **XEQT.TO:** accuracy 0.512; balanced accuracy 0.500; test samples 41; test positive-target rate 0.488.

Model metrics are historical holdout results, not a forecast guarantee or a buy/sell recommendation.

## Data retrieval issues

- None recorded.

## Notes

- Daily bars can be delayed or revised. Check timestamps and provider terms.
- Indicators summarize past prices and are not standalone decision rules.
- No transaction costs, taxes, slippage, or portfolio constraints are modeled.
