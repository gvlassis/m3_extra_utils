import material_color_utilities_python as mcu
import json

def write(file, mode, scheme, scheme_8):
    # See https://code.visualstudio.com/api/references/theme-color and https://code.visualstudio.com/docs/getstarted/userinterface
    # focusBorder: Border for some focused elements
    # foreground: Explorer, Extensions, Command Center, Settings UI, some symbols (e.g. in integrated terminal), ... NOT activity bar, NOR status bar, NOR panel
    # disabledForeground: Some static/disabled elements (e.g. previous/next match in search)
    # descriptionForeground: e.g. descriptions in Extensions
    # icon.foreground: Some icons in Workbench (e.g. cogs, ellipsis, side-by-side). NOT for Activity bar. It also controls the close and modified icons in the unfocused editor group.
    # sash.hoverBorder: Line when resizing
    # toolbar.hoverBackground: When hovering/clicking on an action (e.g. close tab button)
    # editorCodeLens.foreground: e.g. option text in merge
    # pickerGroup.border: e.g. in Command Center the color of separating line and text
    # pickerGroup.foreground: e.g. in Command Center the color of labels

    dictionary = {
        "type": mode,
        "colors": {
            "focusBorder": "#00000000",
            "foreground": mcu.hexFromArgb(scheme.get_onSurface()),
            "disabledForeground": mcu.hexFromArgb(scheme.get_onSurface()),
            "widget.border": "#00000000",
            "widget.shadow": "#00000000",
            "selection.background": mcu.hexFromArgb(scheme.get_primary()) + "5f",
            "descriptionForeground": mcu.hexFromArgb(scheme.get_onSurface()),
            "errorForeground": mcu.hexFromArgb(scheme_8.get_red()),
            "icon.foreground": mcu.hexFromArgb(scheme.get_onSurface()),
            "sash.hoverBorder": mcu.hexFromArgb(scheme.get_tertiary()),
            "textBlockQuote.background": mcu.hexFromArgb(scheme.get_surfaceContainerLow()),
            "textBlockQuote.border": mcu.hexFromArgb(scheme.get_tertiary()),
            "textCodeBlock.background": mcu.hexFromArgb(scheme.get_surfaceContainerLow()),
            "textLink.activeForeground": mcu.hexFromArgb(scheme.get_tertiary()),
            "textLink.foreground": mcu.hexFromArgb(scheme.get_tertiary()),
            "textPreformat.foreground": mcu.hexFromArgb(scheme.get_primary()),
            "textSeparator.foreground": mcu.hexFromArgb(scheme.get_primary()),
            "toolbar.hoverBackground": "#00000000",
            "button.background": mcu.hexFromArgb(scheme.get_primary()),
            "button.foreground": mcu.hexFromArgb(scheme.get_onPrimary()),
            "button.hoverBackground": mcu.hexFromArgb(scheme.get_primary()),
            "button.secondaryForeground": mcu.hexFromArgb(scheme.get_onSecondary()),
            "button.secondaryBackground": mcu.hexFromArgb(scheme.get_secondary()),
            "button.secondaryHoverBackground": mcu.hexFromArgb(scheme.get_secondary()),
            "dropdown.background": mcu.hexFromArgb(scheme.get_surfaceContainerHigh()),
            "dropdown.listBackground": mcu.hexFromArgb(scheme.get_surfaceContainerHigh()),
            "dropdown.border": mcu.hexFromArgb(scheme.get_surfaceContainerHigh()),
            "dropdown.foreground": mcu.hexFromArgb(scheme.get_onSurface()),
            "input.background": mcu.hexFromArgb(scheme.get_surfaceContainer()),
            "inputOption.activeBackground": mcu.hexFromArgb(scheme.get_tertiary()),
            "inputOption.activeBorder": "#00000000",
            "inputOption.activeForeground": mcu.hexFromArgb(scheme.get_onTertiary()),
            "inputValidation.errorBackground": mcu.hexFromArgb(scheme.get_error()),
            "inputValidation.errorForeground": mcu.hexFromArgb(scheme.get_onError()),
            "inputValidation.errorBorder": "#00000000",
            "scrollbar.shadow": "#00000000",
            "scrollbarSlider.activeBackground": mcu.hexFromArgb(scheme.get_tertiary()) + "3f",
            "scrollbarSlider.background": mcu.hexFromArgb(scheme.get_tertiary()) + "3f",
            "scrollbarSlider.hoverBackground": mcu.hexFromArgb(scheme.get_tertiary()) + "3f",
            "badge.foreground": mcu.hexFromArgb(scheme.get_onPrimaryContainer()),
            "badge.background": mcu.hexFromArgb(scheme.get_primaryContainer()),
            "list.activeSelectionBackground": mcu.hexFromArgb(scheme.get_primaryContainer()),
            "list.activeSelectionForeground": mcu.hexFromArgb(scheme.get_onPrimaryContainer()),
            "list.highlightForeground": mcu.hexFromArgb(scheme.get_primary()),
            "list.hoverBackground": "#00000000",
            "list.hoverForeground": mcu.hexFromArgb(scheme.get_onSurface()),
            "activityBar.background": mcu.hexFromArgb(scheme.get_surfaceContainer()),
            "activityBar.foreground": mcu.hexFromArgb(scheme.get_tertiary()),
            "activityBar.inactiveForeground": mcu.hexFromArgb(scheme.get_onSurface()),
            "activityBarBadge.background": mcu.hexFromArgb(scheme.get_primaryContainer()),
            "activityBarBadge.foreground": mcu.hexFromArgb(scheme.get_onPrimaryContainer()),
            "sideBar.background": mcu.hexFromArgb(scheme.get_surfaceContainerLow()),
            "editorGroup.border": "#00000000",
            "editorGroup.dropBackground": mcu.hexFromArgb(scheme.get_tertiary()) + "5f",
            "editorGroupHeader.tabsBackground": mcu.hexFromArgb(scheme.get_surfaceContainerLowest()),
            "editorGroup.dropIntoPromptBackground": mcu.hexFromArgb(scheme.get_surfaceContainerHigh()),
            "tab.activeBackground": mcu.hexFromArgb(scheme.get_primary()),
            "tab.unfocusedActiveBackground": mcu.hexFromArgb(scheme.get_primary()),
            "tab.activeForeground": mcu.hexFromArgb(scheme.get_onPrimary()),
            "tab.border": mcu.hexFromArgb(scheme.get_surfaceContainerLowest()),
            "tab.inactiveBackground": mcu.hexFromArgb(scheme.get_secondary()),
            "tab.unfocusedInactiveBackground": mcu.hexFromArgb(scheme.get_secondary()),
            "tab.inactiveForeground": mcu.hexFromArgb(scheme.get_onSecondary()),
            "tab.unfocusedActiveForeground": mcu.hexFromArgb(scheme.get_onPrimary()),
            "tab.unfocusedInactiveForeground": mcu.hexFromArgb(scheme.get_onSecondary()),
            "editor.background": mcu.hexFromArgb(scheme.get_surface()),
            "editor.foreground": mcu.hexFromArgb(scheme.get_onSurface()),
            "editorLineNumber.foreground": mcu.hexFromArgb(scheme.get_onSurfaceVariant()),
            "editorLineNumber.activeForeground": mcu.hexFromArgb(scheme.get_primary()),
            "editorCursor.background": mcu.hexFromArgb(scheme.get_onPrimary()),
            "editorCursor.foreground": mcu.hexFromArgb(scheme.get_primary()),
            "editor.selectionBackground": mcu.hexFromArgb(scheme.get_primary()) + "5f",
            "editor.selectionHighlightBackground": mcu.hexFromArgb(scheme.get_primary()) + "3f",
            "editor.wordHighlightTextBackground": "#00000000",
            "editor.findMatchBackground": mcu.hexFromArgb(scheme.get_tertiary()) + "5f",
            "editor.findMatchHighlightBackground": mcu.hexFromArgb(scheme.get_tertiary()) + "3f",
            "editor.lineHighlightBorder": "#00000000",
            "editorLink.activeForeground": mcu.hexFromArgb(scheme.get_tertiary()),
            "editorWhitespace.foreground": mcu.hexFromArgb(scheme.get_tertiary()) + "3f",
            "editorCodeLens.foreground": mcu.hexFromArgb(scheme.get_onSurface()),
            "editorBracketMatch.background": mcu.hexFromArgb(scheme.get_secondary()) + "3f",
            "editorBracketMatch.border": "#00000000",
            "editorBracketHighlight.foreground1": mcu.hexFromArgb(scheme_8.get_bright_green()),
            "editorBracketHighlight.foreground2": mcu.hexFromArgb(scheme_8.get_bright_yellow()),
            "editorBracketHighlight.foreground3": mcu.hexFromArgb(scheme_8.get_bright_magenta()),
            "editorBracketHighlight.foreground4": mcu.hexFromArgb(scheme_8.get_bright_cyan()),
            "editorBracketHighlight.unexpectedBracket.foreground": mcu.hexFromArgb(scheme_8.get_bright_red()),
            "editorOverviewRuler.background": "#00000000",
            "editorOverviewRuler.border": "#00000000",
            "editorOverviewRuler.findMatchForeground": "#00000000",
            "editorOverviewRuler.rangeHighlightForeground": "#00000000",
            "editorOverviewRuler.selectionHighlightForeground": "#00000000",
            "editorOverviewRuler.wordHighlightForeground": "#00000000",
            "editorOverviewRuler.wordHighlightStrongForeground": "#00000000",
            "editorOverviewRuler.wordHighlightTextForeground": "#00000000",
            "editorOverviewRuler.modifiedForeground": "#00000000",
            "editorOverviewRuler.addedForeground": "#00000000",
            "editorOverviewRuler.deletedForeground": "#00000000",
            "editorOverviewRuler.errorForeground": "#00000000",
            "editorOverviewRuler.warningForeground": "#00000000",
            "editorOverviewRuler.infoForeground": "#00000000",
            "editorOverviewRuler.bracketMatchForeground": mcu.hexFromArgb(scheme.get_tertiary()),
            "editorGutter.background": mcu.hexFromArgb(scheme.get_surfaceContainerLowest()),
            "editorWidget.background": mcu.hexFromArgb(scheme.get_surfaceContainerHigh()),
            "editorWidget.border": "#00000000",
            "merge.currentHeaderBackground": mcu.hexFromArgb(scheme.get_primary()) + "5f",
            "merge.currentContentBackground": mcu.hexFromArgb(scheme.get_primary()) + "5f",
            "merge.incomingHeaderBackground": mcu.hexFromArgb(scheme.get_tertiary()) + "5f",
            "merge.incomingContentBackground": mcu.hexFromArgb(scheme.get_tertiary()) + "5f",
            "editorOverviewRuler.currentContentForeground": "#00000000",
            "editorOverviewRuler.incomingContentForeground": "#00000000",
            "editorOverviewRuler.commonContentForeground": "#00000000",
            "editorOverviewRuler.commentForeground": "#00000000",
            "editorOverviewRuler.commentUnresolvedForeground": "#00000000",
            "panel.border": "#00000000",
            "panelTitle.activeBorder": "#00000000",
            "panelTitle.activeForeground": mcu.hexFromArgb(scheme.get_primary()),
            "panelTitle.inactiveForeground": mcu.hexFromArgb(scheme.get_onSurface()),
            "statusBar.background": mcu.hexFromArgb(scheme.get_primaryContainer()),
            "statusBar.foreground": mcu.hexFromArgb(scheme.get_onPrimaryContainer()),
            "statusBarItem.activeBackground": "#00000000",
            "statusBarItem.hoverBackground": "#00000000",
            "statusBar.noFolderForeground": mcu.hexFromArgb(scheme.get_onPrimaryContainer()),
            "statusBar.noFolderBackground": mcu.hexFromArgb(scheme.get_primaryContainer()),
            "titleBar.activeBackground": mcu.hexFromArgb(scheme.get_surfaceContainerHighest()),
            "titleBar.activeForeground": mcu.hexFromArgb(scheme.get_onSurface()),
            "titleBar.inactiveBackground": mcu.hexFromArgb(scheme.get_surfaceContainerHighest()),
            "titleBar.inactiveForeground": mcu.hexFromArgb(scheme.get_onSurface()),
            "notificationCenterHeader.foreground": mcu.hexFromArgb(scheme.get_onPrimaryContainer()),
            "notificationCenterHeader.background": mcu.hexFromArgb(scheme.get_primaryContainer()),
            "notifications.border": mcu.hexFromArgb(scheme.get_surfaceContainerLowest()),
            "pickerGroup.border": mcu.hexFromArgb(scheme.get_primary()),
            "pickerGroup.foreground": mcu.hexFromArgb(scheme.get_primary()),
            "keybindingLabel.background": mcu.hexFromArgb(scheme.get_tertiaryContainer()),
            "keybindingLabel.foreground": mcu.hexFromArgb(scheme.get_onTertiaryContainer()),
            "keybindingLabel.border": mcu.hexFromArgb(scheme.get_tertiaryContainer()),
            "keybindingLabel.bottomBorder": mcu.hexFromArgb(scheme.get_tertiaryContainer()),
            "keybindingTable.headerBackground": mcu.hexFromArgb(scheme.get_surfaceContainer()),
            "keybindingTable.rowsBackground": mcu.hexFromArgb(scheme.get_surfaceContainer()),
            "terminal.foreground": mcu.hexFromArgb(scheme.get_onSurface()),
            "terminal.ansiBlack": mcu.hexFromArgb(scheme_8.get_black()),
            "terminal.ansiRed": mcu.hexFromArgb(scheme_8.get_red()),
            "terminal.ansiGreen": mcu.hexFromArgb(scheme_8.get_green()),
            "terminal.ansiYellow": mcu.hexFromArgb(scheme_8.get_yellow()),
            "terminal.ansiBlue": mcu.hexFromArgb(scheme_8.get_blue()),
            "terminal.ansiMagenta": mcu.hexFromArgb(scheme_8.get_magenta()),
            "terminal.ansiCyan": mcu.hexFromArgb(scheme_8.get_cyan()),
            "terminal.ansiWhite": mcu.hexFromArgb(scheme_8.get_white()),
            "terminal.ansiBrightBlack": mcu.hexFromArgb(scheme_8.get_bright_black()),
            "terminal.ansiBrightRed": mcu.hexFromArgb(scheme_8.get_bright_red()),
            "terminal.ansiBrightGreen": mcu.hexFromArgb(scheme_8.get_bright_green()),
            "terminal.ansiBrightYellow": mcu.hexFromArgb(scheme_8.get_bright_yellow()),
            "terminal.ansiBrightBlue": mcu.hexFromArgb(scheme_8.get_bright_blue()),
            "terminal.ansiBrightMagenta": mcu.hexFromArgb(scheme_8.get_bright_magenta()),
            "terminal.ansiBrightCyan": mcu.hexFromArgb(scheme_8.get_bright_cyan()),
            "terminal.ansiBrightWhite": mcu.hexFromArgb(scheme_8.get_bright_white()),
            "terminal.selectionBackground": mcu.hexFromArgb(scheme.get_primary()),
            "terminal.selectionForeground": mcu.hexFromArgb(scheme.get_onPrimary()),
            "terminalCursor.background": mcu.hexFromArgb(scheme.get_onTertiary()),
            "terminalCursor.foreground": mcu.hexFromArgb(scheme.get_tertiary()),
            "walkThrough.embeddedEditorBackground": mcu.hexFromArgb(scheme.get_surfaceContainerLow()),
            "walkThrough.stepTitle.foreground": mcu.hexFromArgb(scheme.get_onSurface()),
            "settings.headerForeground": mcu.hexFromArgb(scheme.get_onSurface()),
            "settings.modifiedItemIndicator": mcu.hexFromArgb(scheme.get_tertiary()),
            "settings.settingsHeaderHoverForeground": mcu.hexFromArgb(scheme.get_onSurface()),
            "notebook.cellBorderColor": "#00000000",
            "notebook.focusedCellBorder": mcu.hexFromArgb(scheme.get_tertiary()),
            "notebook.inactiveFocusedCellBorder": mcu.hexFromArgb(scheme.get_tertiary()),
        },
        "tokenColors": [
            {
                "scope": "markup.bold markup.italic",
                "settings": {"fontStyle": "bold italic"}
            },
			{
                "scope": "markup.bold",
                "settings": {"fontStyle": "bold"}
            },
            {
                "scope": "markup.italic",
                "settings": {"fontStyle": "italic"}
            },
            {
                "scope": "markup.underline",
                "settings": {"fontStyle": "underline"}
            },
            {
                "scope": "markup.strikethrough",
                "settings": {"fontStyle": "strikethrough"}
            },
			{
                "scope": "keyword.control, 	keyword.operator, storage.type, meta.parameter-expansion",
                "settings": {"fontStyle": "bold", "foreground": mcu.hexFromArgb(scheme.get_onSurface())}
            },
            {
                "scope": "constant.numeric.float, constant.numeric.dec, constant.numeric.hex, constant.numeric.bin, constant.numeric.decimal, constant.numeric.integer.binary, constant.numeric.integer.octal, constant.numeric.integer.decimal, constant.numeric.integer.hexadecimal, constant.numeric.integer.yaml, constant.numeric.integer.ruby, constant.numeric.dart, constant.numeric.json, constant.numeric.julia, constant.numeric.perl, constant.numeric.css, constant.language.bool, constant.language.boolean, constant.language.python, constant.language.go, constant.language.dart, constant.language.r, constant.language.java, constant.language.lua, constant.language.json, constant.language.c, constant.language.false.cpp, constant.language.true.cpp, constant.language.julia, constant.language.ruby, constant.language.null, constant.language.nullptr, constant.language.NULL, constant.language.nan, constant.language.infinity, support.constant, constant.other.unicode-range, constant.other.color",
                "settings": {"fontStyle": "bold", "foreground": mcu.hexFromArgb(scheme.get_primary())}
            },
            {
                "scope": "heading.1, meta.separator",
                "settings": {"foreground": mcu.hexFromArgb(scheme.get_primary())}
            },
            {
                "scope": "heading.2, heading.3, heading.4, heading.5, heading.6",
                "settings": {"foreground": mcu.hexFromArgb(scheme.get_secondary())}
            },
            {
                "scope": "comment.line",
                "settings": {"fontStyle": "italic", "foreground": mcu.hexFromArgb(scheme.get_tertiary())}
            },
            {
                "scope": "markup.underline.link",
                "settings": {"fontStyle": "regular", "foreground": mcu.hexFromArgb(scheme.get_tertiary())}
            },
            {
                "scope": "storage.modifier, meta.function.decorator, entity.name.function.decorator",
                "settings": {"fontStyle": "bold italic", "foreground": mcu.hexFromArgb(scheme_8.get_red())}
            },
            {
                "scope": "constant.character.escape, keyword.rainbow2",
                "settings": {"fontStyle": "regular", "foreground": mcu.hexFromArgb(scheme_8.get_red())}
            },
            {
                "scope": "entity.name.function, meta.function-call, markup.list.numbered, support.function, entity.name.function.rainbow3",
                "settings": {"fontStyle": "regular", "foreground": mcu.hexFromArgb(scheme_8.get_green())}
            },
            {
                "scope": "string, comment.rainbow4",
                "settings": {"fontStyle": "regular", "foreground": mcu.hexFromArgb(scheme_8.get_yellow())}
            },
            {
                "scope": "entity.name.type, entity.name.struct, entity.name.enum, entity.name.interface, entity.name.tag, entity.other.attribute-name, string.rainbow5",
                "settings": {"fontStyle": "regular", "foreground": mcu.hexFromArgb(scheme_8.get_blue())}
            },
            {
                "scope": "constant.other.placeholder, meta.format.percent, punctuation.definition.variable, variable.other.normal, 	punctuation.section.array.shell, punctuation.definition.evaluation, variable.language.special.wildcard, constant.character.math, variable.parameter.rainbow6",
                "settings": {"fontStyle": "regular", "foreground": mcu.hexFromArgb(scheme_8.get_magenta())}
            },
			{
                "scope": "keyword.control.table",
                "settings": {"fontStyle": "bold", "foreground": mcu.hexFromArgb(scheme_8.get_cyan())}
            },
            {
                "scope": "markup.raw.block",
                "settings": {"foreground": mcu.hexFromArgb(scheme_8.get_cyan())}
            },
            {
                "scope": "variable.parameter.function.language, meta.function-call.arguments, constant.other.option, constant.numeric.rainbow7",
                "settings": {"fontStyle": "regular", "foreground": mcu.hexFromArgb(scheme_8.get_cyan())}
            },
            {
                "scope": "markup.list.unnumbered",
                "settings": {"foreground": mcu.hexFromArgb(scheme_8.get_bright_green())}
            },
            {
                "scope": "markup.quote",
                "settings": {"foreground": mcu.hexFromArgb(scheme_8.get_bright_blue())}
            },
            {
                "scope": "punctuation.definition.string, markup.quote, entity.name.type.rainbow8",
                "settings": {"fontStyle": "regular", "foreground": mcu.hexFromArgb(scheme_8.get_bright_blue())}
            },
			{
                "scope": "markup.bold.rainbow9",
                "settings": {"fontStyle": "regular", "foreground": mcu.hexFromArgb(scheme_8.get_bright_magenta())}
            },
            {
                "scope": "markup.inline.raw",
                "settings": {"foreground": mcu.hexFromArgb(scheme_8.get_bright_cyan())}
            },
            {
                "scope": "invalid.rainbow10",
                "settings": {"fontStyle": "regular", "foreground": mcu.hexFromArgb(scheme_8.get_bright_cyan())}
            }
        ]
    }

    json.dump(dictionary, file, indent=4)