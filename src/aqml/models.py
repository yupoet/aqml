"""Shared models for AQML validation."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class ValidationIssue:
    """Single validation issue."""

    path: str
    message: str
    level: str = "error"


@dataclass(slots=True)
class ValidationResult:
    """Validation result container."""

    valid: bool
    errors: list[ValidationIssue] = field(default_factory=list)
    warnings: list[ValidationIssue] = field(default_factory=list)
    data: dict[str, Any] | None = None

    def add_error(self, path: str, message: str) -> None:
        self.errors.append(ValidationIssue(path=path, message=message, level="error"))
        self.valid = False

    def add_warning(self, path: str, message: str) -> None:
        self.warnings.append(ValidationIssue(path=path, message=message, level="warning"))
