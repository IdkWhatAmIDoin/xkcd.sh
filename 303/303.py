#!/usr/bin/env python3
import sys
import time
import shutil
import random
import readline

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
    "          comic #303",
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

FAKE_COMPILE_LINES = [
    "gcc -O2 -Wall -c main.c -o main.o",
    "gcc -O2 -Wall -c utils.c -o utils.o",
    "gcc -O2 -Wall -c parser.c -o parser.o",
    "gcc -O2 -Wall -c lexer.c -o lexer.o",
    "gcc -O2 -Wall -c network.c -o network.o",
    "gcc -O2 -Wall -c database.c -o database.o",
    "gcc -O2 -Wall -c auth.c -o auth.o",
    "gcc -O2 -Wall -c config.c -o config.o",
    "gcc -O2 -Wall -c logger.c -o logger.o",
    "gcc -O2 -Wall -c scheduler.c -o scheduler.o",
    "gcc -O2 -Wall -c threadpool.c -o threadpool.o",
    "gcc -O2 -Wall -c cache.c -o cache.o",
    "ld -o myapp main.o utils.o parser.o lexer.o network.o database.o auth.o config.o logger.o scheduler.o threadpool.o cache.o",
    "strip myapp",
    "Build complete.",
]

def prefill_input(prompt, prefill=""):
    readline.set_startup_hook(lambda: readline.insert_text(prefill))
    try:
        return input(prompt)
    finally:
        readline.set_startup_hook()

def fake_compile_scene():
    clear_with_art()
    print("~/project$ make build")
    time.sleep(0.3)
    for line in FAKE_COMPILE_LINES:
        time.sleep(random.uniform(0.15, 0.45))
        print(line)
    time.sleep(0.5)

def manager_scene():
    time.sleep(1.0)
    print("HEY! GET BACK TO WORK!")
    time.sleep(0.8)

    try:
        current = input("~/project$ ")
    except (EOFError, KeyboardInterrupt):
        print()
        return

    time.sleep(0.6)

    keywords = ["comp", "build", "code", "compil"]
    if any(kw in current.lower() for kw in keywords):
        print("Oh. Carry on.")
        time.sleep(2.0)
    else:
        print("...that's not how this works.")
        time.sleep(2.0)

def prompt_scene(first_time=True):
    clear_with_art()
    prefill = "make bui" if first_time else ""

    try:
        cmd = prefill_input("~/project$ ", prefill)
    except (EOFError, KeyboardInterrupt):
        print()
        return False

    if cmd.strip() != "make build":
        print(f"make: *** No rule to make target '{cmd.strip().replace('make ', '')}'. Stop.")
        time.sleep(2.0)
        return False
    return True

def main():
    clear_with_art()
    print("\nthe #1 programmer excuse for legitimately slacking off:")
    print('"my code\'s compiling."')
    time.sleep(2.5)

    first = True
    while True:
        ok = prompt_scene(first)
        first = False
        if ok:
            break

    fake_compile_scene()
    manager_scene()

    clear_with_art()
    show_cursor()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        show_cursor()
        clear()