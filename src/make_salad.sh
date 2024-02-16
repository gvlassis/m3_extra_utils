STRAWBERRY_RED="#e60e27"
TANGERINE_ORANGE="#ffb76e"
PINEAPPLE_YELLOW="#ffd220"
KIWI_GREEN="#8ee53f"
BLUEBERRY_BLUE="#147fb2"
BLACKBERRY_PURPLE="#a73678"
POMEGRANATE_PINK="#f67a92"

script_path="$(readlink -f "${0}")"
src_path="$(dirname "${script_path}")"
root_path="$(dirname "${src_path}")"
out_path="${root_path}/out"

# STRAWBERRY_RED
python3 "${src_path}/make_theme.py" -s "${STRAWBERRY_RED}" --kitty "${out_path}/kitty/strawberry_dark.conf" --vscode "${out_path}/vscode/strawberry_dark.json" --matplotlib "${out_path}/matplotlib/strawberry_dark.mplstyle" --xcolor "${out_path}/xcolor/strawberry_dark.sty" > "/dev/null" --css "${out_path}/css/strawberry_dark.css"
python3 "${src_path}/make_theme.py" -l -s "${STRAWBERRY_RED}" --kitty "${out_path}/kitty/strawberry_light.conf" --vscode "${out_path}/vscode/strawberry_light.json" --matplotlib "${out_path}/matplotlib/strawberry_light.mplstyle" --xcolor "${out_path}/xcolor/strawberry_light.sty" > "/dev/null" --css "${out_path}/css/strawberry_light.css"

# TANGERINE_ORANGE
python3 "${src_path}/make_theme.py" -s "${TANGERINE_ORANGE}" --kitty "${out_path}/kitty/tangerine_dark.conf" --vscode "${out_path}/vscode/tangerine_dark.json" --matplotlib "${out_path}/matplotlib/tangerine_dark.mplstyle" --xcolor "${out_path}/xcolor/tangerine_dark.sty" > "/dev/null" --css "${out_path}/css/tangerine_dark.css"
python3 "${src_path}/make_theme.py" -l -s "${TANGERINE_ORANGE}" --kitty "${out_path}/kitty/tangerine_light.conf" --vscode "${out_path}/vscode/tangerine_light.json" --matplotlib "${out_path}/matplotlib/tangerine_light.mplstyle" --xcolor "${out_path}/xcolor/tangerine_light.sty" > "/dev/null" --css "${out_path}/css/tangerine_light.css"

# PINEAPPLE_YELLOW
python3 "${src_path}/make_theme.py" -s "${PINEAPPLE_YELLOW}" --kitty "${out_path}/kitty/pineapple_dark.conf" --vscode "${out_path}/vscode/pineapple_dark.json" --matplotlib "${out_path}/matplotlib/pineapple_dark.mplstyle" --xcolor "${out_path}/xcolor/pineapple_dark.sty" > "/dev/null" --css "${out_path}/css/pineapple_dark.css"
python3 "${src_path}/make_theme.py" -l -s "${PINEAPPLE_YELLOW}" --kitty "${out_path}/kitty/pineapple_light.conf" --vscode "${out_path}/vscode/pineapple_light.json" --matplotlib "${out_path}/matplotlib/pineapple_light.mplstyle" --xcolor "${out_path}/xcolor/pineapple_light.sty" > "/dev/null" --css "${out_path}/css/pineapple_light.css"

# KIWI_GREEN
python3 "${src_path}/make_theme.py" -s "${KIWI_GREEN}" --kitty "${out_path}/kitty/kiwi_dark.conf" --vscode "${out_path}/vscode/kiwi_dark.json" --matplotlib "${out_path}/matplotlib/kiwi_dark.mplstyle" --xcolor "${out_path}/xcolor/kiwi_dark.sty" > "/dev/null" --css "${out_path}/css/kiwi_dark.css"
python3 "${src_path}/make_theme.py" -l -s "${KIWI_GREEN}" --kitty "${out_path}/kitty/kiwi_light.conf" --vscode "${out_path}/vscode/kiwi_light.json" --matplotlib "${out_path}/matplotlib/kiwi_light.mplstyle" --xcolor "${out_path}/xcolor/kiwi_light.sty" > "/dev/null" --css "${out_path}/css/kiwi_light.css"

# BLUEBERRY_BLUE
python3 "${src_path}/make_theme.py" -s "${BLUEBERRY_BLUE}" --kitty "${out_path}/kitty/blueberry_dark.conf" --vscode "${out_path}/vscode/blueberry_dark.json" --matplotlib "${out_path}/matplotlib/blueberry_dark.mplstyle" --xcolor "${out_path}/xcolor/blueberry_dark.sty" > "/dev/null" --css "${out_path}/css/blueberry_dark.css"
python3 "${src_path}/make_theme.py" -l -s "${BLUEBERRY_BLUE}" --kitty "${out_path}/kitty/blueberry_light.conf" --vscode "${out_path}/vscode/blueberry_light.json" --matplotlib "${out_path}/matplotlib/blueberry_light.mplstyle" --xcolor "${out_path}/xcolor/blueberry_light.sty" > "/dev/null" --css "${out_path}/css/blueberry_light.css"

# BLACKBERRY_PURPLE
python3 "${src_path}/make_theme.py" -s "${BLACKBERRY_PURPLE}" --kitty "${out_path}/kitty/blackberry_dark.conf" --vscode "${out_path}/vscode/blackberry_dark.json" --matplotlib "${out_path}/matplotlib/blackberry_dark.mplstyle" --xcolor "${out_path}/xcolor/blackberry_dark.sty" > "/dev/null" --css "${out_path}/css/blackberry_dark.css"
python3 "${src_path}/make_theme.py" -l -s "${BLACKBERRY_PURPLE}" --kitty "${out_path}/kitty/blackberry_light.conf" --vscode "${out_path}/vscode/blackberry_light.json" --matplotlib "${out_path}/matplotlib/blackberry_light.mplstyle" --xcolor "${out_path}/xcolor/blackberry_light.sty" > "/dev/null" --css "${out_path}/css/blackberry_light.css"

# POMEGRANATE_PINK
python3 "${src_path}/make_theme.py" -s "${POMEGRANATE_PINK}" --kitty "${out_path}/kitty/pomegranate_dark.conf" --vscode "${out_path}/vscode/pomegranate_dark.json" --matplotlib "${out_path}/matplotlib/pomegranate_dark.mplstyle" --xcolor "${out_path}/xcolor/pomegranate_dark.sty" > "/dev/null" --css "${out_path}/css/pomegranate_dark.css"
python3 "${src_path}/make_theme.py" -l -s "${POMEGRANATE_PINK}" --kitty "${out_path}/kitty/pomegranate_light.conf" --vscode "${out_path}/vscode/pomegranate_light.json" --matplotlib "${out_path}/matplotlib/pomegranate_light.mplstyle" --xcolor "${out_path}/xcolor/pomegranate_light.sty" > "/dev/null" --css "${out_path}/css/pomegranate_light.css"