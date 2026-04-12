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
    "          comic #1319",
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
    # opening line
    timed_messages([
        (0.0, '"i spend a lot of time on this task.'),
        (2.0, " i should write a program automating it!\""),
    ], end_delay=2.0)

    # theory
    timed_messages([
        (0.0,  "THEORY:"),
        (0.5,  ""),
        (1.0,  "  [original task]  running..."),
        (2.5,  "  [original task]  done."),
        (3.5,  ""),
        (4.0,  "  [writing code]   writing automation script..."),
        (6.0,  "  [writing code]   done."),
        (7.0,  ""),
        (7.5,  "  [automation]     taking over..."),
        (9.0,  "  [automation]     running original task... done."),
        (10.0, "  [automation]     running original task... done."),
        (11.0, "  [automation]     running original task... done."),
        (12.5, ""),
        (13.0, "  you now have free time."),
        (15.0, "  nice."),
    ], end_delay=2.5)

    # reality
    timed_messages([
        (0.0,  "REALITY:"),
        (0.5,  ""),
        (1.0,  "  [original task]  running..."),
        (3.0,  "  [writing code]   starting automation script..."),
        (5.5,  "  [writing code]   this is taking longer than expected."),
        (8.0,  ""),
        (8.5,  "  [debugging]      why isn't this working."),
        (10.5, "  [debugging]      why do i need version 1.1??"),
        (12.5, "  [debugging]      IT WAS A TYPO"),
        (14.5, ""),
        (15.0, "  [rethinking]     maybe i should restructure the whole thing."),
        (18.0, "  [rethinking]     yeah definitely need to restructure it."),
        (20.5, ""),
        (21.0, "  [ongoing development]  adding edge case handling..."),
        (23.5, "  [ongoing development]  refactoring..."),
        (26.0, "  [ongoing development]  adding more features..."),
        (28.5, "  [ongoing development]  this could be so much better though..."),
        (31.0, ""),
        (31.5, "  [original task]  .............."),
        (33.5, "  [original task]  (no time for original task anymore)"),
        (36.0, ""),
        (36.5, "  'automating' comes from the roots 'auto-' meaning 'self-',"),
        (38.5, "  and 'mating', meaning 'screwing'."),
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