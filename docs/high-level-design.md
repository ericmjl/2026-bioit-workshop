# BioIT World 2026 Workshop — High-Level Design

**Created**: 2026-05-18  
**Presenters**: Eric Ma, Jackie (co-presenters; roles may swap midway)  
**Format**: Slide-less, Socratic workshop (discussion + live demos)  
**Scheduled duration**: 3 hours booked → ~2h 15m content + 15m break

## Problem Statement

Data science team leads in biotech/pharma often inherit teams without strong engineering patterns. Work drifts into an **analysis treadmill** — one-off notebooks and ad hoc deliverables — with no clarity on what the team ships or how. Without that clarity, bus factor grows, onboarding is painful, and leverage from reusable software never materializes.

This workshop gives team leads a **playbook and vocabulary** to standardize what their team ships and how they ship it — grounded in practices from the [Data Science Bootstrap](https://ericmjl.github.io/data-science-bootstrap-notes/) ebook and real patterns from Moderna.

## Goals

1. **Clarity on shipping** — Attendees leave with a working hypothesis: *what* their team ships (technical artifacts) and *where the boundaries are*.
2. **Escape the analysis treadmill** — Reframe work toward reusable outputs (packages, CLIs, APIs, published docs) that create leverage for the team and collaborators.
3. **Concrete technical patterns** — Show (not just tell) tooling that makes the right thing easy: repo init, doc publishing, CLI building, testing/docs/refactoring, agent-assisted development.
4. **Keystone adoption** — Identify one low-effort, high-pain change they can propose to their team on Monday (e.g., standardize shipping format, migrate off conda, adopt a repo template).

## Non-Goals

- **Organizational politics playbook** — We won't teach how to navigate every org's power dynamics; we share principles and stories, not a universal stakeholder map.
- **Spotting-efficiency framework** — We trust team leads to know their domain; we don't teach a formal "find reusable work" methodology.
- **Hands-on for everyone** — Demos are observe-along; coding agents and follow-along repos are optional (not everyone will have access).
- **Full-stack product development** — No databases, auth systems, or production SaaS; focus is internal research tooling.
- **Slides or slide review** — Intentionally slide-less; Socratic discussion + live demos only.
- **Convincing teams with no problems** — "If it ain't broke, don't fix it" is a valid outcome.

## Target Audience

**Primary persona: Data science team lead** (biotech/pharma industry)

- Manages a small-to-medium DS team
- Hasn't been opinionated about team deliverables or engineering standards
- May lack confidence or vocabulary to implement change
- Knows their team's work best; needs tools and patterns, not domain advice

**Secondary**: Individual contributors who influence team practices (may attend but content is lead-focused).

## Content Architecture Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                    WORKSHOP (2h 15m + 15m break)                │
├─────────────────────────────────────────────────────────────────┤
│  Part 1 (~45m)          │  Part 2 (~45m)      │  Part 3 (~45m)  │
│  Foundations &          │  Software           │  Agents &       │
│  Tooling                │  Standardization    │  Automation     │
├─────────────────────────┼─────────────────────┼─────────────────┤
│  • Small-group discuss  │  • Build vs buy     │  • Why standards│
│  • Bus factor, onboard  │  • Formality levels │    still matter │
│  • What we ship         │  • Doc/refactor/test│  • Matt Pocock  │
│  • Live demos: repo     │    (either presenter│    architecture │
│    init, doc publish    │     may lead)       │  • Marimo refactor│
│                         │                     │  • Marimo Air   │
└─────────────────────────┴─────────────────────┴─────────────────┘
         ↑                           ↑                      ↑
    Either presenter may     Either presenter may    Demo-heavy
    lead; other supports     lead; other supports    (observe-along)
    (hands-on help, mic)     (hands-on help, mic)
```

**Supporting materials** (not delivered in-room, but part of the content system):

- Git repo with follow-along setup (PyData Boston pattern)
- Example messy Marimo notebooks + cleaned refactor output
- Discussion question sets per section
- Presenter run-of-show notes

## Core Message (The Through-Line)

> **Decide what your team ships. Standardize how you ship it. Use tools and agents to compress the cost of doing so.**

| Concept | Definition | Examples |
|---------|------------|----------|
| **What you ship** | Reusable output that creates leverage | Python package, CLI on compute, API endpoint, published Confluence/docs, Slack slash command |
| **What you don't ship** | One-off analysis with no repeat path | Ad hoc notebook → email → forget |
| **Keystone change** | Small effort, high pain relief, unlocks other practices | Standardize artifact type; pixi migration; repo template |
| **When to invest** | Repeatable work → architect; one-off with high variation → don't | Bet time where ROI is visible from org knowledge |

## Key Design Decisions

### Decision 1: Discussion-first, not lecture-first

**Choice**: Heavy small-group discussion upfront; demos follow naturally from discussion prompts.

**Rationale**: Audience is team leads who know their context. Inventory and compare-notes exercises surface relevance better than slides. Matches "Socratic" intent and avoids slide overhead.

**Alternatives considered**:
- Lecture-heavy with Q&A: Faster to prep but less engagement; doesn't produce personal hypotheses.
- Fully hands-on lab: Excludes attendees without coding agents; higher TA burden.

### Decision 2: Slide-less delivery

**Choice**: No slides. Discussion questions + live demos + optional follow-along repo.

**Rationale**: Reduces prep/review burden; aligns with Eric's talk style; forces conversational flow.

### Decision 3: Observe-along demos (not mandatory hands-on)

**Choice**: One presenter demos live while the other supports the room; attendees watch. Repo available for later.

**Rationale**: Not everyone has a coding agent or identical environment. The supporting presenter helps those who follow along hands-on.

### Decision 4: Three-part arc maps to adoption journey

**Choice**: (1) Why + tooling → (2) Software practices → (3) Agents

**Rationale**: Agents are the "gateway drug" only *after* fundamentals are motivated. Part 3 explicitly answers: "Why constrain ourselves with standards when agents exist?" — because agents need patterns to follow.

### Decision 5: Flexible co-presenter roles (swap midway)

**Choice**: Eric and Jackie are co-presenters, not fixed lead + TA. Either may lead a segment (discussion, lecture, or demo) while the other supports the room — hands-on help, mic routing, question triage, popcorn contributions. They may swap roles midway through the workshop.

**Rationale**: Two-person delivery scales better in a workshop room. Flexible swapping keeps both presenters engaged, lets each lead topics they know well (e.g., doc/refactor/test), and avoids one person being relegated to support for the full three hours.

**Operational note**: Run-of-show should assign a default lead per segment, with explicit swap points (e.g., at the break).

## Success Criteria (How We Know It Worked)

Attendees can articulate (on exit or in a brief reflection):

1. One **technical artifact** their team should standardize on
2. One **keystone change** they'd propose to their team next week
3. Why **standardization helps agents** (not replaces them)
4. At least one **tool** they'd explore (repo template, doc publishing, CLI, Marimo Pair, architecture-improvement skill)

## Risks and Mitigations

| Risk | Mitigation |
|------|------------|
| Discussion runs long; demos get cut | Timebox sections; presenter run-of-show with hard stops |
| Live demo fails | Pre-recorded fallback clips; cleaned-up "after" artifacts in repo |
| Audience without agents feels excluded | Frame agents as optional accelerator; fundamentals stand alone |
| Content too Moderna-specific | Use industry-generic examples; invite attendee stories via mic |
| "My team won't adopt this" | Keystone principle + incremental adoption; don't fix what isn't broken |

## Source Material

- [Data Science Bootstrap Notes](https://ericmjl.github.io/data-science-bootstrap-notes/) (ebook)
- Transcript: `transcripts/20260518-ideas.md` (interview — audience takeaways)
- Transcript: `transcripts/20260518-1-on-1-with-jackie.md` (session structure + roles)

## Related Designs

- [Part 1 LLD](./designs/part-1-foundations/LLD.md)
- [Part 2 LLD](./designs/part-2-software/LLD.md)
- [Part 3 LLD](./designs/part-3-agents/LLD.md)
- [Workshop Operations LLD](./designs/workshop-ops/LLD.md)
