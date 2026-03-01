# AQML Quick Start Guide

## Your First AQML Strategy

Create a file called `my-strategy.aqml`:

```yaml
aqml: "1.0"

name: My First Strategy
description: "Simple RSI oversold screen"

universe:
  market: A-shares
  exclude: [ST]

rules:
  - type: compare
    field: rsi14
    operator: "<"
    value: 30
```

That's it. This strategy screens for all A-share stocks with RSI(14) below 30.

## Adding More Conditions

```yaml
rules:
  # RSI oversold
  - type: compare
    field: rsi14
    operator: "<"
    value: 30

  # MACD golden cross in last 3 days
  - type: signal
    indicator: macd
    signal: golden_cross
    lookback: 3

  # Volume above average
  - type: compare
    field: volume
    operator: ">"
    reference: volume_ma10
    multiplier: 1.2
```

All rules must be satisfied (implicit AND) for a stock to pass.

## Using Scoring Mode

Want to rank stocks instead of binary pass/fail? Add `scoring` and `weight` to rules:

```yaml
rules:
  - type: compare
    field: rsi14
    operator: "<"
    value: 30
    weight: 50

  - type: signal
    indicator: macd
    signal: golden_cross
    weight: 50

scoring:
  mode: weighted
  min_score: 60
```

## Adding Exit Rules

```yaml
exit_rules:
  stop_loss: 0.05        # Cut losses at -5%
  take_profit: 0.15      # Take profits at +15%
  max_holding_days: 20   # Auto-exit after 20 days
```

## Portfolio Configuration

```yaml
portfolio:
  method: equal_weight    # Split equally across picks
  max_positions: 10       # Hold max 10 stocks
  max_sector_pct: 0.30    # No sector > 30%
```

## Validation

Validate your strategy against the JSON Schema:

```bash
# Python (with jsonschema)
python -c "
import json, yaml, jsonschema
schema = json.load(open('spec/schema.json'))
strategy = yaml.safe_load(open('my-strategy.aqml'))
jsonschema.validate(strategy, schema)
print('✓ Valid AQML')
"
```

## Next Steps

- Browse [examples/](../examples/) for complete strategies
- Read the [full specification](../spec/aqml-v1.0.md)
- Try the [AurumQ platform](https://aurumq.ai) for live execution
