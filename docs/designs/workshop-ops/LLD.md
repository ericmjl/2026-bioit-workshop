# Workshop Operations — Low-Level Design

**Created**: 2026-05-18  
**HLD Link**: [High-Level Design](../../high-level-design.md)

## Overview

This LLD covers everything needed to **deliver** the workshop: materials repo, co-presenter playbook, timing, environment prep, and dry-run checklist. It is not delivered to attendees as a section — it is the operational backbone for Parts 1–3.

## Master Run of Show

| Clock | Segment | Duration | Default lead | Role swap? |
|-------|---------|----------|--------------|------------|
| 0:00 | Part 1: Foundations & Tooling | 45 min | TBD | — |
| 0:45 | **Break** | 15 min | — | **Swap lead/support here** |
| 1:00 | Part 2: Software Standardization | 45 min | TBD | — |
| 1:45 | Part 3: Agents & Automation | 45 min | TBD | Optional swap at 1:45 |
| 2:30 | Buffer / Q&A | 0–15 min | Either | — |

**Booked slot**: 3 hours. **Content**: ~2h 15m. Buffer absorbs discussion overruns or Q&A.

### Suggested default assignment (editable)

| Segment | Lead | Support |
|---------|------|---------|
| Part 1 | Eric | Jackie |
| Part 2 | Jackie | Eric |
| Part 3 | Eric | Jackie |

Swap at break is the natural handoff. Confirm with Jackie before dry run.

## Co-Presenter Playbook

Either presenter may lead or support. When **supporting**:

### During discussion

- Circulate, listen for plenary-worthy comments
- Help quiet groups get unstuck (repeat prompt if needed)
- Answer 1:1 questions without derailing the room

### Mic routing

1. Attendee raises hand or support notices a comment
2. Support **triages**: Can I answer this quietly? Did we already cover this?
3. If worth the room: get mic to attendee, repeat question for recording/back row
4. If not: brief 1:1 answer, "let's take that offline"

### During demos

- Help attendees following along (optional — most observe)
- Watch for error messages on lead's screen; flag if something breaks
- Have fallback recording ready to narrate

### Popcorn contributions

- Either presenter may chime in anytime with examples or corrections
- Don't compete with lead — one voice at a time

## Materials Repo Structure

Follow PyData Boston pattern: public GitHub repo linked at session start.

```
2026-bioit-workshop/          # or dedicated materials repo
├── README.md                 # Setup, follow-along instructions
├── docs/                     # Design docs (optional to link)
├── examples/
│   ├── messy/                # Duplicated Marimo notebooks (Part 3)
│   └── clean/                # Refactored output (Part 3 fallback)
├── templates/
│   └── repo-scaffold/        # Cookiecutter/copier template (Part 1)
├── demos/
│   ├── doc-publishing/       # MkDocs or equivalent (Part 1)
│   └── cli-example/          # Optional CLI demo artifact
└── resources/
    ├── discussion-questions.md
    ├── matt-pocock-architecture-skill.md
    └── marimo-pair-setup.md
```

### README must include

- [ ] Python version requirement
- [ ] Optional: coding agent setup (Cursor, Claude Code, etc.)
- [ ] Optional: Marimo / Marimo Pair install
- [ ] "Observe-along is fine — you don't need any of this installed for the session"

## Environment Prep Checklist

### Presenter machines (both)

- [ ] Repo cloned, dependencies installed
- [ ] Repo init demo tested end-to-end
- [ ] Doc publishing demo tested (<2 min to show publish)
- [ ] Messy notebooks open and verified
- [ ] Agent + architecture skill tested on messy notebooks
- [ ] Clean fallback artifacts verified
- [ ] Marimo Pair tested
- [ ] Screen recording fallbacks exported
- [ ] Offline or low-network fallback plan (local builds only)

### Room / AV

- [ ] HDMI / adapter confirmed
- [ ] Font size readable from back row (terminal ≥ 16pt)
- [ ] Mic for audience questions (or support repeats question)
- [ ] Seaport venue logistics confirmed (Eric: buses/subway; Jackie: bike)

## Dry-Run Checklist

Run at least one full timed dry run before BioIT World.

| Check | Pass? |
|-------|-------|
| Part 1 completes in ≤45 min with one plenary share | |
| Part 2 keystone exercise not cut | |
| Part 3 both demos work or fallbacks ready | |
| Role swap at break feels smooth | |
| Support can triage a planted question correctly | |
| Exit reflection fits in 5 min | |
| Total content ≤2h 15m | |

## Pre-Workshop Content Prep

Generate before session (from transcripts + HLD):

- [ ] Discussion question sets per part
- [ ] Facilitator notes for each prompt
- [ ] Demo step-by-step scripts (see demo-scripts EARS)

Source inputs:

- `transcripts/20260518-ideas.md`
- `transcripts/20260518-1-on-1-with-jackie.md`
- `docs/high-level-design.md`

## Risk Operations

| Risk | Owner | Mitigation |
|------|-------|------------|
| Demo failure | Lead | Fallback recording; narrate pre-built artifact |
| Discussion overrun | Lead | Hard stops in run-of-show; cut plenary shares |
| Low agent adoption in audience | Lead | Frame agents as optional; Parts 1–2 stand alone |
| Co-presenter unclear on role | Both | Confirm default assignment; rehearse swap at break |
| Attendees can't see screen | Support | Repeat key points verbally; repo for later |

## Post-Workshop

- [ ] Repo stays public for follow-along
- [ ] Optional: gather feedback (1-min Google form — artifact, keystone, tool columns)
- [ ] Debrief Eric + Jackie: what to cut/add for next delivery

## Requirements

- [Run-of-Show EARS](./run-of-show-EARS.md)
- [Materials Repo EARS](./materials-repo-EARS.md)

## Related Documents

- [High-Level Design](../../high-level-design.md)
- [Part 1: Foundations & Tooling](../part-1-foundations/LLD.md)
- [Part 2: Software Standardization](../part-2-software/LLD.md)
- [Part 3: Agents & Automation](../part-3-agents/LLD.md)
