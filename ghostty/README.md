# Acme Theme for Ghostty

Port of the [Acme Theme for VS Code](https://github.com/mariusae/acme-theme-vscode) to Ghostty terminal.

These themes are inspired by the classic Acme editor from Plan 9, featuring minimal syntax highlighting and clean, readable color schemes.

## Themes

This port includes all four variants from the original VS Code theme:

- **acme-neo** - Light theme with warm yellow background (#ffffea)
- **acme-white-neo** - Light theme with pure white background (#ffffff)
- **dark-acme-neo** - Dark theme with warm brown tones
- **dark-acme-white-neo** - Dark theme with cool blue-grey tones

## Installation

### Method 1: Direct Copy (Recommended)

Copy the theme file(s) you want to use to Ghostty's configuration directory:

```bash
# Create the themes directory if it doesn't exist
mkdir -p ~/.config/ghostty/themes

# Copy a theme (choose one or copy all)
cp ghostty-themes/acme-neo ~/.config/ghostty/themes/
cp ghostty-themes/acme-white-neo ~/.config/ghostty/themes/
cp ghostty-themes/dark-acme-neo ~/.config/ghostty/themes/
cp ghostty-themes/dark-acme-white-neo ~/.config/ghostty/themes/
```

Then add this line to your `~/.config/ghostty/config` file:

```
theme = acme-neo
```

Replace `acme-neo` with whichever theme variant you prefer.

### Method 2: Include Directly

Alternatively, you can include the theme directly in your Ghostty config:

```bash
# Add to your ~/.config/ghostty/config
echo "theme = /path/to/ghostty-themes/acme-neo" >> ~/.config/ghostty/config
```

### Method 3: Inline Configuration

You can also copy the theme settings directly into your `~/.config/ghostty/config` file if you prefer to keep everything in one place.

## Switching Themes

To switch between themes, simply change the `theme` line in your `~/.config/ghostty/config`:

```
theme = acme-neo           # Light with yellow background
theme = acme-white-neo     # Light with white background
theme = dark-acme-neo      # Dark with warm tones
theme = dark-acme-white-neo # Dark with cool tones
```

## Theme Preview

### Acme Neo (Light)
- Background: Warm yellow (#ffffea) - classic Acme look
- Foreground: Black (#000000)
- Minimal, distraction-free color scheme

### Acme White Neo (Light)
- Background: Pure white (#ffffff)
- Foreground: Black (#000000)
- Clean, modern appearance

### Dark Acme Neo
- Background: Dark brown (#1a1612)
- Foreground: Warm beige (#d4c5a9)
- Comfortable for low-light environments

### Dark Acme White Neo
- Background: Dark blue-grey (#1a1d23)
- Foreground: Cool grey (#c8ccd4)
- Modern dark theme with good contrast

## Building

These themes are automatically generated from the VS Code theme configuration to ensure consistency across all platforms.

The theme files are built from:
- **Color definitions**: `vscode/src/config.py` (source of truth for all colors)
- **Theme metadata**: `vscode/package.json` (source of truth for theme names and variants)

To rebuild the themes:

```bash
cd ghostty
python3 src/build.py
```

This will regenerate all theme files in the `ghostty/` directory.

## About Acme

The Acme editor from Plan 9 is known for its minimalist philosophy and excellent readability. These themes bring that same aesthetic to your terminal, with carefully selected colors that reduce visual clutter while maintaining clear distinction between different elements.

## Credits

- Original VS Code theme by [Marius Eriksen](https://github.com/mariusae)
- Ghostty port created using terminal color definitions from the VS Code theme

## License

Same license as the original Acme Theme for VS Code (MIT License).
