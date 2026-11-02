# Daily Market Intelligence — 2026-11-02

- Generated: 2026-11-02 17:13 EST
- Purpose: educational market observation, not investment advice.
- Prices are daily adjusted OHLCV from the configured public data source.

## Watchlist overview

| Symbol | Last date | Close | Daily return | RSI (14) | RSI interpretation | SMA 20 | SMA 50 | Trend |
|---|---:|---:|---:|---:|---|---:|---:|---|
| AAPL | 2026-11-02 | 338.32 | -1.83% | 46.59 | Middle range (30-70) | 342.36 | 333.62 | Mixed / between SMAs |
| MSFT | 2026-11-02 | 507.12 | -2.83% | 27.84 | Low RSI (<30) | 530.08 | 513.39 | Below both SMAs |
| QQQ | 2026-11-02 | 681.09 | -1.36% | 27.22 | Low RSI (<30) | 724.43 | 724.07 | Below both SMAs |
| RY.TO | 2026-11-02 | 286.21 | 0.80% | 67.62 | Middle range (30-70) | 279.13 | 281.43 | Above both SMAs |
| SHOP.TO | 2026-11-02 | 217.64 | -1.24% | 23.50 | Low RSI (<30) | 237.22 | 213.70 | Mixed / between SMAs |
| SPY | 2026-11-02 | 752.10 | -0.48% | 32.65 | Middle range (30-70) | 769.33 | 766.54 | Below both SMAs |
| VFV.TO | 2026-11-02 | 187.16 | -0.36% | 24.03 | Low RSI (<30) | 193.14 | 191.22 | Below both SMAs |
| XEQT.TO | 2026-11-02 | 44.69 | 0.11% | 31.12 | Middle range (30-70) | 45.51 | 45.52 | Below both SMAs |

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

- **AAPL:** accuracy 0.512; balanced accuracy 0.523; test samples 41; test positive-target rate 0.512.
- **MSFT:** accuracy 0.512; balanced accuracy 0.500; test samples 41; test positive-target rate 0.488.
- **QQQ:** accuracy 0.512; balanced accuracy 0.500; test samples 41; test positive-target rate 0.488.
- **RY.TO:** accuracy 0.537; balanced accuracy 0.504; test samples 41; test positive-target rate 0.463.
- **SHOP.TO:** accuracy 0.439; balanced accuracy 0.500; test samples 41; test positive-target rate 0.561.
- **SPY:** accuracy 0.585; balanced accuracy 0.500; test samples 41; test positive-target rate 0.415.
- **VFV.TO:** accuracy 0.512; balanced accuracy 0.501; test samples 41; test positive-target rate 0.488.
- **XEQT.TO:** accuracy 0.585; balanced accuracy 0.528; test samples 41; test positive-target rate 0.439.

Model metrics are historical holdout results, not a forecast guarantee or a buy/sell recommendation.

## Data retrieval issues

- None recorded.

## Notes

- Daily bars can be delayed or revised. Check timestamps and provider terms.
- Indicators summarize past prices and are not standalone decision rules.
- No transaction costs, taxes, slippage, or portfolio constraints are modeled.
