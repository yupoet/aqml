# AQML Python Validator

The repository now includes a working Python package and CLI for the AQML v2 executable profile.

## Install Locally

```bash
pip install -e .
```

For development:

```bash
pip install -e ".[dev]"
```

## CLI

```bash
aqml validate my-strategy.aqml
aqml normalize my-strategy.aqml --in-place
aqml parse my-strategy.aqml
aqml schema-path
python -m build
```

## Python API

```python
from aqml import normalize, parse, validate

result = validate("my-strategy.aqml")
if result.valid:
    print("✓ Valid AQML strategy")
else:
    for error in result.errors:
        print(f"✗ {error.path}: {error.message}")

strategy = parse("my-strategy.aqml")
print(strategy["name"])

formatted = normalize("my-strategy.aqml")
print(formatted)
```

## Validation Scope

The validator checks:

- YAML parsing via `yaml.safe_load`
- JSON Schema compatibility with `spec/schema.json`
- executable-profile semantics such as rule group depth, tier structure, exit percent ranges, and supported portfolio methods

The package is intentionally dependency-light and does not require AurumQ's database or service layer.

## Packaging

Build artifacts locally:

```bash
python -m build
twine check dist/*
```

Release workflow details are documented in [`RELEASING.md`](RELEASING.md).
