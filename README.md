# xkcd.sh

a collection of xkcd comics reimagined as interactive terminal programs.

## comics

| num | title | description |
|---|-------|-------------|
| [149](https://xkcd.com/149/) | make me a sandwich | fake shell. you know what to type. |
| [303](https://xkcd.com/303/) | compiling | #1 programm excuse. |
| [327](https://xkcd.com/327/) | exploits of a mom | fake school database. little bobby tables. |
| [353](https://xkcd.com/353/) | python | `import antigravity`. that's it. |
| [378](https://xkcd.com/378/) | real programmers | real editors. real chaos. butterflies. |
| [936](https://xkcd.com/936/) | password strength | Tr0ub4dor&3 vs correct horse battery staple. |
| [979](https://xkcd.com/979/) | wisdom of the ancients | who were you, DenverCoder9? |
| [1168](https://xkcd.com/1168/) | tar | you have ten seconds. |
| [1319](https://xkcd.com/1319/) | automation | theory vs reality. |

## requirements

- linux (uses `termios`, `pty`, `tty`, no windows support unless someone manually ports it over)
- python 3.x
- `nano`, `emacs`, `vim`, `ed` (for #378)
- `xdotool` (for #353 and #979)

## usage

each comic is a standalone python script:

```bash
python3 149/149.py
python3 1168/1168.py
# etc.
```

## license

[view](/LICENSE)
