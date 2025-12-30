# acme-neo-theme

Theme inspired by the Acme editor from Plan 9, available for both VS Code and Ghostty terminal.

## Building

### VS Code Themes

```bash
cd vscode
python3 src/build.py
```

### Ghostty Themes

```bash
cd ghostty
python3 src/build.py
```

Both build processes use `vscode/src/config.py` as the source of truth for colors and `vscode/package.json` for theme metadata.
