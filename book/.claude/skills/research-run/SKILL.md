---
name: research-run
description: Collect and code what readers say about the problem online (Reddit, X, LinkedIn, communities)
argument-hint: "[optional: topic or chapter]"
disable-model-invocation: true
---

Before anything else, read `00 Start Here.md`, `01 Planning/Decisions.md`, `01 Planning/Book Status.md` and the last five lines of `01 Planning/Session Log.md`. Follow every rule in CLAUDE.md. Do this one job only.

Job: an online research run, focused on **$ARGUMENTS** if given, otherwise on the chapters with the biggest evidence gaps.

1. Read the latest note in `Research/Online/Runs/` and repeat its searches and method so runs can be compared. If this is the first run, write the method down first: where to search, what search terms, what counts as the reader.
2. Search with whatever tools this session has (web search, Apify, a Reddit or X connector). If none can reach the sources, say so and stop rather than guessing.
3. Save what you found to `Research/Online/posts.csv` (date, platform, handle, link, exact text), skipping anything already there.
4. Use the **research-coder** agent to code new posts by theme, reader fit and chapter.
5. Write a run note in `Research/Online/Runs/YYYY-MM-DD.md` with counts, what's new, and the best lines.
6. Add only new, stronger quotes to the Quote Bank and the chapter notes' `## From research`. Handles stay in `Research/`; the manuscript anonymizes them.
7. Run the quote checker.

When finished, update `01 Planning/Book Status.md` and `00 Start Here.md`, and add one line to `01 Planning/Session Log.md` (date | job | what was done | where it stopped | next). Then tell the author in three lines or fewer what you did and what comes next.
