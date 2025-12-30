# Acme Neo Theme

Theme inspired by the Acme editor from Plan 9, available for VS Code, Zed, Ghostty terminal, and Fish shell.

## Project Structure

This is a multi-platform theme project with a centralized configuration system:

```
.
├── vscode/           # VS Code theme (source of truth)
│   ├── src/
│   │   ├── config.py      # Color definitions and theme configurations (SOURCE OF TRUTH)
│   │   ├── template.json  # VS Code theme template
│   │   └── build.py       # Generate VS Code themes
│   ├── themes/            # Generated VS Code theme files
│   └── package.json       # VS Code extension metadata (SOURCE OF TRUTH for theme labels)
│
├── zed/              # Zed editor theme
│   ├── src/
│   │   ├── template.json  # Zed theme template
│   │   └── build.py       # Generate Zed theme (imports from vscode/src/config.py)
│   └── acme-neo.json      # Generated Zed theme (single file with all variants)
│
├── ghostty/          # Ghostty terminal theme
│   ├── src/
│   │   └── build.py       # Generate Ghostty themes (imports from vscode/src/config.py)
│   └── *-neo             # Generated Ghostty theme files (4 files, no extension)
│
└── fish/             # Fish shell theme
    ├── src/
    │   └── build.py       # Generate Fish themes (imports from vscode/src/config.py)
    └── *-neo.theme       # Generated Fish theme files (4 files with .theme extension)
```

## Source of Truth

All themes derive from two authoritative sources:

1. **`vscode/src/config.py`** - Defines:
   - Color palette (70 colors including light/dark variants)
   - Base theme configurations (light, dark_acme, dark_white)
   - Four theme variants with specific color assignments

2. **`vscode/package.json`** - Defines:
   - Theme display labels used across all platforms
   - Theme metadata and categorization

## Theme Variants

All platforms include four theme variants:

| Variant | Description | Background Colors |
|---------|-------------|-------------------|
| **Acme Neo** | Light theme with warm yellow background (classic Acme look) | `paleyellow_1/2/3` |
| **Acme Neo White** | Light theme with pure white background | `white/gray_1/2` |
| **Acme Neo Dark** | Dark theme with warm brown tones | `darkbrown_1/2/3` |
| **Acme Neo Dark Black** | Dark theme with cool blue-grey tones | `darkgray_1/2/3` |

## Building Themes

Each platform has its own build script that imports from the VS Code configuration:

### VS Code Themes
```bash
cd vscode
python3 src/build.py
```
- Generates 4 separate JSON files in `vscode/themes/`
- Uses `template.json` with string formatting
- Output: `{theme-name}-color-theme.json`

### Zed Themes
```bash
cd zed
python3 src/build.py
```
- Generates a single `acme-neo.json` file with all 4 variants
- Imports colors from `../../vscode/src/config.py`
- Uses `template.json` with recursive string formatting
- Includes special handling for borders, scrollbars, and ANSI colors
- Strips alpha channels where needed (Zed doesn't support alpha in some places)

### Ghostty Themes
```bash
cd ghostty
python3 src/build.py
```
- Generates 4 separate theme files (no file extension)
- Imports colors from `../../vscode/src/config.py`
- No template file (generates directly from config)
- Output format: plain text config with `key = value` pairs
- Output: `{theme-name}-neo` (e.g., `acme-neo`, `dark-acme-white-neo`)

### Fish Shell Themes
```bash
cd fish
python3 src/build.py
```
- Generates 4 separate theme files with `.theme` extension
- Imports colors from `../../vscode/src/config.py`
- No template file (generates directly from config)
- Output format: fish shell theme format with `fish_color_*` variables
- Output: `{theme-name}-neo.theme` (e.g., `acme-neo.theme`)
- Defines colors for syntax highlighting, completion pager, and autosuggestions
- Comments and autosuggestions use greyed out colors for lower contrast

## Build Script Architecture

All build scripts follow a similar pattern:

1. **Import Configuration**: Import `themes` and `colors` from `vscode/src/config.py`
2. **Theme Label Lookup**: Read `vscode/package.json` to get display labels
3. **Theme Generation**: Apply theme data to platform-specific templates/formats
4. **Output**: Write generated theme files to platform directories

### Key Functions

- `theme_filename(name)`: Convert theme name to filename format (kebab-case)
- `strip_alpha(color)`: Remove alpha channel from hex colors (for Zed/Ghostty)
- `get_theme_label(package_json_path, theme_name)`: Extract display label from package.json
- `recursive_format(value)`: Recursively apply theme colors to template (VS Code, Zed)

### Platform-Specific Handling

**Zed** (`zed/src/build.py`):
- `darken_color()` / `lighten_color()`: Adjust colors for hover/active states
- `prepare_theme_dict()`: Adds computed colors for borders, scrollbars, ANSI palette
- Strips alpha channels from all colors
- Uses `bg_3` for dark borders, `border_1` for light borders

**Ghostty** (`ghostty/src/build.py`):
- Direct config file generation (no template)
- Generates 16-color ANSI palette
- Includes cursor and selection colors
- Output format: `key = value` pairs

**Fish** (`fish/src/build.py`):
- Direct config file generation (no template)
- Defines colors for syntax highlighting and completion pager
- All syntax elements use foreground color except comments (grey)
- Output format: `fish_color_* colorvalue` pairs

## Color System

The `vscode/src/config.py` defines a comprehensive color palette:

- **Light colors**: paleyellow (1-4), gray (1-4), warm accent colors
- **Dark warm**: darkbrown (1-4), darkteal (1-2), warmgold (1-2), warmbeige (1-2)
- **Dark cool**: darkgray (1-5), darkblue (1-3), coolgray (1-2)
- **Semantic colors**: red, orange, yellow, green, cyan, blue, purple, magenta (1-2 variants)
- **UI elements**: borders, invisible (transparent)

Each theme variant selects specific colors from this palette for:
- Background layers (bg_1, bg_2, bg_3)
- UI elements (ui_bg, ui_hl)
- Foreground text (fg, fg_dim, fg_faint, fg_ghost)
- Highlights (match_bg, match_focus_bg, selection_bg)
- Chrome elements (badge, button)

## Making Changes

### Adding a New Color

1. Add the color to the `colors` dictionary in `vscode/src/config.py`
2. Rebuild all themes:
   ```bash
   cd vscode && python3 src/build.py
   cd ../zed && python3 src/build.py
   cd ../ghostty && python3 src/build.py
   ```

### Modifying a Theme

1. Edit the theme configuration in `vscode/src/config.py` (in the `themes` list)
2. Rebuild all themes (same as above)

### Changing Theme Labels

1. Edit `vscode/package.json` in the `contributes.themes` array
2. Rebuild Zed and Ghostty themes (they read labels from this file)

### Adding Platform-Specific Colors

For Zed-specific adjustments, edit `prepare_theme_dict()` in `zed/src/build.py`
For Ghostty-specific adjustments, edit `generate_ghostty_theme()` in `ghostty/src/build.py`
For Fish-specific adjustments, edit `generate_fish_theme()` in `fish/src/build.py`

## Development Workflow

1. Make changes to `vscode/src/config.py` (colors or theme definitions)
2. Update `vscode/package.json` if changing theme labels
3. Run all build scripts to regenerate themes:
   ```bash
   cd vscode && python3 src/build.py
   cd ../zed && python3 src/build.py
   cd ../ghostty && python3 src/build.py
   cd ../fish && python3 src/build.py
   ```
4. Test in each platform (VS Code, Zed, Ghostty, Fish)
5. Commit changes to both source files and generated themes

## Notes

- Alpha channels in colors (e.g., `#rrggbbaa`) are preserved in VS Code but stripped for Zed/Ghostty/Fish
- Zed themes use a single JSON file with multiple variants under a `themes` array
- Ghostty themes are individual config files without file extensions
- Fish themes are individual config files with `.theme` extensions
- The build scripts are idempotent - safe to run multiple times
- Fish themes follow the minimal aesthetic: only comments and errors have distinct colors
