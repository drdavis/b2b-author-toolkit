---
up: "[[00 Start Here]]"
type: control
tags: [book, control]
---
# How We Write This Book

The method every shortcut follows. Change it to fit your book, but change it here, so Claude and you are always working from the same page.

## The seven steps
1. **Mind map.** `/mind-map` puts the whole book on one page in `Book Mind Map.canvas`: the promise, the reader, the problem, the framework, the proof and every chapter's one idea. You see the book's shape before you commit to it, and anything not yet settled shows up on the map as a question.
2. **Chapter outline.** `/setup-book` turns the map into the outline: one note per chapter, the Book Blueprint and the Book Status table. `/comparable-books` and `/validate-problem` test the idea before you commit to chapters.
3. **First draft.** Get a first version of each chapter down, whichever way suits you (below). `/voice-capture` first, so drafts sound like you; then `/brief N` and `/draft N`. Gaps stay as markers, never invented: `[STORY NEEDED: ...]`, `[INTERVIEW SLOT: ...]`, `[CHECK: ...]`.
4. **Interview.** `/prep-interview Name`, the call, then `/ingest-interview Name`. Interviews capture stories and exact quotes that fit each chapter, and they test the book: if a chapter's idea doesn't hold for the people it's for, change the outline, not just the wording.
5. **Research quotes and statistics.** `/research-stats` finds published numbers and studies, read at the source, with ready endnotes. `/research-run` collects what readers say online, and `/ingest-source` reads a report you already have. This fills the `[CHECK: ...]` markers; a claim no source supports is stated as your own experience.
6. **Refine.** `/quote-plan` places the best quotes, then `/revise N` writes the next version with the interviews and research taken in at once. Nothing is overwritten.
7. **Check.** `/check-chapter N` matches every quote to its source, dates every number and runs the AI-tells scan; `/humanizer` fixes what still sounds machine-made.

Steps 4 and 5 run side by side, and steps 4 to 6 repeat as material arrives: draft before every interview is in, and refine when two or three new pieces have piled up. Research comes before refining so one revision takes in both, and so a claim that doesn't hold up gets cut before it's polished.

## Ways to get the words out
For the first draft and beyond. Mix these chapter by chapter.

- **Write.** Type your stories and arguments, save them to `Research/Author/` and run `/ingest-author N`.
- **Dictate.** `/dictation-questions N` writes the questions only you can answer. Talk through them, save the recording or transcript to `Research/Author/` and run `/ingest-author N`. Most experts can talk through a story far faster than they can write it.
- **Interview.** `/prep-interview Name`, hold the call, then `/ingest-interview Name`. Other people's stories and exact words become evidence.
- **Hold workshops.** Teach the book live, one part per session, to people who match your reader. Some authors think best with an audience in front of them. A workshop gets your explanations out loud, collects the questions real readers ask, and, if a volunteer agrees, gives you a worked example built on the spot.
  - Plan each session from its chapters: turn their `## Still needed` items and dictation questions into talking points, so teaching the chapter answers them.
  - Open with the consent line: the session is recorded for a book; anyone quoted is described by role, never named, unless they say yes in writing; and they can tell you afterwards if they'd rather you didn't use something they said.
  - Record it, save the transcript to `Research/Transcripts/` and run `/ingest-interview Workshop 1` (or whatever you named it). Your own words go to each chapter's `## From the author`; attendees are quoted by role, exact words only.
  - Keep the questions people ask. They are the best source for each chapter's "Has this happened to you?" lines.
  - Keep the sign-up list. The people who came are the first ones to tell when the book is out.

## When the title is settled, buy the domain
Buy the domain for the title the day you settle it, before the title appears anywhere public. Once it's in a post, a podcast or on a sign-up page, someone can register it first, and you end up with a second-best address for your book. Buy the exact title if you can, plus a short version, and set them to renew automatically. Record it in `Decisions.md`. The author website can come later.

## The layers
Every chapter moves through the same six layers. The `layer` property on the chapter note says where it is, and the Book Map groups chapters by it.

| Layer | What it means | How it gets there |
| --- | --- | --- |
| evidence | Interviews, sources and online research are filed in the chapter note | `/ingest-interview`, `/ingest-source`, `/research-run` |
| voice | The author's own argument and stories are in | `/ingest-author` |
| brief | A one-page plan for the chapter exists and passes the quality gate | `/brief` |
| draft | A first draft exists in `Drafts/` | `/draft` |
| revised | The author's notes are applied | `/revise` |
| checked | An independent check found no unmatched quotes or rule breaks | `/check-chapter` |

The order matters. Evidence and voice come before the brief, and the brief comes before the draft. A draft written without evidence reads like everyone else's book. A draft written without the author's own stories doesn't sound like the author.

## The chapter pattern
Every chapter is read in the same order, so the reader always knows where they are.

1. **Open with a person.** A real client, interviewee or the author, in a real moment. Never a composite.
2. **Has this happened to you?** Three to five lines in the reader's own words, so they recognize themselves.
3. **The idea.** One idea per chapter, said in one sentence.
4. **How it works.** The steps, and a worked example from a real case.
5. **This week.** One action the reader can take in under an hour.
6. **The takeaway.** The line they should remember.

## The quality gate for a brief
A brief passes when every answer is yes:
- Can the one idea be said in one sentence, and is it different from every other chapter's idea?
- Is the opening story real, sourced and named or described by role with consent noted?
- Are the reader quotes exact, with sources?
- Does the worked example come from a real case?
- Can the "this week" action be done in under an hour without buying anything?
- Does the main claim pass the durability test in CLAUDE.md?
- Are all gaps marked `[STORY NEEDED]` or `[EVIDENCE NEEDED]` instead of filled with guesses?

## One unit of work per session
Each session does one job: ingest one interview, brief one chapter, draft one chapter, check one draft. Then `/wrap`. Small sessions keep Claude's context clean and keep the Session Log honest.
