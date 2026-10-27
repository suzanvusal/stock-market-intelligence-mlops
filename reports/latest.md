# Daily Market Intelligence — 2026-10-27

- Generated: 2026-10-27 13:42 EDT
- Purpose: educational market observation, not investment advice.
- Prices are daily adjusted OHLCV from the configured public data source.

## Watchlist overview

| Symbol | Last date | Close | Daily return | RSI (14) | RSI interpretation | SMA 20 | SMA 50 | Trend |
|---|---:|---:|---:|---:|---|---:|---:|---|
| AAPL | 2026-10-27 | 346.00 | 0.61% | 63.20 | Middle range (30-70) | 340.01 | 331.03 | Above both SMAs |
| MSFT | 2026-10-27 | 532.23 | -0.07% | 51.46 | Middle range (30-70) | 529.03 | 510.17 | Above both SMAs |
| QQQ | 2026-10-27 | 721.00 | 1.24% | 33.24 | Middle range (30-70) | 733.17 | 724.92 | Below both SMAs |
| RY.TO | 2026-10-27 | 285.22 | 0.34% | 60.98 | Middle range (30-70) | 277.53 | 281.72 | Above both SMAs |
| SHOP.TO | 2026-10-27 | 233.62 | -0.98% | 49.91 | Middle range (30-70) | 234.34 | 211.90 | Mixed / between SMAs |
| SPY | 2026-10-27 | 769.64 | 0.56% | 43.71 | Middle range (30-70) | 770.41 | 766.69 | Mixed / between SMAs |
| VFV.TO | 2026-10-27 | 192.31 | 0.74% | 36.58 | Middle range (30-70) | 193.91 | 191.14 | Mixed / between SMAs |
| XEQT.TO | 2026-10-27 | 45.42 | 0.69% | 40.37 | Middle range (30-70) | 45.63 | 45.56 | Below both SMAs |

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

- **AAPL:** accuracy 0.463; balanced accuracy 0.489; test samples 41; test positive-target rate 0.537.
- **MSFT:** accuracy 0.488; balanced accuracy 0.500; test samples 41; test positive-target rate 0.512.
- **QQQ:** accuracy 0.463; balanced accuracy 0.500; test samples 41; test positive-target rate 0.537.
- **RY.TO:** accuracy 0.561; balanced accuracy 0.500; test samples 41; test positive-target rate 0.439.
- **SHOP.TO:** accuracy 0.439; balanced accuracy 0.500; test samples 41; test positive-target rate 0.561.
- **SPY:** accuracy 0.561; balanced accuracy 0.500; test samples 41; test positive-target rate 0.439.
- **VFV.TO:** accuracy 0.488; balanced accuracy 0.523; test samples 41; test positive-target rate 0.537.
- **XEQT.TO:** accuracy 0.610; balanced accuracy 0.586; test samples 41; test positive-target rate 0.439.

Model metrics are historical holdout results, not a forecast guarantee or a buy/sell recommendation.

## Data retrieval issues

- None recorded.

## Notes

- Daily bars can be delayed or revised. Check timestamps and provider terms.
- Indicators summarize past prices and are not standalone decision rules.
- No transaction costs, taxes, slippage, or portfolio constraints are modeled.
