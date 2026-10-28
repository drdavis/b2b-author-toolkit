---
name: draft
description: Draft a chapter from its brief in the author's voice
argument-hint: "[chapter number]"
disable-model-invocation: true
---

Before anything else, read `00 Start Here.md`, `01 Planning/Decisions.md`, `01 Planning/Book Status.md` and the last five lines of `01 Planning/Session Log.md`. Follow every rule in CLAUDE.md. Do this one job only.

Job: draft Chapter **$ARGUMENTS**.

1. Read the chapter note's `## Brief` and `## From the author`, and any Parking Lot rows for this chapter. If there's no brief, stop and tell the author to run `/brief $ARGUMENTS` first.
2. Use the **author-voice** skill. If it doesn't exist, stop and recommend `/voice-capture`. Follow the chapter pattern in `01 Planning/How We Write This Book.md` and every writing rule in CLAUDE.md.
3. Open with the key quote and anchor from this chapter's row in `01 Planning/Quote Plan.md`, and use no more than the supporting voices it lists. Use only quotes that exist word for word in this folder. Anonymize online quotes. Name an interviewee only if their consent is yes; otherwise describe them by role. Where the brief has a gap, write `[STORY NEEDED: ...]` in the draft instead of filling it.
4. Save to `Drafts/ChNN v1.md` (or the next version; never overwrite) with properties `chapter`, `version`, `date`, `words`, `brief` link and `tags: [book, draft]`.
5. Don't change the brief. Set the chapter's `layer` to `draft`.

When finished, update `01 Planning/Book Status.md` and `00 Start Here.md`, and add one line to `01 Planning/Session Log.md` (date | job | what was done | where it stopped | next). Then tell the author in three lines or fewer what you did and what comes next. Recommend `/check-chapter` next.
