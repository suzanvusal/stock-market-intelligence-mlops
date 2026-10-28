# Daily Market Intelligence — 2026-10-28

- Generated: 2026-10-28 14:03 EDT
- Purpose: educational market observation, not investment advice.
- Prices are daily adjusted OHLCV from the configured public data source.

## Watchlist overview

| Symbol | Last date | Close | Daily return | RSI (14) | RSI interpretation | SMA 20 | SMA 50 | Trend |
|---|---:|---:|---:|---:|---|---:|---:|---|
| AAPL | 2026-10-28 | 345.60 | -0.43% | 57.57 | Middle range (30-70) | 340.70 | 331.77 | Above both SMAs |
| MSFT | 2026-10-28 | 527.59 | -0.70% | 53.02 | Middle range (30-70) | 529.72 | 511.09 | Mixed / between SMAs |
| QQQ | 2026-10-28 | 722.83 | 0.22% | 37.78 | Middle range (30-70) | 732.34 | 725.04 | Below both SMAs |
| RY.TO | 2026-10-28 | 285.67 | 0.07% | 74.65 | High RSI (>70) | 277.75 | 281.47 | Above both SMAs |
| SHOP.TO | 2026-10-28 | 236.48 | 1.52% | 49.92 | Middle range (30-70) | 235.63 | 212.49 | Above both SMAs |
| SPY | 2026-10-28 | 771.38 | 0.22% | 47.83 | Middle range (30-70) | 770.85 | 766.81 | Above both SMAs |
| VFV.TO | 2026-10-28 | 192.51 | 0.04% | 36.36 | Middle range (30-70) | 193.90 | 191.19 | Mixed / between SMAs |
| XEQT.TO | 2026-10-28 | 45.49 | 0.09% | 44.49 | Middle range (30-70) | 45.63 | 45.55 | Below both SMAs |

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

- **AAPL:** accuracy 0.463; balanced accuracy 0.500; test samples 41; test positive-target rate 0.537.
- **MSFT:** accuracy 0.488; balanced accuracy 0.500; test samples 41; test positive-target rate 0.512.
- **QQQ:** accuracy 0.463; balanced accuracy 0.500; test samples 41; test positive-target rate 0.537.
- **RY.TO:** accuracy 0.488; balanced accuracy 0.483; test samples 41; test positive-target rate 0.439.
- **SHOP.TO:** accuracy 0.415; balanced accuracy 0.500; test samples 41; test positive-target rate 0.585.
- **SPY:** accuracy 0.537; balanced accuracy 0.500; test samples 41; test positive-target rate 0.463.
- **VFV.TO:** accuracy 0.463; balanced accuracy 0.496; test samples 41; test positive-target rate 0.537.
- **XEQT.TO:** accuracy 0.512; balanced accuracy 0.481; test samples 41; test positive-target rate 0.463.

Model metrics are historical holdout results, not a forecast guarantee or a buy/sell recommendation.

## Data retrieval issues

- None recorded.

## Notes

- Daily bars can be delayed or revised. Check timestamps and provider terms.
- Indicators summarize past prices and are not standalone decision rules.
- No transaction costs, taxes, slippage, or portfolio constraints are modeled.
