---
up: "[[00 Start Here]]"
type: control
tags: [book, control]
---
# How We Write This Book

The method every shortcut follows. Change it to fit your book, but change it here, so Claude and you are always working from the same page.

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
