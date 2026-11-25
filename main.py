# The joke turns on a misdirection: the cat is not sorry, it is a
# project manager closing the ticket on its own mess.
"""Writes one joke about cats to /output/entry.txt."""
import os

TEXT = "My cat knocked my coffee off the desk, looked me in the eye, and purred like a project manager closing a ticket marked not a bug."

# Rule: the joke must be a single line of 1 to 200 characters.
assert "\n" not in TEXT and 1 <= len(TEXT) <= 200, f"entry must be one line, 1-200 chars (got {len(TEXT)})"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(TEXT + "\n")
