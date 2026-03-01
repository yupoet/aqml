# AQML Python Validator

> 🚧 Coming soon — `pip install aqml-validator`

## Planned API

```python
from aqml import validate, parse

# Validate a strategy file
result = validate("my-strategy.aqml")
if result.valid:
    print("✓ Valid AQML strategy")
else:
    for error in result.errors:
        print(f"✗ {error.path}: {error.message}")

# Parse into structured object
strategy = parse("my-strategy.aqml")
print(strategy.name)           # Strategy name
print(strategy.rules)          # List of Rule objects
print(strategy.exit_rules)     # ExitRules object
```

## Current Workaround

Use `jsonschema` directly:

```python
import json
import yaml
import jsonschema

with open("spec/schema.json") as f:
    schema = json.load(f)

with open("my-strategy.aqml") as f:
    strategy = yaml.safe_load(f)

try:
    jsonschema.validate(strategy, schema)
    print("✓ Valid AQML")
except jsonschema.ValidationError as e:
    print(f"✗ {e.message}")
```
