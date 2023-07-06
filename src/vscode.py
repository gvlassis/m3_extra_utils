import kitty
import material_color_utilities_python as mcu
import color_defs
import json

def get_wheel_hex(theme, mode):
    RED_WHEEL_blended = mcu.Blend.harmonize(color_defs.RED_WHEEL["value"], theme["source"])
    RED_WHEEL_blended_tonal_palette = mcu.CorePalette.of(RED_WHEEL_blended).a1

    RED_ORANGE_WHEEL_blended = mcu.Blend.harmonize(color_defs.RED_ORANGE_WHEEL["value"], theme["source"])
    RED_ORANGE_WHEEL_blended_tonal_palette = mcu.CorePalette.of(RED_ORANGE_WHEEL_blended).a1

    ORANGE_WHEEL_blended = mcu.Blend.harmonize(color_defs.ORANGE_WHEEL["value"], theme["source"])
    ORANGE_WHEEL_blended_tonal_palette = mcu.CorePalette.of(ORANGE_WHEEL_blended).a1

    ORANGE_YELLOW_WHEEL_blended = mcu.Blend.harmonize(color_defs.ORANGE_YELLOW_WHEEL["value"], theme["source"])
    ORANGE_YELLOW_WHEEL_blended_tonal_palette = mcu.CorePalette.of(ORANGE_YELLOW_WHEEL_blended).a1

    YELLOW_WHEEL_blended = mcu.Blend.harmonize(color_defs.YELLOW_WHEEL["value"], theme["source"])
    YELLOW_WHEEL_blended_tonal_palette = mcu.CorePalette.of(YELLOW_WHEEL_blended).a1

    YELLOW_GREEN_WHEEL_blended = mcu.Blend.harmonize(color_defs.YELLOW_GREEN_WHEEL["value"], theme["source"])
    YELLOW_GREEN_WHEEL_blended_tonal_palette = mcu.CorePalette.of(YELLOW_GREEN_WHEEL_blended).a1

    GREEN_WHEEL_blended = mcu.Blend.harmonize(color_defs.GREEN_WHEEL["value"], theme["source"])
    GREEN_WHEEL_blended_tonal_palette = mcu.CorePalette.of(GREEN_WHEEL_blended).a1

    GREEN_BLUE_WHEEL_blended = mcu.Blend.harmonize(color_defs.GREEN_BLUE_WHEEL["value"], theme["source"])
    GREEN_BLUE_WHEEL_blended_tonal_palette = mcu.CorePalette.of(GREEN_BLUE_WHEEL_blended).a1

    BLUE_WHEEL_blended = mcu.Blend.harmonize(color_defs.BLUE_WHEEL["value"], theme["source"])
    BLUE_WHEEL_blended_tonal_palette = mcu.CorePalette.of(BLUE_WHEEL_blended).a1

    BLUE_VIOLET_WHEEL_blended = mcu.Blend.harmonize(color_defs.BLUE_VIOLET_WHEEL["value"], theme["source"])
    BLUE_VIOLET_WHEEL_blended_tonal_palette = mcu.CorePalette.of(BLUE_VIOLET_WHEEL_blended).a1

    VIOLET_WHEEL_blended = mcu.Blend.harmonize(color_defs.VIOLET_WHEEL["value"], theme["source"])
    VIOLET_WHEEL_blended_tonal_palette = mcu.CorePalette.of(VIOLET_WHEEL_blended).a1

    VIOLET_RED_WHEEL_blended = mcu.Blend.harmonize(color_defs.VIOLET_RED_WHEEL["value"], theme["source"])
    VIOLET_RED_WHEEL_blended_tonal_palette = mcu.CorePalette.of(VIOLET_RED_WHEEL_blended).a1

    if mode == "dark":
        red_wheel = RED_WHEEL_blended_tonal_palette.tone(70)
        red_wheel_hex = mcu.hexFromArgb(red_wheel)

        red_orange_wheel = RED_ORANGE_WHEEL_blended_tonal_palette.tone(70)
        red_orange_wheel_hex = mcu.hexFromArgb(red_orange_wheel)

        orange_wheel = ORANGE_WHEEL_blended_tonal_palette.tone(70)
        orange_wheel_hex = mcu.hexFromArgb(orange_wheel)

        orange_yellow_wheel = ORANGE_YELLOW_WHEEL_blended_tonal_palette.tone(70)
        orange_yellow_wheel_hex = mcu.hexFromArgb(orange_yellow_wheel)

        yellow_wheel = YELLOW_WHEEL_blended_tonal_palette.tone(70)
        yellow_wheel_hex = mcu.hexFromArgb(yellow_wheel)

        yellow_green_wheel = YELLOW_GREEN_WHEEL_blended_tonal_palette.tone(70)
        yellow_green_wheel_hex = mcu.hexFromArgb(yellow_green_wheel)

        green_wheel = GREEN_WHEEL_blended_tonal_palette.tone(70)
        green_wheel_hex = mcu.hexFromArgb(green_wheel)

        green_blue_wheel = GREEN_BLUE_WHEEL_blended_tonal_palette.tone(70)
        green_blue_wheel_hex = mcu.hexFromArgb(green_blue_wheel)

        blue_wheel = BLUE_WHEEL_blended_tonal_palette.tone(70)
        blue_wheel_hex = mcu.hexFromArgb(blue_wheel)

        blue_violet_wheel = BLUE_VIOLET_WHEEL_blended_tonal_palette.tone(70)
        blue_violet_wheel_hex = mcu.hexFromArgb(blue_violet_wheel)

        violet_wheel = VIOLET_WHEEL_blended_tonal_palette.tone(70)
        violet_wheel_hex = mcu.hexFromArgb(violet_wheel)

        violet_red_wheel = VIOLET_RED_WHEEL_blended_tonal_palette.tone(70)
        violet_red_wheel_hex = mcu.hexFromArgb(violet_red_wheel)
    else:
        red_wheel = RED_WHEEL_blended_tonal_palette.tone(50)
        red_wheel_hex = mcu.hexFromArgb(red_wheel)

        red_orange_wheel = RED_ORANGE_WHEEL_blended_tonal_palette.tone(50)
        red_orange_wheel_hex = mcu.hexFromArgb(red_orange_wheel)

        orange_wheel = ORANGE_WHEEL_blended_tonal_palette.tone(50)
        orange_wheel_hex = mcu.hexFromArgb(orange_wheel)

        orange_yellow_wheel = ORANGE_YELLOW_WHEEL_blended_tonal_palette.tone(50)
        orange_yellow_wheel_hex = mcu.hexFromArgb(orange_yellow_wheel)

        yellow_wheel = YELLOW_WHEEL_blended_tonal_palette.tone(50)
        yellow_wheel_hex = mcu.hexFromArgb(yellow_wheel)

        yellow_green_wheel = YELLOW_GREEN_WHEEL_blended_tonal_palette.tone(50)
        yellow_green_wheel_hex = mcu.hexFromArgb(yellow_green_wheel)

        green_wheel = GREEN_WHEEL_blended_tonal_palette.tone(50)
        green_wheel_hex = mcu.hexFromArgb(green_wheel)

        green_blue_wheel = GREEN_BLUE_WHEEL_blended_tonal_palette.tone(50)
        green_blue_wheel_hex = mcu.hexFromArgb(green_blue_wheel)

        blue_wheel = BLUE_WHEEL_blended_tonal_palette.tone(50)
        blue_wheel_hex = mcu.hexFromArgb(blue_wheel)

        blue_violet_wheel = BLUE_VIOLET_WHEEL_blended_tonal_palette.tone(50)
        blue_violet_wheel_hex = mcu.hexFromArgb(blue_violet_wheel)

        violet_wheel = VIOLET_WHEEL_blended_tonal_palette.tone(50)
        violet_wheel_hex = mcu.hexFromArgb(violet_wheel)

        violet_red_wheel = VIOLET_RED_WHEEL_blended_tonal_palette.tone(50)
        violet_red_wheel_hex = mcu.hexFromArgb(violet_red_wheel)

    return [red_wheel_hex, red_orange_wheel_hex, orange_wheel_hex, orange_yellow_wheel_hex, yellow_wheel_hex, yellow_green_wheel_hex, green_wheel_hex, green_blue_wheel_hex, blue_wheel_hex, blue_violet_wheel_hex, violet_wheel_hex, violet_red_wheel_hex]

def write(file, theme, mode):
    ansi_hex = kitty.get_ansi_hex(theme, mode)
    wheel_hex = get_wheel_hex(theme, mode)

    if mode == "dark":
        primary = theme["palettes"]["primary"].tone(80)
        primary_hex = mcu.hexFromArgb(primary)
        # Increase tone to raise
        primary_raised = theme["palettes"]["primary"].tone(85)
        primary_raised_hex = mcu.hexFromArgb(primary_raised)
        on_primary = theme["palettes"]["primary"].tone(20)
        on_primary_hex = mcu.hexFromArgb(on_primary)
        primary_container = theme["palettes"]["primary"].tone(30)
        primary_container_hex = mcu.hexFromArgb(primary_container)
        on_primary_container = theme["palettes"]["primary"].tone(90)
        on_primary_container_hex = mcu.hexFromArgb(on_primary_container)

        secondary = theme["palettes"]["secondary"].tone(80)
        secondary_hex = mcu.hexFromArgb(secondary)
        # Increase tone to raise
        secondary_raised = theme["palettes"]["secondary"].tone(85)
        secondary_raised_hex = mcu.hexFromArgb(secondary_raised)
        on_secondary = theme["palettes"]["secondary"].tone(20)
        on_secondary_hex = mcu.hexFromArgb(on_secondary)
        secondary_container = theme["palettes"]["secondary"].tone(30)
        secondary_container_hex = mcu.hexFromArgb(secondary_container)
        # Increase tone to raise
        secondary_container_raised = theme["palettes"]["secondary"].tone(40)
        secondary_container_raised_hex = mcu.hexFromArgb(secondary_container_raised)
        on_secondary_container = theme["palettes"]["secondary"].tone(90)
        on_secondary_container_hex = mcu.hexFromArgb(on_secondary_container)

        tertiary = theme["palettes"]["tertiary"].tone(80)
        tertiary_hex = mcu.hexFromArgb(tertiary)
        on_tertiary = theme["palettes"]["tertiary"].tone(20)
        on_tertiary_hex = mcu.hexFromArgb(on_tertiary)

        error = theme["palettes"]["error"].tone(80)
        error_hex = mcu.hexFromArgb(error)
        on_error = theme["palettes"]["error"].tone(20)
        on_error_hex = mcu.hexFromArgb(on_error)

        surface_container_lowest = theme["palettes"]["neutral"].tone(4)
        surface_container_lowest_hex = mcu.hexFromArgb(surface_container_lowest)
        surface_container_low = theme["palettes"]["neutral"].tone(10)
        surface_container_low_hex = mcu.hexFromArgb(surface_container_low)
        surface_container = theme["palettes"]["neutral"].tone(12)
        surface_container_hex = mcu.hexFromArgb(surface_container)
        surface_container_high = theme["palettes"]["neutral"].tone(17)
        surface_container_high_hex = mcu.hexFromArgb(surface_container_high)
        surface_container_highest = theme["palettes"]["neutral"].tone(22)
        surface_container_highest_hex = mcu.hexFromArgb(surface_container_highest)
        on_surface = theme["palettes"]["neutral"].tone(90)
        on_surface_hex = mcu.hexFromArgb(on_surface)

        inverse_surface = theme["palettes"]["neutral"].tone(90)
        inverse_surface_hex = mcu.hexFromArgb(inverse_surface)
        inverse_on_surface = theme["palettes"]["neutral"].tone(20)
        inverse_on_surface_hex = mcu.hexFromArgb(inverse_on_surface)
    else:
        primary = theme["palettes"]["primary"].tone(40)
        primary_hex = mcu.hexFromArgb(primary)
        # Decrease tone to raise
        primary_raised = theme["palettes"]["primary"].tone(30)
        primary_raised_hex = mcu.hexFromArgb(primary_raised)
        on_primary = theme["palettes"]["primary"].tone(100)
        on_primary_hex = mcu.hexFromArgb(on_primary)
        primary_container = theme["palettes"]["primary"].tone(90)
        primary_container_hex = mcu.hexFromArgb(primary_container)
        on_primary_container = theme["palettes"]["primary"].tone(10)
        on_primary_container_hex = mcu.hexFromArgb(on_primary_container)

        secondary = theme["palettes"]["secondary"].tone(40)
        secondary_hex = mcu.hexFromArgb(secondary)
        # Decrease tone to raise
        secondary_raised = theme["palettes"]["secondary"].tone(30)
        secondary_raised_hex = mcu.hexFromArgb(secondary_raised)
        on_secondary = theme["palettes"]["secondary"].tone(100)
        on_secondary_hex = mcu.hexFromArgb(on_secondary)
        secondary_container = theme["palettes"]["secondary"].tone(90)
        secondary_container_hex = mcu.hexFromArgb(secondary_container)
        # Decrease tone to raise
        secondary_container_raised = theme["palettes"]["secondary"].tone(85)
        secondary_container_raised_hex = mcu.hexFromArgb(secondary_container_raised)
        on_secondary_container = theme["palettes"]["secondary"].tone(10)
        on_secondary_container_hex = mcu.hexFromArgb(on_secondary_container)

        tertiary = theme["palettes"]["tertiary"].tone(40)
        tertiary_hex = mcu.hexFromArgb(tertiary)
        on_tertiary = theme["palettes"]["tertiary"].tone(100)
        on_tertiary_hex = mcu.hexFromArgb(on_tertiary)

        error = theme["palettes"]["error"].tone(40)
        error_hex = mcu.hexFromArgb(error)
        on_error = theme["palettes"]["error"].tone(100)
        on_error_hex = mcu.hexFromArgb(on_error)

        surface_container_lowest = theme["palettes"]["neutral"].tone(100)
        surface_container_lowest_hex = mcu.hexFromArgb(surface_container_lowest)
        surface_container_low = theme["palettes"]["neutral"].tone(96)
        surface_container_low_hex = mcu.hexFromArgb(surface_container_low)
        surface_container = theme["palettes"]["neutral"].tone(94)
        surface_container_hex = mcu.hexFromArgb(surface_container)
        surface_container_high = theme["palettes"]["neutral"].tone(92)
        surface_container_high_hex = mcu.hexFromArgb(surface_container_high)
        surface_container_highest = theme["palettes"]["neutral"].tone(90)
        surface_container_highest_hex = mcu.hexFromArgb(surface_container_highest)
        on_surface = theme["palettes"]["neutral"].tone(10)
        on_surface_hex = mcu.hexFromArgb(on_surface)

        inverse_surface = theme["palettes"]["neutral"].tone(20)
        inverse_surface_hex = mcu.hexFromArgb(inverse_surface)
        inverse_on_surface = theme["palettes"]["neutral"].tone(95)
        inverse_on_surface_hex = mcu.hexFromArgb(inverse_on_surface)

    # Based on: /Applications/Visual Studio Code.app/Contents/Resources/app/extensions/theme-tomorrow-night-blue/themes/tomorrow-night-blue-color-theme.json
    dictionary = {
        "type": mode,
        "colors": {
            "focusBorder": "#00000000",
            "foreground": on_surface_hex,
            "widget.border": "#00000000",
            "widget.shadow": "#00000000",
            "descriptionForeground": on_surface_hex,
            "icon.foreground": on_surface_hex,
            "selection.background": primary_hex + "5f",
            "textLink.activeForeground": primary_hex,
            "textLink.foreground": primary_hex,
            "textPreformat.foreground": tertiary_hex,
            "textSeparator.foreground": tertiary_hex,
            "toolbar.hoverBackground": "#00000000",
            "button.background": primary_hex,
            "button.foreground": on_primary_hex,
            "button.hoverBackground": primary_raised_hex,
            "button.secondaryForeground": on_secondary_hex,
            "button.secondaryBackground": secondary_hex,
            "button.secondaryHoverBackground": secondary_raised_hex,
            "dropdown.background": surface_container_hex,
            "dropdown.listBackground": surface_container_hex,
            "dropdown.border": "#00000000",
            "dropdown.foreground": on_surface_hex,
            "input.background": surface_container_hex,
            "input.foreground": on_surface_hex,
            "input.placeholderForeground": on_surface_hex,
            "inputOption.activeBackground": tertiary_hex,
            "inputOption.activeBorder": "#00000000",
            "inputOption.activeForeground": on_tertiary_hex,
            "inputOption.hoverBackground": "#00000000",
            "inputValidation.errorBackground": error_hex,
            "inputValidation.errorForeground": on_error_hex,
            "inputValidation.errorBorder": "#00000000",
            "inputValidation.infoBackground": tertiary_hex,
            "inputValidation.infoForeground": on_tertiary_hex,
            "inputValidation.infoBorder": "#00000000",
            "inputValidation.warningBackground": primary_hex,
            "inputValidation.warningForeground": on_primary_hex,
            "inputValidation.warningBorder": "#00000000",
            "scrollbarSlider.activeBackground": secondary_container_raised_hex,
            "scrollbarSlider.background": secondary_container_hex,
            "scrollbarSlider.hoverBackground": secondary_container_raised_hex,
            "badge.foreground": on_primary_container_hex,
            "badge.background": primary_container_hex,
            "list.activeSelectionBackground": primary_container_hex,
            "list.activeSelectionForeground": on_primary_container_hex,
            "list.highlightForeground": primary_hex,
            "list.hoverBackground": primary_hex+"3f",
            "list.invalidItemForeground": error_hex,
            "list.errorForeground": error_hex,
            "list.warningForeground": primary_hex,
            "activityBar.background": surface_container_high_hex,
            "activityBar.foreground": tertiary_hex,
            "activityBarBadge.background": primary_container_hex,
            "activityBarBadge.foreground": on_primary_container_hex,
            "activityBar.inactiveForeground": on_surface_hex,
            "sideBar.background": surface_container_hex,
            "editorGroup.dropBackground": tertiary_hex+"5f",
            "editorGroupHeader.tabsBackground": surface_container_lowest_hex,
            "editorGroup.dropIntoPromptForeground": on_primary_container_hex,
            "editorGroup.dropIntoPromptBackground": primary_container_hex,
            "tab.activeBackground": primary_hex,
            "tab.unfocusedActiveBackground": primary_hex,
            "tab.activeForeground": on_primary_hex,
            "tab.inactiveBackground": secondary_hex,
            "tab.unfocusedInactiveBackground": secondary_hex,
            "tab.inactiveForeground": on_secondary_hex,
            "tab.unfocusedActiveForeground": on_primary_hex,
            "tab.unfocusedInactiveForeground": on_secondary_hex,
            "tab.hoverBackground": primary_hex,
            "tab.unfocusedHoverBackground": primary_hex,
            "editor.background": surface_container_low_hex,
            "editor.foreground": on_surface_hex,
            "editorLineNumber.foreground": on_surface_hex,
            "editorLineNumber.activeForeground": primary_hex,
            "editorCursor.background": on_primary_hex,
            "editorCursor.foreground": primary_hex,
            "editor.selectionBackground": primary_hex + "5f",
            "editor.selectionHighlightBackground": primary_hex + "3f",
            "editor.wordHighlightTextBackground": "#00000000",
            "editor.findMatchBackground": tertiary_hex + "5f",
            "editor.findMatchHighlightBackground": tertiary_hex + "3f",
            "editor.lineHighlightBackground": "#00000000",
            "editor.lineHighlightBorder": "#00000000",
            "editorWhitespace.foreground": tertiary_hex + "5f",
            "editorBracketMatch.background": tertiary_hex + "3f",
            "editorBracketMatch.border": "#00000000",
            "editorBracketHighlight.foreground1": wheel_hex[1],
            "editorBracketHighlight.foreground2": wheel_hex[3],
            "editorBracketHighlight.foreground3": wheel_hex[5],
            "editorBracketHighlight.foreground4": wheel_hex[7],
            "editorBracketHighlight.foreground5": wheel_hex[9],
            "editorBracketHighlight.foreground6": wheel_hex[10],
            "editorBracketHighlight.unexpectedBracket.foreground": wheel_hex[0],
            "editorWidget.foreground": on_surface_hex,
            "editorWidget.background": surface_container_high_hex,
            "editorWidget.border": "#00000000",
            "statusBar.background": surface_container_highest_hex,
            "statusBar.foreground": on_surface_hex,
            "statusBar.border": "#00000000",
            "statusBar.debuggingBackground": tertiary_hex,
            "statusBar.debuggingForeground": on_tertiary_hex,
            "statusBar.debuggingBorder": "#00000000",
            "statusBar.noFolderBackground": surface_container_highest_hex,
            "statusBar.noFolderForeground": on_surface_hex,
            "statusBar.noFolderBorder": "#00000000",
            "statusBarItem.errorBackground": error_hex,
            "statusBarItem.errorForeground": on_error_hex,
            "titleBar.activeBackground": surface_container_highest_hex,
            "titleBar.activeForeground": on_surface_hex,
            "titleBar.inactiveBackground": surface_container_highest_hex,
            "titleBar.inactiveForeground": on_surface_hex,
            "notificationsErrorIcon.foreground": error_hex,
            "notificationsWarningIcon.foreground": primary_hex,
            "notificationsInfoIcon.foreground": tertiary_hex,
            "keybindingLabel.background": tertiary_hex,
            "keybindingLabel.foreground": on_tertiary_hex,
            "keybindingLabel.border": tertiary_hex,
            "keybindingLabel.bottomBorder": tertiary_hex,
            "terminal.ansiBlack": ansi_hex[0],
            "terminal.ansiRed": ansi_hex[1],
            "terminal.ansiGreen": ansi_hex[2],
            "terminal.ansiYellow": ansi_hex[3],
            "terminal.ansiBlue": ansi_hex[4],
            "terminal.ansiMagenta": ansi_hex[5],
            "terminal.ansiCyan": ansi_hex[6],
            "terminal.ansiWhite": ansi_hex[7],
            "terminal.ansiBrightBlack": ansi_hex[0],
            "terminal.ansiBrightRed": ansi_hex[1],
            "terminal.ansiBrightGreen": ansi_hex[2],
            "terminal.ansiBrightYellow": ansi_hex[3],
            "terminal.ansiBrightBlue": ansi_hex[4],
            "terminal.ansiBrightMagenta": ansi_hex[5],
            "terminal.ansiBrightCyan": ansi_hex[6],
            "terminal.ansiBrightWhite": ansi_hex[7],
            "terminal.selectionBackground": primary_hex,
            "terminal.selectionForeground": on_primary_hex,
            "terminalCursor.background": on_primary_hex,
            "terminalCursor.foreground": primary_hex,
            "settings.modifiedItemIndicator": tertiary_hex,
            "settings.headerForeground": on_surface_hex,
            "settings.settingsHeaderHoverForeground": on_surface_hex
        },
        "tokenColors": [
            {
                "scope": [
                    "meta.embedded",
                    "source.groovy.embedded",
                    "meta.jsx.children",
                    "string meta.image.inline.markdown",
                ],
                "settings": {"foreground": on_surface_hex},
            },
            {
                "name": "Comments",
                "scope": ["comment", "string.quoted.docstring"],
                "settings": {"fontStyle": "italic", "foreground": secondary_hex},
            },
            {
                "name": "Foreground, Operator",
                "scope": "keyword.operator.class, keyword.operator, constant.other, source.php.embedded.line",
                "settings": {"fontStyle": "", "foreground": on_surface_hex},
            },
            {
                "name": "Variable, String Link, Regular Expression, Tag Name",
                "scope": "variable, support.other.variable, string.other.link, string.regexp, entity.name.tag, entity.other.attribute-name, meta.tag, declaration.tag, markup.deleted.git_gutter",
                "settings": {"foreground": wheel_hex[4]},
            },
            {
                "name": "Number, Constant, Function Argument, Tag Attribute, Embedded",
                "scope": "constant.numeric, constant.language, support.constant, constant.character, variable.parameter, punctuation.section.embedded, keyword.other.unit",
                "settings": {"fontStyle": "", "foreground": tertiary_hex},
            },
            {
                "name": "Class, Support",
                "scope": "entity.name.class, entity.name.type, entity.name.namespace, entity.name.scope-resolution, support.type, support.class",
                "settings": {"fontStyle": "", "foreground": wheel_hex[6]},
            },
            {
                "name": "String, Symbols, Inherited Class, Markup Heading, GitGutter inserted",
                "scope": "string, constant.other.symbol, entity.other.inherited-class, markup.heading, markup.inserted.git_gutter",
                "settings": {"fontStyle": "", "foreground": wheel_hex[11]},
            },
            {
                "name": "Operator, Misc",
                "scope": "keyword.operator, constant.other.color",
                "settings": {"foreground": wheel_hex[8]},
            },
            {
                "name": "Function, Special Method, Block Level",
                "scope": "entity.name.function, meta.function-call, support.function, keyword.other.special-method, meta.block-level, markup.changed.git_gutter",
                "settings": {"fontStyle": "", "foreground": primary_hex},
            },
            {
                "name": "Keyword, Storage",
                "scope": "keyword, storage, storage.type, entity.name.tag.css",
                "settings": {"fontStyle": "", "foreground": wheel_hex[2]},
            },
            {
                "name": "Invalid",
                "scope": "invalid",
                "settings": {"fontStyle": "", "foreground": error_hex},
            },
            {
                "name": "Separator",
                "scope": "meta.separator",
                "settings": {"foreground": on_surface_hex},
            },
            {
                "name": "Diff foreground",
                "scope": "markup.inserted.diff, markup.deleted.diff, meta.diff.header.to-file, meta.diff.header.from-file",
                "settings": {"foreground": on_surface_hex},
            },
            {
                "name": "Diff insertion",
                "scope": "markup.inserted.diff, meta.diff.header.to-file",
                "settings": {"foreground": primary_hex},
            },
            {
                "name": "Diff deletion",
                "scope": "markup.deleted.diff, meta.diff.header.from-file",
                "settings": {"foreground": error_hex},
            },
            {
                "name": "Diff header",
                "scope": "meta.diff.header.from-file, meta.diff.header.to-file",
                "settings": {"foreground": on_surface_hex},
            },
            {
                "name": "Diff range",
                "scope": "meta.diff.range",
                "settings": {"fontStyle": "italic", "foreground": on_surface_hex},
            },
            {
                "name": "Markup Quote",
                "scope": "markup.quote",
                "settings": {"foreground": tertiary_hex},
            },
            {
                "name": "Markup Lists",
                "scope": "markup.list",
                "settings": {"foreground": tertiary_hex},
            },
            {
                "name": "Markup Styling",
                "scope": "markup.bold, markup.italic",
                "settings": {"foreground": on_surface_hex},
            },
            {
                "name": "Markup: Strong",
                "scope": "markup.bold",
                "settings": {"fontStyle": "bold"},
            },
            {
                "name": "Markup: Emphasis",
                "scope": "markup.italic",
                "settings": {"fontStyle": "italic"},
            },
            {
                "scope": "markup.strikethrough",
                "settings": {"fontStyle": "strikethrough"},
            },
            {
                "name": "Markup Inline",
                "scope": "markup.inline.raw",
                "settings": {"fontStyle": "", "foreground": tertiary_hex},
            },
            {
                "name": "Markup Headings",
                "scope": "markup.heading",
                "settings": {"foreground": primary_hex},
            },
            {"scope": "token.info-token", "settings": {"foreground": tertiary_hex}},
            {"scope": "token.warn-token", "settings": {"foreground": primary_hex}},
            {"scope": "token.error-token", "settings": {"foreground": error_hex}},
            {"scope": "token.debug-token", "settings": {"foreground": tertiary_hex}},
        ],
    }

    json.dump(dictionary, file, indent=4)
