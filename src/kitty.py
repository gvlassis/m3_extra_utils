import material_color_utilities_python as mcu
import color_defs

# Custom system via which you can create the 16 ANSI colors given a theme.
def get_ansi_hex(theme, mode):
    # Blended black is not really black

    # Error red is more red than the blended red

    GREEN_8_blended = mcu.Blend.harmonize(color_defs.GREEN_8["value"], theme["source"])
    GREEN_8_blended_tonal_palette = mcu.CorePalette.of(GREEN_8_blended).a1

    YELLOW_8_blended = mcu.Blend.harmonize(color_defs.YELLOW_8["value"], theme["source"])
    YELLOW_8_blended_tonal_palette = mcu.CorePalette.of(YELLOW_8_blended).a1

    BLUE_8_blended = mcu.Blend.harmonize(color_defs.BLUE_8["value"], theme["source"])
    BLUE_8_blended_tonal_palette = mcu.CorePalette.of(BLUE_8_blended).a1

    MAGENTA_8_blended = mcu.Blend.harmonize(color_defs.MAGENTA_8["value"], theme["source"])
    MAGENTA_8_blended_tonal_palette = mcu.CorePalette.of(MAGENTA_8_blended).a1
    
    CYAN_8_blended = mcu.Blend.harmonize(color_defs.CYAN_8["value"], theme["source"])
    CYAN_8_blended_tonal_palette = mcu.CorePalette.of(CYAN_8_blended).a1

    # Blended white is not really white

    if mode == "dark":
        black_ansi = theme["palettes"]["neutral"].tone(5)
        black_ansi_hex = mcu.hexFromArgb(black_ansi)

        red_ansi = theme["palettes"]["error"].tone(60)
        red_ansi_hex = mcu.hexFromArgb(red_ansi)

        green_ansi = GREEN_8_blended_tonal_palette.tone(75)
        green_ansi_hex = mcu.hexFromArgb(green_ansi)

        yellow_ansi = YELLOW_8_blended_tonal_palette.tone(85)
        yellow_ansi_hex = mcu.hexFromArgb(yellow_ansi)
        
        blue_ansi = BLUE_8_blended_tonal_palette.tone(80)
        blue_ansi_hex = mcu.hexFromArgb(blue_ansi)

        magenta_ansi = MAGENTA_8_blended_tonal_palette.tone(65)
        magenta_ansi_hex = mcu.hexFromArgb(magenta_ansi)

        cyan_ansi = CYAN_8_blended_tonal_palette.tone(80)
        cyan_ansi_hex = mcu.hexFromArgb(cyan_ansi)

        white_ansi = theme["palettes"]["neutral"].tone(80)
        white_ansi_hex = mcu.hexFromArgb(white_ansi)

        bright_black_ansi = theme["palettes"]["neutral"].tone(30)
        bright_black_ansi_hex = mcu.hexFromArgb(bright_black_ansi)

        bright_red_ansi = theme["palettes"]["error"].tone(65)
        bright_red_ansi_hex = mcu.hexFromArgb(bright_red_ansi)

        bright_green_ansi = GREEN_8_blended_tonal_palette.tone(80)
        bright_green_ansi_hex = mcu.hexFromArgb(bright_green_ansi)

        bright_yellow_ansi = YELLOW_8_blended_tonal_palette.tone(90)
        bright_yellow_ansi_hex = mcu.hexFromArgb(bright_yellow_ansi)
        
        bright_blue_ansi = BLUE_8_blended_tonal_palette.tone(85)
        bright_blue_ansi_hex = mcu.hexFromArgb(bright_blue_ansi)

        bright_magenta_ansi = MAGENTA_8_blended_tonal_palette.tone(70)
        bright_magenta_ansi_hex = mcu.hexFromArgb(bright_magenta_ansi)

        bright_cyan_ansi = CYAN_8_blended_tonal_palette.tone(85)
        bright_cyan_ansi_hex = mcu.hexFromArgb(bright_cyan_ansi)

        bright_white_ansi = theme["palettes"]["neutral"].tone(95)
        bright_white_ansi_hex = mcu.hexFromArgb(bright_white_ansi)
    else:
        black_ansi = theme["palettes"]["neutral"].tone(10)
        black_ansi_hex = mcu.hexFromArgb(black_ansi)

        red_ansi = theme["palettes"]["error"].tone(55)
        red_ansi_hex = mcu.hexFromArgb(red_ansi)

        green_ansi = GREEN_8_blended_tonal_palette.tone(55)
        green_ansi_hex = mcu.hexFromArgb(green_ansi)

        yellow_ansi = YELLOW_8_blended_tonal_palette.tone(60)
        yellow_ansi_hex = mcu.hexFromArgb(yellow_ansi)
        
        blue_ansi = BLUE_8_blended_tonal_palette.tone(60)
        blue_ansi_hex = mcu.hexFromArgb(blue_ansi)

        magenta_ansi = MAGENTA_8_blended_tonal_palette.tone(55)
        magenta_ansi_hex = mcu.hexFromArgb(magenta_ansi)

        cyan_ansi = CYAN_8_blended_tonal_palette.tone(60)
        cyan_ansi_hex = mcu.hexFromArgb(cyan_ansi)

        white_ansi = theme["palettes"]["neutral"].tone(80)
        white_ansi_hex = mcu.hexFromArgb(white_ansi)

        bright_black_ansi = theme["palettes"]["neutral"].tone(40)
        bright_black_ansi_hex = mcu.hexFromArgb(bright_black_ansi)

        bright_red_ansi = theme["palettes"]["error"].tone(60)
        bright_red_ansi_hex = mcu.hexFromArgb(bright_red_ansi)

        bright_green_ansi = GREEN_8_blended_tonal_palette.tone(60)
        bright_green_ansi_hex = mcu.hexFromArgb(bright_green_ansi)

        bright_yellow_ansi = YELLOW_8_blended_tonal_palette.tone(65)
        bright_yellow_ansi_hex = mcu.hexFromArgb(bright_yellow_ansi)
        
        bright_blue_ansi = BLUE_8_blended_tonal_palette.tone(65)
        bright_blue_ansi_hex = mcu.hexFromArgb(bright_blue_ansi)

        bright_magenta_ansi = MAGENTA_8_blended_tonal_palette.tone(60)
        bright_magenta_ansi_hex = mcu.hexFromArgb(bright_magenta_ansi)

        bright_cyan_ansi = CYAN_8_blended_tonal_palette.tone(65)
        bright_cyan_ansi_hex = mcu.hexFromArgb(bright_cyan_ansi)

        bright_white_ansi = theme["palettes"]["neutral"].tone(99)
        bright_white_ansi_hex = mcu.hexFromArgb(bright_white_ansi)

    return [black_ansi_hex, red_ansi_hex, green_ansi_hex, yellow_ansi_hex, blue_ansi_hex, magenta_ansi_hex, cyan_ansi_hex, white_ansi_hex, bright_black_ansi_hex, bright_red_ansi_hex, bright_green_ansi_hex, bright_yellow_ansi_hex, bright_blue_ansi_hex, bright_magenta_ansi_hex, bright_cyan_ansi_hex, bright_white_ansi_hex]

def write(file, theme, mode):
    ansi_hex = get_ansi_hex(theme, mode)

    if mode == "dark":
        primary = theme["palettes"]["primary"].tone(80)
        primary_hex = mcu.hexFromArgb(primary)
        on_primary = theme["palettes"]["primary"].tone(20)
        on_primary_hex = mcu.hexFromArgb(on_primary)

        secondary = theme["palettes"]["secondary"].tone(80)
        secondary_hex = mcu.hexFromArgb(secondary)
        on_secondary = theme["palettes"]["secondary"].tone(20)
        on_secondary_hex = mcu.hexFromArgb(on_secondary)

        tertiary = theme["palettes"]["tertiary"].tone(80)
        tertiary_hex = mcu.hexFromArgb(tertiary)

        surface_container_lowest = theme["palettes"]["neutral"].tone(4)
        surface_container_lowest_hex = mcu.hexFromArgb(surface_container_lowest)
        surface_container = theme["palettes"]["neutral"].tone(12)
        surface_container_hex = mcu.hexFromArgb(surface_container)
        surface_container_highest = theme["palettes"]["neutral"].tone(22)
        surface_container_highest_hex = mcu.hexFromArgb(surface_container_highest)
        on_surface = theme["palettes"]["neutral"].tone(90)
        on_surface_hex = mcu.hexFromArgb(on_surface)
    else:
        primary = theme["palettes"]["primary"].tone(40)
        primary_hex = mcu.hexFromArgb(primary)
        on_primary = theme["palettes"]["primary"].tone(100)
        on_primary_hex = mcu.hexFromArgb(on_primary)

        secondary = theme["palettes"]["secondary"].tone(40)
        secondary_hex = mcu.hexFromArgb(secondary)
        on_secondary = theme["palettes"]["secondary"].tone(100)
        on_secondary_hex = mcu.hexFromArgb(on_secondary)

        tertiary = theme["palettes"]["tertiary"].tone(40)
        tertiary_hex = mcu.hexFromArgb(tertiary)

        surface_container_lowest = theme["palettes"]["neutral"].tone(100)
        surface_container_lowest_hex = mcu.hexFromArgb(surface_container_lowest)
        surface_container = theme["palettes"]["neutral"].tone(94)
        surface_container_hex = mcu.hexFromArgb(surface_container)
        surface_container_highest = theme["palettes"]["neutral"].tone(90)
        surface_container_highest_hex = mcu.hexFromArgb(surface_container_highest)
        on_surface = theme["palettes"]["neutral"].tone(10)
        on_surface_hex = mcu.hexFromArgb(on_surface)

    for i in range(0, 16):
        file.write("color%d %s\n" % (i, ansi_hex[i]))

    file.write("background %s\n" % (surface_container_hex))
    file.write("foreground %s\n" % (on_surface_hex))	
    file.write("selection_background %s\n" % (primary_hex))
    file.write("selection_foreground %s\n" % (on_primary_hex))

    file.write("macos_titlebar_color %s\n" % (surface_container_highest_hex))
    file.write("wayland_titlebar_color %s\n" % (surface_container_highest_hex))

    file.write("active_tab_background %s\n" % (primary_hex))
    file.write("active_tab_foreground %s\n" % (on_primary_hex))
    file.write("inactive_tab_background %s\n" % (secondary_hex))
    file.write("inactive_tab_foreground %s\n" % (on_secondary_hex))
    file.write("tab_bar_background %s\n" % (surface_container_lowest_hex))

    file.write("url_color %s" % (tertiary_hex))




