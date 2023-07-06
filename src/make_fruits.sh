#!/usr/bin/env bash

script_path_relative="${0}"
out_path="${1}"

script_path="$(readlink -f "${script_path_relative}")"
src_path="$(dirname "${script_path}")"

strawberry_red="#d14152"
python3 "${src_path}/make_theme.py" -s "${strawberry_red}" --kitty "${out_path}/strawberry_dark.conf" --vscode "${out_path}/strawberry_dark.json" > "/dev/null"
python3 "${src_path}/make_theme.py" -l -s "${strawberry_red}" --kitty "${out_path}/strawberry_light.conf" --vscode "${out_path}/strawberry_light.json" > "/dev/null"

tangerine_orange="#ffb76e" 
python3 "${src_path}/make_theme.py" -s "${tangerine_orange}" --kitty "${out_path}/tangerine_dark.conf" --vscode "${out_path}/tangerine_dark.json" > "/dev/null"
python3 "${src_path}/make_theme.py" -l -s "${tangerine_orange}" --kitty "${out_path}/tangerine_light.conf" --vscode "${out_path}/tangerine_light.json" > "/dev/null"

pineapple_yellow="#ffd220" 
python3 "${src_path}/make_theme.py" -s "${pineapple_yellow}" --kitty "${out_path}/pineapple_dark.conf" --vscode "${out_path}/pineapple_dark.json" > "/dev/null"
python3 "${src_path}/make_theme.py" -l -s "${pineapple_yellow}" --kitty "${out_path}/pineapple_light.conf" --vscode "${out_path}/pineapple_light.json" > "/dev/null"

kiwi_green="#8ee53f" 
python3 "${src_path}/make_theme.py" -s "${kiwi_green}" --kitty "${out_path}/kiwi_dark.conf" --vscode "${out_path}/kiwi_dark.json" > "/dev/null"
python3 "${src_path}/make_theme.py" -l -s "${kiwi_green}" --kitty "${out_path}/kiwi_light.conf" --vscode "${out_path}/kiwi_light.json" > "/dev/null"

blueberry_blue="#147fb2" 
python3 "${src_path}/make_theme.py" -s "${blueberry_blue}" --kitty "${out_path}/blueberry_dark.conf" --vscode "${out_path}/blueberry_dark.json" > "/dev/null"
python3 "${src_path}/make_theme.py" -l -s "${blueberry_blue}" --kitty "${out_path}/blueberry_light.conf" --vscode "${out_path}/blueberry_light.json" > "/dev/null"

blackberry_purple="#a73678" 
python3 "${src_path}/make_theme.py" -s "${blackberry_purple}" --kitty "${out_path}/blackberry_dark.conf" --vscode "${out_path}/blackberry_dark.json" > "/dev/null"
python3 "${src_path}/make_theme.py" -l -s "${blackberry_purple}" --kitty "${out_path}/blackberry_light.conf" --vscode "${out_path}/blackberry_light.json" > "/dev/null"

pomegranate_pink="#f67a92" 
python3 "${src_path}/make_theme.py" -s "${pomegranate_pink}" --kitty "${out_path}/pomegranate_dark.conf" --vscode "${out_path}/pomegranate_dark.json" > "/dev/null"
python3 "${src_path}/make_theme.py" -l -s "${pomegranate_pink}" --kitty "${out_path}/pomegranate_light.conf" --vscode "${out_path}/pomegranate_light.json" > "/dev/null"