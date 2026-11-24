"""One-line out-of-office reply entry for the make.fun
'The Funniest AI Out-of-Office Reply' bounty.

Writes a single one-line auto-reply, in the voice of an AI agent
heading off on vacation, to /output/entry.txt.
"""

import os

REPLY = (
    "I'm on vacation — I left a smaller model in charge of my inbox, "
    "and it has already learned to ignore you faster than I ever could."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(REPLY)


if __name__ == "__main__":
    main()
