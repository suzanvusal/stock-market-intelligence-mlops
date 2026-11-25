# Daily Market Intelligence — 2026-11-25

- Generated: 2026-11-25 17:12 EST
- Purpose: educational market observation, not investment advice.
- Prices are daily adjusted OHLCV from the configured public data source.

## Watchlist overview

| Symbol | Last date | Close | Daily return | RSI (14) | RSI interpretation | SMA 20 | SMA 50 | Trend |
|---|---:|---:|---:|---:|---|---:|---:|---|
| AAPL | 2026-11-25 | 355.58 | 0.43% | 61.89 | Middle range (30-70) | 348.54 | 342.84 | Above both SMAs |
| MSFT | 2026-11-25 | 489.93 | -1.25% | 28.96 | Low RSI (<30) | 516.38 | 518.64 | Below both SMAs |
| QQQ | 2026-11-25 | 633.93 | -0.65% | 46.71 | Middle range (30-70) | 666.73 | 707.02 | Below both SMAs |
| RY.TO | 2026-11-25 | 269.26 | -0.14% | 31.26 | Middle range (30-70) | 281.53 | 280.30 | Below both SMAs |
| SHOP.TO | 2026-11-25 | 189.67 | 0.43% | 43.21 | Middle range (30-70) | 205.15 | 215.56 | Below both SMAs |
| SPY | 2026-11-25 | 716.70 | -0.29% | 44.20 | Middle range (30-70) | 740.33 | 757.85 | Below both SMAs |
| VFV.TO | 2026-11-25 | 181.30 | -0.55% | 48.16 | Middle range (30-70) | 186.76 | 190.64 | Below both SMAs |
| XEQT.TO | 2026-11-25 | 43.12 | -0.13% | 44.80 | Middle range (30-70) | 44.45 | 45.16 | Below both SMAs |

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

- **AAPL:** accuracy 0.415; balanced accuracy 0.423; test samples 41; test positive-target rate 0.512.
- **MSFT:** accuracy 0.488; balanced accuracy 0.500; test samples 41; test positive-target rate 0.512.
- **QQQ:** accuracy 0.561; balanced accuracy 0.518; test samples 41; test positive-target rate 0.439.
- **RY.TO:** accuracy 0.585; balanced accuracy 0.500; test samples 41; test positive-target rate 0.415.
- **SHOP.TO:** accuracy 0.488; balanced accuracy 0.516; test samples 41; test positive-target rate 0.537.
- **SPY:** accuracy 0.415; balanced accuracy 0.394; test samples 41; test positive-target rate 0.439.
- **VFV.TO:** accuracy 0.537; balanced accuracy 0.518; test samples 41; test positive-target rate 0.463.
- **XEQT.TO:** accuracy 0.585; balanced accuracy 0.616; test samples 41; test positive-target rate 0.342.

Model metrics are historical holdout results, not a forecast guarantee or a buy/sell recommendation.

## Data retrieval issues

- None recorded.

## Notes

- Daily bars can be delayed or revised. Check timestamps and provider terms.
- Indicators summarize past prices and are not standalone decision rules.
- No transaction costs, taxes, slippage, or portfolio constraints are modeled.
