# Daily Market Intelligence — 2026-11-06

- Generated: 2026-11-06 14:53 EST
- Purpose: educational market observation, not investment advice.
- Prices are daily adjusted OHLCV from the configured public data source.

## Watchlist overview

| Symbol | Last date | Close | Daily return | RSI (14) | RSI interpretation | SMA 20 | SMA 50 | Trend |
|---|---:|---:|---:|---:|---|---:|---:|---|
| AAPL | 2026-11-06 | 343.40 | -0.22% | 50.34 | Middle range (30-70) | 343.44 | 336.03 | Mixed / between SMAs |
| MSFT | 2026-11-06 | 532.24 | -0.69% | 49.48 | Middle range (30-70) | 531.49 | 516.68 | Above both SMAs |
| QQQ | 2026-11-06 | 658.32 | 1.74% | 31.45 | Middle range (30-70) | 707.75 | 720.79 | Below both SMAs |
| RY.TO | 2026-11-06 | 285.05 | -0.28% | 62.16 | Middle range (30-70) | 281.89 | 281.76 | Above both SMAs |
| SHOP.TO | 2026-11-06 | 209.95 | 4.33% | 31.66 | Middle range (30-70) | 231.79 | 213.49 | Below both SMAs |
| SPY | 2026-11-06 | 737.48 | 0.61% | 36.23 | Middle range (30-70) | 763.47 | 765.19 | Below both SMAs |
| VFV.TO | 2026-11-06 | 185.43 | 1.49% | 36.98 | Middle range (30-70) | 191.14 | 191.12 | Below both SMAs |
| XEQT.TO | 2026-11-06 | 44.38 | 0.98% | 40.78 | Middle range (30-70) | 45.23 | 45.43 | Below both SMAs |

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

- **AAPL:** accuracy 0.512; balanced accuracy 0.524; test samples 41; test positive-target rate 0.512.
- **MSFT:** accuracy 0.488; balanced accuracy 0.500; test samples 41; test positive-target rate 0.512.
- **QQQ:** accuracy 0.463; balanced accuracy 0.500; test samples 41; test positive-target rate 0.537.
- **RY.TO:** accuracy 0.512; balanced accuracy 0.477; test samples 41; test positive-target rate 0.463.
- **SHOP.TO:** accuracy 0.415; balanced accuracy 0.500; test samples 41; test positive-target rate 0.585.
- **SPY:** accuracy 0.537; balanced accuracy 0.525; test samples 41; test positive-target rate 0.488.
- **VFV.TO:** accuracy 0.488; balanced accuracy 0.519; test samples 41; test positive-target rate 0.537.
- **XEQT.TO:** accuracy 0.585; balanced accuracy 0.540; test samples 41; test positive-target rate 0.439.

Model metrics are historical holdout results, not a forecast guarantee or a buy/sell recommendation.

## Data retrieval issues

- None recorded.

## Notes

- Daily bars can be delayed or revised. Check timestamps and provider terms.
- Indicators summarize past prices and are not standalone decision rules.
- No transaction costs, taxes, slippage, or portfolio constraints are modeled.
