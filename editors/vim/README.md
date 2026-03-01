# AQML for Vim / Neovim

Filetype detection and syntax highlighting for AQML files.

## Installation

### Manual

```bash
# Vim
mkdir -p ~/.vim/ftdetect ~/.vim/syntax
cp ftdetect/aqml.vim ~/.vim/ftdetect/
cp syntax/aqml.vim ~/.vim/syntax/

# Neovim
mkdir -p ~/.config/nvim/ftdetect ~/.config/nvim/syntax
cp ftdetect/aqml.vim ~/.config/nvim/ftdetect/
cp syntax/aqml.vim ~/.config/nvim/syntax/
```

### With vim-plug

```vim
" In your .vimrc / init.vim:
Plug 'yupoet/aqml', { 'rtp': 'editors/vim' }
```

### With lazy.nvim

```lua
{ "yupoet/aqml", config = function()
  vim.filetype.add({ extension = { aqml = "aqml" } })
end }
```

## Features

- Automatic `.aqml` filetype detection
- YAML base syntax inherited
- AQML-specific highlights for rule types, indicators, signals, patterns
- Comment toggling with `#`
