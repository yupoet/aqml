# AQML for JetBrains IDEs

File type recognition and syntax highlighting for AQML files in IntelliJ IDEA, PyCharm, WebStorm, GoLand, and other JetBrains IDEs.

## Installation

### Method 1: Import File Type (Recommended)

1. Open **Settings** → **Editor** → **File Types**
2. Click the **⚙️** (gear) icon → **Import**
3. Select the `aqml.xml` file from this directory
4. Click **OK**

### Method 2: Manual Copy

Copy `aqml.xml` to your IDE's config directory:

| OS | Path |
|----|------|
| macOS | `~/Library/Application Support/JetBrains/<IDE>/filetypes/aqml.xml` |
| Linux | `~/.config/JetBrains/<IDE>/filetypes/aqml.xml` |
| Windows | `%APPDATA%\JetBrains\<IDE>\filetypes\aqml.xml` |

Replace `<IDE>` with your specific IDE name (e.g., `PyCharm2024.3`, `IntelliJIdea2024.3`).

### Method 3: Register Manually

1. **Settings** → **Editor** → **File Types**
2. Click **+** to add a new file type
3. Name: `AQML`, Description: `AQML Strategy File`
4. Line comment: `#`
5. Add keywords from each group in `aqml.xml`
6. Under **Registered Patterns**, add `*.aqml`

## Highlighting Groups

| Group | Color | Contents |
|-------|-------|----------|
| Keywords 1 | Bold accent | Top-level sections (`rules`, `portfolio`, `risk`) |
| Keywords 2 | Secondary | Field names (`left`, `right`, `comment`, `rule_points`) |
| Keywords 3 | Type color | Rule types and signals (`compare_all`, `golden_cross`) |
| Keywords 4 | Constant color | Enums and values (`buy`, `sell`, `up`, `ST`) |

## YAML Base Support

JetBrains IDEs have built-in YAML support. AQML files inherit YAML structure recognition (indentation, folding, bracket matching) automatically, with the added AQML-specific keyword highlighting on top.
