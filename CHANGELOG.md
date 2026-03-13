# Changelog

All notable changes to the AQML specification will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/), and this project adheres to [Semantic Versioning](https://semver.org/).

---

## [2.0.0-draft] — 2026-03-13

### Added
- AQML v2 executable-profile specification (`spec/aqml-v2.0.md`)
- JSON Schema aligned with the current AurumQ parser and evaluator
- Documentation for nested logic groups, `compare_all`, tiered scoring, and percentage-based exits
- Editor snippets and syntax updates for `signal_type`, `filters`, grouped logic, and v2 rule keys

### Changed
- Synced all examples from legacy v1-style keys to the executable v2 syntax
- Replaced `weight + scoring.mode` examples with `scoring.rule_points`
- Migrated `stop_loss`, `take_profit`, and `trailing_stop` to percentage-based `*_pct` fields
- Converted historical `lookback` examples to explicit `offset`-based logic groups

### Notes
- `spec/aqml-v1.0.md` now points to the active v2 spec for compatibility
- The repository now documents the executable profile that AurumQ actually runs

## [1.0.0-draft] — 2026-03-01

### Added
- AQML v1.0 specification draft
- JSON Schema validator (`spec/schema.json`)
- 5 rule types: `compare`, `range`, `signal`, `pattern`, `breakout`
- Top-level blocks: `universe`, `rules`, `scoring`, `exit_rules`, `portfolio`, `risk`
- 17+ standard technical indicators (CORE + EXTENDED)
- 3 example strategies: momentum breakout, mean reversion, multi-factor value
- VS Code extension with TextMate grammar and 11 snippets
- JetBrains file type definition
- Vim/Neovim filetype detection and syntax highlighting
- Quick start guide
- Contributing guidelines
- Apache 2.0 license

### Notes
- This is the initial draft release for community review
- The `.aqml` file extension is established as the standard
- Spec is subject to change based on community feedback before 1.0 final
