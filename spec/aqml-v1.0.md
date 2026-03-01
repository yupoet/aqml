# AQML v1.0 Specification

**Aurum Quant Markup Language — Version 1.0 Draft**

| Field | Value |
|-------|-------|
| Version | 1.0-draft |
| Date | 2026-03-01 |
| Author | Paris Yu |
| Status | Draft |
| License | Apache 2.0 |

---

## 1. Introduction

AQML (Aurum Quant Markup Language) is a YAML-based declarative specification for defining quantitative trading strategies. It provides a human-readable, machine-parseable, and AI-generatable format that separates strategy *intent* from *implementation*.

### 1.1 Design Principles

1. **Declarative over imperative** — Describe *what*, not *how*
2. **AI-first authoring** — Structured for LLM generation and optimization
3. **Progressive complexity** — Simple strategies are simple; advanced features are opt-in
4. **Engine-agnostic** — Any conformant engine can parse and execute AQML
5. **Backward compatible** — Future versions must support all prior valid documents

### 1.2 Notation

- **REQUIRED** fields must be present for a valid AQML document
- **OPTIONAL** fields may be omitted; engines should apply documented defaults
- YAML anchors and aliases are permitted but not required

---

## 2. Document Structure

An AQML document is a valid YAML file with the following top-level structure:

```yaml
aqml: "1.0"              # REQUIRED — Spec version

name: string              # REQUIRED — Strategy name
description: string       # OPTIONAL — Human-readable description
version: string           # OPTIONAL — Strategy version (user-defined)

metadata:                 # OPTIONAL — Additional metadata
  author: string
  created_at: date
  tags: [string]
  category: string        # e.g., momentum, value, mean-reversion, composite

universe:                 # OPTIONAL — Stock universe definition
  market: string
  exclude: [string]
  filters: [object]

rules:                    # REQUIRED — Entry conditions
  - {rule_object}

scoring:                  # OPTIONAL — Scoring mode configuration
  mode: string
  min_score: number

exit_rules:               # OPTIONAL — Exit conditions
  stop_loss: number
  take_profit: number
  trailing_stop: number
  max_holding_days: integer

portfolio:                # OPTIONAL — Portfolio construction
  method: string
  max_positions: integer
  max_sector_pct: number

risk:                     # OPTIONAL — Risk management parameters
  max_drawdown: number
  max_single_position: number
  max_sector_concentration: number
```

---

## 3. Top-Level Fields

### 3.1 `aqml` (REQUIRED)

Specifies the AQML specification version this document conforms to.

```yaml
aqml: "1.0"
```

Engines must reject documents with unsupported version numbers.

### 3.2 `name` (REQUIRED)

A human-readable name for the strategy. Must be a non-empty string.

```yaml
name: RSI Mean Reversion Strategy
```

### 3.3 `description` (OPTIONAL)

A longer description of the strategy's intent and logic.

### 3.4 `version` (OPTIONAL)

User-defined version string for tracking strategy iterations.

```yaml
version: "2.1.0"
```

### 3.5 `metadata` (OPTIONAL)

Arbitrary metadata for categorization, attribution, and tooling.

```yaml
metadata:
  author: Paris Yu
  created_at: "2026-03-01"
  tags: [momentum, oversold, volume]
  category: momentum
  source: "Adapted from GTJA Alpha #101"
  backtest_sharpe: 1.85
```

All metadata fields are OPTIONAL. Engines should preserve but may ignore unknown fields.

---

## 4. Universe

Defines the stock universe to screen. If omitted, the engine's default universe applies.

```yaml
universe:
  market: A-shares           # Target market
  exclude: [ST, STAR, BSE]   # Exclusion filters
  filters:                   # Additional universe filters
    - field: total_mv
      operator: ">"
      value: 2000000000      # Market cap > 2B
```

### 4.1 `market` (OPTIONAL)

Target market identifier. Default is engine-specific.

| Value | Description |
|-------|-------------|
| `A-shares` | China A-share market (SSE + SZSE) |
| `A-shares-main` | Main board only |
| `custom` | Custom universe defined by filters |

### 4.2 `exclude` (OPTIONAL)

Array of exclusion labels. Standard labels:

| Label | Description |
|-------|-------------|
| `ST` | Special Treatment stocks |
| `STAR` | STAR Market (科创板) |
| `BSE` | Beijing Stock Exchange (北交所) |
| `ChiNext` | ChiNext board (创业板) |
| `new_listing` | Stocks listed within N days (default: 60) |

### 4.3 `filters` (OPTIONAL)

Array of filter conditions applied to narrow the universe before rule evaluation. Uses the same rule syntax as `rules` (see Section 5).

---

## 5. Rules

The `rules` array defines entry conditions. Each rule is evaluated against every stock in the universe.

### 5.1 Common Rule Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `type` | string | YES | Rule type identifier |
| `weight` | number | NO | Score weight (0-100) when scoring mode is enabled |
| `name` | string | NO | Human-readable label for this rule |
| `enabled` | boolean | NO | Whether this rule is active (default: `true`) |

### 5.2 Rule Type: `compare`

Compares a field value against a fixed value or another field.

```yaml
- type: compare
  field: rsi14          # Left-hand field
  operator: "<"         # Comparison operator
  value: 30             # Fixed value comparison
```

```yaml
- type: compare
  field: close          # Left-hand field
  operator: ">"
  reference: ma20       # Compare against another field
  multiplier: 1.02      # Optional multiplier on reference
```

**Operators**: `>`, `>=`, `<`, `<=`, `==`, `!=`

### 5.3 Rule Type: `range`

Checks if a field value falls within a specified range.

```yaml
- type: range
  field: pe_ttm
  min: 5
  max: 25
  inclusive: true       # Default: true (includes boundaries)
```

### 5.4 Rule Type: `signal`

Detects technical indicator signals (crossovers, divergences, etc.).

```yaml
- type: signal
  indicator: macd
  signal: golden_cross  # Signal name
  lookback: 3           # Signal occurred within last N bars
```

**Standard signals**:

| Indicator | Available Signals |
|-----------|-------------------|
| `macd` | `golden_cross`, `death_cross`, `zero_cross_up`, `zero_cross_down` |
| `kdj` | `golden_cross`, `death_cross`, `overbought`, `oversold` |
| `ma` | `golden_cross`, `death_cross`, `long_arrangement`, `short_arrangement` |
| `boll` | `squeeze`, `expansion`, `upper_touch`, `lower_touch` |

### 5.5 Rule Type: `pattern`

Matches candlestick or price patterns.

```yaml
- type: pattern
  pattern: hammer
  lookback: 5
```

**Standard patterns**: `hammer`, `engulfing_bull`, `engulfing_bear`, `doji`, `morning_star`, `evening_star`, `three_white_soldiers`, `three_black_crows`

### 5.6 Rule Type: `breakout`

Detects price or volume breakouts.

```yaml
- type: breakout
  field: close
  reference: boll_upper
  direction: above      # above | below
  confirmation_bars: 1  # Bars to confirm breakout
```

### 5.7 Rule Evaluation

When scoring mode is **disabled**: All rules must be satisfied (implicit AND logic).

When scoring mode is **enabled**: Each rule contributes its `weight` to the total score. A stock passes if its total score meets `scoring.min_score`.

---

## 6. Scoring

Enables weighted scoring mode for ranking candidates.

```yaml
scoring:
  mode: weighted         # weighted | equal | threshold
  min_score: 60          # Minimum score to qualify (0-100)
```

| Mode | Description |
|------|-------------|
| `weighted` | Each rule contributes its `weight` to total score |
| `equal` | Each matched rule contributes equally |
| `threshold` | Binary — all rules with weight > 0 must match |

---

## 7. Exit Rules

Defines conditions for closing positions. All fields are OPTIONAL.

```yaml
exit_rules:
  stop_loss: 0.05           # Close if loss exceeds 5%
  take_profit: 0.15         # Close if gain reaches 15%
  trailing_stop: 0.08       # Trailing stop at 8% from peak
  max_holding_days: 20      # Close after 20 trading days
```

---

## 8. Portfolio

Configures portfolio construction and position management.

```yaml
portfolio:
  method: score_weighted    # Allocation method
  max_positions: 10         # Maximum concurrent positions
  max_sector_pct: 0.30      # Max 30% in any single sector
  rebalance: weekly         # Rebalance frequency
```

| Method | Description |
|--------|-------------|
| `equal_weight` | Equal allocation across all positions |
| `score_weighted` | Weight by strategy score |
| `market_cap_weighted` | Weight by market capitalization |
| `kelly` | Kelly criterion-based sizing |
| `risk_parity` | Risk parity allocation |

---

## 9. Risk

Risk management parameters for pre-trade and post-trade controls.

```yaml
risk:
  max_drawdown: 0.15              # Portfolio-level max drawdown
  max_single_position: 0.10       # Max 10% in any single stock
  max_sector_concentration: 0.30  # Max 30% in any sector
  var_limit: 0.05                 # Value-at-Risk daily limit
  correlation_threshold: 0.85     # Reject if corr > 0.85 with existing
```

---

## 10. Supported Indicators

AQML strategies may reference any of the following standard indicators. Engines must support at least the indicators marked as CORE.

| Indicator | Fields | Level |
|-----------|--------|-------|
| MA | `ma5`, `ma10`, `ma20`, `ma60`, `ma120`, `ma250` | CORE |
| EMA | `ema5`, `ema10`, `ema20`, `ema60` | CORE |
| MACD | `macd_dif`, `macd_dea`, `macd_hist` | CORE |
| RSI | `rsi6`, `rsi14` | CORE |
| KDJ | `kdj_k`, `kdj_d`, `kdj_j` | CORE |
| BOLL | `boll_upper`, `boll_mid`, `boll_lower` | CORE |
| ATR | `atr14` | EXTENDED |
| CCI | `cci14` | EXTENDED |
| OBV | `obv` | EXTENDED |
| DMI | `dmi_plus`, `dmi_minus`, `dmi_adx` | EXTENDED |
| SAR | `sar` | EXTENDED |
| Supertrend | `supertrend` | EXTENDED |
| MFI | `mfi14` | EXTENDED |
| WR | `wr14` | EXTENDED |
| VolumeMA | `volume_ma5`, `volume_ma10`, `volume_ma20` | CORE |

Engines may support additional indicators beyond this list. Unknown indicator fields should produce a validation warning (not an error) to allow forward compatibility.

---

## 11. Validation

An AQML document is **valid** if:

1. It is valid YAML
2. `aqml` field is present and matches a supported version
3. `name` field is present and non-empty
4. `rules` array is present and contains at least one rule
5. Each rule has a valid `type` field
6. All referenced fields are recognized indicators or fundamental fields
7. Numeric values are within reasonable ranges

The JSON Schema for programmatic validation is at [`schema.json`](schema.json).

---

## Appendix A: File Format

- File extension: **`.aqml`**
- MIME type: `application/x-aqml`
- Character encoding: UTF-8
- Line endings: LF (recommended) or CRLF
- Syntax: YAML 1.2 superset

## Appendix B: Full Example

See the [`examples/`](../examples/) directory for complete, runnable strategy files.

---

*AQML is created and maintained by [Paris Yu](https://aurumq.ai). Contributions welcome.*
