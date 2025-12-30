#!/usr/bin/env python3

import json
import os
import re
import sys

# Add parent directories to path to import from vscode
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../vscode/src"))

from config import themes, colors


def theme_filename(name):
    """Convert theme name to filename format."""
    filename = re.sub(r"[^\w\s-]", "", name.lower())
    filename = re.sub(r"[-\s]+", "-", filename)
    return filename.strip("-")


def strip_alpha(color):
    """Strip alpha channel from hex color if present."""
    if len(color) > 7:
        return color[:7]
    return color


def get_theme_label(package_json_path, theme_name):
    """Get the label from package.json for a given theme name."""
    with open(package_json_path, "r") as f:
        package = json.load(f)

    theme_filename_pattern = theme_filename(theme_name)
    for theme in package.get("contributes", {}).get("themes", []):
        path = theme.get("path", "")
        if theme_filename_pattern in path:
            return theme.get("label", theme_name)

    return theme_name


def generate_ghostty_theme(theme_dict, output_file, label):
    """Generate a ghostty theme file from a theme dictionary."""

    # Get base colors
    bg = theme_dict.get("bg_1")
    fg = strip_alpha(theme_dict.get("fg"))
    selection_bg = strip_alpha(theme_dict.get("selection_bg"))

    # Determine palette based on theme type
    if theme_dict.get("type") == "dark":
        # Dark theme palette
        palette_0 = colors["black"]
        palette_7 = theme_dict.get("bg_3")
        palette_8 = theme_dict.get("gray")
        palette_15 = colors["white"]
    else:
        # Light theme palette
        palette_0 = colors["black"]
        palette_7 = theme_dict.get("bg_3")
        palette_8 = theme_dict.get("gray")
        palette_15 = colors["white"]

    # Build the theme file content
    lines = [
        f"# {label} - {'Dark' if theme_dict.get('type') == 'dark' else 'Light'} theme inspired by the Acme editor from Plan 9",
        "# Generated from VS Code Acme Theme configuration",
        "",
        f"background = {bg}",
        f"foreground = {fg}",
        "",
        f"cursor-color = {fg}",
        "cursor-style = block",
        "cursor-style-blink = false",
        "",
        f"selection-background = {selection_bg}",
        f"selection-foreground = {fg}",
        "",
        "# 16-color palette (ANSI colors)",
        f"palette = 0={palette_0}",
        f"palette = 1={colors['red_1']}",
        f"palette = 2={colors['green_1']}",
        f"palette = 3={colors['yellow_1']}",
        f"palette = 4={colors['blue_1']}",
        f"palette = 5={colors['magenta_1']}",
        f"palette = 6={colors['cyan_1']}",
        f"palette = 7={palette_7}",
        f"palette = 8={palette_8}",
        f"palette = 9={colors['red_2']}",
        f"palette = 10={colors['green_2']}",
        f"palette = 11={colors['yellow_2']}",
        f"palette = 12={colors['blue_2']}",
        f"palette = 13={colors['magenta_2']}",
        f"palette = 14={colors['cyan_2']}",
        f"palette = 15={palette_15}",
        ""
    ]

    with open(output_file, "w") as f:
        f.write("\n".join(lines))


def main():
    # Get paths
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(script_dir, "..")
    package_json_path = os.path.join(script_dir, "../../vscode/package.json")

    # Generate themes
    for theme_dict in themes:
        name = theme_dict.get("name")
        output_name = f"{theme_filename(name)}-neo"
        output_path = os.path.join(output_dir, output_name)

        # Get label from package.json
        label = get_theme_label(package_json_path, name)

        generate_ghostty_theme(theme_dict, output_path, label)
        print(f"Generated: {output_name}")


if __name__ == "__main__":
    main()
