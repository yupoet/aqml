# AQML Quick Start Guide

## Your First AQML Strategy

Create a file called `my-strategy.aqml`:

```yaml
version: "2.0"

name: My First Strategy
description: "Simple RSI oversold screen"
signal_type: buy

filters:
  exclude_st: true

rules:
  - type: range
    indicator: rsi14
    min: 0
    max: 30
    comment: "RSI in oversold zone"
```

That is enough to screen for A-share stocks with RSI(14) below 30.

## Adding More Conditions

```yaml
rules:
  - type: range
    indicator: rsi14
    min: 0
    max: 30
    comment: "RSI oversold"

  - logic: or
    comment: "MACD golden cross within 3 bars"
    conditions:
      - type: signal
        indicator: macd
        signal: golden_cross
        offset: 0
        comment: "MACD golden cross today"
      - type: signal
        indicator: macd
        signal: golden_cross
        offset: -1
        comment: "MACD golden cross yesterday"
      - type: signal
        indicator: macd
        signal: golden_cross
        offset: -2
        comment: "MACD golden cross 2 bars ago"

  - type: compare
    left: volume
    operator: ">"
    right: volume_ma10
    right_multiplier: 1.2
    comment: "Volume above average"
```

Top-level `rules` are implicitly combined with `AND`. Use nested `logic` groups when you need `OR` or `NOT`.

## Using Scoring Mode

Add `scoring.rule_points` to rank candidates instead of requiring every rule to pass:

```yaml
rules:
  - type: range
    indicator: rsi14
    min: 0
    max: 30
    comment: "RSI oversold"

  - type: signal
    indicator: macd
    signal: golden_cross
    offset: 0
    comment: "MACD golden cross today"

scoring:
  max_score: 100
  min_score: 60
  rule_points:
    - points: 50
    - points: 50
```

You can also add tiered fallback scoring:

```yaml
scoring:
  max_score: 100
  min_score: 60
  rule_points:
    - points: 60
      tiers:
        - condition: {indicator: rsi14, min: 30, max: 40}
          points: 30
    - points: 40
```

## Adding Exit Rules

```yaml
exit_rules:
  stop_loss_pct: 5.0
  take_profit_pct: 15.0
  trailing_stop_pct: 8.0
  max_holding_days: 20
```

All exit percentages use whole-number percentages, not decimals.

## Portfolio Configuration

```yaml
portfolio:
  method: equal_weight
  max_positions: 10
  initial_capital: 1000000
```

## Validation

Validate your strategy against the JSON Schema:

```bash
python -c "
import json, yaml, jsonschema
schema = json.load(open('spec/schema.json'))
strategy = yaml.safe_load(open('my-strategy.aqml'))
jsonschema.validate(strategy, schema)
print('✓ Valid AQML')
"
```

Or use the bundled validator CLI:

```bash
pip install -e .
aqml validate my-strategy.aqml
```

For editor-time validation in VS Code:

```bash
cd editors/vscode
npm ci
npm run package
code --install-extension ./aqml-vscode-0.3.0.vsix
```

The packaged extension wires `.aqml` files to the local AQML JSON Schema through the Red Hat YAML extension.

If you have AurumQ locally, you can still cross-check against the current service validator:

```bash
.venv/bin/python - <<'PY'
from pathlib import Path
from aurumq.strategies.service import StrategyService

aqml = Path('my-strategy.aqml').read_text(encoding='utf-8')
StrategyService.validate_aqml(aqml)
print('✓ Valid against AurumQ executable profile')
PY
```

## Next Steps

- Browse [examples/](../examples/) for complete v2 strategies
- Start from a copyable template in [templates/gallery/](../templates/gallery/)
- Read the [full specification](../spec/aqml-v2.0.md)
- Use `aqml validate` to lint generated strategies locally
- Try the [AurumQ platform](https://aurumq.ai) for backtesting and execution
