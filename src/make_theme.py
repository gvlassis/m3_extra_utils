import material_color_utilities_python as mcu
import argparse
import os
import color_defs
import PIL.Image
import kitty
import vscode

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

parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
group = parser.add_mutually_exclusive_group()
parser.add_argument("-8", "--eight", help="Add the 8 3-bit colors as custom colors", action="store_true")
parser.add_argument("-w", "--wheel", help="Add the 12 color wheel colors as custom colors", action="store_true")
# A theme in Kitty is just a .conf file containing kitty settings. You can also create your own themes as .conf files. Put them in ~/.config/kitty/themes. When you select a theme, the kitten simply copies the .conf file to ~/.config/kitty/current-theme.conf and adds an include for current-theme.conf to kitty.conf. 
parser.add_argument("--kitty", metavar="PATH", help="Generate a Kitty theme file at the given path", type=os.path.abspath)
parser.add_argument("--vscode", metavar="PATH", help="Generate a VS Code theme file at the given path", type=os.path.abspath)
parser.add_argument("-l", "--light", help="Generate light theme files instead of dark ones", action="store_true")
group.add_argument("-s", "--source", metavar="HEX", help="Source color", type=str, default="#7851f9")
group.add_argument("-i", "--image", metavar="PATH", help="The image from which to extract the source color", type=os.path.abspath)
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
else:
	mode = "dark"

if args.kitty is not None:
	with open(args.kitty, "w") as file:
		kitty.write(file, theme, mode)

if args.vscode is not None:
	with open(args.vscode, "w") as file:
		vscode.write(file, theme, mode)