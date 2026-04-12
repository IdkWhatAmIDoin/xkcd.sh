# contributing to xkcd.sh

thanks for wanting to contribute. here's everything you need to know.

## requesting a comic

open an issue using the **Comic Request** template. explain what the interactive or theatrical angle would be; a comic that's just dialogue with no interactivity or punchline probably won't work great as a terminal script.

## running locally

```bash
git clone https://github.com/IdkWhatAmIDoin/xkcd.sh
cd xkcd.sh
echo 'export PATH="$PATH:$PWD"' >> ~/.bashrc  # or ~/.zshrc
source ~/.bashrc
xkcd 303
```

or just run the scripts directly:

```bash
python3 303/303.py
```

## submitting a new comic

### file structure

every comic lives in its own folder named after its number:

```
<num>/
  <num>.py        # the main script
  launcher.py     # optional, only if needed (see #149)
```

### code pattern

all comics should follow the same basic structure. look at any existing script for reference, they all share:

- `timed_messages()` for sequenced dialogue/output
- `clear_with_art()` to clear the screen and redraw the xkcd ascii art in the top-right corner
- `hide_cursor()` / `show_cursor()` when animating
- a `try/except KeyboardInterrupt` block in `__main__` that exits cleanly, shows the cursor, and clears the screen
- `print("original comic made by randall munroe")` at the end

the xkcd art block should look like this (just change the comic number):

```python
XKCD_ART = [
    "      _           _ ",
    "__  _| | _____ __| |",
    r"\ \/ / |/ / __/ _` |",
    r" >  <|   < (_| (_| |",
    r"/_/\_\_|\_\___\__,_|",
    "          comic #XXX",
]
```

### dependencies

try to keep external dependencies to zero. if you absolutely need one (like xdotool for focus management), make sure it's documented. don't add pip packages — the whole point is that these are standalone scripts.

### testing checklist

before opening a pr, make sure:

- [ ] runs correctly on a clean terminal
- [ ] ctrl+c exits cleanly — no broken terminal state
- [ ] cursor is restored after exit
- [ ] the xkcd.com page opens at the end (handled by the `xkcd` launcher automatically, but double check your script doesn't break before that)
- [ ] works at different terminal sizes without breaking layout

### updating the repo

when adding a comic, also update:

- **README.md** — add a row to the comics table, and if it has extra deps add a row to the dependencies table
- **.github/ISSUE_TEMPLATE/bug.yml** — add the comic to the dropdown list

### pr guidelines

- one comic per pr
- keep the pr title simple, e.g. `add #538 - security`
- don't refactor existing comics in the same pr as a new one

## questions

open an issue using the **Question** template.