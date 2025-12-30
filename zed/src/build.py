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


def add_alpha(color, alpha):
    """Add alpha channel to hex color."""
    # Strip any existing alpha
    color = strip_alpha(color)
    return color + alpha


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


def darken_color(hex_color, amount=0.1):
    """Darken a hex color by a percentage (0.0 to 1.0)."""
    hex_color = strip_alpha(hex_color)
    r = int(hex_color[1:3], 16)
    g = int(hex_color[3:5], 16)
    b = int(hex_color[5:7], 16)

    r = int(r * (1 - amount))
    g = int(g * (1 - amount))
    b = int(b * (1 - amount))

    return f"#{r:02x}{g:02x}{b:02x}"


def lighten_color(hex_color, amount=0.1):
    """Lighten a hex color by a percentage (0.0 to 1.0)."""
    hex_color = strip_alpha(hex_color)
    r = int(hex_color[1:3], 16)
    g = int(hex_color[3:5], 16)
    b = int(hex_color[5:7], 16)

    r = int(r + (255 - r) * amount)
    g = int(g + (255 - g) * amount)
    b = int(b + (255 - b) * amount)

    return f"#{r:02x}{g:02x}{b:02x}"


def prepare_theme_dict(theme_dict):
    """Prepare a theme dictionary with all required Zed colors."""
    is_dark = theme_dict.get("type") == "dark"

    # Base colors
    bg_1 = strip_alpha(theme_dict.get("bg_1"))
    fg = strip_alpha(theme_dict.get("fg"))

    # Prepare the extended dictionary with all needed colors
    zed_dict = {
        **theme_dict,
        # Appearance
        "appearance": "dark" if is_dark else "light",

        # Strip alpha from base colors
        "bg_1": bg_1,
        "bg_2": strip_alpha(theme_dict.get("bg_2")),
        "bg_3": strip_alpha(theme_dict.get("bg_3")),
        "ui_bg": strip_alpha(theme_dict.get("ui_bg")),
        "ui_hl": strip_alpha(theme_dict.get("ui_hl")),
        "fg": fg,
        "gray": strip_alpha(theme_dict.get("gray")),
        "match_bg": strip_alpha(theme_dict.get("match_bg")),
        "match_focus_bg": strip_alpha(theme_dict.get("match_focus_bg")),
        "selection_bg": strip_alpha(theme_dict.get("selection_bg")),

        # Borders - use subtle bg_3 for dark themes, border_1 for light themes
        "border": strip_alpha(theme_dict.get("bg_3")) if is_dark else strip_alpha(theme_dict.get("border_1", colors["border_1"])),
        "border_focused": strip_alpha(theme_dict.get("blue_1", colors["blue_1"])),
        "border_transparent": add_alpha(bg_1, "00"),

        # Scrollbar colors
        "scrollbar_thumb": strip_alpha(theme_dict.get("gray")),
        "scrollbar_hover": lighten_color(theme_dict.get("gray")) if is_dark else darken_color(theme_dict.get("gray")),
        "scrollbar_active": lighten_color(theme_dict.get("gray"), 0.2) if is_dark else darken_color(theme_dict.get("gray"), 0.2),

        # ANSI colors
        "ansi_black": colors["black"],
        "ansi_bright_black": strip_alpha(theme_dict.get("gray")),
        "ansi_white": strip_alpha(theme_dict.get("bg_3")),
        "ansi_bright_white": colors["white"],

        # Standard colors (stripped of alpha)
        "red_1": strip_alpha(colors["red_1"]),
        "red_2": strip_alpha(colors["red_2"]),
        "green_1": strip_alpha(colors["green_1"]),
        "green_2": strip_alpha(colors["green_2"]),
        "yellow_1": strip_alpha(colors["yellow_1"]),
        "yellow_2": strip_alpha(colors["yellow_2"]),
        "blue_1": strip_alpha(colors["blue_1"]),
        "blue_2": strip_alpha(colors["blue_2"]),
        "cyan_1": strip_alpha(colors["cyan_1"]),
        "cyan_2": strip_alpha(colors["cyan_2"]),
        "magenta_1": strip_alpha(colors["magenta_1"]),
        "magenta_2": strip_alpha(colors["magenta_2"]),
        "orange_1": strip_alpha(colors["orange_1"]),
    }

    return zed_dict


def generate_zed_themes(package_json_path, template_path, output_path):
    """Generate a single Zed theme file with all variants."""

    # Load template
    with open(template_path, "r") as f:
        template = json.load(f)

    # Prepare all theme variants
    theme_variants = []

    for theme_dict in themes:
        name = theme_dict.get("name")
        label = get_theme_label(package_json_path, name)

        # Prepare theme dictionary with all colors
        zed_dict = prepare_theme_dict(theme_dict)
        zed_dict["label"] = label

        # Create a deep copy of the template for this variant
        variant = json.loads(json.dumps(template["themes"][0]))

        # Recursively format the variant with theme colors
        def recursive_format(value):
            if isinstance(value, str):
                try:
                    return value.format(**zed_dict)
                except KeyError as e:
                    print(f"Warning: Missing key {e} for theme {name}")
                    return value
            elif isinstance(value, list):
                return [recursive_format(item) for item in value]
            elif isinstance(value, dict):
                return {key: recursive_format(val) for key, val in value.items()}
            else:
                return value

        variant = recursive_format(variant)
        theme_variants.append(variant)

    # Create the final output
    output = {
        "name": "Acme Neo",
        "author": "mariusae",
        "themes": theme_variants,
        "$schema": "https://zed.dev/schema/themes/v0.2.0.json"
    }

    # Write to file
    with open(output_path, "w") as f:
        json.dump(output, f, indent=2)


def main():
    # Get paths
    script_dir = os.path.dirname(os.path.abspath(__file__))
    template_path = os.path.join(script_dir, "template.json")
    output_dir = os.path.join(script_dir, "..")
    output_path = os.path.join(output_dir, "acme-neo.json")
    package_json_path = os.path.join(script_dir, "../../vscode/package.json")

    # Generate themes
    generate_zed_themes(package_json_path, template_path, output_path)
    print(f"Generated: acme-neo.json with {len(themes)} theme variants")


if __name__ == "__main__":
    main()
