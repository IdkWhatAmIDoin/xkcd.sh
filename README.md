![tar](https://preview.redd.it/9nfvebgzykug1.gif?width=796&auto=webp&s=2e3ff14d9730698fa3eeb904e961301a933536dc)

# xkcd.sh

a collection of xkcd comics reimagined as interactive terminal programs

## comics

| num | title | description | dependencies |
|---|-------|-------------| -------------- |
| [149](https://xkcd.com/149/) | make me a sandwich | fake shell. you know what to type. | python |
| [303](https://xkcd.com/303/) | compiling | #1 programmer excuse. | python |
| [327](https://xkcd.com/327/) | exploits of a mom | fake school database. little bobby tables. | python |
| [353](https://xkcd.com/353/) | python | `import antigravity`. that's it. | python, xdotool |
| [378](https://xkcd.com/378/) | real programmers | real editors. real chaos. butterflies. | python, nano, emacs, vim |
| [538](https://xkcd.com/538/) | security | crypto nerds, dont crypto nerd please. | python |
| [705](https://xkcd.com/705/) | devotion to duty | i'd keep my server running too. | python |
| [936](https://xkcd.com/936/) | password strength | Tr0ub4dor&3 vs correct horse battery staple. | python |
| [979](https://xkcd.com/979/) | wisdom of the ancients | who were you, DenverCoder9? | python, xdotool |
| [1168](https://xkcd.com/1168/) | tar | you have ten seconds. | python |
| [1319](https://xkcd.com/1319/) | automation | theory vs reality. | python |

## requirements

- python 3.x
- linux (or some variation of linux, like wsl2)

## install

```bash
git clone https://github.com/IdkWhatAmIDoin/xkcd.sh
cd xkcd.sh
sudo make install
```

to uninstall:

```bash
sudo make uninstall
```

## installing dependencies

most comics only need python. a few need extra stuff:

| comic | extra deps | apt | pacman | dnf |
|-------|-----------|-----|--------|-----|
| #353 - python | xdotool | `sudo apt install xdotool` | `sudo pacman -S xdotool` | `sudo dnf install xdotool` |
| #378 - real programmers | xdotool, nano, emacs, vim | `sudo apt install xdotool nano emacs vim` | `sudo pacman -S xdotool nano emacs vim` | `sudo dnf install xdotool nano emacs vim` |
| #979 - wisdom of the ancients | xdotool | `sudo apt install xdotool` | `sudo pacman -S xdotool` | `sudo dnf install xdotool` |

note: #378 will not work at all if any of its dependencies are missing.

## manual usage

each comic is a standalone python script and can be run directly without installing:

```bash
python3 149/149.py
python3 1168/1168.py
# etc.
```

or if you just want to run without installing system-wide, add to PATH instead:

```bash
echo 'export PATH="$PATH:$PWD"' | tee -a ~/.zshrc  # or ~/.bashrc
```

## windows support

this project is developed and tested on linux. while it may work via wsl2, there is no native support for windows.

i have no plans to build a windows version, but if you fork this repo to make your own windows version:
- ill gladly link to your repo here
- im happy to give you the code early so that you can get the windows version ready

## contributing

see [CONTRIBUTING.md](CONTRIBUTING.md)

## license

[xkcd.sh is used under the MIT license,](/LICENSE) [and all of the xkcd comics and characters are property of Randall Munroe and are used under CC BY-NC 2.5.](https://creativecommons.org/licenses/by-nc/2.5/)

This is an unofficial fan project and is fully Non-Commercial. I do not sell anything xkcd-related.
