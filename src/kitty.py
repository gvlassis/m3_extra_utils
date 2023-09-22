import material_color_utilities_python as mcu

def write(file, scheme, scheme_8):

    file.write("color0 %s\n" % (mcu.hexFromArgb(scheme_8.get_black())))
    file.write("color1 %s\n" % (mcu.hexFromArgb(scheme_8.get_red())))
    file.write("color2 %s\n" % (mcu.hexFromArgb(scheme_8.get_green())))
    file.write("color3 %s\n" % (mcu.hexFromArgb(scheme_8.get_yellow())))
    file.write("color4 %s\n" % (mcu.hexFromArgb(scheme_8.get_blue())))
    file.write("color5 %s\n" % (mcu.hexFromArgb(scheme_8.get_magenta())))
    file.write("color6 %s\n" % (mcu.hexFromArgb(scheme_8.get_cyan())))
    file.write("color7 %s\n" % (mcu.hexFromArgb(scheme_8.get_white())))
    file.write("color8 %s\n" % (mcu.hexFromArgb(scheme_8.get_bright_black())))
    file.write("color9 %s\n" % (mcu.hexFromArgb(scheme_8.get_bright_red())))
    file.write("color10 %s\n" % (mcu.hexFromArgb(scheme_8.get_bright_green())))
    file.write("color11 %s\n" % (mcu.hexFromArgb(scheme_8.get_bright_yellow())))
    file.write("color12 %s\n" % (mcu.hexFromArgb(scheme_8.get_bright_blue())))
    file.write("color13 %s\n" % (mcu.hexFromArgb(scheme_8.get_bright_magenta())))
    file.write("color14 %s\n" % (mcu.hexFromArgb(scheme_8.get_bright_cyan())))
    file.write("color15 %s\n" % (mcu.hexFromArgb(scheme_8.get_bright_white())))

    file.write("background %s\n" % (mcu.hexFromArgb(scheme.get_surface())))
    file.write("foreground %s\n" % (mcu.hexFromArgb(scheme.get_onSurface())))	
    file.write("selection_background %s\n" % (mcu.hexFromArgb(scheme.get_primary())))
    file.write("selection_foreground %s\n" % (mcu.hexFromArgb(scheme.get_onPrimary())))
    file.write("cursor %s\n" % (mcu.hexFromArgb(scheme.get_tertiary())))
    file.write("cursor_text_color %s\n" % (mcu.hexFromArgb(scheme.get_onTertiary())))

    file.write("macos_titlebar_color %s\n" % (mcu.hexFromArgb(scheme.get_surfaceContainerHighest())))
    file.write("wayland_titlebar_color %s\n" % (mcu.hexFromArgb(scheme.get_surfaceContainerHighest())))

    file.write("active_tab_background %s\n" % (mcu.hexFromArgb(scheme.get_primary())))
    file.write("active_tab_foreground %s\n" % (mcu.hexFromArgb(scheme.get_onPrimary())))
    file.write("inactive_tab_background %s\n" % (mcu.hexFromArgb(scheme.get_secondary())))
    file.write("inactive_tab_foreground %s\n" % (mcu.hexFromArgb(scheme.get_onSecondary())))
    file.write("tab_bar_background %s\n" % (mcu.hexFromArgb(scheme.get_surfaceContainerLowest())))

    file.write("url_color %s\n" % (mcu.hexFromArgb(scheme.get_tertiary())))