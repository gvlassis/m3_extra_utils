import material_color_utilities_python as mcu
import argparse
import os
import PIL.Image
import color_defs
import utils
import scheme_8
import scheme_wheel
import kitty
import vscode
import matplotlib

# If the image has more pixels than the threshold, it would take too much time for the source color to be extracted. Therefore, in such a case the image is resized.
PIXELS_THRESHOLD = 100*100

parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
group = parser.add_mutually_exclusive_group()
group.add_argument("-s", "--source", metavar="HEX", help="Source color", type=str, default="#7851f9")
group.add_argument("-i", "--image", metavar="PATH", help="The image from which to extract the source color", type=os.path.abspath)
parser.add_argument("-l", "--light", help="Generate light schemes instead of dark schemes", action="store_true")
parser.add_argument("--scheme", help="Also print default scheme", action="store_true")
parser.add_argument("-8", "--eight", help="Add the 8 3-bit colors as custom colors", action="store_true")
parser.add_argument("-w", "--wheel", help="Add the 12 color wheel colors as custom colors", action="store_true")
parser.add_argument("--kitty", metavar="PATH", help="Generate a Kitty theme file at the given path", type=os.path.abspath)
parser.add_argument("--vscode", metavar="PATH", help="Generate a VS Code theme file at the given path", type=os.path.abspath)
parser.add_argument("--matplotlib", metavar="PATH", help="Generate a Matplotlib theme file at the given path", type=os.path.abspath)
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

utils.print_theme(theme)

if args.light:
    mode = "light"
    scheme_8 = scheme_8.Scheme8.light(theme)
    scheme_wheel = scheme_wheel.SchemeWheel.light(theme)
else:
    mode = "dark"
    scheme_8 = scheme_8.Scheme8.dark(theme)
    scheme_wheel = scheme_wheel.SchemeWheel.dark(theme)

if args.scheme:
    utils.print_scheme(theme["schemes"][mode])

if args.kitty is not None:
    with open(args.kitty, "w") as file:
        kitty.write(file, theme["schemes"][mode], scheme_8)

if args.vscode is not None:
    with open(args.vscode, "w") as file:
        vscode.write(file, mode, theme["schemes"][mode], scheme_8, scheme_wheel)

if args.matplotlib is not None:
    with open(args.matplotlib, "w") as file:
        matplotlib.write(file, theme["schemes"][mode], scheme_wheel)