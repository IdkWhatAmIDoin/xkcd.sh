#!/usr/bin/env python3
import time
import shutil
import sys

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
    "          comic #327",
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

def typewrite(text, delay=0.04):
    for ch in text:
        print(ch, end="", flush=True)
        time.sleep(delay)
    print()

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

STUDENTS = [
    "Alice Johnson",
    "Bob Smith",
    "Carol White",
    "David Brown",
]

def db_scene():
    clear_with_art()
    print()
    print("  Greenfield Elementary — Student Enrollment System v2.3")
    print("  " + "─" * 50)
    print()
    print("  Current students:")
    for s in STUDENTS:
        print(f"    - {s}")
    print()
    print("  Enter new student name to enroll:")
    print()

    while True:
        try:
            name = input("  sqlite> INSERT INTO Students VALUES ('") 
        except (EOFError, KeyboardInterrupt):
            print()
            return False

        # check for bobby tables
        if "drop table" in name.lower() or "robert');" in name.lower() or name.strip().startswith("Robert');"):
            print()
            time.sleep(0.3)
            print("  executing query...")
            time.sleep(0.5)
            print()
            print("  DROP TABLE Students;")
            time.sleep(0.8)
            print()
            print("  Query OK.")
            time.sleep(0.4)
            print()
            print("  SELECT * FROM Students;")
            time.sleep(0.6)
            print()
            print("  ERROR 1146: Table 'school.Students' doesn't exist")
            time.sleep(1.5)
            return True
        elif name.strip() == "":
            pass
        else:
            full = name.rstrip("'") 
            STUDENTS.append(full.strip("'").strip())
            print()
            print(f"  Query OK. 1 row affected.")
            print()
            print("  Current students:")
            for s in STUDENTS:
                print(f"    - {s}")
            print()

def phone_call():
    timed_messages([
        (0.0,  "[ phone ringing ]"),
        (1.5,  ""),
        (2.0,  "school: hi, this is your son's school."),
        (3.0,  "school: we're having some computer trouble."),
        (5.0,  ""),
        (5.5,  "mom: oh dear — did he break something?"),
        (7.5,  ""),
        (8.0,  "school: in a way—"),
        (10.0, ""),
        (10.5, "school: did you really name your son"),
        (11.5, "school: \"Robert'); DROP TABLE Students;--\" ?"),
        (14.0, ""),
        (14.5, "mom: oh, yes. Little Bobby Tables, we call him."),
        (17.0, ""),
        (17.5, "school: well, we've lost this year's student records."),
        (19.0, "school: i hope you're happy."),
        (21.0, ""),
        (21.5, "mom: and i hope you've learned to sanitize your inputs."),
    ], end_delay=3.0)

def main():
    clear_with_art()
    print()
    print("  type student names to enroll them.")
    print("  or... try something else.")
    time.sleep(2.5)

    exploded = db_scene()

    if exploded:
        phone_call()

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