# Workshop Operations — Low-Level Design

**Created**: 2026-05-18
**HLD Link**: [High-Level Design](../../high-level-design.md)

## Overview

This LLD covers everything needed to **deliver** the workshop: materials repo, co-presenter playbook, timing, environment prep, and dry-run checklist. It is not delivered to attendees as a section — it is the operational backbone for Parts 1–3.

## Master Run of Show

| Clock | Segment | Duration | Lead | Support |
|-------|---------|----------|------|---------|
| 0:00 | Part 1: Foundations & Tooling | 45 min | Eric | Jackie |
| 0:45 | **Break** | 15 min | — | — |
| 1:00 | Part 2: Software Standardization | 45 min | Eric | Jackie |
| 1:45 | Part 3: Agents & Automation | 45 min | Eric | Jackie |
| 2:30 | Buffer / Q&A | 0–15 min | Eric | Jackie |

**Booked slot**: 3 hours. **Content**: ~2h 15m. Buffer absorbs discussion overruns or Q&A.

### Fixed assignment

| Segment | Lead | Support |
|---------|------|---------|
| Part 1 | Eric | Jackie |
| Part 2 | Eric | Jackie |
| Part 3 | Eric | Jackie |

Eric and Jackie are **not** swapping lead/support at the break or between parts. Jackie supports the full session (mic routing, circulation, follow-along help, popcorn examples). Confirm before dry run.

## Co-Presenter Playbook

**Eric** leads every segment (discussion facilitation, demos, bridges). **Jackie** supports throughout. When **supporting**:

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
- Have pre-built artifacts ready to narrate if a demo fails

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
│   ├── messy/                # Part 3 prep staging — copy into live pyds project notebooks/
│   ├── clean/                # Part 3 fallback — pre-built refactor if live agent is slow
│   └── pyds-init-demo/       # Pre-built pyds project init output (Part 1 fallback)
├── demos/
│   └── doc-publishing/       # MkDocs or equivalent (Part 1)
└── resources/
    ├── discussion-questions.md
    ├── keystone-worksheet.md
    ├── exit-reflection.md
    ├── pyds-cli-setup.md     # Part 1: pyds configure + project init
    ├── follow-along-setup.md # Participant setup (uv + pixi)
    ├── facilitator-runbook.md # Presenter chronological script
    ├── matt-pocock-architecture-skill.md
    └── marimo-pair-setup.md
```

### README must include

- [ ] Python version requirement (3.11+)
- [ ] **Follow-along setup** — uv + pixi quick start; `pixi global install nodejs` for `npx`; link to `resources/follow-along-setup.md`
- [ ] Observe-along is fine in-room; follow-along is optional and supported
- [ ] Links to part-specific guides (pyds-cli, coding agents, Marimo Pair)
- [ ] Link to [Data Science Bootstrap Notes](https://ericmjl.github.io/data-science-bootstrap-notes/)

## Environment Prep Checklist

### Presenter machines (both)

- [ ] Repo cloned, dependencies installed
- [ ] `pyds configure` completed; `pyds project init --no-github` tested end-to-end
- [ ] `pyds system status` passes (pixi, git, uv)
- [ ] Doc publishing demo tested (<2 min to show publish)
- [ ] Messy notebooks in `examples/messy/` open and verified
- [ ] Copy from `examples/messy/` into live pyds project `notebooks/` rehearsed
- [ ] Agent + architecture skill tested on copied notebooks in live project
- [ ] Clean fallback artifacts verified (`examples/clean/`, `examples/pyds-init-demo/`)
- [ ] `pixi global install nodejs` completed; `npx --version` passes (Marimo Pair skill install)

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
| Jackie support playbook (mic, circulation) feels smooth | |
| Support can triage a planted question correctly | |
| Exit reflection fits in 5 min | |
| Total content ≤2h 15m | |

## Pre-Workshop Content Prep

Generate before session (from transcripts + HLD):

- [ ] Discussion question sets per part
- [ ] Facilitator notes for each prompt
- [ ] Demo artifact specs (see demo-artifacts EARS per part)

Source inputs:

- `transcripts/20260518-ideas.md`
- `transcripts/20260518-1-on-1-with-jackie.md`
- `docs/high-level-design.md`

## Risk Operations

| Risk | Owner | Mitigation |
|------|-------|------------|
| Demo failure | Lead | Narrate from pre-built artifact in repo |
| Discussion overrun | Lead | Hard stops in run-of-show; cut plenary shares |
| Low agent adoption in audience | Lead | Frame agents as optional; Parts 1–2 stand alone |
| Co-presenter unclear on role | Both | Confirm fixed assignment (Eric lead, Jackie support all parts) |
| Attendees can't see screen | Support | Repeat key points verbally; repo for later |

## Post-Workshop

- [ ] Repo stays public for follow-along
- [ ] Optional: gather feedback (1-min Google form — artifact, keystone, tool columns)
- [ ] Debrief Eric + Jackie: what to cut/add for next delivery

## Requirements

- [Materials Repo EARS](./materials-repo-EARS.md)
- [Discussion Questions EARS](./discussion-questions-EARS.md)
- [Follow-Along Setup EARS](./follow-along-setup-EARS.md)
- [Facilitator Runbook EARS](./facilitator-runbook-EARS.md)

## Related Documents

- [High-Level Design](../../high-level-design.md)
- [Part 1: Foundations & Tooling](../part-1-foundations/LLD.md)
- [Part 2: Software Standardization](../part-2-software/LLD.md)
- [Part 3: Agents & Automation](../part-3-agents/LLD.md)
