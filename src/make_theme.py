import material_color_utilities_python as mcu
import argparse
import os
import PIL.Image
import color_defs
import scheme_8
import scheme_wheel
import kitty
import vscode
import matplotlib

# If the image has more pixels than the threshold, it would take too much time for the source color to be extracted. Therefore, in such a case the image is resized.
PIXELS_THRESHOLD = 100*100

def get_colored(string, argb):
    red = mcu.redFromArgb(argb)
    green = mcu.greenFromArgb(argb)
    blue = mcu.blueFromArgb(argb)

    return "\x1b[38;2;%d;%d;%d;48;2;%d;%d;%dm%s\x1b[0m" % (red, green, blue, red, green, blue, string)

def tonal_palette_to_string(tonal_palette):
    string = ""

    tones = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 95, 99, 100]
    for t in tones:
        argb = tonal_palette.tone(t)
        hex_code = mcu.hexFromArgb(argb)

        new = "%d:%s" % (t, hex_code)
        new_aligned = "%-12s" % (new)
        new_colored = get_colored(new_aligned, argb)

        string = string + new_colored

    return string

def print_theme(theme):
    print( "%-10.10s:%s" %  ("Primary", tonal_palette_to_string(theme["palettes"]["primary"])) )
    print( "%-10.10s:%s" %  ("Secondary", tonal_palette_to_string(theme["palettes"]["secondary"])) )
    print( "%-10.10s:%s" %  ("Tertiary", tonal_palette_to_string(theme["palettes"]["tertiary"])) )
    print( "%-10.10s:%s" %  ("Neutral", tonal_palette_to_string(theme["palettes"]["neutral"])) )
    print( "%-10.10s:%s" %  ("NeutralVariant", tonal_palette_to_string(theme["palettes"]["neutralVariant"])) )
    print( "%-10.10s:%s" %  ("Error", tonal_palette_to_string(theme["palettes"]["error"])) )

    for custom_color in theme["customColors"]:
        tonal_palette = mcu.CorePalette.of(custom_color["value"]).a1
        print( "%-10.10s:%s" %  (custom_color["color"]["name"], tonal_palette_to_string(tonal_palette)) )

def print_scheme(scheme):
    primary_hex = mcu.hexFromArgb(scheme.get_primary())
    primary_new = "Primary:%s" % (primary_hex)
    primary_new_aligned = "%-30s" % (primary_new)
    primary_new_colored = get_colored(primary_new_aligned, scheme.get_primary())
    secondary_hex = mcu.hexFromArgb(scheme.get_secondary())
    secondary_new = "Secondary:%s" % (secondary_hex)
    secondary_new_aligned = "%-30s" % (secondary_new)
    secondary_new_colored = get_colored(secondary_new_aligned, scheme.get_secondary())
    tertiary_hex = mcu.hexFromArgb(scheme.get_tertiary())
    tertiary_new = "Tertiary:%s" % (tertiary_hex)
    tertiary_new_aligned = "%-30s" % (tertiary_new)
    tertiary_new_colored = get_colored(tertiary_new_aligned, scheme.get_tertiary())
    error_hex = mcu.hexFromArgb(scheme.get_error())
    error_new = "Error:%s" % (error_hex)
    error_new_aligned = "%-30s" % (error_new)
    error_new_colored = get_colored(error_new_aligned, scheme.get_error())
    print("%s%s%s%s" % (primary_new_colored, secondary_new_colored, tertiary_new_colored, error_new_colored))

    on_primary_hex = mcu.hexFromArgb(scheme.get_onPrimary())
    on_primary_new = "On:%s" % (on_primary_hex)
    on_primary_new_aligned = "%-30s" % (on_primary_new)
    on_primary_new_colored = get_colored(on_primary_new_aligned, scheme.get_onPrimary())
    on_secondary_hex = mcu.hexFromArgb(scheme.get_onSecondary())
    on_secondary_new = "On:%s" % (on_secondary_hex)
    on_secondary_new_aligned = "%-30s" % (on_secondary_new)
    on_secondary_new_colored = get_colored(on_secondary_new_aligned, scheme.get_onSecondary())
    on_tertiary_hex = mcu.hexFromArgb(scheme.get_onTertiary())
    on_tertiary_new = "On:%s" % (on_tertiary_hex)
    on_tertiary_new_aligned = "%-30s" % (on_tertiary_new)
    on_tertiary_new_colored = get_colored(on_tertiary_new_aligned, scheme.get_onTertiary())
    on_error_hex = mcu.hexFromArgb(scheme.get_onError())
    on_error_new = "On:%s" % (on_error_hex)
    on_error_new_aligned = "%-30s" % (on_error_new)
    on_error_new_colored = get_colored(on_error_new_aligned, scheme.get_onError())
    print("%s%s%s%s" % (on_primary_new_colored, on_secondary_new_colored, on_tertiary_new_colored, on_error_new_colored))

    primary_container_hex = mcu.hexFromArgb(scheme.get_primaryContainer())
    primary_container_new = "Container:%s" % (primary_container_hex)
    primary_container_new_aligned = "%-30s" % (primary_container_new)
    primary_container_new_colored = get_colored(primary_container_new_aligned, scheme.get_primaryContainer())
    secondary_container_hex = mcu.hexFromArgb(scheme.get_secondaryContainer())
    secondary_container_new = "Container:%s" % (secondary_container_hex)
    secondary_container_new_aligned = "%-30s" % (secondary_container_new)
    secondary_container_new_colored = get_colored(secondary_container_new_aligned, scheme.get_secondaryContainer())
    tertiary_container_hex = mcu.hexFromArgb(scheme.get_tertiaryContainer())
    tertiary_container_new = "Container:%s" % (tertiary_container_hex)
    tertiary_container_new_aligned = "%-30s" % (tertiary_container_new)
    tertiary_container_new_colored = get_colored(tertiary_container_new_aligned, scheme.get_tertiaryContainer())
    error_container_hex = mcu.hexFromArgb(scheme.get_errorContainer())
    error_container_new = "Container:%s" % (error_container_hex)
    error_container_new_aligned = "%-30s" % (error_container_new)
    error_container_new_colored = get_colored(error_container_new_aligned, scheme.get_errorContainer())
    print("%s%s%s%s" % (primary_container_new_colored, secondary_container_new_colored, tertiary_container_new_colored, error_container_new_colored))

    on_primary_container_hex = mcu.hexFromArgb(scheme.get_onPrimaryContainer())
    on_primary_container_new = "OnContainer:%s" % (on_primary_container_hex)
    on_primary_container_new_aligned = "%-30s" % (on_primary_container_new)
    on_primary_container_new_colored = get_colored(on_primary_container_new_aligned, scheme.get_onPrimaryContainer())
    on_secondary_container_hex = mcu.hexFromArgb(scheme.get_onSecondaryContainer())
    on_secondary_container_new = "OnContainer:%s" % (on_secondary_container_hex)
    on_secondary_container_new_aligned = "%-30s" % (on_secondary_container_new)
    on_secondary_container_new_colored = get_colored(on_secondary_container_new_aligned, scheme.get_onSecondaryContainer())
    on_tertiary_container_hex = mcu.hexFromArgb(scheme.get_onTertiaryContainer())
    on_tertiary_container_new = "OnContainer:%s" % (on_tertiary_container_hex)
    on_tertiary_container_new_aligned = "%-30s" % (on_tertiary_container_new)
    on_tertiary_container_new_colored = get_colored(on_tertiary_container_new_aligned, scheme.get_onTertiaryContainer())
    on_error_container_hex = mcu.hexFromArgb(scheme.get_onErrorContainer())
    on_error_container_new = "OnContainer:%s" % (on_error_container_hex)
    on_error_container_new_aligned = "%-30s" % (on_error_container_new)
    on_error_container_new_colored = get_colored(on_error_container_new_aligned, scheme.get_onErrorContainer())
    print("%s%s%s%s" % (on_primary_container_new_colored, on_secondary_container_new_colored, on_tertiary_container_new_colored, on_error_container_new_colored))

    surface_dim_hex = mcu.hexFromArgb(scheme.get_surfaceDim())
    surface_dim_new = "Dim:%s" % (surface_dim_hex)
    surface_dim_new_aligned = "%-40s" % (surface_dim_new)
    surface_dim_new_colored = get_colored(surface_dim_new_aligned, scheme.get_surfaceDim())
    surface_hex = mcu.hexFromArgb(scheme.get_surface())
    surface_new = "Surface:%s" % (surface_hex)
    surface_new_aligned = "%-40s" % (surface_new)
    surface_new_colored = get_colored(surface_new_aligned, scheme.get_surface())
    surface_bright_hex = mcu.hexFromArgb(scheme.get_surfaceBright())
    surface_bright_new = "Bright:%s" % (surface_bright_hex)
    surface_bright_new_aligned = "%-40s" % (surface_bright_new)
    surface_bright_new_colored = get_colored(surface_bright_new_aligned, scheme.get_surfaceBright())
    print("%s%s%s" % (surface_dim_new_colored, surface_new_colored, surface_bright_new_colored))

    surface_container_lowest_hex = mcu.hexFromArgb(scheme.get_surfaceContainerLowest())
    surface_container_lowest_new = "Lowest:%s" % (surface_container_lowest_hex)
    surface_container_lowest_new_aligned = "%-24s" % (surface_container_lowest_new)
    surface_container_lowest_new_colored = get_colored(surface_container_lowest_new_aligned, scheme.get_surfaceContainerLowest())
    surface_container_low_hex = mcu.hexFromArgb(scheme.get_surfaceContainerLow())
    surface_container_low_new = "Low:%s" % (surface_container_low_hex)
    surface_container_low_new_aligned = "%-24s" % (surface_container_low_new)
    surface_container_low_new_colored = get_colored(surface_container_low_new_aligned, scheme.get_surfaceContainerLow())
    surface_container_hex = mcu.hexFromArgb(scheme.get_surfaceContainer())
    surface_container_new = "Container:%s" % (surface_container_hex)
    surface_container_new_aligned = "%-24s" % (surface_container_new)
    surface_container_new_colored = get_colored(surface_container_new_aligned, scheme.get_surfaceContainer())
    surface_container_high_hex = mcu.hexFromArgb(scheme.get_surfaceContainerHigh())
    surface_container_high_new = "High:%s" % (surface_container_high_hex)
    surface_container_high_new_aligned = "%-24s" % (surface_container_high_new)
    surface_container_high_new_colored = get_colored(surface_container_high_new_aligned, scheme.get_surfaceContainerHigh())
    surface_container_highest_hex = mcu.hexFromArgb(scheme.get_surfaceContainerHighest())
    surface_container_highest_new = "Highest:%s" % (surface_container_highest_hex)
    surface_container_highest_new_aligned = "%-24s" % (surface_container_highest_new)
    surface_container_highest_new_colored = get_colored(surface_container_highest_new_aligned, scheme.get_surfaceContainerHighest())
    print("%s%s%s%s%s" % (surface_container_lowest_new_colored, surface_container_low_new_colored, surface_container_new_colored, surface_container_high_new_colored, surface_container_highest_new_colored))

    on_surface_hex = mcu.hexFromArgb(scheme.get_onSurface())
    on_surface_new = "OnSurface:%s" % (on_surface_hex)
    on_surface_new_aligned = "%-120s" % (on_surface_new)
    on_surface_new_colored = get_colored(on_surface_new_aligned, scheme.get_onSurface())
    print("%s" % (on_surface_new_colored))

parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
group = parser.add_mutually_exclusive_group()
parser.add_argument("-8", "--eight", help="Add the 8 3-bit colors as custom colors", action="store_true")
parser.add_argument("-w", "--wheel", help="Add the 12 color wheel colors as custom colors", action="store_true")
group.add_argument("-s", "--source", metavar="HEX", help="Source color", type=str, default="#7851f9")
group.add_argument("-i", "--image", metavar="PATH", help="The image from which to extract the source color", type=os.path.abspath)
parser.add_argument("-l", "--light", help="Generate light schemes instead of dark schemes", action="store_true")
parser.add_argument("--scheme", help="Also print default scheme", action="store_true")
# A theme in Kitty is just a .conf file containing kitty settings. You can also create your own themes as .conf files. Put them in ~/.config/kitty/themes. When you select a theme, the kitten simply copies the .conf file to ~/.config/kitty/current-theme.conf and adds an include for current-theme.conf to kitty.conf. 
parser.add_argument("--kitty", metavar="PATH", help="Generate a Kitty theme file at the given path", type=os.path.abspath)
parser.add_argument("--vscode", metavar="PATH", help="Generate a VS Code theme file at the given path", type=os.path.abspath)
parser.add_argument("--matplotlib", metavar="PATH", help="Generate a Matplotlib style sheet at the given path", type=os.path.abspath)
args=parser.parse_args()

custom_colors = []
if args.eight:
    custom_colors = custom_colors + [color_defs.BLACK_8, color_defs.BLUE_8, color_defs.GREEN_8, color_defs.CYAN_8, color_defs.RED_8, color_defs.MAGENTA_8, color_defs.YELLOW_8, color_defs.WHITE_8]
if args.wheel:
    custom_colors = custom_colors + [color_defs.RED_WHEEL, color_defs.RED_ORANGE_WHEEL, color_defs.ORANGE_WHEEL, color_defs.ORANGE_YELLOW_WHEEL, color_defs.YELLOW_WHEEL, color_defs.YELLOW_GREEN_WHEEL, color_defs.GREEN_WHEEL, color_defs.GREEN_BLUE_WHEEL, color_defs.BLUE_WHEEL, color_defs.BLUE_VIOLET_WHEEL, color_defs.VIOLET_WHEEL, color_defs.VIOLET_RED_WHEEL]

if args.image is None:
    theme = mcu.themeFromSourceColor(mcu.argbFromHex(args.source), custom_colors)
else:
    img = PIL.Image.open(args.image)
    
    if img.size[0]*img.size[1] > PIXELS_THRESHOLD:
        w = img.size[0]
        h = img.size[1] 
        a = w/h
        w_ = int((a * PIXELS_THRESHOLD) ** 0.5)
        h_ = int(w_/a)
        img = img.resize((w_,h_))

    theme = mcu.themeFromImage(img, custom_colors)

print_theme(theme)

if args.light:
    mode = "light"
    scheme_8 = scheme_8.Scheme8.light(theme)
    scheme_wheel = scheme_wheel.SchemeWheel.light(theme)
else:
    mode = "dark"
    scheme_8 = scheme_8.Scheme8.dark(theme)
    scheme_wheel = scheme_wheel.SchemeWheel.dark(theme)

if args.scheme:
    print_scheme(theme["schemes"][mode])

if args.kitty is not None:
    with open(args.kitty, "w") as file:
        kitty.write(file, theme["schemes"][mode], scheme_8)

if args.vscode is not None:
    with open(args.vscode, "w") as file:
        vscode.write(file, mode, theme["schemes"][mode], scheme_8, scheme_wheel)

if args.matplotlib is not None:
    with open(args.matplotlib, "w") as file:
        matplotlib.write(file, theme["schemes"][mode], scheme_wheel)