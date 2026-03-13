from __future__ import annotations

from pathlib import Path

from aqml.validator import validate


def test_all_examples_validate() -> None:
    examples = sorted(Path("examples").glob("*.aqml"))
    assert examples

    for path in examples:
        result = validate(path)
        assert result.valid, f"{path}: {[f'{item.path}: {item.message}' for item in result.errors]}"
