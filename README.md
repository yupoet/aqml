<p align="center">
  <img src="assets/aqml-logo.svg" alt="AQML Logo" width="120" />
</p>

<h1 align="center">AQML</h1>
<p align="center"><strong>Aurum Quant Markup Language</strong></p>

<p align="center">
  The executable YAML profile for quantitative trading strategies on AurumQ.
</p>

<p align="center">
  <a href="spec/aqml-v2.0.md">Specification</a> ·
  <a href="examples/">Examples</a> ·
  <a href="docs/">Documentation</a> ·
  <a href="https://aurumq.ai">AurumQ Platform</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/version-2.0--draft-D4A853?style=flat-square" alt="Version" />
  <img src="https://img.shields.io/badge/format-YAML-blue?style=flat-square" alt="Format" />
  <img src="https://img.shields.io/badge/executable-profile-aurumq-4ECDC4?style=flat-square" alt="Executable Profile" />
  <img src="https://img.shields.io/badge/license-Apache--2.0-green?style=flat-square" alt="License" />
</p>

---

## What is AQML?

**AQML** (Aurum Quant Markup Language) is a declarative, YAML-based format for defining quantitative strategies. This repository tracks the **AQML v2 executable profile** that AurumQ currently parses, validates, backtests, and runs in production.

AQML is designed to be:

- **Human-readable**: strategies read like structured investment notes
- **Machine-parseable**: the same document can be validated and executed
- **AI-generatable**: LLMs can reliably produce and revise valid strategy files

## Quick Example

```yaml
# momentum-breakout.aqml
version: "2.0"

name: Momentum Breakout Strategy
description: "RSI oversold + MACD golden cross with volume confirmation"
signal_type: buy

filters:
  exclude_st: true
  exclude_kcb: true
  exclude_bj: true

rules:
  - type: range
    indicator: rsi14
    min: 0
    max: 30
    comment: "RSI in oversold zone"

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
    right_multiplier: 1.5
    comment: "Volume above 10-day average"

scoring:
  max_score: 100
  min_score: 60
  rule_points:
    - points: 40
    - points: 35
    - points: 25

exit_rules:
  stop_loss_pct: 5.0
  take_profit_pct: 15.0
  max_holding_days: 20

portfolio:
  method: score_weighted
  max_positions: 10
  initial_capital: 1000000

risk:
  max_drawdown: 15.0
  max_single_position: 10.0
```

## Specification

The active executable specification is [`spec/aqml-v2.0.md`](spec/aqml-v2.0.md).

### Core Concepts

| Concept | Description |
|---------|-------------|
| **Filters** | Exclude ST/KCB/BJ stocks, enforce liquidity and market-cap gates |
| **Rules** | Declarative conditions with nested `and/or/not` logic groups |
| **Scoring** | Ranked selection via `rule_points`, `tiers`, and optional bonuses |
| **Exit Rules** | Percentage-based stop-loss, take-profit, trailing stop, time exits |
| **Portfolio** | Position sizing and allocation method |
| **Risk** | Portfolio-level risk guards |

### Rule Types

| Type | Description | Example |
|------|-------------|---------|
| `compare` | Compare `left` against `right` with optional offsets/multipliers | `close > ma20` |
| `compare_all` | Ensure price is above or below multiple indicators | `close > ma60/90/125/250` |
| `range` | Check whether an indicator falls within a range | `pe_ttm between 5 and 25` |
| `signal` | Detect technical events on boolean signal columns | `MACD golden_cross` |
| `pattern` | Match candlestick patterns | `hammer pattern` |
| `breakout` | Detect cross-through against a level | `close breaks up through boll_upper` |
| `logic group` | Compose conditions with `and`, `or`, `not` | `or: [MACD, KDJ]` |

### Migration Highlights

| Old form | Executable v2 form |
|----------|--------------------|
| `field` / `value` / `reference` / `multiplier` | `left` / `right` / `right_multiplier` |
| `range.field` | `range.indicator` |
| `breakout.field` / `breakout.reference` | `breakout.price` / `breakout.level` |
| `direction: above|below` | `direction: up|down` |
| `lookback` | explicit `offset` or an `or` logic group |
| `weight + scoring.mode` | `scoring.rule_points` |
| `stop_loss`, `take_profit`, `trailing_stop` | `*_pct` percentage fields |

## File Extension

AQML strategy files use the **`.aqml`** extension:

```
strategies/
├── momentum-breakout.aqml
├── mean-reversion.aqml
└── multi-factor-value.aqml
```

The `.aqml` extension establishes AQML as a first-class file format with dedicated IDE support, syntax highlighting, and validation tooling.

## IDE Support

| IDE | Support | Install |
|-----|---------|---------|
| **VS Code** | Syntax highlighting + snippets + YAML schema validation | [Extension](editors/vscode/) |
| **JetBrains** | File type recognition + highlighting | [Plugin](editors/jetbrains/) |
| **Vim / Neovim** | Filetype detection + YAML highlighting | [Config](editors/vim/) |
| **GitHub** | Syntax highlighting in repos | Automatic via `.gitattributes` |

## Ecosystem

### Reference Implementation

[AurumQ](https://aurumq.ai) is the reference implementation and execution engine for AQML strategies, providing:

- Full AQML v2 executable-profile parser and validator
- Nested rule groups, `compare_all`, tiered scoring, and percentage-based exits
- Backtesting and scheduled execution for A-share screening strategies
- AI-powered strategy generation (natural language → AQML)

### Validator

JSON Schema is provided at [`spec/schema.json`](spec/schema.json). The repository now also ships a lightweight Python validator package and CLI:

```bash
pip install -e .
aqml validate examples/simple-rsi.aqml
python -m build
```

Python API:

```python
from aqml import parse, validate

result = validate("examples/simple-rsi.aqml")
strategy = parse("examples/simple-rsi.aqml")
```

GitHub Actions now cover CI, wheel/sdist builds, and PyPI/TestPyPI release flow for the validator package. The VS Code extension is also packaged as a `.vsix` with a dedicated GitHub Actions workflow and Marketplace publish flow.

### Strategy Template Gallery

Ready-to-copy starter templates now live in [`templates/gallery/`](templates/gallery/). The gallery is distinct from [`examples/`](examples/):

- `examples/` show the full executable profile and source conversions
- `templates/gallery/` provides opinionated starting points with tuning hints and a machine-readable [`index.yaml`](templates/gallery/index.yaml)

## Roadmap

- [x] AQML v2 executable-profile draft
- [x] JSON Schema for validation
- [x] Example strategy library synced to the executable parser
- [x] Nested logic groups, `compare_all`, and tiered scoring
- [x] Python validator package (`aqml-validator`)
- [x] VS Code extension packaging
- [x] Strategy template gallery
- [ ] Multi-language validator (JavaScript, Go)
- [ ] AQML v3.0: multi-asset strategies and custom factor expressions

## Contributing

We welcome contributions. See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

Useful contributions include:

- strategy examples aligned with the executable profile
- spec clarifications and migration notes
- editor tooling and validators
- translations and docs improvements

## License

AQML specification is licensed under [Apache License 2.0](LICENSE).

Strategy files created using AQML belong to their authors.

---

<p align="center">
  <sub>Created by <a href="mailto:paris@aurumq.ai">Paris Yu</a> · Powered by <a href="https://www.aurumq.ai">AurumQ</a></sub>
</p>
