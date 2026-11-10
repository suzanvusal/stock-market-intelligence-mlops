# Daily Market Intelligence — 2026-11-10

- Generated: 2026-11-10 15:20 EST
- Purpose: educational market observation, not investment advice.
- Prices are daily adjusted OHLCV from the configured public data source.

## Watchlist overview

| Symbol | Last date | Close | Daily return | RSI (14) | RSI interpretation | SMA 20 | SMA 50 | Trend |
|---|---:|---:|---:|---:|---|---:|---:|---|
| AAPL | 2026-11-10 | 348.12 | -0.73% | 52.84 | Middle range (30-70) | 344.21 | 337.26 | Above both SMAs |
| MSFT | 2026-11-10 | 533.20 | -2.20% | 50.08 | Middle range (30-70) | 531.10 | 517.80 | Above both SMAs |
| QQQ | 2026-11-10 | 673.08 | -0.92% | 35.59 | Middle range (30-70) | 700.78 | 719.16 | Below both SMAs |
| RY.TO | 2026-11-10 | 287.82 | -0.18% | 57.93 | Middle range (30-70) | 283.28 | 281.98 | Above both SMAs |
| SHOP.TO | 2026-11-10 | 205.91 | -4.17% | 29.76 | Low RSI (<30) | 228.11 | 213.40 | Below both SMAs |
| SPY | 2026-11-10 | 749.10 | -0.48% | 39.79 | Middle range (30-70) | 760.65 | 764.53 | Below both SMAs |
| VFV.TO | 2026-11-10 | 189.07 | 0.00% | 42.88 | Middle range (30-70) | 190.30 | 191.08 | Below both SMAs |
| XEQT.TO | 2026-11-10 | 45.26 | -0.23% | 46.69 | Middle range (30-70) | 45.15 | 45.41 | Mixed / between SMAs |

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

- **AAPL:** accuracy 0.488; balanced accuracy 0.483; test samples 41; test positive-target rate 0.488.
- **MSFT:** accuracy 0.512; balanced accuracy 0.500; test samples 41; test positive-target rate 0.488.
- **QQQ:** accuracy 0.463; balanced accuracy 0.500; test samples 41; test positive-target rate 0.537.
- **RY.TO:** accuracy 0.488; balanced accuracy 0.455; test samples 41; test positive-target rate 0.463.
- **SHOP.TO:** accuracy 0.439; balanced accuracy 0.500; test samples 41; test positive-target rate 0.561.
- **SPY:** accuracy 0.537; balanced accuracy 0.526; test samples 41; test positive-target rate 0.488.
- **VFV.TO:** accuracy 0.488; balanced accuracy 0.519; test samples 41; test positive-target rate 0.537.
- **XEQT.TO:** accuracy 0.634; balanced accuracy 0.601; test samples 41; test positive-target rate 0.439.

Model metrics are historical holdout results, not a forecast guarantee or a buy/sell recommendation.

## Data retrieval issues

- None recorded.

## Notes

- Daily bars can be delayed or revised. Check timestamps and provider terms.
- Indicators summarize past prices and are not standalone decision rules.
- No transaction costs, taxes, slippage, or portfolio constraints are modeled.
