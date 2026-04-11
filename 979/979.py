#!/usr/bin/env python3
import http.server
import threading
import subprocess
import tempfile
import time
import shutil
import os
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
    "          comic #979",
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

def raise_terminal():
    if shutil.which("xdotool"):
        try:
            wid = subprocess.check_output(
                ["xdotool", "search", "--class", "terminal"],
                stderr=subprocess.DEVNULL
            ).strip().split()
            if wid:
                subprocess.run(["xdotool", "windowraise", wid[-1]], stderr=subprocess.DEVNULL)
                subprocess.run(["xdotool", "windowfocus", wid[-1]], stderr=subprocess.DEVNULL)
                subprocess.run(["xdotool", "windowactivate", "--sync", wid[-1]], stderr=subprocess.DEVNULL)
        except Exception:
            pass

GOOGLE_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>segfault in malloc() only when array size is prime number - Google Search</title>
<style>
* { margin: 0; padding: 0; box-sizing: border-box; }
body { font-family: arial, sans-serif; background: #fff; color: #202124; }
header { padding: 16px 24px; display: flex; align-items: center; gap: 24px; border-bottom: 1px solid #ebebeb; }
.logo { font-size: 28px; font-weight: bold; }
.logo span:nth-child(1){color:#4285f4}.logo span:nth-child(2){color:#ea4335}
.logo span:nth-child(3){color:#fbbc05}.logo span:nth-child(4){color:#4285f4}
.logo span:nth-child(5){color:#34a853}.logo span:nth-child(6){color:#ea4335}
.searchbar { display: flex; align-items: center; border: 1px solid #dfe1e5; border-radius: 24px; padding: 8px 16px; width: 580px; font-size: 16px; gap: 8px; box-shadow: 0 1px 3px rgba(0,0,0,0.1); }
nav { padding: 8px 160px; display: flex; gap: 24px; border-bottom: 1px solid #ebebeb; }
nav a { color: #202124; text-decoration: none; font-size: 13px; padding: 8px 0; }
nav a.active { color: #1a73e8; border-bottom: 3px solid #1a73e8; }
.results { padding: 20px 160px; }
.result-count { font-size: 13px; color: #70757a; margin-bottom: 24px; }
.result { margin-bottom: 28px; max-width: 600px; }
.result .url { font-size: 12px; color: #202124; margin-bottom: 2px; }
.result .favicon { width:16px;height:16px;background:#ddd;border-radius:50%;display:inline-block;vertical-align:middle;margin-right:4px; }
.result h3 { font-size: 20px; font-weight: normal; margin-bottom: 4px; }
.result h3 a { color: #1a0dab; text-decoration: none; }
.result h3 a:hover { text-decoration: underline; }
.result .snippet { font-size: 14px; color: #4d5156; line-height: 1.58; }
.result .date { color: #70757a; }
.no-result { color: #70757a; font-size: 14px; font-style: italic; margin-top: 32px; }
</style>
</head>
<body>
<header>
  <div class="logo"><span>G</span><span>o</span><span>o</span><span>g</span><span>l</span><span>e</span></div>
  <div class="searchbar"><span>segfault in malloc() only when array size is prime number</span></div>
</header>
<nav>
  <a href="#" class="active">All</a>
  <a href="#">Images</a>
  <a href="#">Videos</a>
  <a href="#">News</a>
  <a href="#">Forums</a>
</nav>
<div class="results">
  <div class="result-count">About 3 results (0.47 seconds)</div>
  <div class="result">
    <div class="url"><span class="favicon"></span>stackoverflow.com › questions › segfault-malloc-prime</div>
    <h3><a href="#">Segfault when allocating memory — size matters? [closed]</a></h3>
    <p class="snippet"><span class="date">Mar 14, 2019 — </span>This question was closed as "not reproducible". The original poster never responded to requests for a minimal reproducible example...</p>
  </div>
  <div class="result">
    <div class="url"><span class="favicon"></span>gcc.gnu.org › bugzilla › show_bug</div>
    <h3><a href="#">Bug #84732 — malloc segfault non-deterministic [INVALID]</a></h3>
    <p class="snippet"><span class="date">Aug 3, 2017 — </span>Marked INVALID. Could not reproduce. Reporter did not follow up after initial submission...</p>
  </div>
  <div class="result">
    <div class="url"><span class="favicon"></span>forums.devchat.io › c-programming › malloc-prime-seg...</div>
    <h3><a href="FORUM_URL">segfault in malloc() ONLY when array size is prime?? [SOLVED]</a></h3>
    <p class="snippet"><span class="date">Nov 7, 2003 — </span>Has anyone seen this before? I've been losing my mind for three days. malloc() segfaults but <b>only</b> when the array size happens to be a prime number. Composite sizes work fine. I know how insane this sounds...</p>
  </div>
  <p class="no-result">Hmm, that's about it. Try different search terms?</p>
</div>
</body>
</html>"""

FORUM_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>segfault in malloc() ONLY when array size is prime?? [SOLVED] - DevChat Forums</title>
<style>
* { margin: 0; padding: 0; box-sizing: border-box; }
body { font-family: "Trebuchet MS", arial, sans-serif; background: #e8e8e8; color: #333; font-size: 13px; }
header { background: #1a3a5c; padding: 10px 20px; color: white; }
header h1 { font-size: 22px; letter-spacing: 1px; }
header p { font-size: 11px; color: #aac; margin-top: 2px; }
.breadcrumb { background: #d0d8e0; padding: 6px 20px; font-size: 11px; color: #555; border-bottom: 1px solid #bbb; }
.breadcrumb a { color: #1a3a5c; text-decoration: none; }
.container { max-width: 860px; margin: 16px auto; padding: 0 12px; }
.thread-title { background: #1a3a5c; color: white; padding: 8px 12px; font-size: 15px; font-weight: bold; border-radius: 4px 4px 0 0; display: flex; justify-content: space-between; align-items: center; }
.solved-badge { background: #27ae60; color: white; font-size: 10px; padding: 2px 8px; border-radius: 3px; }
.post { background: white; border: 1px solid #c0c8d0; border-top: none; display: flex; }
.post-sidebar { width: 130px; min-width: 130px; background: #f0f4f8; border-right: 1px solid #c0c8d0; padding: 12px; text-align: center; }
.post-sidebar .username { font-weight: bold; color: #1a3a5c; font-size: 12px; }
.post-sidebar .avatar { width:50px;height:50px;background:#ccd;border-radius:4px;margin:6px auto;display:flex;align-items:center;justify-content:center;font-size:20px;color:#888; }
.post-sidebar .join-date, .post-sidebar .post-count { font-size: 10px; color: #888; }
.post-body { flex: 1; padding: 12px 16px; }
.post-header { display: flex; justify-content: space-between; color: #888; font-size: 11px; border-bottom: 1px solid #eee; padding-bottom: 8px; margin-bottom: 10px; }
.post-content { line-height: 1.6; font-size: 13px; }
.post-content code { background:#f0f0f0;padding:1px 4px;font-family:monospace;font-size:12px;border:1px solid #ddd; }
.post-content pre { background:#1e1e1e;color:#d4d4d4;padding:12px;margin:8px 0;font-family:monospace;font-size:12px;line-height:1.5;overflow-x:auto;border-radius:3px; }
.post-content .quote { background:#f5f5f5;border-left:3px solid #aaa;padding:8px 12px;margin:8px 0;color:#555;font-style:italic; }
.op-badge { background:#e74c3c;color:white;font-size:9px;padding:1px 5px;border-radius:2px;margin-left:4px; }
.mod-badge { background:#8e44ad;color:white;font-size:9px;padding:1px 5px;border-radius:2px;margin-left:4px; }
.solved-post .post-sidebar { background: #d5f5e3; }
.solved-post .post-body { background: #f0faf4; }
.pagination { text-align: right; padding: 8px 0; font-size: 11px; color: #888; }
#scroll-sentinel { height: 1px; }
</style>
</head>
<body>
<header>
  <h1>DevChat Forums</h1>
  <p>The internet's premier C/C++ discussion board since 1999</p>
</header>
<div class="breadcrumb">
  <a href="#">Home</a> &rsaquo; <a href="#">C / C++</a> &rsaquo; <a href="#">Memory Management</a> &rsaquo; segfault in malloc() ONLY when array size is prime??
</div>
<div class="container">
  <div class="thread-title">
    segfault in malloc() ONLY when array size is prime??
    <span class="solved-badge">SOLVED</span>
  </div>

  <div class="post">
    <div class="post-sidebar">
      <div class="username">DenverCoder9 <span class="op-badge">OP</span></div>
      <div class="avatar">👤</div>
      <div class="join-date">Joined: Feb 2001</div>
      <div class="post-count">Posts: 47</div>
    </div>
    <div class="post-body">
      <div class="post-header"><span>#1 — <b>segfault in malloc() ONLY when array size is prime??</b></span><span>Nov 7, 2003, 2:14 AM</span></div>
      <div class="post-content">
        <p>Ok I know how insane this sounds but hear me out.</p><br>
        <p>I've been debugging this for THREE DAYS and I finally isolated it. My program segfaults in malloc() but <em>only</em> when the requested array size is a prime number. Composite sizes work completely fine.</p><br>
        <pre>int *arr = malloc(sizeof(int) * n);  // segfaults if n is prime
// works fine: n=4, n=6, n=8, n=9, n=10
// always crashes: n=2, n=3, n=5, n=7, n=11, n=13...</pre><br>
        <p>I've verified with a primality test. I am not making this up. Running on Gentoo, gcc 3.3.1, glibc 2.3.2.</p><br>
        <p>Anyone else seen this? Am I losing my mind?</p>
      </div>
    </div>
  </div>

  <div class="post">
    <div class="post-sidebar">
      <div class="username">xor_master</div>
      <div class="avatar">👤</div>
      <div class="join-date">Joined: Mar 2000</div>
      <div class="post-count">Posts: 1,203</div>
    </div>
    <div class="post-body">
      <div class="post-header"><span>#2</span><span>Nov 7, 2003, 3:02 AM</span></div>
      <div class="post-content">
        <p>That's not possible. malloc doesn't care about number theory. You must have memory corruption somewhere else. Classic heap overflow.</p><br>
        <p>Run it under valgrind and post the output.</p>
      </div>
    </div>
  </div>

  <div class="post">
    <div class="post-sidebar">
      <div class="username">DenverCoder9 <span class="op-badge">OP</span></div>
      <div class="avatar">👤</div>
      <div class="join-date">Joined: Feb 2001</div>
      <div class="post-count">Posts: 47</div>
    </div>
    <div class="post-body">
      <div class="post-header"><span>#3</span><span>Nov 7, 2003, 9:47 AM</span></div>
      <div class="post-content">
        <div class="quote">Run it under valgrind and post the output.</div><br>
        <p>Valgrind shows nothing before the crash. I wrote a completely minimal test case, 40 lines, no other allocations. Same behavior.</p><br>
        <pre>// This crashes:
int *x = malloc(sizeof(int) * 7);

// This is fine:
int *x = malloc(sizeof(int) * 8);</pre><br>
        <p>I know. I KNOW.</p>
      </div>
    </div>
  </div>

  <div class="post">
    <div class="post-sidebar">
      <div class="username">ptr_wizard</div>
      <div class="avatar">👤</div>
      <div class="join-date">Joined: Sep 1999</div>
      <div class="post-count">Posts: 4,521</div>
    </div>
    <div class="post-body">
      <div class="post-header"><span>#4</span><span>Nov 7, 2003, 11:15 AM</span></div>
      <div class="post-content">
        <p>Can you post your full test case? Also what kernel version? There were some weird glibc/kernel interactions around 2.4.x with certain allocation patterns.</p><br>
        <p>Also are you on 32 or 64 bit? Some early 64-bit ports had alignment bugs.</p>
      </div>
    </div>
  </div>

  <div class="post">
    <div class="post-sidebar">
      <div class="username">DenverCoder9 <span class="op-badge">OP</span></div>
      <div class="avatar">👤</div>
      <div class="join-date">Joined: Feb 2001</div>
      <div class="post-count">Posts: 47</div>
    </div>
    <div class="post-body">
      <div class="post-header"><span>#5</span><span>Nov 7, 2003, 2:33 PM</span></div>
      <div class="post-content">
        <p>kernel 2.4.22, 32-bit. Here's the full test:</p><br>
        <pre>#include &lt;stdlib.h&gt;
#include &lt;stdio.h&gt;

int main() {
    int n = 7;  // change to 8: works. change to 7: crash.
    int *arr = (int*)malloc(sizeof(int) * n);
    if (!arr) { puts("null"); return 1; }
    arr[0] = 42;
    printf("%d\n", arr[0]);
    free(arr);
    return 0;
}</pre><br>
        <p>compiled with: <code>gcc -O0 -g test.c -o test</code></p><br>
        <p>segfault is in malloc itself according to gdb, not in my code.</p>
      </div>
    </div>
  </div>

  <div class="post">
    <div class="post-sidebar">
      <div class="username">xor_master</div>
      <div class="avatar">👤</div>
      <div class="join-date">Joined: Mar 2000</div>
      <div class="post-count">Posts: 1,203</div>
    </div>
    <div class="post-body">
      <div class="post-header"><span>#6</span><span>Nov 8, 2003, 12:01 AM</span></div>
      <div class="post-content">
        <p>I just tried your exact code on my machine (Debian, same gcc, 2.4.20 kernel) and it works fine. Both 7 and 8.</p><br>
        <p>This is almost certainly a hardware issue. Bad RAM? Run memtest86.</p>
      </div>
    </div>
  </div>

  <div class="post">
    <div class="post-sidebar">
      <div class="username">DenverCoder9 <span class="op-badge">OP</span></div>
      <div class="avatar">👤</div>
      <div class="join-date">Joined: Feb 2001</div>
      <div class="post-count">Posts: 47</div>
    </div>
    <div class="post-body">
      <div class="post-header"><span>#7</span><span>Nov 8, 2003, 8:19 AM</span></div>
      <div class="post-content">
        <p>Ran memtest86 overnight. No errors. Tried on two different machines. Same result on both.</p><br>
        <p>I've been awake for 36 hours. I need to ship this code next week.</p>
      </div>
    </div>
  </div>

  <div class="post">
    <div class="post-sidebar">
      <div class="username">ForumMod <span class="mod-badge">MOD</span></div>
      <div class="avatar">🛡️</div>
      <div class="join-date">Joined: Jan 1999</div>
      <div class="post-count">Posts: 12,004</div>
    </div>
    <div class="post-body">
      <div class="post-header"><span>#8</span><span>Nov 9, 2003, 3:44 PM</span></div>
      <div class="post-content">
        <p>Marking thread as pending. DenverCoder9 please update when resolved.</p>
      </div>
    </div>
  </div>

  <div class="post solved-post">
    <div class="post-sidebar">
      <div class="username">DenverCoder9 <span class="op-badge">OP</span></div>
      <div class="avatar">👤</div>
      <div class="join-date">Joined: Feb 2001</div>
      <div class="post-count">Posts: 47</div>
    </div>
    <div class="post-body">
      <div class="post-header"><span>#9 — <b>✓ SOLVED</b></span><span>Nov 12, 2003, 11:58 PM</span></div>
      <div class="post-content">
        <p>nvm figured it out</p>
      </div>
    </div>
  </div>

  <div class="pagination">Page 1 of 1 — 9 posts</div>
  <div id="scroll-sentinel"></div>
</div>

<script>
const SIGNAL_URL = "SIGNAL_URL_PLACEHOLDER";
let signaled = false;

const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting && !signaled) {
      signaled = true;
      fetch(SIGNAL_URL).catch(() => {});
    }
  });
}, { threshold: 1.0 });

observer.observe(document.getElementById('scroll-sentinel'));
</script>
</body>
</html>"""

DIALOGUE = [
    "never have i felt so close to another soul",
    "and yet so helplessly alone",
    "as when i google an error",
    "and there's one result",
    "a thread by someone with the same problem",
    "and no answer",
    "last posted to in 2003",
    "",
    "who were you, DenverCoder9?",
    "what did you see?!",
]

def typewriter_messages():
    clear_with_art()
    hide_cursor()
    row = 2
    try:
        for line in DIALOGUE:
            move(row, 2)
            for ch in line:
                print(ch, end="", flush=True)
                time.sleep(0.06)
            row += 1
            time.sleep(0.6)
        time.sleep(3.0)
    finally:
        show_cursor()

def main():
    tmpdir = tempfile.mkdtemp()
    signal_received = threading.Event()

    # start signal server
    class SignalHandler(http.server.BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            signal_received.set()
        def log_message(self, *args):
            pass

    server = http.server.HTTPServer(("127.0.0.1", 0), SignalHandler)
    port = server.server_address[1]
    server_thread = threading.Thread(target=server.serve_forever, daemon=True)
    server_thread.start()

    signal_url = f"http://127.0.0.1:{port}/signal"

    # write forum html with signal url injected
    forum_path = os.path.join(tmpdir, "979_forum.html")
    forum_html = FORUM_HTML.replace("SIGNAL_URL_PLACEHOLDER", signal_url)
    with open(forum_path, "w") as f:
        f.write(forum_html)

    # write google html with forum path injected
    google_path = os.path.join(tmpdir, "979_google.html")
    forum_file_url = f"file://{forum_path}"
    google_html = GOOGLE_HTML.replace("FORUM_URL", forum_file_url)
    with open(google_path, "w") as f:
        f.write(google_html)

    # grab terminal wid before opening browser
    terminal_wid = None
    if shutil.which("xdotool"):
        try:
            terminal_wid = subprocess.check_output(
                ["xdotool", "getactivewindow"], stderr=subprocess.DEVNULL
            ).strip().decode()
        except Exception:
            pass

    # show intro
    clear_with_art()
    print()
    print("  searching: segfault in malloc() only when array size is prime number")
    time.sleep(1.5)

    # open google page
    subprocess.Popen(["xdg-open", f"file://{google_path}"],
                     stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # wait for scroll signal
    signal_received.wait()
    server.shutdown()

    # raise terminal
    if terminal_wid and shutil.which("xdotool"):
        time.sleep(0.3)
        subprocess.run(["xdotool", "windowactivate", "--sync", terminal_wid], stderr=subprocess.DEVNULL)
        subprocess.run(["xdotool", "windowraise", terminal_wid], stderr=subprocess.DEVNULL)
        subprocess.run(["xdotool", "windowfocus", terminal_wid], stderr=subprocess.DEVNULL)

    typewriter_messages()

    clear_with_art()
    show_cursor()

    # cleanup
    import shutil as sh
    sh.rmtree(tmpdir, ignore_errors=True)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        show_cursor()
        clear()