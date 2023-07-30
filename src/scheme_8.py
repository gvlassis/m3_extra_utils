import material_color_utilities_python as mcu
import color_defs
import json

class Scheme8:
    def __init__(self, props):
        self.props = props

    def get_black(self):
        return self.props["black"]
    
    def get_red(self):
        return self.props["red"]

    def get_green(self):
        return self.props["green"]
    
    def get_yellow(self):
        return self.props["yellow"]

    def get_blue(self):
        return self.props["blue"]

    def get_magenta(self):
        return self.props["magenta"]
    
    def get_cyan(self):
        return self.props["cyan"]
    
    def get_white(self):
        return self.props["white"]
    
    def get_bright_black(self):
        return self.props["bright_black"]
    
    def get_bright_red(self):
        return self.props["bright_red"]

    def get_bright_green(self):
        return self.props["bright_green"]
    
    def get_bright_yellow(self):
        return self.props["bright_yellow"]

    def get_bright_blue(self):
        return self.props["bright_blue"]

    def get_bright_magenta(self):
        return self.props["bright_magenta"]
    
    def get_bright_cyan(self):
        return self.props["bright_cyan"]
    
    def get_bright_white(self):
        return self.props["bright_white"]

    black = property(get_black)
    red = property(get_red)
    green = property(get_green)
    yellow = property(get_yellow)
    blue = property(get_blue)
    magenta = property(get_magenta)
    cyan = property(get_cyan)
    white = property(get_white)
    bright_black = property(get_bright_black)
    bright_red = property(get_bright_red)
    bright_green = property(get_bright_green)
    bright_yellow = property(get_bright_yellow)
    bright_blue = property(get_bright_blue)
    bright_magenta = property(get_bright_magenta)
    bright_cyan = property(get_bright_cyan)
    bright_white = property(get_bright_white)

    @staticmethod
    def light(theme):
        # Blended black is not really black
        # Error red is more red than the blended red
        green = mcu.Blend.harmonize(color_defs.GREEN_8["value"], theme["source"])
        green_tonal_palette = mcu.CorePalette.of(green).a1
        yellow = mcu.Blend.harmonize(color_defs.YELLOW_8["value"], theme["source"])
        yellow_tonal_palette = mcu.CorePalette.of(yellow).a1
        blue = mcu.Blend.harmonize(color_defs.BLUE_8["value"], theme["source"])
        blue_tonal_palette = mcu.CorePalette.of(blue).a1
        magenta = mcu.Blend.harmonize(color_defs.MAGENTA_8["value"], theme["source"])
        magenta_tonal_palette = mcu.CorePalette.of(magenta).a1
        cyan = mcu.Blend.harmonize(color_defs.CYAN_8["value"], theme["source"])
        cyan_tonal_palette = mcu.CorePalette.of(cyan).a1
        # Blended white is not really white

        return Scheme8({
            "black": theme["palettes"]["neutral"].tone(10),
            "red": theme["palettes"]["error"].tone(55),
            "green": green_tonal_palette.tone(55),
            "yellow": yellow_tonal_palette.tone(60), 
            "blue": blue_tonal_palette.tone(60),
            "magenta": magenta_tonal_palette.tone(55),
            "cyan": cyan_tonal_palette.tone(60),
            "white": theme["palettes"]["neutral"].tone(80),
            "bright_black": theme["palettes"]["neutral"].tone(40),
            "bright_red": theme["palettes"]["error"].tone(60),
            "bright_green": green_tonal_palette.tone(60),
            "bright_yellow": yellow_tonal_palette.tone(65),
            "bright_blue": blue_tonal_palette.tone(65),
            "bright_magenta": magenta_tonal_palette.tone(60),
            "bright_cyan": cyan_tonal_palette.tone(55),
            "bright_white": theme["palettes"]["neutral"].tone(99)
        })

    @staticmethod
    def dark(theme):
        # Blended black is not really black
        # Error red is more red than the blended red
        green = mcu.Blend.harmonize(color_defs.GREEN_8["value"], theme["source"])
        green_tonal_palette = mcu.CorePalette.of(green).a1
        yellow = mcu.Blend.harmonize(color_defs.YELLOW_8["value"], theme["source"])
        yellow_tonal_palette = mcu.CorePalette.of(yellow).a1
        blue = mcu.Blend.harmonize(color_defs.BLUE_8["value"], theme["source"])
        blue_tonal_palette = mcu.CorePalette.of(blue).a1
        magenta = mcu.Blend.harmonize(color_defs.MAGENTA_8["value"], theme["source"])
        magenta_tonal_palette = mcu.CorePalette.of(magenta).a1
        cyan = mcu.Blend.harmonize(color_defs.CYAN_8["value"], theme["source"])
        cyan_tonal_palette = mcu.CorePalette.of(cyan).a1
        # Blended white is not really white

        return Scheme8({
            "black": theme["palettes"]["neutral"].tone(5),
            "red": theme["palettes"]["error"].tone(60),
            "green": green_tonal_palette.tone(75),
            "yellow": yellow_tonal_palette.tone(85), 
            "blue": blue_tonal_palette.tone(80),
            "magenta": magenta_tonal_palette.tone(65),
            "cyan": cyan_tonal_palette.tone(80),
            "white": theme["palettes"]["neutral"].tone(80),
            "bright_black": theme["palettes"]["neutral"].tone(30),
            "bright_red": theme["palettes"]["error"].tone(65),
            "bright_green": green_tonal_palette.tone(80),
            "bright_yellow": yellow_tonal_palette.tone(90),
            "bright_blue": blue_tonal_palette.tone(85),
            "bright_magenta": magenta_tonal_palette.tone(70),
            "bright_cyan": cyan_tonal_palette.tone(85),
            "bright_white": theme["palettes"]["neutral"].tone(95)
        })

    def toJSON(self):
        return json.dumps(self.props)
