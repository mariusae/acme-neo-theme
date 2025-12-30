# Fish Shell Themes

Fish shell themes for the Acme Neo color scheme.

## Installation

Fish themes should be placed in `~/.config/fish/themes/` directory:

```bash
# Create themes directory if it doesn't exist
mkdir -p ~/.config/fish/themes

# Copy the theme file you want to use
cp acme-neo.theme ~/.config/fish/themes/
```

## Usage

To apply a theme, use the `fish_config` command or set it directly:

```bash
# Using fish_config (opens web interface)
fish_config theme choose

# Or set directly in your config.fish
echo "fish_config theme choose acme-neo" >> ~/.config/fish/config.fish
```

## Available Themes

- `acme-neo.theme` - Light theme with warm yellow background
- `acme-white-neo.theme` - Light theme with pure white background
- `dark-acme-neo.theme` - Dark theme with warm brown tones
- `dark-acme-white-neo.theme` - Dark theme with cool blue-grey tones

## Building

The fish themes are generated from the source configuration:

```bash
cd fish
python3 src/build.py
```

This imports colors from `vscode/src/config.py` and generates all theme variants.

## Theme Features

Fish themes define colors for:
- **Syntax highlighting** - commands, parameters, quotes, operators, etc.
- **Comments** - lower contrast grey (following Acme neo philosophy)
- **Errors** - red color for error messages
- **Autosuggestions** - grey color
- **Completion pager** - colors for completions and descriptions
- **Selection** - background color for selected text

All syntax elements except comments and errors use the same foreground color, maintaining the minimal aesthetic of the Acme editor.
