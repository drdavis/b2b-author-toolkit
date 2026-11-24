---
name: mind-map
description: Put the whole book on one page as an Obsidian Canvas, before the outline. Step 1 of the seven steps
argument-hint: "[optional: a file with your notes or dictation about the book]"
disable-model-invocation: true
---

Before anything else, read `00 Start Here.md`, `01 Planning/Decisions.md`, `01 Planning/Book Status.md` and the last five lines of `01 Planning/Session Log.md`. Follow every rule in CLAUDE.md. Do this one job only. Also read `01 Planning/Book Brief.md`, and `01 Planning/Book Mind Map.canvas` if it exists.

Job: put the whole book on one page in `01 Planning/Book Mind Map.canvas`, so the author can see its shape before outlining it. It is step 1 of the seven steps in `01 Planning/How We Write This Book.md`: mind map, outline (`/setup-book` turns the map into chapters), first draft, interview, research, refine, check. Run it again whenever the book changes shape.

1. **Get everything out first.** If `$ARGUMENTS` names a file, read it. If the Book Brief and chapter notes are already filled in, start from them. Otherwise ask the author to talk through everything they know about the book, in any order, typed or dictated: who it's for, the problem, the stories they keep telling, the framework, chapter ideas, what they want a reader to do next. Don't impose structure yet.
2. **Sort it into branches:** the title and promise in the center; who it's for and who it isn't; the problem the reader hasn't named; the framework; the proof (stories, clients, data, people to interview); the parts and chapters, each with its one idea in a sentence and the reader bonus or exercise it carries, if there is one; and what the book leads to for a reader who wants more.
3. **Ask about the gaps,** one question at a time, only for branches that are empty or vague. Anything still open goes on the map as a question, like "Title: ?" or "Ch7: one idea?". Never fill a gap with a guess.
4. **Show the branches as a short indented list** and ask what to change. Write nothing until the author says it's right.
5. **Write the canvas** in Obsidian's JSON Canvas format: `{"nodes": [...], "edges": [...]}`. Each node is `{"id", "type": "text", "text", "x", "y", "width", "height"}` with the text in Markdown; each edge is `{"id", "fromNode", "toNode"}`. Put the title node at `x: 0, y: 0`; the reader, problem, framework, proof and leads-to branches in a column to its left; the parts in a column to its right; and each part's chapters in a column to the right of their part. Leave at least 60 pixels between nodes so nothing overlaps. Draw an edge from the title to each branch and part, and from each part to its chapters. Keep each node to a few lines; the detail lives in the chapter notes. If the canvas already exists, keep the author's own edits and positions and change only what this session changed.
6. If the map changes anything already settled in `01 Planning/Decisions.md`, list it for the author instead of changing it. Ideas that don't belong on the map go in `01 Planning/Parking Lot.md`.

When finished, update `00 Start Here.md` (if `/setup-book` hasn't run yet, it stays the next step) and add one line to `01 Planning/Session Log.md` (date | job | what was done | where it stopped | next). Then tell the author in three lines or fewer what you did and what comes next. Tell them to open `01 Planning/Book Mind Map.canvas` in Obsidian to see it; Canvas is built in, so there's nothing to install.
