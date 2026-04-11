#!/usr/bin/env python3
import time

def move(row, col):
    print(f"\033[{row};{col}H", end="", flush=True)

def clear():
    print("\033[2J", end="", flush=True)

def hide_cursor():
    print("\033[?25l", end="", flush=True)

def show_cursor():
    print("\033[?25h", end="", flush=True)

def get_terminal_size():
    import shutil
    return shutil.get_terminal_size()

XKCD_ART = [
    "      _           _ ",
    "__  _| | _____ __| |",
    r"\ \/ / |/ / __/ _` |",
    r" >  <|   < (_| (_| |",
    r"/_/\_\_|\_\___\__,_|",
    "         comic #1168"
]

TOP_MESSAGES = [
    (0.0,  "Rob!"),
    (1.5,  "You use Unix!"),
    (3.0,  "Come quick!"),
    (7.5,  "To disarm the bomb, simply enter a valid tar command"),
    (8.0,  "on your first try."),
    (8.5,  "No googling."),
    (9.0,  "You have ten seconds."),
    (10.0, "Rob?"),
    (21.0, ""),
]

TYPEWRITER_TEXT = "I'm so sorry."
TYPEWRITER_START = 13.0

def draw_art(cols):
    art_width = max(len(line) for line in XKCD_ART)
    for i, line in enumerate(XKCD_ART):
        col = cols - art_width + 1
        move(i + 1, col)
        print(line, end="", flush=True)

def main():
    cols, rows = get_terminal_size()

    clear()
    hide_cursor()

    draw_art(cols)

    move(rows - 3, 1)
    print("─" * cols, flush=True)
    move(rows - 2, 1)
    print("~# ", end="", flush=True)

    start = time.time()
    shown = set()
    top_row = 2
    typed = 0

    try:
        while True:
            now = time.time()
            elapsed = now - start

            for i, (t, msg) in enumerate(TOP_MESSAGES):
                if i not in shown and elapsed >= t:
                    shown.add(i)
                    move(top_row, 2)
                    print(msg, flush=True)
                    top_row += 1

            if elapsed >= TYPEWRITER_START:
                chars_to_show = int((elapsed - TYPEWRITER_START) / 0.09)
                chars_to_show = min(chars_to_show, len(TYPEWRITER_TEXT))
                if chars_to_show > typed:
                    typed = chars_to_show
                    move(rows - 2, 1)
                    print(f"\033[K~# {TYPEWRITER_TEXT[:typed]}", end="", flush=True)

            if elapsed >= TYPEWRITER_START + len(TYPEWRITER_TEXT) * 0.09 + 2.0:
                break

            time.sleep(0.05)

    finally:
        show_cursor()
        clear()
        move(1, 1)
        print('xkcd')

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        show_cursor()
        print("\033[2J\033[H", end="")