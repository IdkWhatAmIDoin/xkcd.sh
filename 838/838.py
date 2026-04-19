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
    "          comic #838",
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

def typewrite(text, delay=0.09):
    for ch in text:
        print(ch, end="", flush=True)
        time.sleep(delay)

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

NICE_LIST = [
    "alice",
    "bob",
    "carol",
    "david",
    "eve",
    "frank",
    "grace",
    "hank",
]

NAUGHTY_LIST = [
    "mallory",
    "oscar",
    "peggy",
    "trudy",
    "victor",
]

COL_W = 16  # inner width of each column (excluding "| " and " |")

def draw_list_frame(start_row, start_col, nice, naughty):
    border    = "+" + "-" * (COL_W + 2) + "+"
    header_n  = f"|{'NICE':^{COL_W + 2}}|"
    header_ng = f"|{'NAUGHTY':^{COL_W + 2}}|"
    gap = "   "

    def pr(row, text):
        move(row, start_col)
        print(text, flush=True)

    pr(start_row,     border + gap + border)
    pr(start_row + 1, header_n + gap + header_ng)
    pr(start_row + 2, border + gap + border)

    max_rows = max(len(nice), len(naughty))
    for i in range(max_rows):
        ne = nice[i]    if i < len(nice)    else ""
        ng = naughty[i] if i < len(naughty) else ""
        pr(start_row + 3 + i, f"| {ne:<{COL_W}} |" + gap + f"| {ng:<{COL_W}} |")

    bottom_row = start_row + 3 + max_rows
    pr(bottom_row, border + gap + border)
    return bottom_row


def santa_scene():
    clear_with_art()
    hide_cursor()
    cols, rows = get_terminal_size()

    total_width = (COL_W + 4) * 2 + 3
    start_col = max(2, (cols - total_width) // 2 + 1)
    list_start_row = 8

    bottom_row = draw_list_frame(list_start_row, start_col, NICE_LIST, NAUGHTY_LIST)

    # mail notification via timed loop
    mail_row = bottom_row + 2
    mail_lines = [
        (1.5,  "[ new mail for root ]"),
        (2.2,  "  From: sudo@homebox"),
        (2.7,  "  Subj: INCIDENT REPORT"),
        (3.2,  "  Body: robm is not in the sudoers file."),
    ]
    start = time.time()
    shown = set()
    cur_row = mail_row
    last_t = max(t for t, _ in mail_lines)
    try:
        while True:
            elapsed = time.time() - start
            for i, (t, msg) in enumerate(mail_lines):
                if i not in shown and elapsed >= t:
                    shown.add(i)
                    move(cur_row, start_col)
                    print(msg, flush=True)
                    cur_row += 1
            if len(shown) == len(mail_lines) and elapsed >= last_t + 2.0:
                break
            time.sleep(0.05)
    finally:
        show_cursor()

    # santa reacts
    hide_cursor()
    move(2, 2)
    for ch in "ho ho ho.":
        print(ch, end="", flush=True)
        time.sleep(0.09)
    print(flush=True)

    move(3, 2)
    for ch in "robm. naughty list it is.":
        print(ch, end="", flush=True)
        time.sleep(0.09)
    print(flush=True)

    # pause before writing
    time.sleep(1.2)

    border = "+" + "-" * (COL_W + 2) + "+"
    gap = "   "
    nice_col = start_col
    naughty_col = start_col + (COL_W + 4) + 3
    new_entry_row = list_start_row + 3 + len(NAUGHTY_LIST)

    # open the naughty box bottom
    move(bottom_row, nice_col)
    print(border + gap + "| " + " " * COL_W + " |", flush=True)

    # type robm in
    move(new_entry_row, naughty_col)
    print("| ", end="", flush=True)
    show_cursor()
    for ch in "robm":
        print(ch, end="", flush=True)
        time.sleep(0.09)
    hide_cursor()
    print(" " * (COL_W - 4) + " |", flush=True)

    # seal the box
    move(bottom_row + 1, naughty_col)
    print(border, flush=True)

    time.sleep(3.5)
    show_cursor()

def sudo_scene():
    clear_with_art()
    hide_cursor()
    start = time.time()
    shown = set()
    row = 2

    lines = [
        (0.0,  "  robm@homebox ~$ sudo su"),
        (0.8,  "  Password:"),
        (2.0,  "  robm is not in the sudoers file."),
        (2.01,  "  This incident will be reported."),
        (2.02,  "  robm@homebox ~$ "),
    ]

    last_t = max(t for t, _ in lines)
    try:
        while True:
            elapsed = time.time() - start
            for i, (t, msg) in enumerate(lines):
                if i not in shown and elapsed >= t:
                    shown.add(i)
                    move(row, 2)
                    print(msg, flush=True)
                    row += 1
            if len(shown) == len(lines) and elapsed >= last_t + 2.5:
                break
            time.sleep(0.05)
    finally:
        show_cursor()

def dialogue_scene():
    timed_messages([
        (0.0, "robm: hey -- who does sudo report these \"incidents\" to?"),
        (3.5, ""),
        (4.0, "megan:  you know, i've never checked."),
    ], end_delay=3.5)

def main():
    sudo_scene()
    dialogue_scene()
    santa_scene()

    clear_with_art()
    show_cursor()
    print("original comic made by randall munroe")
    print()
    print('title text: "he sees you when you\'re sleeping, he knows when you\'re awake,')
    print("            he's copied on /var/spool/mail/root,")
    print('            so be good for goodness\' sake."')

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        show_cursor()
        clear()
        print("original comic made by randall munroe")