"""AQML validator exceptions."""

from __future__ import annotations

from aqml.models import ValidationIssue


class AQMLError(Exception):
    """Base exception for AQML operations."""


class AQMLValidationError(AQMLError):
    """Raised when validation fails and an exception API is preferred."""

    def __init__(self, issues: list[ValidationIssue]):
        self.issues = issues
        message = (
            "; ".join(f"{issue.path}: {issue.message}" for issue in issues)
            or "AQML validation failed"
        )
        super().__init__(message)
