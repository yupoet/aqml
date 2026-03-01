# Security Policy

## Scope

AQML is a file format specification. It does not execute code. However, security considerations exist in:

1. **Parsers and validators** — Implementations consuming `.aqml` files should guard against YAML deserialization attacks (e.g., always use `yaml.safe_load()` in Python, never `yaml.load()`).
2. **Strategy content** — AQML files may contain proprietary trading logic. Handle with appropriate access controls.

## Reporting a Vulnerability

If you discover a security issue in the AQML specification, reference implementation, or tooling:

1. **Do not** open a public GitHub issue
2. Email **paris@aurumq.ai** with:
   - Description of the vulnerability
   - Steps to reproduce
   - Potential impact assessment
3. You will receive acknowledgment within 48 hours
4. We aim to address confirmed issues within 7 days

## Supported Versions

| Version | Supported |
|---------|-----------|
| 1.0-draft | ✅ |

## Best Practices for Implementations

- Always use safe YAML parsing (`safe_load`, not `load`)
- Validate against JSON Schema before processing
- Sanitize numeric inputs (reject NaN, Infinity)
- Limit file size to prevent resource exhaustion
- Do not evaluate arbitrary expressions within field values
