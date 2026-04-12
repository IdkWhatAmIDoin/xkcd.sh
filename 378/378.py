#!/usr/bin/env python3
import os
import pty
import time
import signal
import sys
import termios
import tty
import shutil
import select
import fcntl

def set_title(title):
    print(f"\033]0;{title}\a", end="", flush=True)


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
    "          comic #378",
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

def run_editor_full(cmd, setup_keys, segments, hold_time=0.5, startup_time=1.2):
    set_title(f"xkcd 378: REAL programmers use {cmd[0]}")

    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)

    pid, master_fd = pty.fork()

    if pid == 0:
        os.execvp(cmd[0], cmd)
        sys.exit(1)

    fl = fcntl.fcntl(master_fd, fcntl.F_GETFL)
    fcntl.fcntl(master_fd, fcntl.F_SETFL, fl | os.O_NONBLOCK)

    def drain(timeout=0.05):
        try:
            r, _, _ = select.select([master_fd], [], [], timeout)
            if r:
                data = os.read(master_fd, 4096)
                os.write(sys.stdout.fileno(), data)
        except OSError:
            pass

    def drain_for(secs):
        end = time.time() + secs
        while time.time() < end:
            drain(0.05)

    try:
        tty.setraw(fd)

        drain_for(startup_time)

        for key in setup_keys:
            os.write(master_fd, key)
            time.sleep(0.2)
            drain(0.1)

        for pause, text in segments:
            drain_for(pause)
            for ch in text:
                os.write(master_fd, ch.encode())
                time.sleep(0.09)
                drain(0.05)

        drain_for(hold_time)

    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

    try:
        os.kill(pid, signal.SIGKILL)
        os.waitpid(pid, 0)
    except Exception:
        pass
    try:
        os.close(master_fd)
    except Exception:
        pass

    time.sleep(0.3)

    sys.stdout.write("\x1b[?1004l"); sys.stdout.flush()



def timed_messages(messages, end_delay=2.0):
    import termios
    termios.tcflush(sys.stdin.fileno(), termios.TCIFLUSH)
    sys.stdout.write("\x1b[?1004l"); sys.stdout.flush()
    os.system("stty sane")
    clear_with_art()
    hide_cursor()

    start = time.time()
    shown = set()
    row = 2

    last_t = max(t for t, _ in messages)

    try:
        while True:
            sys.stdout.write("\x1b[?1004l"); sys.stdout.flush()
            elapsed = time.time() - start
            for i, (t, msg) in enumerate(messages):
                if i not in shown and elapsed >= t:
                    shown.add(i)
                    move(row, 2)
                    print(msg, flush=True)
                    row += 1
                    sys.stdout.write("\x1b[?1004l"); sys.stdout.flush()
            if len(shown) == len(messages) and elapsed >= last_t + end_delay:
                break
            time.sleep(0.05)
            sys.stdout.write("\x1b[?1004l"); sys.stdout.flush()
    finally:
        show_cursor()


def main():
    for ed in ["nano", "emacs", "vi", "ed", "cat"]:
        if not shutil.which(ed):
            print(f"missing: {ed}")
            sys.exit(1)

    tmpfile = "/tmp/378_real_programmers.txt"
    with open(tmpfile, "w") as f:
        f.write("")

    # nano
    clear_with_art()
    run_editor_full(
        ["nano", tmpfile],
        setup_keys=[],
        segments=[
            (0.0, "ynano? REAL programmers use"),
        ],
        hold_time=0.5,
        startup_time=1.2,
    )
    
    sys.stdout.write("\x1b[?1004l"); sys.stdout.flush()

    # emacs
    clear_with_art()
    run_editor_full(
        ["emacs", "-nw", tmpfile],
        setup_keys=[],
        segments=[
            (0.0, "Emacs."),
            (1.0, "\nHey. REAL programmers use"),
        ],
        hold_time=0.5,
        startup_time=0.8,
    )

    sys.stdout.write("\x1b[?1004l"); sys.stdout.flush()

    # vi
    clear_with_art()
    run_editor_full(
        ["vi", tmpfile],
        setup_keys=[b"G", b"A"],
        segments=[
            (0.0, "Vim."),
            (1.0, "\nWell, REAL programmers use"),
        ],
        hold_time=0.5,
        startup_time=1.2,
    )

    sys.stdout.write("\x1b[?1004l"); sys.stdout.flush()

    # ed
    clear_with_art()
    run_editor_full(
        ["ed", tmpfile],
        setup_keys=[b"a\n"],
        segments=[
            (0.0, "ed."),
            (1.0, "\nNo, REAL programmers use"),
        ],
        hold_time=0.5,
        startup_time=1.2,
    )

    sys.stdout.write("\x1b[?1004l"); sys.stdout.flush()

    # cat
    clear_with_art()
    run_editor_full(
        ["cat"],
        setup_keys=[],
        segments=[
            (0.0, "cat."),
            (1.0, "\nREAL programmers use a magnetized needle and a steady hand."),
        ],
        hold_time=0.5,
        startup_time=0.5,
    )

    sys.stdout.write("\x1b[?1004l"); sys.stdout.flush()

    # butterfly / cosmic ray finale
    timed_messages([
        (0.0,  "Excuse me, but REAL programmers use butterflies."),
        (3.0,  "They open their hands and let the delicate wings flap once."),
        (6.0,  "The disturbance ripples outward,"),
        (7.5,  "changing the flow of the Eddy currents in the upper atmosphere."),
        (10.0, "These cause momentary pockets of higher-pressure air to form,"),
        (12.5, "which act as lenses that deflect incoming cosmic rays,"),
        (15.0, "focusing them to strike the drive platter"),
        (17.0, "and flip the derired bit."), # the bit WAS flipped, look at derired, its supposed to be desired but i flipped a bit
        (20.0, "Nice."),
        (21.5, "'Course, there's an Emacs command to do that."),
        (24.0, "Oh yeah! Good ol' C-x M-c M-butterfly..."),
        (27.0, "dammit, Emacs."),
    ], end_delay=3.0)

    sys.stdout.write("\x1b[?1004l"); sys.stdout.flush()

    clear_with_art()
    show_cursor()
    move(1, 1)
    print("original comic made by randall munroe")

    try:
        os.remove(tmpfile)
    except Exception:
        pass


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        show_cursor()
        clear()
        move(1, 1)
        print("original comic made by randall munroe")