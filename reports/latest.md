# Daily Market Intelligence — 2026-11-24

- Generated: 2026-11-24 17:56 EST
- Purpose: educational market observation, not investment advice.
- Prices are daily adjusted OHLCV from the configured public data source.

## Watchlist overview

| Symbol | Last date | Close | Daily return | RSI (14) | RSI interpretation | SMA 20 | SMA 50 | Trend |
|---|---:|---:|---:|---:|---|---:|---:|---|
| AAPL | 2026-11-24 | 354.07 | 1.43% | 54.56 | Middle range (30-70) | 347.94 | 342.37 | Above both SMAs |
| MSFT | 2026-11-24 | 496.13 | 0.74% | 25.68 | Low RSI (<30) | 518.38 | 518.63 | Below both SMAs |
| QQQ | 2026-11-24 | 638.10 | -1.99% | 38.78 | Middle range (30-70) | 671.31 | 708.42 | Below both SMAs |
| RY.TO | 2026-11-24 | 269.64 | -0.24% | 27.35 | Low RSI (<30) | 282.39 | 280.57 | Below both SMAs |
| SHOP.TO | 2026-11-24 | 188.85 | -2.13% | 37.55 | Middle range (30-70) | 207.44 | 215.38 | Below both SMAs |
| SPY | 2026-11-24 | 718.78 | -0.49% | 36.05 | Middle range (30-70) | 743.11 | 758.56 | Below both SMAs |
| VFV.TO | 2026-11-24 | 182.31 | -1.30% | 41.00 | Middle range (30-70) | 187.31 | 190.76 | Below both SMAs |
| XEQT.TO | 2026-11-24 | 43.17 | -0.94% | 38.18 | Middle range (30-70) | 44.57 | 45.20 | Below both SMAs |

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

- **AAPL:** accuracy 0.463; balanced accuracy 0.458; test samples 41; test positive-target rate 0.488.
- **MSFT:** accuracy 0.488; balanced accuracy 0.500; test samples 41; test positive-target rate 0.512.
- **QQQ:** accuracy 0.561; balanced accuracy 0.530; test samples 41; test positive-target rate 0.463.
- **RY.TO:** accuracy 0.585; balanced accuracy 0.500; test samples 41; test positive-target rate 0.415.
- **SHOP.TO:** accuracy 0.439; balanced accuracy 0.474; test samples 41; test positive-target rate 0.537.
- **SPY:** accuracy 0.439; balanced accuracy 0.415; test samples 41; test positive-target rate 0.439.
- **VFV.TO:** accuracy 0.463; balanced accuracy 0.450; test samples 41; test positive-target rate 0.463.
- **XEQT.TO:** accuracy 0.561; balanced accuracy 0.598; test samples 41; test positive-target rate 0.342.

Model metrics are historical holdout results, not a forecast guarantee or a buy/sell recommendation.

## Data retrieval issues

- None recorded.

## Notes

- Daily bars can be delayed or revised. Check timestamps and provider terms.
- Indicators summarize past prices and are not standalone decision rules.
- No transaction costs, taxes, slippage, or portfolio constraints are modeled.
