# Daily Market Intelligence — 2026-11-04

- Generated: 2026-11-04 15:20 EST
- Purpose: educational market observation, not investment advice.
- Prices are daily adjusted OHLCV from the configured public data source.

## Watchlist overview

| Symbol | Last date | Close | Daily return | RSI (14) | RSI interpretation | SMA 20 | SMA 50 | Trend |
|---|---:|---:|---:|---:|---|---:|---:|---|
| AAPL | 2026-11-04 | 352.51 | 6.21% | 57.77 | Middle range (30-70) | 343.06 | 334.90 | Above both SMAs |
| MSFT | 2026-11-04 | 558.43 | 7.19% | 58.06 | Middle range (30-70) | 531.10 | 515.40 | Above both SMAs |
| QQQ | 2026-11-04 | 693.35 | 1.18% | 37.06 | Middle range (30-70) | 717.49 | 723.33 | Below both SMAs |
| RY.TO | 2026-11-04 | 292.85 | 2.60% | 72.67 | High RSI (>70) | 280.38 | 281.77 | Above both SMAs |
| SHOP.TO | 2026-11-04 | 214.39 | 7.09% | 26.76 | Low RSI (<30) | 234.85 | 213.73 | Mixed / between SMAs |
| SPY | 2026-11-04 | 767.89 | 1.79% | 47.55 | Middle range (30-70) | 767.63 | 766.47 | Above both SMAs |
| VFV.TO | 2026-11-04 | 190.83 | 1.47% | 40.19 | Middle range (30-70) | 192.41 | 191.30 | Below both SMAs |
| XEQT.TO | 2026-11-04 | 45.44 | 1.77% | 44.77 | Middle range (30-70) | 45.40 | 45.50 | Mixed / between SMAs |

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
- **RY.TO:** accuracy 0.561; balanced accuracy 0.537; test samples 41; test positive-target rate 0.463.
- **SHOP.TO:** accuracy 0.439; balanced accuracy 0.500; test samples 41; test positive-target rate 0.561.
- **SPY:** accuracy 0.537; balanced accuracy 0.500; test samples 41; test positive-target rate 0.463.
- **VFV.TO:** accuracy 0.488; balanced accuracy 0.499; test samples 41; test positive-target rate 0.512.
- **XEQT.TO:** accuracy 0.707; balanced accuracy 0.664; test samples 41; test positive-target rate 0.415.

Model metrics are historical holdout results, not a forecast guarantee or a buy/sell recommendation.

## Data retrieval issues

- None recorded.

## Notes

- Daily bars can be delayed or revised. Check timestamps and provider terms.
- Indicators summarize past prices and are not standalone decision rules.
- No transaction costs, taxes, slippage, or portfolio constraints are modeled.
