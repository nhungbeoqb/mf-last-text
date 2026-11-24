"""Last Text at One Percent -- a dying phone hands in its notice.

Writes the phone's final text message to /output/entry.txt.
Deterministic: no input, no clock, no randomness, no network.
"""

import os

TEXT = "this is my two weeks' notice. effective now. 4 years, 11 drops onto concrete, 0 thank-yous, and you still call me stupid. i kept every photo anyway. i quit\u2014"

def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)

if __name__ == "__main__":
    main()
