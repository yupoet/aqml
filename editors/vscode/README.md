# AQML for Visual Studio Code

Syntax highlighting, schema-aware validation, and snippets for [AQML](https://github.com/yupoet/aqml) (Aurum Quant Markup Language) strategy files.

This extension targets the **AQML v2 executable profile** used by AurumQ.

## Features

- Syntax highlighting for AQML sections, rule types, indicators, operators, and signals
- Snippets for common strategy blocks such as `aqml`, `rule-compare`, `rule-signal`, and `portfolio`
- Automatic `.aqml` file association
- YAML schema validation, hover text, and completion through the Red Hat YAML extension
- Bundled local schema copy so validation works from the packaged `.vsix`

## Installation

### VSIX Package

```bash
cd editors/vscode
npm ci
npm run package
code --install-extension ./aqml-vscode-0.3.0.vsix
```

### Marketplace

After the extension is published to the VS Code Marketplace:

```bash
code --install-extension aurumq.aqml
```

The extension declares `redhat.vscode-yaml` as a dependency, so VS Code will install the YAML language support automatically.

## Packaging

```bash
cd editors/vscode
npm ci
npm run package
```

This produces a versioned `.vsix` and refreshes `schema/aqml.schema.json` from `../../spec/schema.json` before packaging.

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

## Release Flow

- CI packaging: [`.github/workflows/vscode-extension.yml`](../../.github/workflows/vscode-extension.yml)
- Marketplace publish: [`.github/workflows/publish-vscode-extension.yml`](../../.github/workflows/publish-vscode-extension.yml)
- Release guide: [`RELEASING.md`](RELEASING.md)
