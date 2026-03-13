"""AQML schema access helpers."""

from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path
from typing import Any


def schema_path() -> Path:
    """Return the active schema path."""

    package_schema = Path(__file__).with_name("data").joinpath("schema.json")
    if package_schema.exists():
        return package_schema

    repo_schema = Path(__file__).resolve().parents[2] / "spec" / "schema.json"
    return repo_schema


@lru_cache(maxsize=1)
def load_schema() -> dict[str, Any]:
    """Load the bundled AQML JSON Schema."""

    return json.loads(schema_path().read_text(encoding="utf-8"))
