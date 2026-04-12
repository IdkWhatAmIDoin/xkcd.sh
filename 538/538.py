#!/usr/bin/env python3
import time
import shutil

def move(row, col):
    print(f"\033[{row};{col}H", end="", flush=True)

def clear():
    print("\033[2J\033[H", end="", flush=True)

def hide_cursor():
    print("\033[?25l", end="", flush=True)

def show_cursor():
    print("\033[?25h", end="", flush=True)

def get_terminal_size():
    return shutil.get_terminal_size()

XKCD_ART = [
    "      _           _ ",
    "__  _| | _____ __| |",
    r"\ \/ / |/ / __/ _` |",
    r" >  <|   < (_| (_| |",
    r"/_/\_\_|\_\___\__,_|",
    "          comic #538",
]

def draw_art():
    cols, _ = get_terminal_size()
    art_width = max(len(line) for line in XKCD_ART)
    for i, line in enumerate(XKCD_ART):
        col = cols - art_width + 1
        move(i + 1, col)
        print(line, end="", flush=True)

def clear_with_art():
    clear()
    draw_art()

def timed_messages(messages, end_delay=2.0):
    clear_with_art()
    hide_cursor()
    start = time.time()
    shown = set()
    row = 2
    last_t = max(t for t, _ in messages)
    try:
        while True:
            elapsed = time.time() - start
            for i, (t, msg) in enumerate(messages):
                if i not in shown and elapsed >= t:
                    shown.add(i)
                    move(row, 2)
                    print(msg, flush=True)
                    row += 1
            if len(shown) == len(messages) and elapsed >= last_t + end_delay:
                break
            time.sleep(0.05)
    finally:
        show_cursor()

def main():
    timed_messages([
        (0.0,  "A CRYPTO NERD'S IMAGINATION:"),
        (1.5,  ""),
        (2.0,  "  his laptop's encrypted."),
        (3.5,  "  let's build a million-dollar cluster to crack it."),
        (6.0,  ""),
        (6.5,  "  [cluster]                      spinning up 10,000 nodes..."),
        (8.5,  "  [cluster]                      beginning brute force attack..."),
        (10.5, "  [cluster]                      0.0000001% complete..."),
        (12.5, "  [cluster]                      estimated time remaining: 3.7 billion years"),
        (15.0, ""),
        (15.5, "  no good! it's 4096-bit RSA!"),
        (17.5, ""),
        (18.0, "  blast! our evil plan is foiled."),
    ], end_delay=2.5)

    timed_messages([
        (0.0,  "WHAT WOULD ACTUALLY HAPPEN:"),
        (1.5,  ""),
        (2.0,  "  his laptop's encrypted."),
        (3.5,  ""),
        (4.0,  "  [acquiring $5 wrench]          done."),
        (6.0,  "  [hitting him with it]          done."),
        (8.5,  "  [password obtained]            got it."),
        (11.0, ""),
        (11.5, "  huh."),
        (13.0, "  that was way easier."),
    ], end_delay=3.0)

    clear_with_art()
    show_cursor()
    print("original comic made by randall munroe")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        show_cursor()
        clear()
        print("original comic made by randall munroe")