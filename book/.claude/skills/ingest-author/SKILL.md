---
name: ingest-author
description: Bring the author's own dictation, voice memo or recording into the book and file every idea where it belongs
argument-hint: "[chapter number] [file name, or paste the text]"
disable-model-invocation: true
---

Before anything else, read `00 Start Here.md`, `01 Planning/Decisions.md`, `01 Planning/Book Status.md` and the last five lines of `01 Planning/Session Log.md`. Follow every rule in CLAUDE.md. Do this one job only. Also read `01 Planning/Parking Lot.md`.

Job: ingest the author's material for Chapter **$ARGUMENTS** (the chapter they were working on; the material may serve others too).

1. **Save the source.** If it was pasted, save it word for word to `Research/Author/YYYY-MM-DD ChN short topic.md` with properties (`date`, `source`, `chapter_intended`, `raw: true`) and the line "Raw source. Do not edit." Never change the author's words in the raw file, even to fix typos.
2. **Break it into ideas.** Go through it in order. For each idea, story or line worth keeping, decide where it belongs: this chapter, another chapter, the introduction or conclusion, a reader bonus, the title, or nowhere yet.
3. **This chapter's material** goes in its `## From the author` section: the main argument in their words, each story (one line, with the opening words of the paragraph it starts in), and lines worth keeping word for word. Add stories as candidates under `### 1. Open with a person` or `### 4. How it works` where they fit.
4. **Everything else is kept, never dropped.** Ideas for another chapter go in that chapter's `## From the author` with the exact words and a link to the raw file. Every idea filed elsewhere gets a row in `01 Planning/Parking Lot.md`. An idea with no home yet lives in the Parking Lot with status "no home yet".
5. If a chapter that received material already has a draft, add a revise line to its `## Still needed`.
6. Any idea for a reader bonus (an assessment, worksheet, checklist or template) also gets a row in `Bonuses/Bonus Status.md` with status idea.
7. Set this chapter's `layer` to `voice` if it was at `evidence`.

When finished, update `01 Planning/Book Status.md` and `00 Start Here.md`, and add one line to `01 Planning/Session Log.md` (date | job | what was done | where it stopped | next). Then tell the author in three lines or fewer what you did and what comes next. Say what went into this chapter and what was filed elsewhere.
