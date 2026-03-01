---
name: Strategy Example
about: Submit a new AQML strategy example for the examples/ directory
title: "[Example] "
labels: example, contribution
assignees: ''
---

## Strategy Name

## Category

- [ ] Momentum
- [ ] Value
- [ ] Mean Reversion
- [ ] Breakout
- [ ] Fundamental
- [ ] Composite

## Description

Brief description of the strategy logic and why it's interesting.

## AQML File

```yaml
aqml: "1.0"

name: Your Strategy Name
description: ""

rules:
  - type: compare
    field: rsi14
    operator: "<"
    value: 30
```

## Validation

- [ ] I have validated this file against `spec/schema.json`
- [ ] All referenced indicators are from the standard list in Section 10
- [ ] The strategy has a meaningful `description`
