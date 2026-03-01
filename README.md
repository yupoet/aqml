<p align="center">
  <img src="assets/aqml-logo.svg" alt="AQML Logo" width="120" />
</p>

<h1 align="center">AQML</h1>
<p align="center"><strong>Aurum Quant Markup Language</strong></p>

<p align="center">
  The world's first AI-native declarative standard for quantitative trading strategies.
</p>

<p align="center">
  <a href="spec/aqml-v1.0.md">Specification</a> ·
  <a href="examples/">Examples</a> ·
  <a href="docs/">Documentation</a> ·
  <a href="https://aurumq.ai">AurumQ Platform</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/version-1.0--draft-D4A853?style=flat-square" alt="Version" />
  <img src="https://img.shields.io/badge/format-YAML-blue?style=flat-square" alt="Format" />
  <img src="https://img.shields.io/badge/AI--native-✓-4ECDC4?style=flat-square" alt="AI Native" />
  <img src="https://img.shields.io/badge/license-Apache--2.0-green?style=flat-square" alt="License" />
</p>

---

## What is AQML?

**AQML** (Aurum Quant Markup Language) is a declarative, YAML-based specification for defining quantitative trading strategies. It is designed to be:

- **Human-readable** — Write and review strategies like reading a document
- **Machine-parseable** — Validate, execute, and backtest with any conformant engine
- **AI-generatable** — LLMs can natively read, write, and optimize AQML strategies

AQML eliminates the need to write Python, C++, or any programming language to define trading logic. Describe *what* conditions to screen for, not *how* to implement them.

## Quick Example

```yaml
# momentum-breakout.aqml.yaml
aqml: "1.0"

name: Momentum Breakout Strategy
description: "RSI oversold + MACD golden cross with volume confirmation"

universe:
  market: A-shares
  exclude: [ST, STAR, BSE]

rules:
  - type: compare
    field: rsi14
    operator: "<"
    value: 30
    weight: 40

  - type: signal
    indicator: macd
    signal: golden_cross
    weight: 35

  - type: compare
    field: volume
    operator: ">"
    reference: volume_ma10
    multiplier: 1.5
    weight: 25

scoring:
  mode: weighted
  min_score: 60

exit_rules:
  stop_loss: 0.05
  take_profit: 0.15
  max_holding_days: 20

portfolio:
  method: score_weighted
  max_positions: 10
  max_sector_pct: 0.3

risk:
  max_drawdown: 0.15
  max_single_position: 0.1
```

## Why AQML?

| Feature | AQML | Python-based (Qlib, VN.py, LEAN) |
|---------|------|-----------------------------------|
| Learning curve | Minutes | Weeks to months |
| AI generation | Native — LLMs output valid AQML directly | Fragile — generated code often has bugs |
| Readability | Plain YAML, self-documenting | Requires reading source code |
| Validation | JSON Schema, instant feedback | Runtime errors only |
| Version control | Clean diffs, meaningful commits | Noisy code diffs |
| Portability | Engine-agnostic specification | Locked to specific framework |
| Collaboration | Non-developers can review & contribute | Developer-only |

## Specification

The full AQML v1.0 specification is available at [`spec/aqml-v1.0.md`](spec/aqml-v1.0.md).

### Core Concepts

| Concept | Description |
|---------|-------------|
| **Universe** | Define which stocks to screen (market, exclusions, filters) |
| **Rules** | Declarative conditions using 5+ rule types |
| **Scoring** | Optional weighted scoring mode for ranking candidates |
| **Exit Rules** | Stop-loss, take-profit, trailing stop, time-based exits |
| **Portfolio** | Position sizing, allocation method, concentration limits |
| **Risk** | Pre-trade and post-trade risk parameters |

### Rule Types

| Type | Description | Example |
|------|-------------|---------|
| `compare` | Compare field against value or reference | `rsi14 < 30` |
| `range` | Check if field is within a range | `pe_ttm between 5 and 25` |
| `signal` | Technical indicator signal detection | `macd golden_cross` |
| `pattern` | Candlestick or price pattern matching | `hammer pattern` |
| `breakout` | Price/volume breakout detection | `close > boll_upper` |

## File Extension

AQML strategy files use the **`.aqml`** extension:

```
strategies/
├── momentum-breakout.aqml
├── mean-reversion.aqml
└── multi-factor-value.aqml
```

The `.aqml` extension establishes AQML as a first-class file format with dedicated IDE support, syntax highlighting, and validation tooling.

### IDE Support

| IDE | Support | Install |
|-----|---------|---------|
| **VS Code** | Syntax highlighting + validation | [Extension](editors/vscode/) |
| **JetBrains** | File type recognition + highlighting | [Plugin](editors/jetbrains/) |
| **Vim / Neovim** | Filetype detection + YAML highlighting | [Config](editors/vim/) |
| **GitHub** | Syntax highlighting in repos | Automatic via `.gitattributes` |

## Ecosystem

### Reference Implementation

[AurumQ](https://aurumq.ai) is the reference implementation and execution engine for AQML strategies, providing:

- Full AQML v1.0 parser and validator
- 17+ built-in technical indicators
- Institutional-grade backtesting engine
- AI-powered strategy generation (natural language → AQML)
- Real-time signal tracking across 4,800+ A-shares

### Validator

```bash
pip install aqml-validator  # coming soon
```

```python
from aqml import validate

result = validate("my-strategy.aqml.yaml")
if result.valid:
    print("✓ Valid AQML strategy")
else:
    for error in result.errors:
        print(f"✗ {error}")
```

## Roadmap

- [x] AQML v1.0 specification draft
- [x] JSON Schema for validation
- [x] Example strategy library
- [ ] Python validator package (`aqml-validator`)
- [ ] VS Code extension (syntax highlighting + validation)
- [ ] Strategy template gallery
- [ ] Multi-language validator (JavaScript, Go)
- [ ] AQML v2.0 — nested logic groups, OR/NOT operators

## Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

Ways to contribute:
- 📝 Submit strategy examples
- 🐛 Report spec ambiguities or issues
- 🔧 Build validators or tooling
- 🌐 Translate documentation
- 💡 Propose spec extensions via RFC

## License

AQML specification is licensed under [Apache License 2.0](LICENSE).

Strategy files created using AQML belong to their authors.

---

<p align="center">
  <sub>Created by <a href="https://aurumq.ai">Paris Yu</a> · Powered by <a href="https://aurumq.ai">AurumQ</a></sub>
</p>
