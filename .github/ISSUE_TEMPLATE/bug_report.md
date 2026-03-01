---
name: Bug Report / Spec Issue
about: Report an ambiguity, inconsistency, or error in the AQML specification
title: "[Bug] "
labels: bug, spec
assignees: yupoet
---

## Section Reference

Which part of the spec is affected? (e.g., "Section 5.2 — Rule Type: compare")

## Description

A clear description of the issue.

## Expected Behavior

What the spec should say or how it should work.

## Current Behavior

What actually happens or what is currently written.

## Example AQML

```yaml
# Minimal .aqml file that demonstrates the issue
aqml: "1.0"
name: Bug Example
rules:
  - type: compare
    field: rsi14
    operator: "<"
    value: 30
```

## Additional Context

Any other context, screenshots, or references.
