---
name: lint
description: Monthly health check of the book folder. Finds gaps, contradictions and loose ends, and changes nothing
disable-model-invocation: true
---

Before anything else, read `00 Start Here.md`, `01 Planning/Decisions.md`, `01 Planning/Book Status.md` and the last five lines of `01 Planning/Session Log.md`. Follow every rule in CLAUDE.md. Do this one job only.

Job: check the health of the whole book folder. Change nothing.

Find and report:
1. Notes with missing or broken properties (no `tags`, no `layer` on a chapter, `interviews` entries that aren't links).
2. People, sources or ideas mentioned in notes that have no note of their own or aren't linked.
3. Orphans: notes nothing links to.
4. Contradictions between notes or between sources.
5. Claims or statistics that are undated or may be outdated by newer sources.
6. Quotes the quote checker flags (run it).
7. Parking Lot ideas that now have an obvious home.
8. Chapters whose draft is older than material added to their note since.

Report a numbered list with a suggested fix for each, most important first. Add one line to the Session Log.
