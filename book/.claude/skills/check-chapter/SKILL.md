---
name: check-chapter
description: Independent check of a chapter draft against its sources and the writing rules
argument-hint: "[chapter number]"
disable-model-invocation: true
---

Before anything else, read `00 Start Here.md`, `01 Planning/Decisions.md`, `01 Planning/Book Status.md` and the last five lines of `01 Planning/Session Log.md`. Follow every rule in CLAUDE.md. Do this one job only.

Job: check the latest draft of Chapter **$ARGUMENTS**.

1. Run the quote check on the notes the draft draws from: `python3 -I .claude/skills/check-chapter/check_quotes.py "$PWD"`. `[]` means every quote in the chapter notes, Quote Bank and interview notes matches its source. `--selftest` proves the checker still catches a bad quote.
2. Hand the draft to the **chapter-checker** agent, giving it only the draft's file path, so the check is done by an agent that didn't write the draft.
3. Report its findings as a list, grouped: quotes that don't match, numbers without a date or source, rule breaks, durability concerns, missing parts of the chapter pattern. Add anything the quote checker listed. Don't edit the draft.
4. If nothing serious was found, set the chapter's `layer` to `checked`.

When finished, update `01 Planning/Book Status.md` and `00 Start Here.md`, and add one line to `01 Planning/Session Log.md` (date | job | what was done | where it stopped | next). Then tell the author in three lines or fewer what you did and what comes next.
