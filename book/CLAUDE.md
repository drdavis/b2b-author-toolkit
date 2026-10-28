# [Book title]: instructions for Claude

This folder is the working home of [Author name]'s book. Read this file before drafting, researching or editing anything here. Run `/setup-book` once to fill in every [bracketed] part.

## The book in one paragraph
[Who the book is for, the problem they have that they haven't named yet, what the book promises, the framework it's built on, the rough length and number of chapters, and the working title.]

## Start every session here
1. Read this file, then `00 Start Here.md`, `01 Planning/Decisions.md`, `01 Planning/Book Status.md` and the last five lines of `01 Planning/Session Log.md`.
2. Keep the context small. In chapter notes, read only the sections the job needs. Never read a full transcript: search it. Read only the latest draft of the chapter in hand.
3. Do one unit of work only (ingest, brief, draft, revise, check). The shortcuts are in `.claude/skills/`.
4. Don't reopen anything in `Decisions.md` unless [Author name] asks.
5. Before finishing, update `00 Start Here.md`, `Book Status.md` and the chapter note's properties, and add one line to the Session Log: date | job | what was done | where it stopped | next.

## Where things are
- `00 Start Here.md`: the one-page handoff. Where the book stands and what's next.
- `Book Map.base`: the dashboard. Every chapter, its stage, its interviews and drafts.
- `01 Planning/`: Book Brief, Book Status, Decisions, Session Log, Parking Lot, Chapter Template, How We Write This Book.
- `02 Interviews/`: the Interview Guide, one `Prep - Name.md` before each interview, and one note per interview with its coded findings.
- `Chapters/`: one note per chapter in the shape of `01 Planning/Chapter Template.md`. Drafts never go here.
- `Drafts/`: `Ch01 v1.md`, `Ch01 v2.md`. Never overwrite an earlier version.
- `Research/`: raw material, never edited. `Transcripts/` for interviews, `Author/` for the author's own dictation and samples, `Sources/` for articles, reports and books, `Online/` for Reddit, X and LinkedIn runs. `Quote Bank.md` holds the best lines.
- `01 Planning/Parking Lot.md`: every idea that doesn't fit the current chapter, with where it belongs. Nothing the author says is dropped.

## Writing rules
- The author's voice: use the `author-voice` skill (built by `/voice-capture`). If it doesn't exist yet, say so before drafting.
- [Words and habits the author never uses. For example: no em dashes, no exclamation points, no hype words such as unlock, transform, elevate, game-changer.]
- Every chapter follows the chapter pattern in `01 Planning/How We Write This Book.md`.
- Durability test: would the chapter's main claim have been true five years ago and still be true five years from now? If not, it belongs in an online companion, not the printed book. No screenshots, menu paths or prices in print.
- Date every statistic.
- Other books: credit what each does well, then name the opportunity for our reader. Never criticize another book.
- [No pitch for the author's services inside chapters, or the author's own rule here.]

## Evidence rules
- Quotes are exact words only. If you can't match the words to a source, don't use them as a quote.
- Interview quotes carry the transcript timestamp, like `[07:23]`, and must match the transcript in `Research/Transcripts/` word for word.
- Name an interviewee in the manuscript only when their consent is recorded as yes. Until then, describe them by role.
- Anonymize Reddit, X, LinkedIn and community quotes in the manuscript unless the person gave permission. Handles stay in `Research/`.
- Never invent interviews, numbers or client stories. If a chapter needs a story that doesn't exist yet, write `[STORY NEEDED: ...]` and add it to the chapter's `## Still needed` list.
- After any job that adds or changes quotes, run the quote checker: `python3 -I .claude/skills/check-chapter/check_quotes.py "$PWD"`. It prints `[]` when every quote matches. Fix anything it lists before finishing.

## Theme codes
The problems the reader has, coded so every quote and story can be sorted. `/setup-book` writes these with the author.
A [theme]; B [theme]; C [theme]; D [theme]; E [theme]; F [theme]; G [theme]; H [theme]; I [theme]; J other.

## Working with Claude
- Never use subagents to draft chapter prose. Use them for coding research and checking drafts.
- Ask before deleting or moving anything.
