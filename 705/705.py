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
    "          comic #705",
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
        (0.0,  "you: we took the hostages."),
        (2.0,  "you: secured the building."),
        (4.0,  "you: cut the communication lines like you said."),
        (6.5,  ""),
        (7.0,  "boss: excellent."),
    ], end_delay=2.0)

    timed_messages([
        (0.0,  "you: but then this guy climbed up the ventilation ducts."),
        (2.5,  "you: walked across broken glass."),
        (4.5,  "you: killed anyone we sent to stop him."),
        (7.0,  ""),
        (7.5,  "boss: and he rescued the hostages?"),
    ], end_delay=2.0)

    timed_messages([
        (0.0,  "you: no, he ignored them."),
        (2.0,  "you: he just reconnected the cables we cut."),
        (4.5,  "you: muttering something about \"uptime\"."),
        (7.0,  ""),
        (7.5,  "boss: shit."),
        (9.0,  "boss: we're dealing with a sysadmin."),
    ], end_delay=3.5)

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