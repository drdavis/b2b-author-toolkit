---
name: voice-capture
description: Study how the author writes and talks, then build their author-voice skill so every draft sounds like them
disable-model-invocation: true
---

Job: build the author's voice profile and save it as a skill Claude uses whenever it drafts.

1. **Gather samples.** Read everything in `Research/Author/Samples/`. Ask for more until you have three to six pieces of the author's own unedited writing or speech: a client email, a LinkedIn post, an article, a talk or podcast transcript. Speech is valuable because it's how they sound before they edit. Ask the author to paste anything that isn't in the folder, and save each one word for word to `Research/Author/Samples/` with the date and what it is. Ghostwritten or heavily edited pieces don't count; ask.
2. **Interview the author, one question at a time:**
   - Who do you picture reading this?
   - When you explain your work to a client over coffee, how do you start?
   - What words or phrases make you cringe when you see them in business writing?
   - Which writers or speakers do you like listening to, and why?
   - What do people say about how you explain things?
   - What do you never want to sound like?
   - Is there a metaphor, phrase or story you use all the time?
   - Read this paragraph [write one generic paragraph on their topic]. What's wrong with it?
3. **Analyze.** From the samples and answers, work out: register (how formal), sentence rhythm, signature openers, connectors and filler words they actually use, vocabulary that's theirs, words and habits they refuse, how they structure an argument, how they close, and the drift signals that mean a draft has stopped sounding like them. Quote their real sentences as evidence; never invent an example and present it as theirs.
4. **Write the skill.** Fill in `.claude/skills/voice-capture/voice-profile-template.md` section by section and save the result as `.claude/skills/author-voice/SKILL.md`. Every section quotes the author's real sentences as evidence. Where there isn't enough evidence for a section yet, say so in that section and ask for another sample rather than guessing.
5. **Test it.** Rewrite the generic paragraph from step 2 using the new skill. Ask the author to score it from 1 to 10 and say what's off. Fix the profile and try again until they score it 8 or higher. Record each round in the skill's `## Test record` with the date and score.
6. Add a line to `01 Planning/Decisions.md`: voice profile built, the date, and "re-run every six months or after a positioning shift".

When finished, update `01 Planning/Book Status.md` and `00 Start Here.md`, and add one line to `01 Planning/Session Log.md` (date | job | what was done | where it stopped | next). Then tell the author in three lines or fewer what you did and what comes next.
