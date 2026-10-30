# Daily Market Intelligence — 2026-10-30

- Generated: 2026-10-30 13:50 EDT
- Purpose: educational market observation, not investment advice.
- Prices are daily adjusted OHLCV from the configured public data source.

## Watchlist overview

| Symbol | Last date | Close | Daily return | RSI (14) | RSI interpretation | SMA 20 | SMA 50 | Trend |
|---|---:|---:|---:|---:|---|---:|---:|---|
| AAPL | 2026-10-30 | 345.55 | -0.96% | 56.31 | Middle range (30-70) | 342.13 | 333.06 | Above both SMAs |
| MSFT | 2026-10-30 | 521.65 | -1.60% | 36.02 | Middle range (30-70) | 530.97 | 512.91 | Mixed / between SMAs |
| QQQ | 2026-10-30 | 688.28 | -3.78% | 28.19 | Low RSI (<30) | 728.08 | 724.66 | Below both SMAs |
| RY.TO | 2026-10-30 | 282.59 | -1.95% | 66.01 | Middle range (30-70) | 278.61 | 281.31 | Above both SMAs |
| SHOP.TO | 2026-10-30 | 215.74 | -7.69% | 30.53 | Middle range (30-70) | 236.90 | 213.33 | Mixed / between SMAs |
| SPY | 2026-10-30 | 754.65 | -1.91% | 33.76 | Middle range (30-70) | 770.41 | 766.75 | Below both SMAs |
| VFV.TO | 2026-10-30 | 187.40 | -2.18% | 23.43 | Low RSI (<30) | 193.51 | 191.21 | Below both SMAs |
| XEQT.TO | 2026-10-30 | 44.48 | -2.07% | 28.84 | Low RSI (<30) | 45.57 | 45.53 | Below both SMAs |

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
- **MSFT:** accuracy 0.488; balanced accuracy 0.500; test samples 41; test positive-target rate 0.512.
- **QQQ:** accuracy 0.488; balanced accuracy 0.500; test samples 41; test positive-target rate 0.512.
- **RY.TO:** accuracy 0.537; balanced accuracy 0.500; test samples 41; test positive-target rate 0.463.
- **SHOP.TO:** accuracy 0.415; balanced accuracy 0.500; test samples 41; test positive-target rate 0.585.
- **SPY:** accuracy 0.561; balanced accuracy 0.500; test samples 41; test positive-target rate 0.439.
- **VFV.TO:** accuracy 0.488; balanced accuracy 0.500; test samples 41; test positive-target rate 0.512.
- **XEQT.TO:** accuracy 0.561; balanced accuracy 0.500; test samples 41; test positive-target rate 0.439.

Model metrics are historical holdout results, not a forecast guarantee or a buy/sell recommendation.

## Data retrieval issues

- None recorded.

## Notes

- Daily bars can be delayed or revised. Check timestamps and provider terms.
- Indicators summarize past prices and are not standalone decision rules.
- No transaction costs, taxes, slippage, or portfolio constraints are modeled.
