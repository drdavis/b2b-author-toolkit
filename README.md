# The B2B Author Toolkit

**A Claude system for consultants, founders and executives writing a business book. Your stories, your interviews, your voice, organized so the book actually gets written.**

---

### Watch the 9-minute walkthrough

[![Building a Second Brain for Book Writing: a walkthrough of the system on a real book in progress](https://cdn.loom.com/sessions/thumbnails/5b2607352bca46a8b98e8dc09b9dde67-481012f22602317e.gif)](https://www.loom.com/share/5b2607352bca46a8b98e8dc09b9dde67)

This shows my own book, early in the process. The kit is a cleaned-up, general version of it, so a few folders and names differ.

---

## I have Claude. Now what?

Most experts who sit down to write a book with AI hit the same wall. You open a chat, explain your idea, get something back that sounds like everyone else's business book, and next week you start over because Claude has forgotten all of it. The problem isn't Claude. It's that there's no system around it.

The reality is, a business book is a project with a lot of moving parts: interviews, client stories, research, your own half-finished ideas, a dozen chapters at different stages. When I started writing my own book, *Too Good to Be a Secret*, I didn't want a writing assistant. I wanted a working system. So I built one, piece by piece, and this is it, cleaned up so you can use it for yours.

Here's what you get:

- **A book folder Claude reads every session.** It already knows your reader, your framework, your rules and where you left off. You explain it once.
- **A mind map before the outline.** `/mind-map` puts the whole book on one page in Obsidian, so you see its shape before you commit to chapters. `/setup-book` then turns the map into your outline.
- **Your voice as a skill.** `/voice-capture` studies how you actually write and talk, then builds a voice profile Claude uses for every draft. You score it until it sounds like you.
- **An evidence system.** Interviews, sources and online research get coded by theme and filed into the chapters they serve, with exact quotes and timestamps. A quote checker proves every quote matches its source.
- **A writing pipeline.** Every chapter moves through the same layers: evidence, voice, brief, draft, revised, checked. One shortcut per step.
- **A book you can see.** A Book Blueprint at the center, a dashboard of every chapter and where it stands, and a connections view of how your chapters, interviews and sources link up, inside Obsidian.
- **A place for every idea.** A Parking Lot so nothing you say gets lost, and a Bonuses area that collects reader bonus ideas as they come up.

It's built on [Andrej Karpathy's LLM Wiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f): raw sources you never touch, and a set of linked notes Claude maintains on top of them. I took that idea and shaped it around how a nonfiction book really gets made.

## Who it's for

Experts writing a B2B or business nonfiction book from their own practice: consultants, fractional executives, founders, coaches, agency owners. It works best when the book draws on real client stories and interviews, because that's where the system does the most for you.

It isn't a ghostwriter. It won't write your book from a prompt. It organizes the material only you have, keeps every quote honest, and drafts in your voice from a brief you approve.

## What you need

- A paid Claude plan (Pro or Max) and the Claude desktop app, from [claude.ai/download](https://claude.ai/download). You'll use its **Code** tab. You won't write any code; it just means Claude can work inside a folder on your computer.
- [Obsidian](https://obsidian.md), free. This is where you read, browse and see the map.
- About 90 minutes to two hours for setup.

## Get started

1. **Download this toolkit.** Click the green **Code** button at the top of this page, then **Download ZIP**, and unzip it. (Or `git clone` it if you know how.)
2. **Copy the `book` folder into your Obsidian vault** and rename it after your book. It contains a hidden `.claude` folder with all the shortcuts; copying the folder brings it along.
3. **Open that folder in Claude's Code tab** and type `/mind-map`. Talk through everything you know about the book, in any order, and Claude puts it on one page.
4. **Type `/setup-book`.** Claude turns the map into an outline, asks only what the map didn't answer, and fills everything in.
5. **Run `/voice-capture`** so every draft sounds like you.

The full walkthrough, with every click, is in **[docs/getting-started.md](docs/getting-started.md)**.

## Mind map, outline, then write or dictate

That's the order the toolkit follows. Map the whole book on one page, turn the map into an outline, then fill each chapter whichever way suits you: write it, dictate it, interview people for it, or teach it live in a workshop and bring the recording in. Some experts think best with an audience in front of them, and a few workshops, one per part of the book, can fill many of the gaps only you can fill.

One thing not to put off: the day you settle on a title, buy the domain for it, before anyone hears the title in public. Once a title is out, someone can register it first, and you're left with a second-best address for your book. The author website can come later.

The details, including how to run a workshop, are in **[How We Write This Book](book/01%20Planning/How%20We%20Write%20This%20Book.md)**.

## The shortcuts

Type these in Claude's Code tab with your book folder open.

| Stage | Shortcut | What it does |
| --- | --- | --- |
| Set up | `/mind-map` | Puts the whole book on one page, as an Obsidian Canvas, before the outline |
| | `/setup-book` | Turns the map into your outline: interviews you for the rest, then writes your CLAUDE.md, Book Brief and one note per chapter |
| | `/voice-capture` | Studies your writing and builds your `author-voice` skill |
| | `/comparable-books` | Researches the books on your shelf: what each does well and the opening it leaves you |
| | `/validate-problem` | Scores your book's problem: painful, pervasive, priority now, and whether people pay to fix it |
| Evidence | `/prep-interview Name` | Builds an interview plan aimed at the chapters that need evidence most |
| | `/ingest-interview Name` | Saves the transcript, codes it by theme, feeds exact quotes into the chapters (workshop recordings too) |
| | `/ingest-source file` | Reads an article, report or PDF and feeds what's useful into the chapters |
| | `/research-run` | Collects and codes what your readers say about the problem online |
| | `/dictation-questions N` | Writes questions you answer out loud, the fastest way to get your own stories in |
| | `/ingest-author N` | Files your own dictation or voice memos, so no idea gets lost |
| | `/quote-plan` | Places one key quote, one anchor and at most three interview voices in each chapter |
| Write | `/brief N` | A one-page plan for chapter N, checked against a quality gate |
| | `/draft N` | Drafts chapter N from its brief, in your voice |
| | `/revise N notes` | Applies your notes as a new version; nothing is overwritten |
| | `/check-chapter N` | An independent agent checks every quote, number and rule |
| | `/humanizer` | Rewrites AI-sounding passages so they read like you, without changing what they say |
| | `/bonus Name` | Plans or builds a reader bonus: an assessment, worksheet or checklist |
| Run it | `/status` | Where the book stands and the single most useful next step |
| | `/wrap` | Ends the session and updates the status pages and log |
| | `/lint` | Monthly health check: gaps, contradictions, loose ends |

How the pieces fit together is in **[docs/how-it-works.md](docs/how-it-works.md)**.

## The rules it keeps for you

These are built in, because a business book lives or dies on trust:

- Quotes are exact words only, checked against the source.
- Interviewees are named only when they've said yes.
- Nothing is invented. A missing story becomes `[STORY NEEDED]`, not a made-up client.
- Raw material is never edited. Drafts are never overwritten.
- Every statistic gets a date.
- No AI slop. Every draft is checked against 24 AI writing tells (staged contrasts, one-line closers, stock words like "delve" and "crucial", dashes everywhere), and a scan flags the ones a script can find. The list is adapted from Siqi Chen's [humanizer](https://github.com/blader/humanizer) v4.0.0 (MIT), which draws on Wikipedia's "Signs of AI writing". The humanizer skill itself is included too, unchanged with its license, as `/humanizer`, for rewriting whatever the check flags.

## About

Built by Don Davis, D3 Digital Media Marketing, while writing *Too Good to Be a Secret: How Consultants and Fractional Executives Become the Expert Buyers, Colleagues and AI Recommend*. If you build your book with it, I'd like to hear how it went.

- **Connect with me on LinkedIn:** [linkedin.com/in/dondavis](https://www.linkedin.com/in/dondavis/)
- **Want to go further with content systems?** Join my Skool community: [skool.com/visibility-7361](https://www.skool.com/visibility-7361/about)

Released under the [MIT License](LICENSE).
