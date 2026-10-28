---
up: "[[00 Start Here]]"
type: control
tags: [book, control, template]
---
# Chapter Template

Every note in `Chapters/` uses this shape, so each chapter grows the same way and every shortcut knows where things go. The [[Book Blueprint]] shows one short block per chapter; the chapter note holds the full material.

**How a chapter note grows**

| When this happens | It writes to | Shortcut |
| --- | --- | --- |
| An interview is ingested | `## From interviews` (one block per person) and `## The chapter pattern` | `/ingest-interview Name` |
| A source or online run is coded | `## From research` | `/ingest-source`, `/research-run` |
| The author records or dictates | `## From the author` | `/ingest-author N` |
| The chapter is briefed | `## Brief` | `/brief N` |
| A draft is written or revised | `Drafts/ChNN vX.md` (never this note) and the `layer` property | `/draft N`, `/revise N` |
| Any session ends | the `layer` and `updated` properties, and the chapter's block in the Book Blueprint | `/wrap` |

Rules for every section:
- Quotes are exact words, with the source file. Interview quotes also carry the transcript timestamp, like `[07:23]`.
- Interviewees are named only when `consent` is `yes`. Until then the manuscript describes them by role.
- Online quotes stay anonymized in the manuscript. Handles and links stay here.
- Missing material is marked, not invented: `[STORY NEEDED: ...]` or `[EVIDENCE NEEDED: ...]`.

---

## The template

Copy everything below this line into a new chapter note.

```markdown
---
up: "[[Book Blueprint]]"
chapter: N
part: 1
layer: evidence        # evidence > voice > brief > draft > revised > checked
write_order: N
interviews: []         # links to interview notes, like "[[2026-10-01 Jane Smith|Jane Smith]]"
sources: []            # links to source notes in Research/Sources
updated: YYYY-MM-DD
tags: [book, chapter]
---
# Chapter N. Title

> **The job of this chapter:** one sentence on what the reader should believe or do by the end.

## Brief
_Empty until `/brief N`._

## The chapter pattern
The working skeleton, in the order the chapter will be read. Each step lists the material on hand and what's still missing.

### 1. Open with a person
- [STORY NEEDED: what kind of story would open this chapter best]

### 2. Has this happened to you?
- Reader quotes, exact, with sources.

### 3. The idea
- The one idea, in one sentence.

### 4. How it works
- The steps, and a worked example.

### 5. This week
- One action the reader can take in under an hour.

### 6. The takeaway
- The line the reader should remember.

## From interviews
_One block per person: `### Name · date · role · consent: yes/no/to confirm`, then links to the transcript and interview note, quotes with timestamps, and story lines._

## From research
_Sources and online runs: exact quotes with the file they came from._

## From the author
_The author's own argument, stories and lines worth keeping, from dictation or recordings._

## Still needed
- [ ] 
```
