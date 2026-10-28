---
name: bonus
description: Plan or build a reader bonus (an assessment, worksheet, checklist or template the book points to)
argument-hint: "[bonus name]"
disable-model-invocation: true
---

Before anything else, read `00 Start Here.md`, `01 Planning/Decisions.md`, `01 Planning/Book Status.md` and the last five lines of `01 Planning/Session Log.md`. Follow every rule in CLAUDE.md. Do this one job only.

Also read `Bonuses/Bonus Status.md`.

Job: work on the bonus **$ARGUMENTS**. If no name was given, list the bonus ideas in Bonus Status and in the Parking Lot, recommend the one that does the most for the reader, and stop.

1. If it has no file in `Bonuses/`, create `Bonuses/<name>.md` with properties (`up: "[[Bonus Status]]"`, `chapters: [links]`, `status: planned`, `tags: [book, bonus]`) and: which chapter points to it, what the reader gets, what format it takes, how long it takes the reader, and what it leads to for a reader who wants more.
2. If it already has a plan, build the next piece of it.
3. Bonuses follow the same voice and evidence rules as the book. A bonus built on interview material uses exact quotes and respects consent.
4. Add a link to the bonus in the chapter note it supports.

When finished, update `Bonuses/Bonus Status.md` and `00 Start Here.md`, and add one line to `01 Planning/Session Log.md` (date | job | what was done | where it stopped | next). Then tell the author in three lines or fewer what you did and what comes next.
