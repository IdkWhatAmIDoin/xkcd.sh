#!/usr/bin/env python3
import time
import random
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
    "          comic #936",
]

WORDS = [
    "correct","horse","battery","staple","anchor","panel","river","cloud",
    "table","chair","window","garden","castle","forest","bridge","candle",
    "basket","carpet","ladder","bottle","butter","camera","dancer","engine",
    "fabric","goblin","hammer","island","jacket","kettle","lemon","marble",
    "napkin","orange","parrot","quartz","rabbit","saddle","tunnel","umbrella",
    "velvet","walnut","yellow","zipper","almond","banter","cactus","donkey",
    "falcon","gravel","harbor","insect","jungle","ketchup","lantern","muffin",
    "noodle","oyster","peanut","quiver","rocket","sandal","teapot","urchin",
    "violin","weasel","xenon","yogurt","zenith","acorn","badger","cobalt",
    "dagger","enamel","ferret","geyser","hollow","igloo","jelly","kelp",
    "locket","mortar","nymph","oblong","pewter","quinoa","riddle","salmon",
    "thistle","ulcer","vortex","walrus","xylophone","yonder","zephyr",
    "admiral","biscuit","cobbler","daffodil","emerald","flannel","garlic",
    "hazel","inkwell","jasper","knapsack","linen","magnet","nectarine",
    "ocelot","pepper","quarrel","raven","saffron","timber","upward",
    "varnish","waffle","yarn","zinc","amber","burrow","cedar","drizzle",
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
    move(1, 1)

def typewrite(text, row, col, delay=0.07):
    move(row, col)
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

def bad_password_scene():
    clear_with_art()
    hide_cursor()

    _, rows = get_terminal_size()

    messages = [
        (0.0,  "Tr0ub4dor&3"),
        (1.5,  ""),
        (2.0,  "  uncommon base word....... 16 bits"),
        (3.0,  "  caps?.................... +1 bit"),
        (4.0,  "  common substitutions..... +3 bits"),
        (5.0,  "  numeral.................. +3 bits"),
        (6.0,  "  punctuation.............. +4 bits"),
        (7.0,  "  order unknown............ +3 bits"),
        (8.0,  "                             -------"),
        (8.5,  "  ~ 28 bits of entropy"),
        (10.0, ""),
        (10.5, "  2^28 = 3 days at 1000 guesses/sec"),
        (12.0, ""),
        (12.5, "  difficulty to guess:   EASY"),
        (14.0, "  difficulty to remember: HARD"),
        (16.0, ""),
        (16.5, "  was it trombone? no, troubador."),
        (18.0, "  and one of the 0s was a zero?"),
        (19.5, "  and there was some symbol..."),
    ]

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
            if len(shown) == len(messages) and elapsed >= last_t + 2.0:
                break
            time.sleep(0.05)
    finally:
        show_cursor()

def good_password_scene():
    words = random.sample(WORDS, 4)
    passphrase = " ".join(words)

    clear_with_art()
    hide_cursor()

    _, rows = get_terminal_size()

    # show "four random common words" label first
    move(2, 2)
    print("four random common words:", flush=True)
    time.sleep(1.5)

    # typewrite each word with a pause
    move(4, 4)
    show_cursor()
    col = 4
    for i, word in enumerate(words):
        for ch in word:
            print(ch, end="", flush=True)
            time.sleep(0.09)
        if i < len(words) - 1:
            print(" ", end="", flush=True)
            time.sleep(0.4)

    hide_cursor()
    time.sleep(1.0)

    messages_after = [
        (0.0,  ""),
        (0.5,  "  four common words, randomly chosen"),
        (1.5,  ""),
        (2.0,  "  ~ 44 bits of entropy"),
        (3.0,  ""),
        (3.5,  "  2^44 = 550 years at 1000 guesses/sec"),
        (5.0,  ""),
        (5.5,  "  difficulty to guess:    HARD"),
        (7.0,  "  difficulty to remember: YOU'VE ALREADY MEMORIZED IT"),
    ]

    start = time.time()
    shown = set()
    row = 6
    last_t = max(t for t, _ in messages_after)

    try:
        while True:
            elapsed = time.time() - start
            for i, (t, msg) in enumerate(messages_after):
                if i not in shown and elapsed >= t:
                    shown.add(i)
                    move(row, 2)
                    print(msg, flush=True)
                    row += 1
            if len(shown) == len(messages_after) and elapsed >= last_t + 2.0:
                break
            time.sleep(0.05)
    finally:
        show_cursor()

def main():
    bad_password_scene()
    good_password_scene()

    timed_messages([
        (0.0, "through 20 years of effort, we've successfully trained"),
        (2.0, "everyone to use passwords that are hard for humans to remember,"),
        (4.0, "but easy for computers to guess."),
    ], end_delay=3.0)

    clear_with_art()
    show_cursor()
    move(1, 1)
    print("original comic made by randall munroe")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        show_cursor()
        clear()
        move(1, 1)
        print("original comic made by randall munroe")