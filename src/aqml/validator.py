"""AQML validation logic."""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any

from jsonschema import Draft7Validator

from aqml.loader import load_aqml
from aqml.models import ValidationResult
from aqml.schema import load_schema

_VALID_RULE_TYPES = {"compare", "compare_all", "signal", "range", "pattern", "breakout"}
_VALID_LOGIC = {"and", "or", "not"}
_VALID_PORTFOLIO_METHODS = {"equal_weight", "score_weighted"}


def _format_jsonschema_path(parts: Sequence[Any]) -> str:
    if not parts:
        return "$"

    out = "$"
    for part in parts:
        if isinstance(part, int):
            out += f"[{part}]"
        else:
            out += f".{part}"
    return out


def _validate_rule_item(
    item: dict[str, Any], path: str, result: ValidationResult, depth: int = 0
) -> None:
    if "logic" in item:
        if depth > 3:
            result.add_error(path, "logic group nesting depth cannot exceed 3")

        logic = str(item.get("logic", "")).lower()
        if logic not in _VALID_LOGIC:
            result.add_error(path, "logic must be one of: and, or, not")

        conditions = item.get("conditions", [])
        if not isinstance(conditions, list) or not conditions:
            result.add_error(path, "conditions must be a non-empty list")
            return

        for index, condition in enumerate(conditions):
            if not isinstance(condition, dict):
                result.add_error(f"{path}.conditions[{index}]", "condition must be an object")
                continue
            _validate_rule_item(condition, f"{path}.conditions[{index}]", result, depth + 1)
        return

    rule_type = item.get("type")
    if rule_type not in _VALID_RULE_TYPES:
        valid = ", ".join(sorted(_VALID_RULE_TYPES))
        result.add_error(path, f"rule type must be one of: {valid}")


def _validate_scoring(config: dict[str, Any], result: ValidationResult) -> None:
    scoring = config.get("scoring", {})
    if not scoring:
        return

    rule_points = scoring.get("rule_points", [])
    rules = config.get("rules", [])
    if len(rule_points) > len(rules):
        result.add_error(
            "$.scoring.rule_points", "rule_points cannot exceed the number of top-level rules"
        )

    for index, rule_point in enumerate(rule_points):
        tiers = rule_point.get("tiers", [])
        if not isinstance(tiers, list):
            result.add_error(f"$.scoring.rule_points[{index}].tiers", "tiers must be a list")
            continue
        if len(tiers) > 10:
            result.add_error(
                f"$.scoring.rule_points[{index}].tiers", "at most 10 tiers are allowed"
            )
        for tier_index, tier in enumerate(tiers):
            if not isinstance(tier, dict):
                result.add_error(
                    f"$.scoring.rule_points[{index}].tiers[{tier_index}]",
                    "tier must be an object",
                )
                continue
            if "condition" not in tier or "points" not in tier:
                result.add_error(
                    f"$.scoring.rule_points[{index}].tiers[{tier_index}]",
                    "tier must contain condition and points",
                )


def _validate_exit_rules(config: dict[str, Any], result: ValidationResult) -> None:
    exit_rules = config.get("exit_rules", {})
    if not exit_rules:
        return

    for key in ("stop_loss_pct", "take_profit_pct", "trailing_stop_pct"):
        value = exit_rules.get(key)
        if value is None:
            continue
        if not isinstance(value, (int, float)) or not (0 < value <= 100):
            result.add_error(f"$.exit_rules.{key}", "must be a number between 0 and 100")

    max_holding_days = exit_rules.get("max_holding_days")
    if max_holding_days is not None and (
        not isinstance(max_holding_days, int) or max_holding_days <= 0
    ):
        result.add_error("$.exit_rules.max_holding_days", "must be a positive integer")


def _validate_risk(config: dict[str, Any], result: ValidationResult) -> None:
    risk = config.get("risk", {})
    if not risk:
        return

    for key in ("max_drawdown", "max_single_position"):
        value = risk.get(key)
        if value is None:
            continue
        if not isinstance(value, (int, float)) or not (0 < value <= 100):
            result.add_error(f"$.risk.{key}", "must be a number between 0 and 100")


def _validate_portfolio(config: dict[str, Any], result: ValidationResult) -> None:
    portfolio = config.get("portfolio", {})
    if not portfolio:
        return

    method = portfolio.get("method")
    if method and method not in _VALID_PORTFOLIO_METHODS:
        valid = ", ".join(sorted(_VALID_PORTFOLIO_METHODS))
        result.add_error("$.portfolio.method", f"must be one of: {valid}")

    max_positions = portfolio.get("max_positions")
    if max_positions is not None and (not isinstance(max_positions, int) or max_positions <= 0):
        result.add_error("$.portfolio.max_positions", "must be a positive integer")


def _run_schema_validation(config: dict[str, Any], result: ValidationResult) -> None:
    validator = Draft7Validator(load_schema())
    for error in sorted(validator.iter_errors(config), key=lambda item: list(item.absolute_path)):
        result.add_error(_format_jsonschema_path(error.absolute_path), error.message)


def _run_semantic_validation(config: dict[str, Any], result: ValidationResult) -> None:
    rules = config.get("rules", [])

    if not isinstance(rules, list):
        result.add_error("$.rules", "rules must be a list")
        return

    if len(rules) == 0:
        result.add_error("$.rules", "at least one rule is required")
    if len(rules) > 20:
        result.add_error("$.rules", "at most 20 rules are allowed")

    for index, rule in enumerate(rules):
        if not isinstance(rule, dict):
            result.add_error(f"$.rules[{index}]", "rule must be an object")
            continue
        _validate_rule_item(rule, f"$.rules[{index}]", result)

    _validate_scoring(config, result)
    _validate_exit_rules(config, result)
    _validate_risk(config, result)
    _validate_portfolio(config, result)


def validate(source: str | Any) -> ValidationResult:
    """Validate AQML from a path or raw YAML string."""

    config, issues, _, _ = load_aqml(source)
    result = ValidationResult(valid=True, data=config)

    for issue in issues:
        result.add_error(issue.path, issue.message)

    if config is None:
        return result

    _run_schema_validation(config, result)
    _run_semantic_validation(config, result)
    return result


def parse(source: str | Any) -> dict[str, Any]:
    """Parse AQML and raise on validation errors."""

    result = validate(source)
    if not result.valid or result.data is None:
        messages = "; ".join(f"{issue.path}: {issue.message}" for issue in result.errors)
        raise ValueError(messages or "AQML validation failed")
    return result.data
