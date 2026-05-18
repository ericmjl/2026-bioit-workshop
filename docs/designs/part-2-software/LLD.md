# Part 2: Software Standardization — Low-Level Design

**Created**: 2026-05-18
**Duration**: ~45 minutes
**Default lead**: TBD (good candidate for Jackie — doc/refactor/test)
**HLD Link**: [High-Level Design](../../high-level-design.md)

## Overview

Part 2 is **the road to getting there**. Part 1 showed the destination — frictionless project starts, docs from code. Now attendees discuss the **practices** that produce that end state: documentation, refactoring, and testing. A short formality aside covers when buy makes sense (regulated) vs build (research). The section closes with a **keystone exercise**: one low-effort, high-pain change to propose to their team on Monday.

This section balances discussion (~45%) and a focused mini-lecture (~15–20 min).

## Section Goals

By the end of Part 2, attendees should be able to:

1. Understand which **practices** (docs, refactor, test) matter most for their team's context
2. Articulate **what** to document and **when** to start — distinct from Part 1's "docs flow from repo" inspiration
3. Name one **keystone change** they'd propose to their team (high pain, low effort)
4. Draft the **Monday conversation** they'd have with their team about standardizing shipping

## Run of Show

| Time | Block | Mode | Lead |
|------|-------|------|------|
| 0:00–0:05 | Bridge from Part 1: destination → road | Brief monologue | Lead |
| 0:05–0:15 | Discussion: docs / refactor / test — what's your experience? | Discussion | Lead facilitates |
| 0:15–0:25 | Mini-lecture: how to doc, refactor, test | Mini-lecture | Either presenter |
| 0:25–0:30 | Formality aside: when buy vs build (2 min within lecture) | Mini-lecture | Lead |
| 0:30–0:38 | Keystone exercise (individual → pair share) | Exercise | Lead |
| 0:38–0:43 | Optional plenary share + Monday conversation script | Discussion | Lead |
| 0:43–0:45 | Bridge to Part 3: agents compress the cost | Brief monologue | Lead |

## Bridge In (lead, ~2 min)

> Before the break, you saw what good looks like — a team where starting a project is frictionless and docs flow from code. That was the **destination**. This segment is the **road**: the practices your team would need to get there, and the one change you'd make first.

## Discussion Design

### Block A: Docs / Refactor / Test Experience (~10 min)

**Prompt set**:

1. Does your team write docs? Where do they live — repo, wiki, nowhere?
2. When do you refactor vs ship and move on?
3. What testing exists today — none, manual, automated, CI?
4. What would your team push back on if you introduced any of these?

**Facilitation notes**:

- Draw on Part 1 inventory: "Given what your team ships today, which of these is the biggest gap?"
- Support captures 1–2 plenary examples before mini-lecture
- Don't preach perfection — "enough structure that the next person can follow"

**Bridge to mini-lecture**:

> You don't need perfection. You need enough structure that the next person — or an agent — can follow the pattern. Here's what that looks like in practice.

## Mini-Lecture: How to Doc, Refactor, Test (~10 min)

Either presenter leads. **Differentiation from Part 1**: Part 1 showed doc publishing as inspiration; this segment covers **what to write** and **when to start**.

### Documentation

- Doc what the *next person* needs: install, run, inputs/outputs, assumptions
- Start now — even a README beats a wiki page nobody updates
- Docs in the repo (Part 1 demo) only help if you actually write them

### Refactoring

- Refactor when you **duplicate code** — that's the signal
- Goal: extract reusable functions/modules; CLI and package are the destination
- Not "refactor for elegance" — refactor for reuse and onboarding

### Testing

- Start with smoke tests on core logic (not 100% coverage)
- CI runs tests on every push — template repos (Part 1 demo) should include this
- Tests are how you trust refactors and agent-generated changes

**Optional live touch**: Show a test file or doc page from workshop repo — not a full demo.

## Formality Aside (~2 min, within mini-lecture)

Brief context-setting — not a standalone discussion block:

| Context | Default stance | One-line rationale |
|---------|----------------|-------------------|
| Regulated (GxP, clinical, prod) | **Buy** validated tools | Don't burden innovators with compliance |
| Research / exploratory | **Build** for yourself | Cheap, fast; agents compress build time |
| Shared internal platform | **Build** with docs + tests | Others depend on it; bus factor matters |

**Key line**: "In research, build is cool because your audience is yourself and your immediate team. In regulated contexts, buy so you're not reinventing validation."

No extended build-vs-buy debate — if someone wants to go deep, take it offline.

## Keystone Exercise (~8 min)

**Individual** (3 min):

> Write down one change your team could make that is **high pain relief, low effort**. Examples: standardize on one artifact type, adopt `pyds project init` for new repos, migrate off conda, require docs in repo.

**Pair share** (3 min): Compare with neighbor. Would their team buy in?

**Optional plenary** (2 min): One volunteer shares.

**Anchor stories** (lead may offer if room is quiet):

- **Pixi migration**: High pain (conda env hell), staged effort, unlocked multi-version research
- **Standardizing shipping format**: Clarity for collaborators; contract of what DS delivers

## Monday Conversation Script

Each attendee leaves Part 2 with a rough script for their team:

> "I attended a workshop on how DS teams standardize their practices. I'd like us to start by agreeing on one or two technical artifacts we always ship. Can we discuss what those should be?"

## Bridge Out (lead, ~30 sec)

> You've named one practice your team could adopt. Part 3 is about the tool that **compresses the cost** of all of this — coding agents. The practices you just identified? Agents can help enforce them — if you have the fundamentals in place.

## Attendee Output

Each attendee leaves Part 2 with:

- [ ] One keystone change written down
- [ ] A rough script for the Monday team conversation

## Edge Cases

| Situation | Handling |
|-----------|----------|
| "We can't build — IT blocks us" | Formality aside: keystone might be process or buy, not build |
| "Testing is overkill for notebooks" | Agree for one-offs; draw line at "reused more than twice" |
| Pushback on doc/refactor/test segment | Keep to 10 min; point to bootstrap ebook for depth |
| Part 1 ran long; Part 2 starts late | Cut optional plenary; keep keystone exercise |
| "We already do all of this" | Great — keystone might be standardizing *what* you ship (Part 1), not practices |

## Dependencies

- Part 1 complete (attendees have inventory, pain points, and a picture of "good")
- Workshop repo may include example test/doc files
- Bootstrap ebook chapters on testing, docs (reference, not required reading in room)

## Requirements

- [Keystone Worksheet EARS](./keystone-worksheet-EARS.md)
- [Discussion Questions EARS](../workshop-ops/discussion-questions-EARS.md)

## Related Documents

- [High-Level Design](../../high-level-design.md)
- [Part 1: Foundations & Tooling](../part-1-foundations/LLD.md)
- [Part 3: Agents & Automation](../part-3-agents/LLD.md)
