# Daily Market Intelligence — 2026-11-11

- Generated: 2026-11-11 15:03 EST
- Purpose: educational market observation, not investment advice.
- Prices are daily adjusted OHLCV from the configured public data source.

## Watchlist overview

| Symbol | Last date | Close | Daily return | RSI (14) | RSI interpretation | SMA 20 | SMA 50 | Trend |
|---|---:|---:|---:|---:|---|---:|---:|---|
| AAPL | 2026-11-11 | 354.57 | 1.74% | 54.28 | Middle range (30-70) | 344.81 | 337.86 | Above both SMAs |
| MSFT | 2026-11-11 | 520.04 | -2.46% | 49.66 | Middle range (30-70) | 530.41 | 518.18 | Mixed / between SMAs |
| QQQ | 2026-11-11 | 692.24 | 2.59% | 46.52 | Middle range (30-70) | 699.03 | 718.90 | Below both SMAs |
| RY.TO | 2026-11-11 | 290.39 | 0.98% | 61.76 | Middle range (30-70) | 284.07 | 282.15 | Above both SMAs |
| SHOP.TO | 2026-11-11 | 212.97 | 2.33% | 37.05 | Middle range (30-70) | 226.60 | 213.61 | Below both SMAs |
| SPY | 2026-11-11 | 760.61 | 1.43% | 48.58 | Middle range (30-70) | 760.24 | 764.56 | Mixed / between SMAs |
| VFV.TO | 2026-11-11 | 192.82 | 1.84% | 53.94 | Middle range (30-70) | 190.21 | 191.17 | Above both SMAs |
| XEQT.TO | 2026-11-11 | 45.88 | 1.33% | 56.91 | Middle range (30-70) | 45.16 | 45.42 | Above both SMAs |

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

- **AAPL:** accuracy 0.463; balanced accuracy 0.471; test samples 41; test positive-target rate 0.512.
- **MSFT:** accuracy 0.512; balanced accuracy 0.500; test samples 41; test positive-target rate 0.488.
- **QQQ:** accuracy 0.439; balanced accuracy 0.500; test samples 41; test positive-target rate 0.561.
- **RY.TO:** accuracy 0.463; balanced accuracy 0.452; test samples 41; test positive-target rate 0.488.
- **SHOP.TO:** accuracy 0.463; balanced accuracy 0.516; test samples 41; test positive-target rate 0.561.
- **SPY:** accuracy 0.537; balanced accuracy 0.546; test samples 41; test positive-target rate 0.512.
- **VFV.TO:** accuracy 0.439; balanced accuracy 0.512; test samples 41; test positive-target rate 0.585.
- **XEQT.TO:** accuracy 0.585; balanced accuracy 0.563; test samples 41; test positive-target rate 0.463.

Model metrics are historical holdout results, not a forecast guarantee or a buy/sell recommendation.

## Data retrieval issues

- None recorded.

## Notes

- Daily bars can be delayed or revised. Check timestamps and provider terms.
- Indicators summarize past prices and are not standalone decision rules.
- No transaction costs, taxes, slippage, or portfolio constraints are modeled.
