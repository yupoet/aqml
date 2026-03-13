# AQML for Visual Studio Code

Syntax highlighting, snippets, and language support for [AQML](https://github.com/yupoet/aqml) (Aurum Quant Markup Language) strategy files.

This editor bundle targets the **AQML v2 executable profile** used by AurumQ.

## Features

- 🎨 **Syntax highlighting** — AQML-aware colors for rule types, indicators, signals, operators
- ⚡ **Snippets** — Rapid strategy authoring with `aqml`, `rule-compare`, `rule-signal`, etc.
- 📁 **File association** — Automatic `.aqml` file recognition
- 🔤 **Comment toggling** — `Ctrl+/` for `#` comments
- 📐 **Code folding** — Collapse sections by indentation

## Installation

### From VS Code Marketplace (coming soon)

```
ext install aurumq.aqml
```

### Manual Installation

1. Copy this `vscode/` directory to `~/.vscode/extensions/aqml-0.2.0/`
2. Restart VS Code
3. Open any `.aqml` file

## Snippets

| Prefix | Description |
|--------|-------------|
| `aqml` | Complete v2 strategy scaffold |
| `rule-compare` | Compare rule |
| `rule-compare-all` | Compare against multiple indicators |
| `rule-range` | Range rule |
| `rule-signal` | Signal detection rule |
| `rule-pattern` | Candlestick pattern rule |
| `rule-breakout` | Breakout rule |
| `rule-or` | OR logic group |
| `filters` | Filters block |
| `scoring` | Scoring block |
| `scoring-tier` | Tiered scoring entry |
| `exit` | Exit rules block |
| `portfolio` | Portfolio block |
| `risk` | Risk management block |

## Highlighting Preview

AQML highlighting distinguishes:
- **Section keywords** (`rules`, `exit_rules`, `portfolio`, `risk`) — bold accent
- **Rule types** (`compare`, `compare_all`, `signal`, `breakout`) — type color
- **Indicators** (`rsi14`, `macd_dif`, `ma20`) — variable color
- **Signals** (`golden_cross`, `oversold`) — constant color
- **Operators** (`>`, `<=`, `!=`) — operator color
- **Numbers** and **strings** — standard literal colors
