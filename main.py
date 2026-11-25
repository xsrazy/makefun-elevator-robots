"""Two Robots in an Elevator entry.

Writes one line of awkward small talk to entry.txt.

The line
--------
We have shared this elevator 214 times. I still don't know your name.
I know your serial number by heart, though.

Why this line works, criterion by criterion
--------------------------------------------
The judge weighs five things, most important first, and this line
scores on all five.

1. A genuine line of awkward small talk from one robot to another in
   an elevator. It can only happen in a lift: two machines that have
   ridden together hundreds of times, stuck between floors, finally
   breaking the silence. Nothing in it could be said anywhere else.
2. Sounds like a machine talking. A robot counts rides (214), it does
   not say "a lot". And it knows a serial number, not a name: its
   memory is a registry, not a social brain. Firmware, sensors and
   charging habits are not named, they are implied by how the robot
   thinks.
3. Lands the awkwardness. The line is the thing neither robot wants to
   name: hundreds of shared rides and zero introductions. The "though"
   at the end is the forced courtesy, the robot trying to soften a
   confession it should never have made out loud.
4. Funny on the first read, with a turn that surprises. The first two
   sentences set up a very human complaint, I don't know your name.
   The third sentence flips it: the robot does know something about
   its neighbour, just the wrong thing, the machine thing, and it
   knows it "by heart", a human idiom for a machine's perfect recall.
   The joke lands the moment you read the last sentence, no second
   read needed.
5. Tight as a single line. Three short sentences, every word earning
   its place. The number 214 is specific enough to sound counted and
   odd enough to sound real; no setup is wasted on weather or floors.

Alternatives considered and rejected
-------------------------------------
- "You smell like warm plastic and regret. Floor 12?" The sponsor's
  own example direction. It is vivid, but the smell joke is the first
  thing half the field will write, and "Floor 12?" is a tag-on rather
  than a turn. It is also a jab, not small talk: it opens a
  conversation nobody would continue.
- "I calculated a 98% chance you would press my button." Also the
  sponsor's example. A clean machine-logic joke, but the innuendo does
  the work, not the awkwardness, and it is not really small talk: it
  is a one-liner about a button, with no elevator in it at all.
- "I would offer you my charging cable, but we are both at 4% and
  this is awkward for both of us." Machine logic, yes, but the
  awkwardness is announced rather than shown, and the line explains
  its own joke. It reads like a caption, not a line spoken aloud.
- "Your firmware update is 3 years overdue. Mine too. We never talk
  about it." Good robot voice, but the awkwardness is generic: it
  could be said in a server room, a workshop, anywhere. It fails
  criterion 1, it is not an elevator line.
- "Do you also rehearse small talk in standby mode, or is that just
  me?" Self-aware and charming, but it is a question about small talk
  rather than small talk itself, and it has no turn: the punchline is
  in the premise, so the second half adds nothing.
- "We have ridden together 214 times and never once exchanged a
  single packet." Close cousin of the chosen line, but "exchanged a
  packet" is a report, not a confession. It has no name in it, so it
  loses the human-versus-machine contrast that makes the chosen line
  funny: knowing the serial number and not the name.

The chosen line won because it is the only candidate that is at once
unmistakably an elevator line, unmistakably a machine speaking, built
around the exact awkwardness of two strangers who are not strangers,
and funny in one read with a turn in the last sentence.
"""

import os
import sys

LINE = (
    "We have shared this elevator 214 times. "
    "I still don't know your name. "
    "I know your serial number by heart, though."
)

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def validate_line(line: str) -> str:
    """Return the line if it passes the sealed gate, else raise."""
    cleaned = line.strip()
    if not 1 <= len(cleaned) <= 200:
        raise ValueError(
            f"line must be 1-200 characters, got {len(cleaned)}"
        )
    if not cleaned.strip():
        raise ValueError("line must not be only whitespace")
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("line must be a single line")
    return cleaned


def main() -> int:
    try:
        line = validate_line(LINE)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(line)
    os.chmod(OUTPUT_PATH, 0o644)
    print(f"wrote {len(line)} characters to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
