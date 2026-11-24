---
name: research-stats
description: Find published statistics and studies that tell the book's story, read each one at its source, and file them with ready endnotes (step 5 of 7)
argument-hint: "[optional: a chapter, a claim or a topic]"
disable-model-invocation: true
---

Before anything else, read `00 Start Here.md`, `01 Planning/Decisions.md`, `01 Planning/Book Status.md` and the last five lines of `01 Planning/Session Log.md`. Follow every rule in CLAUDE.md. Do this one job only.

Job: step 5 of the seven steps in `01 Planning/How We Write This Book.md`. Find the published numbers and findings that make the book's case, focused on **$ARGUMENTS** if given, otherwise on every chapter's main claim and every `[CHECK: ...]` marker in the drafts. It runs before `/revise`, so a single revision can take in the interviews and the research together.

1. **Plan the story first.** Read the Book Brief and each chapter's `## Brief` (or its one idea in the Book Blueprint). Write the book's case as five to ten beats: the problem, why it's getting worse, what works, why it takes time, why the reader should keep going. Under each beat, list the claims that need a number, and add every `[CHECK: ...]` from the latest drafts.
2. **Search, then read at the source.** Use whatever search tools this session has. If none can reach the sources, say so and stop rather than guessing. For every figure, open the publisher's own page, PDF, press release or journal article and copy the exact words. A figure found only second hand goes under "Unverified leads". A number everyone repeats with no traceable source (the 21-day habit, the rule of seven touches) goes under "Myths". Neither goes in the book. Subagents may search in parallel, one beat each, but they return exact words with the URL and never write chapter prose.
3. **Record every entry the same way:** the exact words; author, title, publisher and date; who was asked, how many and where; the limits; theme and chapter; and a ready endnote in Chicago notes and bibliography style (author, title, publisher or journal, date, page or figure, then the DOI or URL). Every figure carries its year. For journal papers, check for a retraction or correction, and note it if an author has had other work retracted.
4. **Check it independently.** A fresh subagent with web access re-opens the headline figures at their sources and confirms the words, numbers and page references. Fix what it finds and record the result in the run note.
5. **Write the run note** in `Research/Studies/Runs/YYYY-MM-DD.md`:
   - the story in numbers, one plain line per beat, each with its year and source;
   - reasons for the reader to keep going;
   - contradictions between sources, and which figure the book uses;
   - which figures are durable enough for print and which belong in an online update (anything about fast-moving tools, platforms or prices);
   - how to cite them in the text and in the back matter, with ready endnotes by chapter;
   - then the full entries, the unverified leads and the myths.
6. **File the best.** Add the strongest picks to each chapter note's `## From research` (exact words, short source, link, theme) and to the Quote Bank. A claim with no outside source stays the author's own: the draft says "in my experience", not "research shows". Ask the author how to state it.
7. Run the quote checker: `python3 -I .claude/skills/check-chapter/check_quotes.py "$PWD"`. Fix anything it lists.

When finished, update `01 Planning/Book Status.md` and `00 Start Here.md`, and add one line to `01 Planning/Session Log.md` (date | job | what was done | where it stopped | next). Then tell the author in three lines or fewer what you found, which claims have no source, and that `/revise N` is next.
