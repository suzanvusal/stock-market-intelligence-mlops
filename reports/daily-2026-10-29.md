# Daily Market Intelligence — 2026-10-29

- Generated: 2026-10-29 14:12 EDT
- Purpose: educational market observation, not investment advice.
- Prices are daily adjusted OHLCV from the configured public data source.

## Watchlist overview

| Symbol | Last date | Close | Daily return | RSI (14) | RSI interpretation | SMA 20 | SMA 50 | Trend |
|---|---:|---:|---:|---:|---|---:|---:|---|
| AAPL | 2026-10-29 | 350.10 | 1.82% | 67.50 | Middle range (30-70) | 341.60 | 332.40 | Above both SMAs |
| MSFT | 2026-10-29 | 528.09 | -0.55% | 44.97 | Middle range (30-70) | 530.66 | 512.05 | Mixed / between SMAs |
| QQQ | 2026-10-29 | 713.17 | -1.71% | 33.11 | Middle range (30-70) | 731.03 | 725.05 | Below both SMAs |
| RY.TO | 2026-10-29 | 287.97 | 0.54% | 81.44 | High RSI (>70) | 278.27 | 281.36 | Above both SMAs |
| SHOP.TO | 2026-10-29 | 232.77 | -1.15% | 48.90 | Middle range (30-70) | 236.67 | 213.04 | Mixed / between SMAs |
| SPY | 2026-10-29 | 767.47 | -0.63% | 40.73 | Middle range (30-70) | 771.07 | 766.84 | Mixed / between SMAs |
| VFV.TO | 2026-10-29 | 190.79 | -0.77% | 35.75 | Middle range (30-70) | 193.77 | 191.21 | Below both SMAs |
| XEQT.TO | 2026-10-29 | 45.26 | -0.40% | 44.73 | Middle range (30-70) | 45.61 | 45.54 | Below both SMAs |

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

- **AAPL:** accuracy 0.512; balanced accuracy 0.531; test samples 41; test positive-target rate 0.537.
- **MSFT:** accuracy 0.488; balanced accuracy 0.500; test samples 41; test positive-target rate 0.512.
- **QQQ:** accuracy 0.463; balanced accuracy 0.500; test samples 41; test positive-target rate 0.537.
- **RY.TO:** accuracy 0.512; balanced accuracy 0.492; test samples 41; test positive-target rate 0.463.
- **SHOP.TO:** accuracy 0.415; balanced accuracy 0.500; test samples 41; test positive-target rate 0.585.
- **SPY:** accuracy 0.537; balanced accuracy 0.500; test samples 41; test positive-target rate 0.463.
- **VFV.TO:** accuracy 0.512; balanced accuracy 0.524; test samples 41; test positive-target rate 0.512.
- **XEQT.TO:** accuracy 0.537; balanced accuracy 0.478; test samples 41; test positive-target rate 0.439.

Model metrics are historical holdout results, not a forecast guarantee or a buy/sell recommendation.

## Data retrieval issues

- None recorded.

## Notes

- Daily bars can be delayed or revised. Check timestamps and provider terms.
- Indicators summarize past prices and are not standalone decision rules.
- No transaction costs, taxes, slippage, or portfolio constraints are modeled.
