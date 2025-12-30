# acme-neo-theme

Theme inspired by the Acme editor from Plan 9, available for VS Code, Zed, Ghostty terminal, and Fish shell.

## Building

All themes are generated from the same source configuration to ensure consistency across platforms.

### VS Code Themes

```bash
cd vscode
python3 src/build.py
```

### Zed Themes

```bash
cd zed
python3 src/build.py
```

### Ghostty Themes

```bash
cd ghostty
python3 src/build.py
```

### Fish Shell Themes

```bash
cd fish
python3 src/build.py
```

All build processes use:
- `vscode/src/config.py` as the source of truth for colors
- `vscode/package.json` as the source of truth for theme metadata

## Theme Variants

All platforms include four theme variants:

- **Acme Neo** - Light theme with warm yellow background (classic Acme look)
- **Acme Neo White** - Light theme with pure white background
- **Acme Neo Dark** - Dark theme with warm brown tones
- **Acme Neo Dark Black** - Dark theme with cool blue-grey tones
