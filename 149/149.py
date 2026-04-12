#!/usr/bin/env python3
import os
import time

def move(row, col):
    print(f"\033[{row};{col}H", end="", flush=True)

def clear():
    print("\033[2J\033[H", end="", flush=True)

def get_terminal_size():
    import shutil
    return shutil.get_terminal_size()

XKCD_ART = [
    "      _           _ ",
    "__  _| | _____ __| |",
    r"\ \/ / |/ / __/ _` |",
    r" >  <|   < (_| (_| |",
    r"/_/\_\_|\_\___\__,_|",
    "          comic #149"
]

def draw_art():
    cols, rows = get_terminal_size()
    art_width = max(len(line) for line in XKCD_ART)
    for i, line in enumerate(XKCD_ART):
        col = cols - art_width + 1
        move(i + 1, col)
        print(line, end="", flush=True)

def clear_with_art():
    clear()
    draw_art()
    move(7, 1)  # start printing below the art

def main():
    clear_with_art()

    is_root = os.geteuid() == 0

    if is_root:
        print("Okay.")
        print("original comic made by randall munroe")
    else:
        print("What? Make it yourself.")
        print(r"*hint: sudo is the way to go*")
        print("original comic made by randall munroe")

if __name__ == "__main__":
    main()
