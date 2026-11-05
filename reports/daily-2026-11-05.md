# Daily Market Intelligence — 2026-11-05

- Generated: 2026-11-05 15:30 EST
- Purpose: educational market observation, not investment advice.
- Prices are daily adjusted OHLCV from the configured public data source.

## Watchlist overview

| Symbol | Last date | Close | Daily return | RSI (14) | RSI interpretation | SMA 20 | SMA 50 | Trend |
|---|---:|---:|---:|---:|---|---:|---:|---|
| AAPL | 2026-11-05 | 344.84 | -1.34% | 51.02 | Middle range (30-70) | 343.13 | 335.47 | Above both SMAs |
| MSFT | 2026-11-05 | 533.90 | -3.94% | 51.91 | Middle range (30-70) | 531.53 | 516.09 | Above both SMAs |
| QQQ | 2026-11-05 | 649.68 | -6.11% | 30.80 | Middle range (30-70) | 712.53 | 722.09 | Below both SMAs |
| RY.TO | 2026-11-05 | 285.78 | -2.32% | 59.43 | Middle range (30-70) | 281.10 | 281.78 | Above both SMAs |
| SHOP.TO | 2026-11-05 | 200.71 | -5.64% | 25.49 | Low RSI (<30) | 232.98 | 213.45 | Below both SMAs |
| SPY | 2026-11-05 | 733.90 | -4.29% | 35.77 | Middle range (30-70) | 765.57 | 765.85 | Below both SMAs |
| VFV.TO | 2026-11-05 | 182.92 | -3.93% | 31.36 | Middle range (30-70) | 191.67 | 191.19 | Below both SMAs |
| XEQT.TO | 2026-11-05 | 43.98 | -3.13% | 34.93 | Middle range (30-70) | 45.30 | 45.46 | Below both SMAs |

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
- **MSFT:** accuracy 0.463; balanced accuracy 0.500; test samples 41; test positive-target rate 0.537.
- **QQQ:** accuracy 0.488; balanced accuracy 0.500; test samples 41; test positive-target rate 0.512.
- **RY.TO:** accuracy 0.488; balanced accuracy 0.458; test samples 41; test positive-target rate 0.463.
- **SHOP.TO:** accuracy 0.439; balanced accuracy 0.500; test samples 41; test positive-target rate 0.561.
- **SPY:** accuracy 0.537; balanced accuracy 0.500; test samples 41; test positive-target rate 0.463.
- **VFV.TO:** accuracy 0.488; balanced accuracy 0.499; test samples 41; test positive-target rate 0.512.
- **XEQT.TO:** accuracy 0.634; balanced accuracy 0.576; test samples 41; test positive-target rate 0.415.

Model metrics are historical holdout results, not a forecast guarantee or a buy/sell recommendation.

## Data retrieval issues

- None recorded.

## Notes

- Daily bars can be delayed or revised. Check timestamps and provider terms.
- Indicators summarize past prices and are not standalone decision rules.
- No transaction costs, taxes, slippage, or portfolio constraints are modeled.
