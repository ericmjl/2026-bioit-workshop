# Part 1: Foundations & Tooling — Low-Level Design

**Created**: 2026-05-18
**Duration**: ~45 minutes
**Lead**: Eric · **Support**: Jackie (fixed for full workshop)
**HLD Link**: [High-Level Design](../../high-level-design.md)

## Overview

Part 1 asks two questions: **what does your team ship today**, and **what could good look like?** Attendees inventory their team's current work, surface clarity and bus-factor problems, and articulate a first-pass hypothesis of *what their team ships*. Discussion leads into live demos that show the **destination** — what a team with its act together looks like — not a tutorial on how to get there.

This section is **discussion-heavy** (~60% of segment time). Demos are observe-along and **aspirational**; Part 2 covers adoption.

## Section Goals

By the end of Part 1, attendees should be able to:

1. Name the **technical artifacts** their team currently produces (and whether they're consistent)
2. Recognize **bus factor** and **onboarding friction** as signals that standardization may help
3. Distinguish the **analysis treadmill** from work worth rearchitecting (repeatable → architect; high-variation one-off → don't)
4. See what a **standardized team's workflow** looks like — frictionless project start, docs that flow from code

## Run of Show

| Time | Block | Mode | Lead |
|------|-------|------|------|
| 0:00–0:05 | Framing: who this is for, what we'll build toward | Brief monologue | Lead |
| 0:05–0:20 | Small-group discussion: team inventory | Discussion | Lead facilitates; support circulates |
| 0:20–0:30 | Small-group discussion: bus factor & onboarding | Discussion | Lead facilitates |
| 0:30–0:35 | Plenary debrief: 2–3 groups share | Discussion | Support runs mic |
| 0:35–0:42 | Demo: what frictionless project start looks like | Live demo | Lead demos; support helps follow-along |
| 0:42–0:45 | Demo: what docs-from-code looks like + bridge to break | Live demo + close | Lead demos |
| 0:45 | **Hard stop → 15m break** | Break | — |

**Timebox rule**: If discussion runs long at 0:28, cut plenary to one share and move to demos. Demos are non-negotiable — they set up Part 2 by showing the destination.

## Discussion Design

### Block A: Team Work Inventory (~15 min)

**Setup** (lead reads aloud):

> Turn to your neighbors. You're discussing your **team's** work — not your personal projects. Inventory what your team actually delivers day-to-day.

**Prompt set**:

1. What does your team produce in a typical month? List concrete outputs.
2. Are those outputs consistent across team members, or does everyone ship something different?
3. If a collaborator asked "what does your data science team deliver?", could every member give the same answer?
4. What fraction of work feels like a one-off analysis vs. something reused?

**Facilitation notes**:

- Groups of 3–4 (neighbor seating)
- Support presenter listens for good plenary candidates
- Don't solve problems yet — just inventory

### Block B: Bus Factor & Onboarding (~10 min)

**Prompt set**:

1. If your most specialized team member left tomorrow, how long until someone else could continue their work?
2. How easy is it for team members to onboard onto each other's repos/notebooks?
3. Do you see silos — individuals working in bespoke ways that others can't follow?
4. Is your team growing? Does that change the urgency?

**Bridge to demos** (lead, ~1 min):

> You've surfaced the gaps — inconsistency, bus factor, onboarding pain. Before we talk about how to get there, let me show you what it looks like when a team *has* its act together. This is the destination, not the tutorial.

## Live Demos (Inspiration, Not Instruction)

Demos are **show-don't-tell**: attendees should leave thinking "I want that for my team," not "I need to install this now." Part 2 covers the practices and the first change to make.

### Demo 1: What Frictionless Project Start Looks Like

**Purpose**: Show the end state — starting a new project doesn't require reinventing structure every time.

**Content** (live demo uses [pyds-cli](https://ericmjl.github.io/pyds-cli/)):

- Run `pyds project init --no-github` to scaffold a new project in one interactive command
- Highlight what pyds encodes via the [cookiecutter-python-project](https://github.com/ericmjl/cookiecutter-python-project) template: `notebooks/`, a named source package with CLI stub, pre-commit hooks, pytest layout, and pixi environment setup
- Narrate aspirationally: "On a team that has its act together, the first commit is already aligned with team standards. No one debates folder structure on day one."

**Prep requirements**:

- [ ] `pyds configure` completed on presenter's machine before the workshop
- [ ] Prerequisites verified: `pixi`, `git`, `uv` (`pyds system status`)
- [ ] `pyds project init --no-github` tested end-to-end before the session
- [ ] Fallback: `examples/pyds-init-demo/` in workshop materials (narrate from pre-built tree if live init fails)

### Demo 2: What Docs-From-Code Looks Like

**Purpose**: Show the end state — documentation isn't a separate chore; it flows from the repo.

**Content**:

- Connect repo to doc publishing (MkDocs/Material, Sphinx, or GitHub Pages pattern)
- Show a small edit → auto-publish cycle
- Narrate aspirationally: "When docs live in the repo, they're always current. Your collaborators — and later, your agents — can find what they need."

**Prep requirements**:

- [ ] Doc site already deployed or deployable in <2 min
- [ ] Fallback: show published URL + local build

### Bridge Out (lead, ~30 sec before break)

> You've seen what good looks like — frictionless starts, docs that flow from code. After the break, we'll talk about **how your team gets there**: the practices that matter, and the one change you'd make first.

## Stories & Examples (Use Sparingly)

| Story | When to use | Point |
|-------|-------------|-------|
| Standardizing shipping format at Moderna | Plenary debrief or framing | Clarity for collaborators; "contract" of what DS ships |
| mRNA design workflow → code → production | If group asks "what does reusable look like?" | 4 notebooks → reusable code; designer freed for higher-level work |
| Cryo-EM: ad hoc → routine → deployed tool | If group asks "how do you spot reusable work?" | Patterns emerge over time; invest when repetition appears |

**Do not** turn Part 1 into a Moderna case-study session. One story max unless audience pulls more.

## Attendee Output (Informal)

No worksheet required, but attendees should leave Part 1 with mental notes on:

- [ ] One artifact type their team should standardize on
- [ ] One bus-factor or clarity pain point they'd name to their team
- [ ] A picture of what "good" could look like for their team

*(Keystone change formalized in Part 2; exit reflection in Part 3.)*

## Edge Cases

| Situation | Handling |
|-----------|----------|
| "Our team is fine, no problems" | Validate — non-goal is forcing change. Ask: "What would break first if you doubled in size?" |
| "We're too regulated to build tools" | Acknowledge; Part 2 formality aside covers buy vs build in regulated contexts |
| Group dominates airtime | Support triages: "Hold that — good for plenary" or answer 1:1 |
| Demo environment fails | Switch to `examples/pyds-init-demo/`; narrate from pre-built project tree |
| Low discussion energy | Lead asks a provocative question: "Dashboards — how many of you ship them? How many maintain them?" |
| "Can we follow along now?" | Observe-along for now; repo linked at close; Part 2 is about what to adopt first |

## Dependencies

- Workshop repo with setup instructions ([Workshop Operations LLD](../workshop-ops/LLD.md))
- Discussion question bank ([Discussion Questions EARS](../workshop-ops/discussion-questions-EARS.md))
- Repo template and doc publishing demo environment pre-tested (`pyds project init`, doc site)

## Requirements

- [Demo Artifacts EARS](./demo-artifacts-EARS.md)
- [Discussion Questions EARS](../workshop-ops/discussion-questions-EARS.md)

## Related Documents

- [High-Level Design](../../high-level-design.md)
- [Part 2: Software Standardization](../part-2-software/LLD.md)
- [Workshop Operations](../workshop-ops/LLD.md)
