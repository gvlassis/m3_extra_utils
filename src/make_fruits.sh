#!/usr/bin/env bash

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

python3 "${src_path}/make_theme.py" -s "${STRAWBERRY_RED}" --kitty "${out_path}/strawberry_dark.conf" --vscode "${out_path}/strawberry_dark.json" > "/dev/null"
python3 "${src_path}/make_theme.py" -l -s "${STRAWBERRY_RED}" --kitty "${out_path}/strawberry_light.conf" --vscode "${out_path}/strawberry_light.json" > "/dev/null"

python3 "${src_path}/make_theme.py" -s "${TANGERINE_ORANGE}" --kitty "${out_path}/tangerine_dark.conf" --vscode "${out_path}/tangerine_dark.json" > "/dev/null"
python3 "${src_path}/make_theme.py" -l -s "${TANGERINE_ORANGE}" --kitty "${out_path}/tangerine_light.conf" --vscode "${out_path}/tangerine_light.json" > "/dev/null"

python3 "${src_path}/make_theme.py" -s "${PINEAPPLE_YELLOW}" --kitty "${out_path}/pineapple_dark.conf" --vscode "${out_path}/pineapple_dark.json" > "/dev/null"
python3 "${src_path}/make_theme.py" -l -s "${PINEAPPLE_YELLOW}" --kitty "${out_path}/pineapple_light.conf" --vscode "${out_path}/pineapple_light.json" > "/dev/null"
 
python3 "${src_path}/make_theme.py" -s "${KIWI_GREEN}" --kitty "${out_path}/kiwi_dark.conf" --vscode "${out_path}/kiwi_dark.json" > "/dev/null"
python3 "${src_path}/make_theme.py" -l -s "${KIWI_GREEN}" --kitty "${out_path}/kiwi_light.conf" --vscode "${out_path}/kiwi_light.json" > "/dev/null"
 
python3 "${src_path}/make_theme.py" -s "${BLUEBERRY_BLUE}" --kitty "${out_path}/blueberry_dark.conf" --vscode "${out_path}/blueberry_dark.json" > "/dev/null"
python3 "${src_path}/make_theme.py" -l -s "${BLUEBERRY_BLUE}" --kitty "${out_path}/blueberry_light.conf" --vscode "${out_path}/blueberry_light.json" > "/dev/null"

python3 "${src_path}/make_theme.py" -s "${BLACKBERRY_PURPLE}" --kitty "${out_path}/blackberry_dark.conf" --vscode "${out_path}/blackberry_dark.json" > "/dev/null"
python3 "${src_path}/make_theme.py" -l -s "${BLACKBERRY_PURPLE}" --kitty "${out_path}/blackberry_light.conf" --vscode "${out_path}/blackberry_light.json" > "/dev/null"

python3 "${src_path}/make_theme.py" -s "${POMEGRANATE_PINK}" --kitty "${out_path}/pomegranate_dark.conf" --vscode "${out_path}/pomegranate_dark.json" > "/dev/null"
python3 "${src_path}/make_theme.py" -l -s "${POMEGRANATE_PINK}" --kitty "${out_path}/pomegranate_light.conf" --vscode "${out_path}/pomegranate_light.json" > "/dev/null"