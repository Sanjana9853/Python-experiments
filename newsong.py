import sys
import time

sys.stdout.reconfigure(encoding="utf-8")

LYRICS = """
Hua he aaj pehli baar🌙
jo aise muskuraayaa hoon..🥰
Tumhe dekha to jaana ye..💓
Ke kyun duniya main aayaa hoon..🌍💕
Ye jaan lekar ke ja meri..💓💞
Tumhein jeene mein aayaa hoon..🤗💝
Main tumse ishq krne kii..😙💖
ijazat rab se laaya hoon🫣💘..

"""

CHAR_DELAY = 0.08
LINE_PAUSE = 0.8

COLORS = [
    "\033[38;5;205m",
    "\033[38;5;213m",
    "\033[38;5;27m",
    "\033[38;5;75m",
    "\033[38;5;117m",
    "\033[38;5;51m",
    "\033[38;5;129m",
    "\033[38;5;141m",
]
RESET = "\033[0m"


def type_line(line, color):
    sys.stdout.write(color)
    for ch in line:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(CHAR_DELAY)
    sys.stdout.write(RESET + "\n")
    time.sleep(LINE_PAUSE)


if __name__ == "__main__":
    lines = LYRICS.strip().splitlines()
    for i, line in enumerate(lines):
        type_line(line, COLORS[i % len(COLORS)])