# Voice profile template

The shape `/voice-capture` fills in to build the `author-voice` skill. Every section is evidence-based: it quotes the author's real sentences from `Research/Author/Samples/` or their interview answers, never invented examples. A section with no evidence yet says so instead of guessing.

Save the finished profile as `.claude/skills/author-voice/SKILL.md`. Everything below the line is the file.

---

```markdown
---
name: author-voice
description: Write in [Author name]'s voice: [the kinds of writing, such as book chapters, LinkedIn posts, emails, articles, talks]. Use whenever drafting or revising anything published under their name, even when they don't say "in my voice". Don't use for internal notes or documents where they're the reader, not the author.
---

# [Author name]: voice profile

Built [date] from [N] samples ([list them: a talk transcript, two client emails, a LinkedIn post, etc.]) and a voice interview. Re-run `/voice-capture` every six months or after a major positioning shift.

## Audience
Who they write for, and what that reader believes about their own problem before they start reading. One short paragraph.

## Register
How formal they sound, described as a position between two familiar points (for example, somewhere between a text to a friend and a keynote speech). Then one real sentence of theirs that anchors the register, and a line on what that sentence shows.

## Signature sentence starters
The openers they actually use, as a list of five to eight. Mark the one or two that carry the most weight and say when they reach for them.

## Refused words, phrases and habits
Everything they never want in their writing: words, stock phrases, punctuation habits, formats (such as bullet lists standing in for reasoning), opener styles and AI filler. Include the ones they named in the interview and the ones conspicuously absent from every sample.

## Rhythm
How their sentences and paragraphs move: long or short, built up or punchy, how a point is set up, landed and grounded. Describe the pattern in one or two lines, then show it with a real passage and point out where each part of the pattern falls.

## Vocabulary fingerprints
Words and phrases that are distinctly theirs: proprietary metaphors, their standard for "good", the verbs they use for results. One line each on what the word does for them.

## Connectors and discourse markers
The filler and transition words they really use, and what each one signals (softening, checking in, arriving at the real point, closing a list).

## How they build an argument
The structural moves in order, for persuasive pieces. For example: how they open on the reader's problem, where they put their own position, how they bring in proof (a story they witnessed, data, a client), how they close (practical instruction, a low-pressure next step). Three to six numbered moves.

## Formatting habits
Paragraph length, use of headings and lists, punctuation tics, how they emphasize, how they sign off. Note any differences between formats (email versus long-form versus social).

## Human moments to keep
The real-person details that make them recognizable: admissions, references to their own work or clients, regional plain-spokenness, generosity signals. Drafts should include one or two of these where they fit naturally.

## Drift signals
The signs a draft has stopped sounding like them. A list of five to eight, each specific enough to catch in an edit (an opener style, a sentence pattern, a word, a format).

## Reader alignment
One short paragraph on how the voice fits the reader: what register earns this reader's trust, and what would lose it.

## Anchor passage
One real passage of theirs, quoted exactly, with the sample file it came from. This is the calibration point for sentence length, transitions and the close.

## How to use this skill
1. Use it for every draft and revision published under their name.
2. Mirror the rhythm and the argument moves; avoid every refused word and drift signal.
3. After drafting, reread against the drift signals before handing the draft over.

## Test record
- [date]: generic paragraph rewritten, scored [N]/10 by the author. What they said was off: [notes]. Fixed: [what changed].
```
