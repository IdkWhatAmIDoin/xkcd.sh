![tar](https://preview.redd.it/9nfvebgzykug1.gif?width=796&auto=webp&s=2e3ff14d9730698fa3eeb904e961301a933536dc)

# xkcd.sh

a collection of xkcd comics reimagined as interactive terminal programs

## comics

| num | title | description | dependencies |
|---|-------|-------------|
| [149](https://xkcd.com/149/) | make me a sandwich | fake shell. you know what to type. | python |
| [303](https://xkcd.com/303/) | compiling | #1 programmer excuse. | python |
| [327](https://xkcd.com/327/) | exploits of a mom | fake school database. little bobby tables. | python |
| [353](https://xkcd.com/353/) | python | `import antigravity`. that's it. | python, xdotool |
| [378](https://xkcd.com/378/) | real programmers | real editors. real chaos. butterflies. | python, nano, emacs, vim, ed |
| [936](https://xkcd.com/936/) | password strength | Tr0ub4dor&3 vs correct horse battery staple. | python | 
| [979](https://xkcd.com/979/) | wisdom of the ancients | who were you, DenverCoder9? | python, xdotool |
| [1168](https://xkcd.com/1168/) | tar | you have ten seconds. | python |
| [1319](https://xkcd.com/1319/) | automation | theory vs reality. | python |

## requirements

- linux (may work on macos but not tested, no windows support for now)
- python 3.x

## add to PATH (optional)

`echo 'export PATH="$PATH:$PWD"' | tee -a ~/.zshrc` or `~/.bashrc`, depending on your shell this may vary

## usage

run `./xkcd` or `xkcd` (depends on if you added to PATH) `[comic number]` to get a terminal representation of that comic.

## manual usage

each comic is a standalone python script:

```bash
python3 149/149.py
python3 1168/1168.py
# etc.
```

they can be executed directly if you dont wanna install the `xkcd` tool.

## license

[xkcd.sh is used under the MIT license,](/LICENSE) [and all of the xkcd comics and characters are property of Randall Munroe and are used under CC BY-NC 2.5.](https://creativecommons.org/licenses/by-nc/2.5/) 
