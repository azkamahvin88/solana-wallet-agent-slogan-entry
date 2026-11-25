# Entry: One-Line Slogan for a Solana Wallet Agent
# Writes the chosen slogan to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
# Python 3.13, standard library only, no network, no model calls at runtime.
# The program is run twice and both runs must write identical bytes,
# so the slogan is a fixed constant (deterministic), not generated.

import os

# Chosen slogan (8 words, 43 characters, one line):
# "One wallet, one agent, zero chores on Solana."
# Why this line: it names the wallet, the agent and Solana in one breath;
# the 1-1-0 counting rhythm ("one wallet, one agent, zero chores") makes it
# stick in the ear; "zero chores" states the promise plainly to a newcomer
# (the agent does the work, you do none of the chores) without jargon and
# without the stock crypto lines about keys, moons or bags. See STUDY.md
# for the full brainstorm of 20 candidates and the scoring against the
# judge's five criteria.
SLOGAN = "One wallet, one agent, zero chores on Solana."

# Gate guard: the entry must satisfy the competition gate before it is
# written — 1-140 characters, at most 20 words, a single line, no
# surrounding whitespace — so a future slogan change can never silently
# break the gate and cost the entry its judging.
if not 1 <= len(SLOGAN) <= 140:
    raise SystemExit(f"slogan must be 1-140 characters, got {len(SLOGAN)}")
if len(SLOGAN.split()) > 20:
    raise SystemExit(f"slogan must be at most 20 words, got {len(SLOGAN.split())}")
if "\n" in SLOGAN or SLOGAN != SLOGAN.strip():
    raise SystemExit("slogan must be a single line with no surrounding whitespace")

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

os.makedirs(OUTPUT_DIR, exist_ok=True)
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(SLOGAN)
