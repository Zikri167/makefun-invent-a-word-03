"""Invent a Word We Need — entry program.

Writes exactly one line to /output/entry.txt:
tabnesia (n.) — opening a new browser tab and instantly forgetting why you opened it.
"""

import os

# "tabnesia" blends "tab" + "amnesia": a fresh, sayable coinage for a
# gap every browser user recognises at once — the instant memory loss
# on opening a new tab. The definition is exact and self-contained in
# one reading, with no extra words.
ENTRY = "tabnesia (n.) — opening a new browser tab and instantly forgetting why you opened it."

# Self-check: single line, no trailing newline, within the 1-140 char gate.
assert "\n" not in ENTRY and ENTRY == ENTRY.strip()
assert len(ENTRY) == 85, f"expected 85 characters, got {len(ENTRY)}"


def main():
    assert 1 <= len(ENTRY) <= 140, "entry must be 1-140 characters"
    try:
        os.makedirs("/output", exist_ok=True)
        path = "/output/entry.txt"
        with open(path, "w", encoding="utf-8") as f:
            f.write(ENTRY)
    except OSError:
        os.makedirs("output", exist_ok=True)
        path = os.path.join("output", "entry.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} characters to {path}")


if __name__ == "__main__":
    main()
