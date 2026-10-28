---
up: "[[00 Start Here]]"
type: control
tags: [book, control, blueprint]
---
# Book Blueprint

The whole book on one page: who's been interviewed, how much evidence each chapter has, and one short block per chapter. Every chapter note points `up` to this page, so it sits at the center of the ExcaliBrain map with the chapters around it.

Shortcuts read only the section they need (the roster, the evidence map, or one chapter's block), never the whole page. `/setup-book` creates the chapter blocks; `/prep-interview`, `/ingest-interview` and `/wrap` keep the rest current.

## Interview roster

| Person | Company | Role | Date | Consent | Status | Chapters fed | Best line |
| --- | --- | --- | --- | --- | --- | --- | --- |

Status is one of: to invite, scheduled, recorded, ingested.

## Evidence map

How much material each chapter has. Counts come from the chapter notes.

| Ch | Interviews | Research | Author material | Opening story | Biggest gap |
| --- | --- | --- | --- | --- | --- |

## Chapters

One block per chapter, in book order. Copy this shape:

```markdown
### ChN. Title
- **Layer:** evidence
- **The one idea:** (from the brief, once there is one)
- **Open with:** the strongest opening story so far, or [STORY NEEDED]
- **Interview voices:** [[YYYY-MM-DD Name|Name]], ...
- **Biggest gap:** 
- **Ask next:** questions for the next interview that would fill the gap
- **Next step:** the shortcut to run, like `/brief N`
```

## Change log

One line per change to this page, newest first.
