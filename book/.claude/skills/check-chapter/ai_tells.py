"""Flag word-level AI tells in chapter drafts (the patterns are in ai-tells.md).

Usage: python3 -I .claude/skills/check-chapter/ai_tells.py "$PWD" [Drafts/file.md ...] [--selftest]
With no files named, scans the latest version of each piece in Drafts/.
Skips front matter, blockquote lines (draft notes, epigraphs), anything inside double quotes
and [MARKER: ...] notes, so exact quotes are never flagged. "To fix" lines should be fixed or
kept on purpose; hints only matter in clusters. Shapes (triads, closers after a story) need a reader.
"""
import re
import sys
from pathlib import Path

PATTERNS = [  # (label, to fix?, regex); ' also matches a curly apostrophe
    ("1 not X but Y", True, r"\bnot (just|only|merely)\b[^.]*\bbut\b|\bit'?s not\b[^.]*[,;:] it'?s\b|\b(doesn't|does not|isn't|is not) mean\b[^.]*\. it means\b|\b(didn't|doesn't|don't|isn't|wasn't) just\b"),
    ("2 closer", True, r"\b(read that again|let that sink in|that'?s the (real )?(win|point|lesson)[.:]|that (distinction )?matters\.)"),
    ("3 deep-sounding saying", True, r"\b(the real question is|at its core|what really matters|fundamentally|the heart of the matter|the deeper issue)\b"),
    ("4 run-up", True, r"\b(let'?s dive in|let'?s explore|let'?s break (this|it) down|here'?s what you need to know|without further ado|real talk|let'?s be honest)\b"),
    ("5 arguing with no one", True, r"\b(to be clear|don'?t get me wrong|i'?m not saying|this is not to say|one might be tempted|a tempting approach)\b"),
    ("8 dash", True, r"[—–]|\s--\s"),
    ("22 chatbot residue", True, r"\b(i hope this helps|great question|let me know if|would you like me to)\b|\bcertainly!"),
    ("rule: hype word", True, r"\b(unlock(s|ed|ing)?|transform(s|ed|ing|ative)?|elevat(e|es|ed|ing)|game[- ]changer|leverag(e|es|ed|ing))\b"),
    ("rule: exclamation point", True, r"!"),
    ("12 AI word", False, r"\b(actually|additionally|align(s|ed)? with|bolster(s|ed)?|crucial|deep dive|delve[sd]?|enduring|enhanc(e|es|ed|ing)|garner(s|ed)?|highlight(s|ed|ing)|interplay|intricate|intricacies|landscape|meticulous(ly)?|pivotal|quietly|robust|showcas(e|es|ed|ing)|tapestry|testament|underscor(e|es|ed|ing)|valuable|vibrant)\b"),
    ("13 inflated significance", False, r"\b(stands as|plays an? (key|crucial|vital|pivotal) role|evolving landscape|setting the stage|indelible|the future looks bright|exciting times)\b"),
    ("15 -ing rider", False, r", (highlighting|underscoring|emphasizing|ensuring|reflecting|symbolizing|fostering|showcasing|cultivating|encompassing)\b"),
    ("16 sales language", False, r"\b(nestled|breathtaking|renowned|groundbreaking|stunning|must-visit|in the heart of|diverse array|profound)\b"),
    ("18 avoiding is/has", False, r"\b(serves as|functions as|boasts)\b"),
]
PATTERNS = [(label, fix, re.compile(rx.replace("'", "['’]"), re.I)) for label, fix, rx in PATTERNS]
# Voice starters are fine at the voice profile's rate; more than STARTER_LIMIT per chapter is flagged.
STARTERS = re.compile(r"(?:^|(?<=[.?!] ))(?:(?:here['’]s the thing|the thing is|the reality is)\b|honestly\b|(?:hey, )?look,)", re.I)
STARTER_LIMIT = 2
QUOTED = re.compile(r'"[^"]*"|“[^”]*”')
MARKER = re.compile(r"\[[A-Z][A-Z ]*(?::[^\]]*)?\]")


def scan(text):
    hits, starters, front = [], [], False
    for n, line in enumerate(text.splitlines(), 1):
        if n == 1 and line.strip() == "---":
            front = True
            continue
        if front:
            front = line.strip() != "---"
            continue
        if line.lstrip().startswith(">"):
            continue
        prose = QUOTED.sub('""', MARKER.sub("", line))
        hits += [(n, label, fix, m.group(0)) for label, fix, rx in PATTERNS for m in rx.finditer(prose)]
        starters += [n for _ in STARTERS.finditer(prose)]
    return hits, starters


def report(path):
    hits, starters = scan(path.read_text(encoding="utf-8"))
    fix = [h for h in hits if h[2]]
    hints = {}
    for n, label, to_fix, word in hits:
        if not to_fix:
            hints.setdefault(label, []).append(f"{word.lower()} L{n}")
    print(f"{path.name}: {len(fix)} to fix, {len(hits) - len(fix)} hints")
    for n, label, _, word in fix:
        print(f"  L{n} {label}: {word.strip()}")
    for label, items in hints.items():
        print(f"  hint {label} x{len(items)}: {', '.join(items)}")
    if len(starters) > STARTER_LIMIT:
        print(f"  voice starters x{len(starters)} (keep {STARTER_LIMIT} or fewer): {', '.join(f'L{n}' for n in starters)}")


def latest(drafts):
    best = {}
    for p in drafts.glob("* v*.md"):
        m = re.fullmatch(r"(.+) v(\d+)\.md", p.name)
        if m and int(m[2]) > best.get(m[1], (0, None))[0]:
            best[m[1]] = (int(m[2]), p)
    return sorted((p for _, p in best.values()), key=lambda p: p.name)


def selftest():
    sample = "\n".join([
        "---", "title: x", "note: actually crucial", "---",          # 1-4 front matter
        "> Notes on v2: crucial — delve",                        # 5 draft note
        "It's not just a website, it's a door.",                      # 6
        'She said "actually this is crucial!" and left.',             # 7 quote
        "Here's the thing. Look, the reality is simple. Honestly, it works.",  # 8
        "This is a robust plan — mostly.",                       # 9
        "[STORY NEEDED: a crucial client]",                           # 10 marker
        "That's the point of view. She didn't just post. That's the point.",  # 11
    ])
    hits, starters = scan(sample)
    found = {(n, label) for n, label, _, _ in hits}
    assert (6, "1 not X but Y") in found, hits
    assert [h[3] for h in hits if h[0] == 11] == ["didn't just", "That's the point."], hits
    assert (9, "8 dash") in found and (9, "12 AI word") in found, hits
    assert not [h for h in hits if h[0] in (2, 3, 5, 7, 8, 10)], hits
    assert starters == [8, 8, 8], starters
    assert [p.name for p in latest_fixture()] == ["Ch01 v10.md", "Ch02 v2.md"]
    print("selftest ok")


def latest_fixture():
    import tempfile
    d = Path(tempfile.mkdtemp())
    for name in ["Ch01 v9.md", "Ch01 v10.md", "Ch02 v1.md", "Ch02 v2.md", "Reading copy.md"]:
        (d / name).write_text("")
    return latest(d)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        selftest()
        sys.exit()
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()
    files = [Path(a) if Path(a).is_absolute() else root / a for a in sys.argv[2:]] or latest(root / "Drafts")
    for f in files:
        report(f)
