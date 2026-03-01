# Changelog

All notable changes to the AQML specification will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/), and this project adheres to [Semantic Versioning](https://semver.org/).

---

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
