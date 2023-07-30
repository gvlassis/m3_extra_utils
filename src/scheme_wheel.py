import material_color_utilities_python as mcu
import color_defs
import json

class SchemeWheel:
    def __init__(self, props):
        self.props = props

    def get_red(self):
        return self.props["red"]

    def get_red_orange(self):
        return self.props["red_orange"]

    def get_orange(self):
        return self.props["orange"]

    def get_orange_yellow(self):
        return self.props["orange_yellow"]

    def get_yellow(self):
        return self.props["yellow"]

    def get_yellow_green(self):
        return self.props["yellow_green"]

    def get_green(self):
        return self.props["green"]
    
    def get_green_blue(self):
        return self.props["green_blue"]
    
    def get_blue(self):
        return self.props["blue"]
    
    def get_blue_violet(self):
        return self.props["blue_violet"]

    def get_violet(self):
        return self.props["violet"]

    def get_violet_red(self):
        return self.props["violet_red"]

    red = property(get_red) 
    red_orange = property(get_red_orange)
    orange = property(get_orange)
    orange_yellow = property(get_orange_yellow)
    yellow = property(get_yellow)
    yellow_green = property(get_yellow_green)
    green = property(get_green)
    green_blue = property(get_green_blue)
    blue = property(get_blue)
    blue_violet = property(get_blue_violet)
    violet = property(get_violet)
    violet_red = property(get_violet_red)

    @staticmethod
    def light(theme):
        red = mcu.Blend.harmonize(color_defs.RED_WHEEL["value"], theme["source"])
        red_tonal_palette = mcu.CorePalette.of(red).a1
        red_orange = mcu.Blend.harmonize(color_defs.RED_ORANGE_WHEEL["value"], theme["source"])
        red_orange_tonal_palette = mcu.CorePalette.of(red_orange).a1
        orange = mcu.Blend.harmonize(color_defs.ORANGE_WHEEL["value"], theme["source"])
        orange_tonal_palette = mcu.CorePalette.of(orange).a1
        orange_yellow = mcu.Blend.harmonize(color_defs.ORANGE_YELLOW_WHEEL["value"], theme["source"])
        orange_yellow_tonal_palette = mcu.CorePalette.of(orange_yellow).a1
        yellow = mcu.Blend.harmonize(color_defs.YELLOW_WHEEL["value"], theme["source"])
        yellow_tonal_palette = mcu.CorePalette.of(yellow).a1
        yellow_green = mcu.Blend.harmonize(color_defs.YELLOW_GREEN_WHEEL["value"], theme["source"])
        yellow_green_tonal_palette = mcu.CorePalette.of(yellow_green).a1
        green = mcu.Blend.harmonize(color_defs.GREEN_WHEEL["value"], theme["source"])
        green_tonal_palette = mcu.CorePalette.of(green).a1
        green_blue = mcu.Blend.harmonize(color_defs.GREEN_BLUE_WHEEL["value"], theme["source"])
        green_blue_tonal_palette = mcu.CorePalette.of(green_blue).a1
        blue = mcu.Blend.harmonize(color_defs.BLUE_WHEEL["value"], theme["source"])
        blue_tonal_palette = mcu.CorePalette.of(blue).a1
        blue_violet = mcu.Blend.harmonize(color_defs.BLUE_VIOLET_WHEEL["value"], theme["source"])
        blue_violet_tonal_palette = mcu.CorePalette.of(blue_violet).a1
        violet = mcu.Blend.harmonize(color_defs.VIOLET_WHEEL["value"], theme["source"])
        violet_tonal_palette = mcu.CorePalette.of(violet).a1
        violet_red = mcu.Blend.harmonize(color_defs.VIOLET_RED_WHEEL["value"], theme["source"])
        violet_red_tonal_palette = mcu.CorePalette.of(violet_red).a1

        return SchemeWheel({
            "red": red_tonal_palette.tone(50),
            "red_orange": red_orange_tonal_palette.tone(50),
            "orange": orange_tonal_palette.tone(50),
            "orange_yellow": orange_yellow_tonal_palette.tone(50),
            "yellow": yellow_tonal_palette.tone(50),
            "yellow_green": yellow_green_tonal_palette.tone(50),
            "green": green_tonal_palette.tone(50),
            "green_blue": green_blue_tonal_palette.tone(50),
            "blue": blue_tonal_palette.tone(50),
            "blue_violet": blue_violet_tonal_palette.tone(50), 
            "violet": violet_tonal_palette.tone(50),
            "violet_red": violet_red_tonal_palette.tone(50)
        })

    @staticmethod
    def dark(theme):
        red = mcu.Blend.harmonize(color_defs.RED_WHEEL["value"], theme["source"])
        red_tonal_palette = mcu.CorePalette.of(red).a1
        red_orange = mcu.Blend.harmonize(color_defs.RED_ORANGE_WHEEL["value"], theme["source"])
        red_orange_tonal_palette = mcu.CorePalette.of(red_orange).a1
        orange = mcu.Blend.harmonize(color_defs.ORANGE_WHEEL["value"], theme["source"])
        orange_tonal_palette = mcu.CorePalette.of(orange).a1
        orange_yellow = mcu.Blend.harmonize(color_defs.ORANGE_YELLOW_WHEEL["value"], theme["source"])
        orange_yellow_tonal_palette = mcu.CorePalette.of(orange_yellow).a1
        yellow = mcu.Blend.harmonize(color_defs.YELLOW_WHEEL["value"], theme["source"])
        yellow_tonal_palette = mcu.CorePalette.of(yellow).a1
        yellow_green = mcu.Blend.harmonize(color_defs.YELLOW_GREEN_WHEEL["value"], theme["source"])
        yellow_green_tonal_palette = mcu.CorePalette.of(yellow_green).a1
        green = mcu.Blend.harmonize(color_defs.GREEN_WHEEL["value"], theme["source"])
        green_tonal_palette = mcu.CorePalette.of(green).a1
        green_blue = mcu.Blend.harmonize(color_defs.GREEN_BLUE_WHEEL["value"], theme["source"])
        green_blue_tonal_palette = mcu.CorePalette.of(green_blue).a1
        blue = mcu.Blend.harmonize(color_defs.BLUE_WHEEL["value"], theme["source"])
        blue_tonal_palette = mcu.CorePalette.of(blue).a1
        blue_violet = mcu.Blend.harmonize(color_defs.BLUE_VIOLET_WHEEL["value"], theme["source"])
        blue_violet_tonal_palette = mcu.CorePalette.of(blue_violet).a1
        violet = mcu.Blend.harmonize(color_defs.VIOLET_WHEEL["value"], theme["source"])
        violet_tonal_palette = mcu.CorePalette.of(violet).a1
        violet_red = mcu.Blend.harmonize(color_defs.VIOLET_RED_WHEEL["value"], theme["source"])
        violet_red_tonal_palette = mcu.CorePalette.of(violet_red).a1

        return SchemeWheel({
            "red": red_tonal_palette.tone(70),
            "red_orange": red_orange_tonal_palette.tone(70),
            "orange": orange_tonal_palette.tone(70),
            "orange_yellow": orange_yellow_tonal_palette.tone(70),
            "yellow": yellow_tonal_palette.tone(70),
            "yellow_green": yellow_green_tonal_palette.tone(70),
            "green": green_tonal_palette.tone(70),
            "green_blue": green_blue_tonal_palette.tone(70),
            "blue": blue_tonal_palette.tone(70),
            "blue_violet": blue_violet_tonal_palette.tone(70), 
            "violet": violet_tonal_palette.tone(70),
            "violet_red": violet_red_tonal_palette.tone(70)
        })

    def toJSON(self):
        return json.dumps(self.props)