# Daily Market Intelligence — 2026-11-12

- Generated: 2026-11-12 15:41 EST
- Purpose: educational market observation, not investment advice.
- Prices are daily adjusted OHLCV from the configured public data source.

## Watchlist overview

| Symbol | Last date | Close | Daily return | RSI (14) | RSI interpretation | SMA 20 | SMA 50 | Trend |
|---|---:|---:|---:|---:|---|---:|---:|---|
| AAPL | 2026-11-12 | 355.27 | -0.10% | 55.02 | Middle range (30-70) | 345.53 | 338.48 | Above both SMAs |
| MSFT | 2026-11-12 | 521.97 | 0.16% | 49.14 | Middle range (30-70) | 529.59 | 518.70 | Mixed / between SMAs |
| QQQ | 2026-11-12 | 687.34 | -0.44% | 45.18 | Middle range (30-70) | 696.90 | 718.44 | Below both SMAs |
| RY.TO | 2026-11-12 | 289.26 | -0.26% | 61.80 | Middle range (30-70) | 284.65 | 282.30 | Above both SMAs |
| SHOP.TO | 2026-11-12 | 209.03 | -1.67% | 35.45 | Middle range (30-70) | 224.40 | 213.90 | Below both SMAs |
| SPY | 2026-11-12 | 757.04 | -0.36% | 48.74 | Middle range (30-70) | 759.46 | 764.42 | Below both SMAs |
| VFV.TO | 2026-11-12 | 192.02 | -0.32% | 54.44 | Middle range (30-70) | 190.06 | 191.25 | Above both SMAs |
| XEQT.TO | 2026-11-12 | 45.60 | -0.58% | 56.24 | Middle range (30-70) | 45.15 | 45.42 | Above both SMAs |

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

- **AAPL:** accuracy 0.537; balanced accuracy 0.533; test samples 41; test positive-target rate 0.488.
- **MSFT:** accuracy 0.488; balanced accuracy 0.500; test samples 41; test positive-target rate 0.512.
- **QQQ:** accuracy 0.463; balanced accuracy 0.500; test samples 41; test positive-target rate 0.537.
- **RY.TO:** accuracy 0.463; balanced accuracy 0.452; test samples 41; test positive-target rate 0.488.
- **SHOP.TO:** accuracy 0.439; balanced accuracy 0.494; test samples 41; test positive-target rate 0.561.
- **SPY:** accuracy 0.512; balanced accuracy 0.521; test samples 41; test positive-target rate 0.512.
- **VFV.TO:** accuracy 0.439; balanced accuracy 0.512; test samples 41; test positive-target rate 0.585.
- **XEQT.TO:** accuracy 0.561; balanced accuracy 0.537; test samples 41; test positive-target rate 0.463.

Model metrics are historical holdout results, not a forecast guarantee or a buy/sell recommendation.

## Data retrieval issues

- None recorded.

## Notes

- Daily bars can be delayed or revised. Check timestamps and provider terms.
- Indicators summarize past prices and are not standalone decision rules.
- No transaction costs, taxes, slippage, or portfolio constraints are modeled.
