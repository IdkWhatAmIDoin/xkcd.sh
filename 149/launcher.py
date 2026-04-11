#!/usr/bin/env python3
import subprocess
import os
import shutil

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
BIN = os.path.join(SCRIPT_DIR, "149")

def clear():
    print("\033[2J\033[H", end="", flush=True)

clear()

while True:
    try:
        cmd = input("~$ ")
    except (EOFError, KeyboardInterrupt):
        print()
        break

    if cmd == "make me a sandwich":
        subprocess.run([BIN])
    elif cmd == "sudo make me a sandwich":
        subprocess.run(["sudo", BIN])
    elif cmd in ("exit", "quit", "q"):
        break
    elif cmd == "":
        pass
    elif shutil.which(cmd.split()[0]):
        print(f"{cmd} is a valid command but i dont feel like runnin it rn")
    else:
        print(f"{cmd} not found")