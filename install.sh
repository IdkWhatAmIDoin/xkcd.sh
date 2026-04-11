#!/bin/bash

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "installing dependencies..."

install_pkgs() {
    PKGS="xdotool emacs vim ed nano python3 python3-pip"
    if command -v apt-fast &>/dev/null; then
        sudo apt-fast update && sudo apt-fast install -y $PKGS
    elif command -v apt &>/dev/null; then
        sudo apt update && sudo apt install -y $PKGS
    elif command -v dnf &>/dev/null; then
        sudo dnf install -y $PKGS
    elif command -v pacman &>/dev/null; then
        sudo pacman -Sy --noconfirm $PKGS
    elif command -v zypper &>/dev/null; then
        sudo zypper install -y $PKGS
    elif command -v brew &>/dev/null; then
        brew install $PKGS
    else
        echo "couldn't detect a package manager, install these manually: $PKGS"
        exit 1
    fi
}

install_pkgs

echo ""
echo "detecting shell..."

SHELL_NAME="$(basename "$SHELL")"
case "$SHELL_NAME" in
    zsh)  RC="$HOME/.zshrc" ;;
    bash) RC="$HOME/.bashrc" ;;
    fish) RC="$HOME/.config/fish/config.fish" ;;
    ksh)  RC="$HOME/.kshrc" ;;
    *)    RC="$HOME/.profile" ;;
esac

echo "shell: $SHELL_NAME -> $RC"
echo ""

# add xkcd to PATH
if ! grep -q "xkcd.sh" "$RC" 2>/dev/null; then
    echo "adding xkcd to PATH in $RC..."
    if [ "$SHELL_NAME" = "fish" ]; then
        echo "fish_add_path $SCRIPT_DIR" >> "$RC"
    else
        echo "export PATH=\"\$PATH:$SCRIPT_DIR\"" >> "$RC"
    fi
else
    echo "xkcd already in PATH, skipping."
fi

# vi alias
if ! grep -q 'alias vi=' "$RC" 2>/dev/null; then
    echo "adding vi=vim alias to $RC..."
    if [ "$SHELL_NAME" = "fish" ]; then
        echo "alias vi vim" >> "$RC"
    else
        echo 'alias vi="vim"' >> "$RC"
    fi
else
    echo "vi alias already exists, skipping."
fi

chmod +x "$SCRIPT_DIR/xkcd"

echo ""
echo "done! restart your shell or run: source $RC"
echo "then you can run: xkcd <comic number>"
echo "e.g. xkcd 1168"