# AQML Editor Support

IDE and editor integrations for `.aqml` files.

| Editor | Features | Directory |
|--------|----------|-----------|
| **VS Code** | Syntax highlighting, v2 snippets, language config | [`vscode/`](vscode/) |
| **JetBrains** | File type recognition, 4-group keyword highlighting | [`jetbrains/`](jetbrains/) |
| **Vim / Neovim** | Filetype detection, YAML-based syntax highlighting | [`vim/`](vim/) |

## Quick Setup

### VS Code
```bash
cp -r editors/vscode ~/.vscode/extensions/aqml-0.2.0
# Restart VS Code
```

### JetBrains (PyCharm, IntelliJ, etc.)
```
Settings → Editor → File Types → ⚙️ Import → select editors/jetbrains/aqml.xml
```

### Vim / Neovim
```bash
cp editors/vim/ftdetect/aqml.vim ~/.vim/ftdetect/
cp editors/vim/syntax/aqml.vim ~/.vim/syntax/
```

## GitHub

`.aqml` files get YAML syntax highlighting on GitHub automatically via `.gitattributes`. No additional setup needed.
