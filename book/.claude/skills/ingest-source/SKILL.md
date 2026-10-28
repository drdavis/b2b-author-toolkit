---
name: ingest-source
description: Read an article, report, PDF or book notes, write a source note, and feed what's useful into the chapter notes
argument-hint: "[file name in Research/Sources]"
disable-model-invocation: true
---

Before anything else, read `00 Start Here.md`, `01 Planning/Decisions.md`, `01 Planning/Book Status.md` and the last five lines of `01 Planning/Session Log.md`. Follow every rule in CLAUDE.md. Do this one job only.

Job: ingest the source **$ARGUMENTS** from `Research/Sources/`. This follows Andrej Karpathy's LLM Wiki pattern: the raw file is never changed, and Claude maintains linked notes on top of it.

1. Read the full source. If it's a PDF or web page, extract the text and save it beside the original as `Name.txt` so later quote checks can find the words.
2. **Discuss before writing.** Tell the author the three to five most useful things in it for this book, which chapters they serve, and anything that contradicts what the book already says. Wait for their go-ahead.
3. Write a source note `Research/Sources/Name - note.md` with properties (`type: source`, `author`, `date`, `url` if any, `chapters: [links]`, `tags: [book, source]`), a two-sentence summary, the key points, and the best exact quotes with page or section.
4. For each chapter it serves, add a short block under `## From research` in the chapter note: the source link, the point, exact quotes. Add the source link to the chapter's `sources` property.
5. Add the one or two strongest lines to `Research/Quote Bank.md` under `## Research`.
6. Date every statistic. If two sources disagree, note the contradiction in both chapter blocks.
7. Run the quote checker and fix anything it lists.

When finished, update `01 Planning/Book Status.md` and `00 Start Here.md`, and add one line to `01 Planning/Session Log.md` (date | job | what was done | where it stopped | next). Then tell the author in three lines or fewer what you did and what comes next.
