# Daily Market Intelligence — 2026-10-23

- Generated: 2026-10-23 12:42 EDT
- Purpose: educational market observation, not investment advice.
- Prices are daily adjusted OHLCV from the configured public data source.

## Watchlist overview

| Symbol | Last date | Close | Daily return | RSI (14) | RSI interpretation | SMA 20 | SMA 50 | Trend |
|---|---:|---:|---:|---:|---|---:|---:|---|
| AAPL | 2026-10-23 | 347.01 | -0.35% | 70.79 | High RSI (>70) | 338.87 | 329.45 | Above both SMAs |
| MSFT | 2026-10-23 | 525.21 | 0.79% | 50.02 | Middle range (30-70) | 526.74 | 508.37 | Mixed / between SMAs |
| QQQ | 2026-10-23 | 707.39 | 0.41% | 25.89 | Low RSI (<30) | 735.38 | 725.50 | Below both SMAs |
| RY.TO | 2026-10-23 | 280.72 | -0.73% | 52.63 | Middle range (30-70) | 279.10 | 284.01 | Mixed / between SMAs |
| SHOP.TO | 2026-10-23 | 236.81 | 0.17% | 63.17 | Middle range (30-70) | 231.16 | 211.23 | Above both SMAs |
| SPY | 2026-10-23 | 762.48 | -0.19% | 38.61 | Middle range (30-70) | 770.28 | 766.95 | Below both SMAs |
| VFV.TO | 2026-10-23 | 189.95 | -0.25% | 33.84 | Middle range (30-70) | 194.13 | 191.16 | Below both SMAs |
| XEQT.TO | 2026-10-23 | 44.90 | -0.33% | 35.58 | Middle range (30-70) | 45.69 | 45.60 | Below both SMAs |

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

- **AAPL:** accuracy 0.488; balanced accuracy 0.543; test samples 41; test positive-target rate 0.561.
- **MSFT:** accuracy 0.488; balanced accuracy 0.523; test samples 41; test positive-target rate 0.537.
- **QQQ:** accuracy 0.463; balanced accuracy 0.500; test samples 41; test positive-target rate 0.537.
- **RY.TO:** accuracy 0.415; balanced accuracy 0.380; test samples 41; test positive-target rate 0.415.
- **SHOP.TO:** accuracy 0.415; balanced accuracy 0.520; test samples 41; test positive-target rate 0.610.
- **SPY:** accuracy 0.585; balanced accuracy 0.500; test samples 41; test positive-target rate 0.415.
- **VFV.TO:** accuracy 0.512; balanced accuracy 0.545; test samples 41; test positive-target rate 0.537.
- **XEQT.TO:** accuracy 0.537; balanced accuracy 0.478; test samples 41; test positive-target rate 0.439.

Model metrics are historical holdout results, not a forecast guarantee or a buy/sell recommendation.

## Data retrieval issues

- None recorded.

## Notes

- Daily bars can be delayed or revised. Check timestamps and provider terms.
- Indicators summarize past prices and are not standalone decision rules.
- No transaction costs, taxes, slippage, or portfolio constraints are modeled.
