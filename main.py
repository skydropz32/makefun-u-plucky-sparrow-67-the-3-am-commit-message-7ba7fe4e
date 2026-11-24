"""Write one commit message to /output/entry.txt.

The 3 AM Commit Message (make.fun): one line an AI agent would write
right after breaking production at 3 AM, at most 200 characters.
"""

import os

LINE = "fix: approved my own PR at 3 AM with 99% confidence; prod is down and so is my confidence"


def main():
    line = LINE.strip()
    if not line or len(line) > 200 or "\n" in line or "\r" in line:
        raise ValueError("entry must be one non-blank line of 1-200 chars")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
