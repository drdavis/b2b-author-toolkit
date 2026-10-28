# Getting started

Every click, from "I have Claude" to your first chapter brief. Plan on about 90 minutes, spread over a couple of sittings if you like.

## 1. Install Claude and find the Code tab (10 min)

1. Download the Claude desktop app from [claude.ai/download](https://claude.ai/download), install it and sign in. You need a paid plan (Pro or Max) for the Code tab.
2. At the top of the window you'll see tabs. **Chat** is the one you know. **Code** is the one this toolkit uses.
3. "Code" just means Claude can work inside a folder on your computer: read your files, create new ones and keep them organized. You won't write any code.

Claude asks before it changes things. The first time it wants to edit a file or run a command you'll see a prompt to approve, and you can say no.

## 2. Install Obsidian and make your vault (10 min)

1. Download [Obsidian](https://obsidian.md) and open it.
2. Choose **Create new vault**. Name it something like `Second Brain` and put it in your Documents folder, or in iCloud Drive if you want it on your phone too. A vault is just a regular folder.

## 3. Add the toolkit (5 min)

1. On the toolkit's GitHub page, click the green **Code** button, then **Download ZIP**. Unzip it.
2. Copy the `book` folder into your vault and rename it after your book, like `My Book`.
3. The folder has a hidden `.claude` folder inside it. That's where the shortcuts live, and it comes along when you copy the folder. To see it on a Mac, press **Cmd+Shift+.** in Finder.

Your book folder now looks like this:

```
My Book/
├── CLAUDE.md              instructions Claude reads every session
├── 00 Start Here.md       one page: where the book stands, what's next
├── Book Map.base          the dashboard
├── 01 Planning/           brief, status, decisions, session log, templates
├── 02 Interviews/         interview guide, prep notes, interview notes
├── Chapters/              one note per chapter
├── Drafts/                Ch01 v1.md, Ch01 v2.md, never overwritten
├── Research/              raw material, never edited
│   ├── Transcripts/
│   ├── Sources/
│   ├── Author/Samples/    your own writing, for /voice-capture
│   └── Online/
└── .claude/               the shortcuts (skills) and checking agents
```

## 4. Set up your book (30 min)

1. In the Claude app, go to the **Code** tab and start a new session.
2. When it asks for a folder, pick your **book folder** (not the whole vault). The shortcuts only load when Claude opens the folder that contains `.claude`.
3. Type `/setup-book` and press Enter.

Claude interviews you one question at a time: the reader, the problem they haven't named, your framework, your proof, your chapter list, the problems readers run into. Take your time. The better defined your answers are, the better every chapter will be. At the end Claude shows you a summary and waits for your OK before it writes anything.

## 5. Capture your voice (20 min)

1. Put three to six pieces of your own writing in `Research/Author/Samples/`. Mix them: a client email, a LinkedIn post, an article, a podcast or talk transcript. Unedited is better. Nothing ghostwritten.
2. Type `/voice-capture`.

Claude studies the samples, asks you a few questions about how you sound, and builds a skill called `author-voice`. Then it rewrites a paragraph and asks you to score it from 1 to 10. Keep going until it's an 8 or better. Every draft from now on uses it. The profile follows a fixed structure (register, rhythm, signature openers, refused words, how you build an argument, drift signals, an anchor passage and more), which you can read in `.claude/skills/voice-capture/voice-profile-template.md`.

## 6. Add the visual layer (10 min)

Obsidian already has **Graph view** (Cmd+G), the web of dots and lines. Two more pieces make the book easy to see.

**The dashboard.** Open `Book Map.base`. It's built into Obsidian (a feature called Bases), so there's nothing to install. The tabs at the top show every chapter, chapters grouped by stage, every draft, every interview and every source.

**The mind map.** ExcaliBrain shows one note in the middle and everything connected to it around it. It needs two helper plugins.

1. In Obsidian, open **Settings** (the gear, bottom left), then **Community plugins**.
2. If you see Restricted mode, click **Turn on community plugins**.
3. Click **Browse**, search **Dataview**, click **Install**, then **Enable**.
4. Do the same for **Excalidraw**, then **ExcaliBrain**, in that order.
5. Quit Obsidian fully (**Cmd+Q** on a Mac) and reopen it.
6. Open any chapter note, press **Cmd+P** (Ctrl+P on Windows), type **ExcaliBrain** and choose **ExcaliBrain: Start**.

Every chapter note has an `up` property pointing to `00 Start Here`, so the book's hub sits above each chapter, with its interviews and sources around it.

**Tip for Graph view:** click the gear in the graph, open **Groups**, and give each kind of note its own colour: `tag:#chapter`, `tag:#interview`, `path:Research`.

## 7. Run it every week

Every session starts and ends the same way, so Claude always picks up exactly where you left off.

| | What you type | What happens |
| --- | --- | --- |
| Start | `/status` | Where the book stands and the most useful next step |
| Work | one shortcut | Ingest one interview, brief one chapter, draft one chapter |
| Close | `/wrap` | Status pages and the Session Log get updated |
| Monthly | `/lint` | A health check of the whole folder |

Then once a week, open the Book Map and look at what moved and what's stuck.

## When you get stuck

Paste the step into Claude and ask it to walk you through it. It's good at that. If a shortcut doesn't show up when you type `/`, check that Claude's Code tab has your book folder open, not the vault above it.
