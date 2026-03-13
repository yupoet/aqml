"""AQML loading and normalization helpers."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

from aqml.models import ValidationIssue


def _is_probable_path(value: str) -> bool:
    if "\n" in value or "\r" in value:
        return False
    return Path(value).exists()


def read_text(source: str | Path) -> tuple[str, Path | None]:
    """Read AQML from a path or accept raw YAML text."""

    if isinstance(source, Path):
        return source.read_text(encoding="utf-8"), source

    if _is_probable_path(source):
        path = Path(source)
        return path.read_text(encoding="utf-8"), path

    return source, None


def load_aqml(
    source: str | Path,
) -> tuple[dict[str, Any] | None, list[ValidationIssue], str, Path | None]:
    """Parse AQML text into a dictionary."""

    text, path = read_text(source)

    try:
        data = yaml.safe_load(text)
    except yaml.YAMLError as exc:
        return None, [ValidationIssue(path="$", message=f"YAML parse error: {exc}")], text, path

    if not isinstance(data, dict):
        return (
            None,
            [ValidationIssue(path="$", message="AQML document must be a YAML object")],
            text,
            path,
        )

    return data, [], text, path


def normalize(source: str | Path) -> str:
    """Normalize AQML YAML formatting via safe parse and dump."""

    data, issues, _, _ = load_aqml(source)
    if issues:
        message = "; ".join(issue.message for issue in issues)
        raise ValueError(message)

    return yaml.safe_dump(
        data,
        allow_unicode=True,
        default_flow_style=False,
        sort_keys=False,
        width=1000,
    )
