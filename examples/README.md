# AQML Strategy Examples

This directory contains reference strategies demonstrating various AQML patterns.

| File | Category | Complexity | Description |
|------|----------|------------|-------------|
| [`simple-rsi.aqml`](simple-rsi.aqml) | Momentum | ⭐ Beginner | Single-rule RSI oversold screen |
| [`momentum-breakout.aqml`](momentum-breakout.aqml) | Momentum | ⭐⭐ Intermediate | RSI + MACD + volume confirmation |
| [`mean-reversion.aqml`](mean-reversion.aqml) | Mean Reversion | ⭐⭐ Intermediate | Bollinger Band bounce + fundamentals |
| [`multi-factor-value.aqml`](multi-factor-value.aqml) | Value | ⭐⭐⭐ Advanced | PE/PB/ROE multi-factor with MA trend |
| [`dual-thrust.aqml`](dual-thrust.aqml) | Breakout | ⭐⭐ Intermediate | Classic Dual Thrust range breakout |
| [`kdj-golden-cross.aqml`](kdj-golden-cross.aqml) | Signal | ⭐ Beginner | KDJ golden cross with volume filter |

## Validating Examples

```bash
# Python
pip install jsonschema pyyaml
python -c "
import json, yaml, jsonschema, glob
schema = json.load(open('spec/schema.json'))
for f in glob.glob('examples/*.aqml'):
    strategy = yaml.safe_load(open(f))
    jsonschema.validate(strategy, schema)
    print(f'✓ {f}')
"
```

## Contributing

We welcome strategy examples! See [CONTRIBUTING.md](../CONTRIBUTING.md) for guidelines, or use the [Strategy Example issue template](https://github.com/yupoet/aqml/issues/new?template=strategy_example.md).
