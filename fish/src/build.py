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


def generate_fish_theme(theme_dict, output_file, label, universal=False):
    """Generate a fish theme file from a theme dictionary."""

    # Get base colors
    bg = strip_alpha(theme_dict.get("bg_1"))
    fg = strip_alpha(theme_dict.get("fg"))
    gray = strip_alpha(theme_dict.get("gray"))

    # For comments, use gray (same as Zed, since Fish doesn't support alpha transparency)
    comment_color = gray

    # For universal theme, use medium-contrast colors that work on both light and dark backgrounds
    if universal:
        # Use blue_muted - balanced luminance for visibility on both light and dark terminals
        selection_bg = strip_alpha(colors["blue_muted"])  # Medium blue-gray
        selected_item_bg = strip_alpha(colors["blue_muted"])  # Same for consistency
        selected_fg = colors["white"]  # White text on dark backgrounds
    else:
        selection_bg = strip_alpha(theme_dict.get("selection_bg"))
        selected_item_bg = strip_alpha(theme_dict.get("ui_hl"))
        selected_fg = fg

    # Build the theme file content
    lines = [
        f"# {label}",
        f"# {'Universal' if universal else 'Dark' if theme_dict.get('type') == 'dark' else 'Light'} theme inspired by the Acme editor from Plan 9",
        "# Generated from VS Code Acme Theme configuration",
        "",
        "# Syntax Highlighting Colors",
        f"fish_color_normal {fg}",
        f"fish_color_command {fg}",
        f"fish_color_keyword {fg}",
        f"fish_color_quote {fg}",
        f"fish_color_redirection {fg}",
        f"fish_color_end {fg}",
        f"fish_color_error {strip_alpha(colors['red_1'])}",
        f"fish_color_param {fg}",
        f"fish_color_comment {comment_color}",
        f"fish_color_selection --background={selection_bg}",
        f"fish_color_operator {fg}",
        f"fish_color_escape {fg}",
        f"fish_color_autosuggestion {gray}",
        "",
        "# Completion Pager Colors",
        f"fish_pager_color_progress {gray}",
        f"fish_pager_color_background",
        f"fish_pager_color_prefix {fg}",
        f"fish_pager_color_completion {fg}",
        f"fish_pager_color_description {gray}",
        f"fish_pager_color_selected_background --background={selected_item_bg}",
        f"fish_pager_color_selected_prefix {selected_fg}",
        f"fish_pager_color_selected_completion {selected_fg}",
        f"fish_pager_color_selected_description {selected_fg}",
        f"fish_pager_color_secondary_background",
        f"fish_pager_color_secondary_prefix {fg}",
        f"fish_pager_color_secondary_completion {fg}",
        f"fish_pager_color_secondary_description {gray}",
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
        output_name = f"{theme_filename(name)}-neo.theme"
        output_path = os.path.join(output_dir, output_name)

        # Get label from package.json
        label = get_theme_label(package_json_path, name)

        generate_fish_theme(theme_dict, output_path, label)
        print(f"Generated: {output_name}")

    # Generate universal theme based on the first light theme (Acme)
    light_theme = themes[0]  # Acme theme
    universal_output_path = os.path.join(output_dir, "acme-universal-neo.theme")
    generate_fish_theme(light_theme, universal_output_path, "Acme Neo Universal", universal=True)
    print(f"Generated: acme-universal-neo.theme")


if __name__ == "__main__":
    main()
