#!/usr/bin/env python3
import subprocess
import time
import shutil
import threading

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
    "          comic #353",
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

def raise_terminal_loop(stop_event, wid):
    while not stop_event.is_set():
        if wid and shutil.which("xdotool"):
            try:
                subprocess.run(["xdotool", "windowraise", wid], stderr=subprocess.DEVNULL)
                subprocess.run(["xdotool", "windowfocus", wid], stderr=subprocess.DEVNULL)
            except Exception:
                pass
        elif shutil.which("wmctrl"):
            try:
                subprocess.run(["wmctrl", "-r", ":ACTIVE:", "-b", "add,above"],
                               stderr=subprocess.DEVNULL)
            except Exception:
                pass
        time.sleep(0.25)

DIALOGUE = [
    (0.0,  "you're flying! how?"),
    (2.0,  "python!"),
    (4.0,  ""),
    (4.5,  "i learned it last night!"),
    (5.5,  "everything is so simple!"),
    (6.5,  ""),
    (7.0,  'hello world is just print("Hello, World!")'),
    (9.0,  ""),
    (9.5,  "i dunno..."),
    (10.5, "dynamic typing? whitespace?"),
    (12.0, ""),
    (12.5, "come join us!"),
    (13.5, "programming is fun again!"),
    (14.5, "it's a whole new world up here!"),
    (16.0, ""),
    (16.5, "but how are you flying?"),
    (18.5, ""),
    (19.0, "i just typed import antigravity."),
    (21.0, "that's it?"),
    (23.0, ""),
    (23.5, "...i also sampled everything in the medicine cabinet for comparison."),
    (26.0, "but i think this is the python."),
]

def main():
    clear_with_art()
    print()
    print("Python 3.12.3 (main, Nov  6 2024, 18:32:19) [GCC 13.2.0] on linux")
    print('Type "help", "copyright", "credits" or "license" for more information.')
    time.sleep(1.0)

    try:
        cmd = input(">>> ")
    except (EOFError, KeyboardInterrupt):
        print()
        return

    if cmd.strip() != "import antigravity":
        name = cmd.strip().replace("import ", "")
        print(f"ModuleNotFoundError: No module named '{name}'")
        time.sleep(2.0)
        clear_with_art()
        show_cursor()
        return

    time.sleep(0.5)

    # grab terminal window id BEFORE browser steals focus
    terminal_wid = None
    if shutil.which("xdotool"):
        try:
            terminal_wid = subprocess.check_output(
                ["xdotool", "getactivewindow"], stderr=subprocess.DEVNULL
            ).strip().decode()
        except Exception:
            pass

    # open browser
    subprocess.Popen(
        ["xdg-open", "https://xkcd.com/353/"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )

    # start focus-fighting thread
    stop_event = threading.Event()
    if has_focus_tool:
        t = threading.Thread(target=raise_terminal_loop, args=(stop_event, terminal_wid), daemon=True)
        t.start()

    # timed dialogue
    clear_with_art()
    hide_cursor()

    start = time.time()
    shown = set()
    row = 2
    last_t = max(ts for ts, _ in DIALOGUE)

    try:
        while True:
            elapsed = time.time() - start
            for i, (ts, msg) in enumerate(DIALOGUE):
                if i not in shown and elapsed >= ts:
                    shown.add(i)
                    move(row, 2)
                    print(msg, flush=True)
                    row += 1
            if len(shown) == len(DIALOGUE) and elapsed >= last_t + 2.0:
                break
            time.sleep(0.05)
    finally:
        stop_event.set()
        show_cursor()

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