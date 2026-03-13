from __future__ import annotations

from pathlib import Path

from aqml.cli import main


def test_cli_validate_example(capsys) -> None:
    example = Path("examples/simple-rsi.aqml")
    exit_code = main(["validate", str(example)])
    captured = capsys.readouterr()

    assert exit_code == 0
    assert f"OK {example}" in captured.out


def test_cli_schema_path(capsys) -> None:
    exit_code = main(["schema-path"])
    captured = capsys.readouterr()

    assert exit_code == 0
    assert captured.out.strip().endswith("schema.json")
