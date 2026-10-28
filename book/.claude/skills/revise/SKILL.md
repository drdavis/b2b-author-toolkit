---
name: revise
description: Revise the latest chapter draft from the author's notes
argument-hint: "[chapter number] [notes]"
disable-model-invocation: true
---

Before anything else, read `00 Start Here.md`, `01 Planning/Decisions.md`, `01 Planning/Book Status.md` and the last five lines of `01 Planning/Session Log.md`. Follow every rule in CLAUDE.md. Do this one job only.

Job: revise the latest draft of Chapter **$0** using the author's notes (everything after the chapter number): $ARGUMENTS

1. Find the highest version in `Drafts/` for this chapter.
2. Apply the notes, using the **author-voice** skill. Keep everything else unless the notes say otherwise.
3. Save as the next version; never overwrite. At the top, list what changed.
4. Set the chapter's `layer` to `revised`.

When finished, update `01 Planning/Book Status.md` and `00 Start Here.md`, and add one line to `01 Planning/Session Log.md` (date | job | what was done | where it stopped | next). Then tell the author in three lines or fewer what you did and what comes next.
