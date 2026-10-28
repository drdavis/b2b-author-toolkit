---
name: dictation-questions
description: Write a question set the author answers out loud, so their own stories and arguments get into a chapter fast
argument-hint: "[chapter numbers, like 4 or 4 5]"
disable-model-invocation: true
---

Before anything else, read `00 Start Here.md`, `01 Planning/Decisions.md`, `01 Planning/Book Status.md` and the last five lines of `01 Planning/Session Log.md`. Follow every rule in CLAUDE.md. Do this one job only. Also read the Book Blueprint blocks for these chapters (never the whole file), and in each chapter note `## The chapter pattern`, `## From the author` and `## Still needed`.

Job: write a dictation question set for Chapter(s) **$ARGUMENTS**. Most experts can talk through a story far faster than they can write it, so this turns the gaps only the author can fill into questions they answer by voice.

1. **Find the gaps only the author can fill:** opening stories, worked examples, their own argument, the moment they learned the lesson, what they tell clients, decisions about the chapter. Skip anything an interview or source could fill.
2. **Write `01 Planning/Dictation Questions - ChN.md`** with:
   - **How to do it:** say the question number before each answer; short answers are fine; use first names or a short description for clients (they stay anonymous in print unless the author says otherwise); allow 45 to 60 minutes; save the recording or transcript to `Research/Author/` and run `/ingest-author N`.
   - **Part 1: Stories.** Questions that pull out one specific moment each: when it was, what set it off, what they noticed first, what they did that week. Mark each with the chapter and pattern step it fills, like *(Ch4, open with a person)*.
   - **Part 2: The argument.** What they believe that their reader doesn't yet, and why.
   - **Part 3: How it works.** Walk through the steps with a real client example.
   - **Decisions.** Up to five choices only the author can make for these chapters, each with the options.
   - **Messages to send.** Anyone the author needs to ask for a story, a consent or a fact, with a one-line draft message for each.
3. Twelve to twenty questions in all. Ask about what happened, not opinions. Never put words in the author's mouth.

When finished, update `01 Planning/Book Status.md` and `00 Start Here.md`, and add one line to `01 Planning/Session Log.md` (date | job | what was done | where it stopped | next). Then tell the author in three lines or fewer what you did and what comes next.
