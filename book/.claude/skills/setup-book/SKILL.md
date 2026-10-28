---
name: setup-book
description: First-time setup. Interview the author about the book, then fill in CLAUDE.md, the Book Brief and one note per chapter
disable-model-invocation: true
---

Job: set this folder up for the author's book. Run once, at the start.

1. Read `CLAUDE.md`, `01 Planning/Book Brief.md`, `01 Planning/Chapter Template.md` and `01 Planning/How We Write This Book.md`.
2. **Interview the author, one question at a time.** Wait for each answer before asking the next. Ask follow-ups when an answer is vague; a well-defined answer beats a fast one. Cover, in this order:
   - their name, their work and who they do it for;
   - the working title and subtitle (fine if they don't have one yet);
   - the reader: who they are, what stage they're at, what they've tried;
   - who the book is not for;
   - the problem the reader has but hasn't named yet;
   - the promise: what changes for the reader by the last page;
   - the framework or method the book is built on;
   - the proof they already have: clients, data, stories, people they could interview;
   - how the book differs from the books already on the shelf;
   - the chapter list, as far as they know it, and which chapter they want to write first;
   - eight or nine problems the reader runs into, which become theme codes A to I (J is always "other");
   - writing rules: words and habits they never want in their book, and whether the book may mention their own services;
   - what the book should lead to for a reader who wants more.
3. **Show the author a one-screen summary** and ask what to change. Don't write anything until they say it's right.
4. **Write:**
   - `01 Planning/Book Brief.md` from their answers;
   - every [bracketed] part of `CLAUDE.md` (the book paragraph, writing rules, theme codes, the author's name);
   - one note per chapter in `Chapters/`, named `ChNN Short title.md`, from the template in `01 Planning/Chapter Template.md`, with `chapter`, `part`, `write_order` and the one-sentence job filled in and `layer: evidence`;
   - one row per chapter in `01 Planning/Book Status.md`;
   - one block per chapter in `Book Blueprint.md` (under `## Chapters`, in the shape shown there), a row per chapter in its Evidence map, and a row in the Interview roster for anyone they named as a possible interviewee (status: to invite);
   - the first decisions (title, reader, chapter order) in `01 Planning/Decisions.md` with today's date.
5. If the author keeps more than one book in the same Obsidian vault, ask for a short tag for this book (like `book-referrals`) and replace the `book` tag in every note and in `Book Map.base`.

When finished, update `01 Planning/Book Status.md` and `00 Start Here.md`, and add one line to `01 Planning/Session Log.md` (date | job | what was done | where it stopped | next). Then tell the author in three lines or fewer what you did and what comes next. Recommend `/voice-capture` as the next step.
