from __future__ import annotations

from pathlib import Path

import pytest

from aqml.loader import normalize
from aqml.schema import schema_path
from aqml.validator import parse, validate

VALID_AQML = """
version: "2.0"
name: Demo Strategy
description: Demo description
signal_type: buy
rules:
  - type: compare
    left: close
    operator: ">"
    right: ma20
    comment: Close above MA20
"""


def test_validate_raw_text() -> None:
    result = validate(VALID_AQML)
    assert result.valid
    assert result.data is not None
    assert result.data["name"] == "Demo Strategy"


def test_parse_path() -> None:
    example = Path("examples/simple-rsi.aqml")
    parsed = parse(example)
    assert parsed["version"] == "2.0"
    assert parsed["signal_type"] == "buy"


def test_invalid_legacy_shape_is_rejected() -> None:
    legacy = """
aqml: "1.0"
name: Old Strategy
rules:
  - type: compare
    field: rsi14
    operator: "<"
    value: 30
"""
    result = validate(legacy)
    assert not result.valid
    messages = [issue.message for issue in result.errors]
    assert any("signal_type" in message or "description" in message for message in messages)


def test_invalid_logic_depth_is_rejected() -> None:
    too_deep = """
version: "2.0"
name: Deep Strategy
description: invalid depth
signal_type: buy
rules:
  - logic: and
    comment: level0
    conditions:
      - logic: and
        comment: level1
        conditions:
          - logic: and
            comment: level2
            conditions:
              - logic: and
                comment: level3
                conditions:
                  - logic: and
                    comment: level4
                    conditions:
                      - type: compare
                        left: close
                        operator: ">"
                        right: ma20
                        comment: base
"""
    result = validate(too_deep)
    assert not result.valid
    assert any("nesting depth" in issue.message for issue in result.errors)


def test_invalid_exit_pct_is_rejected() -> None:
    bad_exit = """
version: "2.0"
name: Exit Strategy
description: invalid exit
signal_type: buy
rules:
  - type: compare
    left: close
    operator: ">"
    right: ma20
    comment: base
exit_rules:
  stop_loss_pct: 120
"""
    result = validate(bad_exit)
    assert not result.valid
    assert any("stop_loss_pct" in issue.path for issue in result.errors)


def test_normalize_roundtrip() -> None:
    normalized = normalize(VALID_AQML)
    reparsed = parse(normalized)
    assert reparsed["version"] == "2.0"


def test_parse_invalid_raises() -> None:
    with pytest.raises(ValueError):
        parse("version: '2.0'\nname: bad\n")


def test_packaged_schema_matches_repo_schema() -> None:
    packaged = schema_path().read_text(encoding="utf-8")
    repo = Path("spec/schema.json").read_text(encoding="utf-8")
    assert packaged == repo
