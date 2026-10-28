---
name: ingest-interview
description: Bring an interview transcript into the book, code it by theme, and feed exact quotes into the chapter notes
argument-hint: "[person name]"
disable-model-invocation: true
---

Before anything else, read `00 Start Here.md`, `01 Planning/Decisions.md`, `01 Planning/Book Status.md` and the last five lines of `01 Planning/Session Log.md`. Follow every rule in CLAUDE.md. Do this one job only. Also read `01 Planning/Chapter Template.md`.

Job: ingest the interview with **$ARGUMENTS**.

1. **Find the transcript.** Look in `Research/Transcripts/`, or use the recording tool connected to this session (Fireflies, Zoom, Otter) if there is one. If nothing is found, ask the author to export it and drop it in `Research/Transcripts/`. If `02 Interviews/Prep - $ARGUMENTS.md` exists, read it: it lists the gaps this call was meant to fill.
2. **Save the transcript** as `Research/Transcripts/YYYY-MM-DD Name.md`, word for word, one line per turn in the shape `[mm:ss - mm:ss] Speaker: words` (convert the tool's format; never change the words). Add properties: `date`, `people`, `recording` link, `consent_to_quote` (yes, no, or "to confirm" if it isn't in the call), `interview_note` link, `tags: [book, transcript]`, and the line "Raw source. Do not edit."
3. **Write the interview note** `02 Interviews/YYYY-MM-DD Name.md` with properties (`interviewee`, `role`, `date`, `transcript` link, `consent`, `tags: [book, interview]`), then five reflection questions marked "draft for the author": what surprised you, what mattered most to them, what a transcript can't capture, what challenged or confirmed your thinking, what else to remember. Draft them from the transcript; never invent the author's reactions.
4. **Code the call.** Add `## Coded findings` to the interview note: a table of # | Exact words | Time | Theme | Reader fit | Chapters | Use, then `### Stories`, one line each with its start time. Quotes are exact words with the timestamp of the line they start on. Aim for 12 to 25 findings. The **research-coder** agent can do the first pass.
5. **Feed the chapter notes.** For each chapter the call serves, add a block under `## From interviews` (`### Name · date · role · consent: ...`, links to transcript and note, quotes with timestamps, story lines). Update `## The chapter pattern` where the call gives an opening story or fills a gap, tick anything in `## Still needed` it settles, and add `"[[YYYY-MM-DD Name|Name]]"` to the chapter's `interviews` property. Ask the author to close the chapter note in Obsidian first.
6. **Feed the Quote Bank** with the five to eight strongest lines.
7. **Flag drafted chapters.** If a chapter it fed already has a draft, add `- [ ] Revise draft vN: what the call adds, from Name` to its `## Still needed`.
8. **Run the quote checker** and fix anything it lists. Report any quote you had to drop.

When finished, update `01 Planning/Book Status.md` and `00 Start Here.md`, and add one line to `01 Planning/Session Log.md` (date | job | what was done | where it stopped | next). Then tell the author in three lines or fewer what you did and what comes next. Name which chapters got stronger.
