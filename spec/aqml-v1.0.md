# AQML v1.0 Specification

AQML v1.0 is retained here as a compatibility entry point only.

The active, executable profile is now **AQML v2.0**, which aligns with the current AurumQ parser and evaluator:

- Current spec: [`aqml-v2.0.md`](aqml-v2.0.md)
- Current schema: [`schema.json`](schema.json)
- Migrated examples: [`../examples/`](../examples/)

Key breaking changes from the original v1 draft include:

- `compare` now uses `left` / `right` instead of `field` / `value` / `reference`
- `range` now uses `indicator`
- `breakout` now uses `price` / `level` with `direction: up|down`
- `lookback` is represented with `offset` or nested logic groups
- `scoring.rule_points` replaces `weight + scoring.mode`
- exit and risk percentages use whole-number percentage fields such as `stop_loss_pct`

Use AQML v2.0 for any new strategy or tooling work.
