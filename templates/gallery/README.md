# AQML Strategy Template Gallery

This directory contains ready-to-copy AQML starter templates.

Unlike [`examples/`](../../examples/), these files are organized as reusable starting points for common strategy intents:

- fast starter screens
- ranked multi-factor templates
- trend-following templates
- mean-reversion templates

Each template is:

- valid against the current AQML v2 executable profile
- listed in [`index.yaml`](index.yaml) with metadata and tuning hints
- designed to be copied and edited directly

## How To Use

1. Pick a template from [`index.yaml`](index.yaml).
2. Copy the `.aqml` file into your own strategy folder.
3. Rename `name` and update the documented tuning knobs.
4. Validate locally:

```bash
aqml validate my-strategy.aqml
```

## Templates

| Template | Category | Difficulty | Best for |
|----------|----------|------------|----------|
| [`starter-rsi-oversold.aqml`](starter-rsi-oversold.aqml) | Mean reversion | Beginner | Simple oversold rebound screens |
| [`starter-momentum-breakout.aqml`](starter-momentum-breakout.aqml) | Momentum | Beginner | RSI + MACD + volume confirmation |
| [`starter-value-quality.aqml`](starter-value-quality.aqml) | Value | Intermediate | Cheap stocks with quality and trend filters |
| [`starter-trend-following.aqml`](starter-trend-following.aqml) | Trend | Beginner | MA alignment and volume expansion |
| [`starter-low-volatility.aqml`](starter-low-volatility.aqml) | Low volatility | Intermediate | Squeeze setups with quality filters |
