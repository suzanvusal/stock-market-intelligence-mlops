# Daily Market Intelligence — 2026-10-18

- Generated: 2026-10-18 08:41 EDT
- Purpose: educational market observation, not investment advice.
- Prices are daily adjusted OHLCV from the configured public data source.

## Watchlist overview

| Symbol | Last date | Close | Daily return | RSI (14) | RSI interpretation | SMA 20 | SMA 50 | Trend |
|---|---:|---:|---:|---:|---|---:|---:|---|
| AAPL | 2026-10-16 | 343.46 | 0.43% | 56.40 | Middle range (30-70) | 337.42 | 325.69 | Above both SMAs |
| MSFT | 2026-10-16 | 529.05 | -1.93% | 63.19 | Middle range (30-70) | 520.22 | 505.37 | Above both SMAs |
| QQQ | 2026-10-16 | 709.80 | -2.50% | 33.37 | Middle range (30-70) | 742.52 | 726.33 | Below both SMAs |
| RY.TO | 2026-10-16 | 280.01 | 0.36% | 41.12 | Middle range (30-70) | 280.10 | 285.43 | Below both SMAs |
| SHOP.TO | 2026-10-16 | 239.71 | -5.08% | 74.05 | High RSI (>70) | 220.29 | 208.27 | Above both SMAs |
| SPY | 2026-10-16 | 763.25 | -1.11% | 47.59 | Middle range (30-70) | 771.18 | 767.40 | Below both SMAs |
| VFV.TO | 2026-10-16 | 192.10 | -1.39% | 42.95 | Middle range (30-70) | 194.33 | 191.10 | Mixed / between SMAs |
| XEQT.TO | 2026-10-16 | 45.46 | -0.85% | 42.65 | Middle range (30-70) | 45.82 | 45.66 | Below both SMAs |

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
