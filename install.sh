#!/usr/bin/env bash

APPS="i3 i3blocks alacritty nitrogen picom rofi brave-browser"
DIRS="i3 i3blocks alacritty rofi"

initdirectories() {
    for dir in $DIRS; do
        if [ -d "$HOME/.config/$dir" ]; then
            cp -fr "$HOME/.config/$dir" ./
            echo "$HOME/.config/$dir copied to $PWD/$dir."
        else
            echo "$HOME/.config/$dir does not exist, skipping."
        fi
    done
}

checkprograms() {
    echo "* MISSING PROGRAMS"
    local missing=0

    for app in $APPS; do
        if ! command -v "$app" >/dev/null; then
            echo "$app is not installed."
            missing=1
        fi
    done

    if [ "$missing" -eq 1 ]; then
        echo "Some programs are missing. Please install them."
        exit 1
    else
        echo "No missing programs found."
    fi
}

copyfiles() {
    echo "* COPYING FILES"

    for dir in $DIRS; do
        if [ -d "$dir" ]; then
            cp -rf "$dir" "$HOME/.config/" && \
            echo "INFO: $dir copied successfully." || \
            echo "ERROR: $dir could not be copied."
        else
            echo "$dir does not exist, skipping."
        fi
    done
}

installfonts() {
	echo "* JETBRAINSMONO FONT IS INSTALLING"
	bash <(curl -fsSL https://raw.githubusercontent.com/JetBrains/JetBrainsMono/master/install_manual.sh)
}

main() {
    if [ "$1" == "i" ]; then
        initdirectories
    else
        checkprograms
        copyfiles
	installfonts
    fi
}

main "$@"

