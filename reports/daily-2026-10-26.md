# Daily Market Intelligence — 2026-10-26

- Generated: 2026-10-26 14:26 EDT
- Purpose: educational market observation, not investment advice.
- Prices are daily adjusted OHLCV from the configured public data source.

## Watchlist overview

| Symbol | Last date | Close | Daily return | RSI (14) | RSI interpretation | SMA 20 | SMA 50 | Trend |
|---|---:|---:|---:|---:|---|---:|---:|---|
| AAPL | 2026-10-26 | 343.07 | -1.34% | 62.71 | Middle range (30-70) | 339.14 | 330.21 | Above both SMAs |
| MSFT | 2026-10-26 | 532.01 | 1.43% | 51.61 | Middle range (30-70) | 527.84 | 509.11 | Above both SMAs |
| QQQ | 2026-10-26 | 713.41 | 1.28% | 27.75 | Low RSI (<30) | 734.08 | 725.10 | Below both SMAs |
| RY.TO | 2026-10-26 | 284.29 | 0.89% | 59.71 | Middle range (30-70) | 279.09 | 283.73 | Above both SMAs |
| SHOP.TO | 2026-10-26 | 236.37 | 0.06% | 56.11 | Middle range (30-70) | 232.89 | 211.52 | Above both SMAs |
| SPY | 2026-10-26 | 765.48 | 0.73% | 38.26 | Middle range (30-70) | 770.14 | 766.72 | Below both SMAs |
| VFV.TO | 2026-10-26 | 190.92 | 0.82% | 33.09 | Middle range (30-70) | 193.94 | 191.12 | Below both SMAs |
| XEQT.TO | 2026-10-26 | 45.13 | 0.65% | 35.70 | Middle range (30-70) | 45.65 | 45.57 | Below both SMAs |

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

- **AAPL:** accuracy 0.488; balanced accuracy 0.523; test samples 41; test positive-target rate 0.537.
- **MSFT:** accuracy 0.463; balanced accuracy 0.500; test samples 41; test positive-target rate 0.537.
- **QQQ:** accuracy 0.488; balanced accuracy 0.500; test samples 41; test positive-target rate 0.512.
- **RY.TO:** accuracy 0.463; balanced accuracy 0.404; test samples 41; test positive-target rate 0.415.
- **SHOP.TO:** accuracy 0.390; balanced accuracy 0.500; test samples 41; test positive-target rate 0.610.
- **SPY:** accuracy 0.585; balanced accuracy 0.500; test samples 41; test positive-target rate 0.415.
- **VFV.TO:** accuracy 0.512; balanced accuracy 0.545; test samples 41; test positive-target rate 0.537.
- **XEQT.TO:** accuracy 0.561; balanced accuracy 0.512; test samples 41; test positive-target rate 0.439.

Model metrics are historical holdout results, not a forecast guarantee or a buy/sell recommendation.

## Data retrieval issues

- None recorded.

## Notes

- Daily bars can be delayed or revised. Check timestamps and provider terms.
- Indicators summarize past prices and are not standalone decision rules.
- No transaction costs, taxes, slippage, or portfolio constraints are modeled.
