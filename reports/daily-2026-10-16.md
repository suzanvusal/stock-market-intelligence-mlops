# Daily Market Intelligence — 2026-10-16

- Generated: 2026-10-16 12:17 EDT
- Purpose: educational market observation, not investment advice.
- Prices are daily adjusted OHLCV from the configured public data source.

## Watchlist overview

| Symbol | Last date | Close | Daily return | RSI (14) | RSI interpretation | SMA 20 | SMA 50 | Trend |
|---|---:|---:|---:|---:|---|---:|---:|---|
| AAPL | 2026-10-16 | 344.75 | 0.80% | 57.78 | Middle range (30-70) | 337.49 | 325.72 | Above both SMAs |
| MSFT | 2026-10-16 | 528.88 | -1.96% | 63.05 | Middle range (30-70) | 520.21 | 505.36 | Above both SMAs |
| QQQ | 2026-10-16 | 716.99 | -1.51% | 36.65 | Middle range (30-70) | 742.88 | 726.47 | Below both SMAs |
| RY.TO | 2026-10-16 | 280.09 | 0.39% | 41.27 | Middle range (30-70) | 280.10 | 285.43 | Below both SMAs |
| SHOP.TO | 2026-10-16 | 248.65 | -1.54% | 83.35 | High RSI (>70) | 220.73 | 208.45 | Above both SMAs |
| SPY | 2026-10-16 | 767.50 | -0.56% | 52.11 | Middle range (30-70) | 771.40 | 767.49 | Mixed / between SMAs |
| VFV.TO | 2026-10-16 | 193.33 | -0.76% | 46.94 | Middle range (30-70) | 194.39 | 191.13 | Mixed / between SMAs |
| XEQT.TO | 2026-10-16 | 45.67 | -0.39% | 45.40 | Middle range (30-70) | 45.83 | 45.67 | Mixed / between SMAs |

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

- **AAPL:** accuracy 0.463; balanced accuracy 0.504; test samples 41; test positive-target rate 0.561.
- **MSFT:** accuracy 0.439; balanced accuracy 0.500; test samples 41; test positive-target rate 0.561.
- **QQQ:** accuracy 0.463; balanced accuracy 0.500; test samples 41; test positive-target rate 0.537.
- **RY.TO:** accuracy 0.342; balanced accuracy 0.369; test samples 41; test positive-target rate 0.415.
- **SHOP.TO:** accuracy 0.415; balanced accuracy 0.520; test samples 41; test positive-target rate 0.610.
- **SPY:** accuracy 0.634; balanced accuracy 0.559; test samples 41; test positive-target rate 0.415.
- **VFV.TO:** accuracy 0.463; balanced accuracy 0.522; test samples 41; test positive-target rate 0.561.
- **XEQT.TO:** accuracy 0.561; balanced accuracy 0.526; test samples 41; test positive-target rate 0.463.

Model metrics are historical holdout results, not a forecast guarantee or a buy/sell recommendation.

## Data retrieval issues

- None recorded.

## Notes

- Daily bars can be delayed or revised. Check timestamps and provider terms.
- Indicators summarize past prices and are not standalone decision rules.
- No transaction costs, taxes, slippage, or portfolio constraints are modeled.
