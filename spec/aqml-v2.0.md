# AQML v2.0 Specification

**Aurum Quant Markup Language — Executable Profile Draft**

| Field | Value |
|-------|-------|
| Version | 2.0-draft |
| Date | 2026-03-13 |
| Status | Draft |
| Alignment | AurumQ executable parser and evaluator |
| License | Apache 2.0 |

---

## 1. Introduction

AQML (Aurum Quant Markup Language) is a YAML-based declarative format for expressing quantitative trading strategies. This document specifies the **AQML v2 executable profile** currently implemented by AurumQ.

AQML v2 prioritizes:

1. **Executable fidelity**: every documented construct maps to real parser and evaluator behavior
2. **Human readability**: strategies remain concise and reviewable in plain YAML
3. **AI authoring**: the format is stable enough for LLM generation and revision workflows
4. **Progressive complexity**: simple screens stay short while complex strategies can use groups, scoring, and portfolio blocks

---

## 2. Document Structure

An AQML document is a valid YAML object with the following top-level shape:

```yaml
version: "2.0"          # REQUIRED
name: string            # REQUIRED
description: string     # REQUIRED
signal_type: buy        # REQUIRED: buy | sell

filters: {}             # OPTIONAL
rules: []               # REQUIRED: 1-20 items, supports rule groups
scoring: {}             # OPTIONAL
exit_rules: {}          # OPTIONAL
risk: {}                # OPTIONAL
portfolio: {}           # OPTIONAL
universe: {}            # OPTIONAL
metadata: {}            # OPTIONAL
```

### Required fields

- `version` must be `"2.0"`
- `name` must be a non-empty string
- `description` must be a non-empty string
- `signal_type` must be `buy` or `sell`
- `rules` must contain at least one rule or rule group

---

## 3. Rule Model

### 3.1 Common conventions

- Every top-level rule item should include a `comment`
- Top-level `rules` are combined with implicit `AND`
- Nested groups use `logic: and|or|not`
- Historical checks use `offset` where `0` means current bar and `-1` means previous bar
- The evaluator supports at most 3 nested logic levels

### 3.2 `compare`

Compare two operands, each of which may be a numeric literal or an indicator/column name.

```yaml
- type: compare
  left: close
  operator: ">"
  right: ma20
  comment: "Close above MA20"
```

Optional operand transforms:

```yaml
- type: compare
  left: close
  operator: "<"
  right: close
  right_offset: -5
  right_multiplier: 1.05
  comment: "5-day gain below 5%"
```

Supported operators: `>`, `>=`, `<`, `<=`, `==`, `!=`

### 3.3 `compare_all`

Compare one price series against a list of indicators.

```yaml
- type: compare_all
  price: close
  indicators: [ma60, ma90, ma125, ma250]
  operator: ">"
  min_above_pct: 1.0
  max_above_pct: 5.0
  comment: "Close above all long MAs without chasing"
```

### 3.4 `signal`

Detect a boolean event column such as `macd_golden_cross`.

```yaml
- type: signal
  indicator: macd
  signal: golden_cross
  offset: 0
  comment: "MACD golden cross today"
```

For "within N bars" semantics, use an `or` group:

```yaml
- logic: or
  comment: "MACD golden cross within 3 bars"
  conditions:
    - type: signal
      indicator: macd
      signal: golden_cross
      offset: 0
      comment: "Today"
    - type: signal
      indicator: macd
      signal: golden_cross
      offset: -1
      comment: "Yesterday"
    - type: signal
      indicator: macd
      signal: golden_cross
      offset: -2
      comment: "Two bars ago"
```

### 3.5 `range`

Check whether an indicator falls within a range.

```yaml
- type: range
  indicator: pe_ttm
  min: 5
  max: 25
  comment: "Reasonable valuation"
```

At least one of `min` or `max` must be present.

### 3.6 `pattern`

Match one or more candlestick patterns against `candle_type`.

```yaml
- type: pattern
  pattern: hammer
  offset: 0
  comment: "Hammer today"
```

```yaml
- type: pattern
  pattern: [small_yang, mid_yang, big_yang]
  offset: -1
  comment: "Bullish candle yesterday"
```

### 3.7 `breakout`

Detect cross-through versus a level from the previous bar to the current bar.

```yaml
- type: breakout
  price: close
  level: boll_upper
  direction: up
  offset: 0
  comment: "Close breaks above upper Bollinger band"
```

`direction` must be `up` or `down`.

### 3.8 Logic groups

Use groups to express `AND`, `OR`, and `NOT`.

```yaml
- logic: and
  comment: "Trend plus confirmation"
  conditions:
    - type: compare
      left: close
      operator: ">"
      right: ma20
      comment: "Close above MA20"
    - logic: or
      comment: "One bullish signal"
      conditions:
        - type: signal
          indicator: macd
          signal: golden_cross
          offset: 0
          comment: "MACD cross"
        - type: signal
          indicator: kdj
          signal: golden_cross
          offset: 0
          comment: "KDJ cross"
```

---

## 4. Filters

`filters` are applied before rule evaluation.

```yaml
filters:
  exclude_st: true
  exclude_kcb: true
  exclude_cyb: false
  exclude_bj: true
  min_amount: 5000
  min_market_cap: 30
  include_industries: [电子, 计算机]
  exclude_limit_up: true
  exclude_limit_down: false
```

Supported keys:

- `exclude_st`
- `exclude_kcb`
- `exclude_cyb`
- `exclude_bj`
- `min_amount`
- `min_market_cap`
- `include_industries`
- `exclude_limit_up`
- `exclude_limit_down`

`universe.exclude` is also supported and is mapped internally to filter flags for `ST`, `STAR`, `BSE`, and `new_listing`.

---

## 5. Scoring

When `scoring` is present, the evaluator accumulates points instead of requiring every rule to pass.

```yaml
scoring:
  max_score: 100
  min_score: 60
  rule_points:
    - points: 35
    - points: 25
      required: true
    - points: 20
      tiers:
        - condition: {indicator: rsi14, min: 30, max: 40}
          points: 10
```

### 5.1 `rule_points`

- one entry per top-level rule item
- `points` is the score granted when that rule item passes
- `required: true` makes the whole strategy score zero if that rule item fails
- `tiers` provides fallback partial scoring when the main rule fails

### 5.2 Tier conditions

Tier `condition` supports:

- compare-style: `{left: ma5, operator: ">", right: ma10}`
- range-style: `{indicator: rsi14, min: 30, max: 50}`

### 5.3 Volume bonus

```yaml
scoring:
  max_score: 110
  min_score: 60
  rule_points:
    - points: 60
    - points: 40
  volume_bonus:
    enabled: true
    lookback: 5
    multiplier: 1.5
    points: 10
```

---

## 6. Exit Rules

All exit percentages use whole-number percentages, not decimals.

```yaml
exit_rules:
  stop_loss_pct: 8.0
  take_profit_pct: 15.0
  trailing_stop_pct: 5.0
  max_holding_days: 20
```

---

## 7. Risk

```yaml
risk:
  max_drawdown: 15.0
  max_single_position: 10.0
```

---

## 8. Portfolio

```yaml
portfolio:
  method: equal_weight
  max_positions: 10
  initial_capital: 1000000
```

Supported `method` values:

- `equal_weight`
- `score_weighted`

Additional portfolio metadata may be present, but only the two methods above are guaranteed by the executable profile.

---

## 9. Universe

```yaml
universe:
  market: A-shares
  exclude: [ST, STAR, BSE, new_listing]
  include_boards: [Shanghai, Shenzhen]
```

`universe` describes selection scope. Numeric or liquidity pre-filters should be expressed with top-level `filters`.

---

## 10. Metadata

`metadata` is preserved for attribution and classification. Unknown keys are allowed.

```yaml
metadata:
  author: AQML Community
  created_at: "2026-03-13"
  tags: [momentum, breakout]
  category: momentum
  source: "Converted from open-source research"
```

---

## 11. Compatibility Notes

The original v1 draft documented keys that no longer match current execution semantics. Migrating to v2 requires these changes:

| Legacy draft form | Executable v2 form |
|------------------|--------------------|
| `aqml: "1.0"` | `version: "2.0"` |
| `field`, `value`, `reference`, `multiplier` | `left`, `right`, `right_multiplier` |
| `range.field` | `range.indicator` |
| `breakout.field`, `breakout.reference`, `above|below` | `breakout.price`, `breakout.level`, `up|down` |
| `lookback` | `offset` or grouped offsets |
| `weight` + `scoring.mode` | `scoring.rule_points` |
| `stop_loss`, `take_profit`, `trailing_stop` decimal ratios | `*_pct` whole-number percentages |

Use the updated examples and schema in this repository as the canonical reference for new AQML work.
