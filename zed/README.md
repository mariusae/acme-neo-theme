# Acme Theme for Zed

Port of the [Acme Theme for VS Code](https://github.com/mariusae/acme-theme-vscode) to the Zed editor.

These themes are inspired by the classic Acme editor from Plan 9, featuring minimal syntax highlighting and clean, readable color schemes.

## Themes

This port includes all four variants from the original VS Code theme:

- **Acme Neo** - Light theme with warm yellow background (#ffffea)
- **Acme Neo White** - Light theme with pure white background (#ffffff)
- **Acme Neo Dark** - Dark theme with warm brown tones
- **Acme Neo Dark Black** - Dark theme with cool blue-grey tones

## Installation

1. Open Zed's theme directory:
   ```bash
   mkdir -p ~/.config/zed/themes
   ```

2. Copy the theme file:
   ```bash
   cp acme-neo.json ~/.config/zed/themes/
   ```

3. Open Zed and select the theme:
   - Open the command palette (Cmd+Shift+P on macOS, Ctrl+Shift+P on Linux)
   - Type "theme selector: toggle" or "zed: select theme"
   - Choose one of the Acme Neo variants:
     - Acme Neo (light with yellow background)
     - Acme Neo White (light with white background)
     - Acme Neo Dark (dark with warm tones)
     - Acme Neo Dark Black (dark with cool tones)

Alternatively, you can set the theme in your Zed `settings.json`:

```json
{
  "theme": "Acme Neo"
}
```

## Theme Philosophy

The Acme theme follows the minimalist philosophy of the Plan 9 Acme editor:

- **Minimal syntax highlighting** - Most code elements use the foreground color, reducing visual noise
- **Strategic color use** - Colors are used sparingly:
  - Strings in green
  - Comments in muted gray
  - Regex patterns in magenta
  - Links and hints in blue
- **Clean UI** - Subtle backgrounds and borders that don't distract from content
- **Excellent readability** - Carefully selected backgrounds and contrast ratios

## Building

These themes are automatically generated from the VS Code theme configuration to ensure consistency across all platforms.

The theme files are built from:
- **Color definitions**: `vscode/src/config.py` (source of truth for all colors)
- **Theme metadata**: `vscode/package.json` (source of truth for theme names and variants)

To rebuild the themes:

```bash
cd zed
python3 src/build.py
```

This will regenerate `acme-neo.json` with all four theme variants.

## Theme Preview

### Acme Neo (Light)
- Background: Warm yellow (#ffffea) - classic Acme look
- Foreground: Black (#000000)
- UI accents: Cyan tones
- Minimal, distraction-free color scheme

### Acme Neo White (Light)
- Background: Pure white (#ffffff)
- Foreground: Black (#000000)
- UI accents: Blue tones
- Clean, modern appearance

### Acme Neo Dark
- Background: Dark brown (#1a1612)
- Foreground: Warm beige (#d4c5a9)
- UI accents: Dark teal
- Comfortable for low-light environments with warm tones

### Acme Neo Dark Black
- Background: Dark blue-grey (#1a1d23)
- Foreground: Cool grey (#c8ccd4)
- UI accents: Dark blue
- Modern dark theme with good contrast and cool tones

## About Acme

The Acme editor from Plan 9 is known for its minimalist philosophy and excellent readability. These themes bring that same aesthetic to Zed, with carefully selected colors that reduce visual clutter while maintaining clear distinction between different elements.

## Credits

- Original VS Code theme by [Marius Eriksen](https://github.com/mariusae)
- Zed port generated from the VS Code theme configuration

## License

Same license as the original Acme Theme for VS Code (MIT License).
