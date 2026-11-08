---
description: The AI writing tells to cut from chapter prose. Adapted from the humanizer skill (MIT). Read by /draft, /revise and the chapter-checker.
tags: [book, control]
---
# AI tells

**Summary**: The patterns that make prose read as machine-written, adapted for this book from the humanizer skill, which draws on Wikipedia's "Signs of AI writing". Draft and revise sessions clear them before saving; the chapter-checker reports any that remain.

## How to use it
- **Drafting or revising:** before saving, read the chapter once against this list and fix what you find in your own prose. Then run the scanner on the new file and clear every line under "to fix", or keep it on purpose: `python3 -I .claude/skills/check-chapter/ai_tells.py "$PWD" "Drafts/ChNN vN.md"`. With no file named, it scans the latest version of every chapter.
- **Checking:** `/check-chapter N` runs the scanner, and the chapter-checker reports the patterns a script can't see (shapes, triads, closers).
- Fix by stating the point plainly. Keep every fact. Never add a fact, name, number, date or quote to smooth a sentence; if a sentence needs a detail you don't have, write `[STORY NEEDED: ...]` or a simpler sentence.
- Patterns 1 to 5 justify an edit on one sighting. Patterns marked *weak* need company from other tells in the same passage.

## What overrides the list in this book
- **The author's voice profile wins.** If it lists a starter this list flags (for example "Here's the thing" or "Look,"), keep it at about the profile's rate: once or twice a chapter, leading into a real point. The scanner flags more than two.
- **Quotes stay exact.** Never edit inside an interview quote, an online quote or an epigraph, whatever words it uses. The scanner skips quoted text and blockquotes.
- **Dated statistics are required.** "As of 2026" on a statistic is the evidence rule, not pattern 23.
- **Working markers are not tells.** `[STORY NEEDED]`, `[CHECK]` and similar markers stay until the gap is filled.
- **The chapter pattern's fixed sections are not decoration.** Pattern 20 doesn't apply to them.
- **A contrast that corrects something the reader believes stays.** That is often the chapter's argument. Pattern 1 targets contrasts with no one on the other side.

## A. Staging instead of stating (strong: act on one sighting)
1. **Not X but Y.** Not just X, but Y; it's not X, it's Y; "This doesn't mean X. It means Y."; a clipped tail (", no guessing"). The negative half names something no one claimed, so the positive half sounds bigger. State the point. Keep the contrast only when the reader really holds the belief it corrects.
2. **One-line closers and fragments.** A one-sentence paragraph that repeats the one before; "That matters."; "Read that again."; "Let that sink in."; a line after a story that names what it showed ("The lesson was clear:"); a row of fragments ("No plan. No system. No leads."). Cut it, or make it add a new fact or consequence.
3. **Sayings that sound deep.** The real question is, at its core, what really matters, fundamentally, the heart of the matter, X is the currency of Y, X becomes a trap. Replace the saying with the specific claim.
4. **Run-up before the point.** Let's dive in, let's break this down, here's what you need to know, now let's look at, without further ado, let's be honest, real talk. Remove the run-up and make the point. (See the voice override for starters the author really uses.)
5. **Arguing with no one.** To be clear, don't get me wrong, I'm not saying, this is not to say, you might think... but, a tempting approach would be. Remove the defense unless the reader actually holds that objection.

## B. Rhythm by rule
6. **Forced triads.** Things arriving in threes to sound complete, in one sentence or across three parallel examples. Keep three only when there are three real things.
7. **Repeated openings.** Several sentences in a row starting with the same word. Merge or vary them; repetition on purpose for rhythm is fine.
8. **Dashes.** No em dashes, en dashes or double hyphens in prose. Use a period, comma, colon or parentheses, or rewrite the sentence.
9. **Stacked qualifiers** (*weak*). Could potentially, might arguably, it's also possible. One honest hedge is fine.
10. **Hyphenated pairs after the noun** (*weak*). "A long-term plan" keeps the hyphen; "the plan is long term" drops it.
11. **Hidden actors** (*weak*). Passive voice or a missing subject where the reader needs to know who acts.

## C. Inflation
12. **Overused AI words.** actually, additionally, align with, bolstered, crucial, deep dive, delve, enduring, enhance, garner, highlight (verb), interplay, intricate, key (adjective), landscape, meticulous, pivotal, quietly, robust, showcase, tapestry, testament, underscore, valuable, vibrant. One is a hint; a cluster is a tell.
13. **Inflated significance.** Stands as a testament, a pivotal moment, plays a key role, setting the stage for, evolving landscape, indelible mark, the future looks bright. Keep the fact and drop the significance. End a section on its last concrete fact.
14. **Vague connection.** Associated with, connected to, tied to, linked to. Say what the relationship is, if the source says.
15. **-ing riders.** ", highlighting...", ", ensuring...", ", reflecting...", ", fostering..." bolted onto a fact to make it sound deeper. Keep the fact.
16. **Sales language.** Rich (figurative), profound, renowned, groundbreaking, stunning, nestled, in the heart of, diverse array. Say what the thing is.
17. **Borrowed authority.** Experts say, studies show, industry reports, observers note, with no named source. Name the source and its date, or cut the claim (the evidence rules already require this).
18. **Avoiding is, are and has.** Serves as, stands as, functions as, boasts, features, offers. Use is, are and has.

## D. Formatting by rule
19. **Bold as decoration.** Bold on every item, or lists where each item has a bold label and a colon. Turn a labeled list into prose when the labels carry nothing.
20. **Decorative headings.** Title Case On Every Word, emojis, arrows, a rule between every section, headings written for effect. Use sentence case and name what the section holds.

## E. Leftovers from the chat and the draft
22. **Chatbot residue.** I hope this helps, great question, certainly!, let me know if, would you like me to. Remove.
23. **Knowledge-limit disclaimers.** Based on available information, not widely documented, it is believed that, likely grew up or studied. State what the source doesn't show, or cut the sentence.
24. **Heading repeated in the first line.** Cut the sentence that restates the heading.
25. **Narrating the text.** "In this section we'll explore", "as mentioned above", "the table below compares". Say the thing. A one-line pointer to another chapter is fine, and so are the working notes at the top of a draft (not for print).

Left out from the humanizer: 21 (curly quotes; a typesetting choice, and changing them would break exact-quote matching) and 26 (writing for the wrong reader; it applies to replies, not chapters).

## Source and license
Adapted from humanizer v3.1.0 by Siqi Chen (https://github.com/blader/humanizer), which draws on Wikipedia's "Signs of AI writing" (WikiProject AI Cleanup). Used under the MIT License:

> MIT License
> 
> Copyright (c) 2025 Siqi Chen
> 
> Permission is hereby granted, free of charge, to any person obtaining a copy
> of this software and associated documentation files (the "Software"), to deal
> in the Software without restriction, including without limitation the rights
> to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
> copies of the Software, and to permit persons to whom the Software is
> furnished to do so, subject to the following conditions:
> 
> The above copyright notice and this permission notice shall be included in all
> copies or substantial portions of the Software.
> 
> THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
> IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
> FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
> AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
> LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
> OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
> SOFTWARE.
