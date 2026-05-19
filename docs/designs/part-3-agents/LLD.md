# Part 3: Agents & Automation — Low-Level Design

**Created**: 2026-05-18  
**Duration**: ~45 minutes  
**Lead**: Eric · **Support**: Jackie (fixed for full workshop)  
**HLD Link**: [High-Level Design](../../high-level-design.md)

## Overview

Part 3 closes the arc: Part 1 diagnosed *what your team ships* and showed *what good looks like*; Part 2 named *the practices and one keystone change* to get there. Now: **agents amplify your standards**. Attendees learn why standardization still matters in the agent age, then watch demos where agents help enforce the practices from Part 2 — refactoring duplicated notebook code, interacting with Marimo in real time.

This section is **demo-heavy** (~70%). Observe-along only; repo contains before/after artifacts for later exploration.

## Section Goals

By the end of Part 3 (and the workshop), attendees should be able to:

1. Explain why **standards enable agents** rather than replacing them
2. Connect the **keystone change** from Part 2 to what agents could help with
3. Describe the **architecture improvement** pattern (find seams → deepen interfaces → refactor)
4. Name at least one tool to explore post-workshop (architecture skill, Marimo Pair, CLI)

## Run of Show

| Time | Block | Mode | Lead |
|------|-------|------|------|
| 0:00–0:08 | Bridge in + why standards still matter in the agent age | Mini-lecture | Lead |
| 0:08–0:10 | Brief discussion: who uses coding agents today? | Pulse check | Support runs mic |
| 0:10–0:28 | Demo: messy notebooks → architecture skill → refactor | Live demo | Lead demos |
| 0:28–0:38 | Demo: Marimo Pair interaction mode | Live demo | Lead demos |
| 0:38–0:43 | Exit reflection: one artifact, one keystone, one tool | Individual | Lead |
| 0:43–0:45 | Close: thanks, repo link, optional Q&A buffer | Monologue | Either |

## Bridge In + Mini-Lecture: Agents Amplify Your Standards (~8 min)

**Open with Part 2 callback** (lead, ~1 min):

> In Part 2 you wrote down one keystone change — one practice your team could adopt. Now imagine an agent that helps you enforce it. That's what this segment is about. Agents don't replace standards; they **amplify** them.

**Core argument**:

- Agents behave like **half an employee** — productive but need direction
- Without the practices from Part 2 — docs, structure, patterns — agents **can't set patterns for you**
- Agents are very good at **following** patterns — so Part 1's picture of "good" and Part 2's practices pay off here
- Coding agents **compress build/refactor time** — lowers the ROI threshold for the keystone change you named

**Memorable line**:

> "If you didn't do your fundamentals right — no standard structure, no good documentation — your agents are going to struggle."

**Optional 1-min discussion**: Show of hands — who has access to a coding agent at work? (Calibrates demo relevance; no shaming if few.)

## Live Demo 1: Architecture Improvement on Messy Notebooks (~18 min)

### Narrative arc

1. **Show the mess** — Marimo notebooks with duplicated functions, slightly modified copies. *This is what happens when Part 2's practices aren't in place.*
2. **Apply the skill** — Matt Pocock's codebase architecture improvement skill; agent identifies seams/interfaces to deepen
3. **Show the refactor** — Cleaned-up code in a separate directory (pre-built fallback). *This is what Part 2's refactoring practice produces.*
4. **Connect to your keystone** — "If your keystone was 'require docs in repo' or 'extract duplicated code,' an agent can help you get there faster — but only if you point it at structured work."

### Demo script (high level)

```
1. Callback to Part 1: open the live pyds project created during Demo 2 (or re-init if needed)
2. Copy messy notebooks from workshop repo `examples/messy/` into live project `notebooks/`
   — narrate: "Even with a good scaffold, analysis debt still lands here"
3. Open copied notebooks — 2–3 files with obvious duplicated functions
4. Frame: "This is the analysis treadmill from Part 1 — duplicated code, no shared modules"
5. Explain "seams" and "deepen" (30 sec — point to YouTube/resource in repo)
6. Prompt agent with architecture improvement skill against the live project's notebooks/
7. Walk through agent's proposed extractions (ideally in the live project)
8. If live refactor is slow: show `examples/clean/` fallback — pre-built refactored package
9. Tie back: "Part 2 said refactor when you duplicate — here's an agent doing that work"
10. Optional: run extracted CLI or import shared function from live or fallback project
```

### Prep requirements

- [ ] Messy notebooks authored in workshop repo `examples/messy/` with realistic duplication
- [ ] Copy-into-live-project step rehearsed (Part 1 pyds project → Part 3 notebooks/)
- [ ] Pre-run agent refactor saved in `examples/clean/` as fallback (narrate if live agent is slow)
- [ ] Architecture improvement skill installed / prompt ready
- [ ] Matt Pocock codebase architecture improvement skill
- [ ] YouTube explainer on "deepen" (link in repo README)

## Live Demo 2: Marimo Pair (~10 min)

### Purpose

Show a **different interaction mode** for notebook work — agent controlling a Marimo notebook in real time via Marimo Pair. "Taste of the future" in observe-along form; attendees can try later using `resources/marimo-pair-setup.md`.

### Demo script (high level)

```
1. Open Marimo Pair session on a notebook relevant to workshop theme
2. Show natural-language control: add cell, refactor, explain
3. Contrast with copy-paste into ChatGPT — workflow stays in the notebook
4. Point attendees to marimo-pair-setup.md for optional follow-along
```

### Prep requirements

- [ ] Marimo Pair working on presenter's machine
- [ ] Notebook pre-loaded (can be same domain as Demo 1 post-refactor)
- [ ] Fallback: skip live session and walk through a notebook that was prepared beforehand

## Exit Reflection (~5 min)

**Individual, on paper or notes app** (lead reads aloud):

1. **One technical artifact** my team should standardize on: ___
2. **One keystone change** I'll propose next week: ___
3. **One tool** I'll explore: ___

**Close** (lead):

- Repo URL for follow-along materials
- Bootstrap ebook link for depth
- "If nothing is broken on your team, don't fix it. If clarity is missing, start with what you ship."

## Edge Cases

| Situation | Handling |
|-----------|----------|
| Few attendees use agents | Frame as "coming soon" — Parts 1–2 stand alone; keystone doesn't require agents |
| Agent demo is slow | Cut to pre-built clean output; narrate what agent would do |
| Audience wants hands-on | Point to repo; support helps motivated folks after session |
| Running over time | Cut Marimo Pair to 5 min or skip; keep exit reflection |
| "Agents make standards obsolete" | Redirect to bridge-in argument: agents follow patterns, don't create them |

## Dependencies

- Part 1 complete (diagnosis + picture of good)
- Part 2 complete (practices + keystone change written down)
- Workshop repo: `examples/messy/` (prep staging), live pyds project from Part 1 (demo target), `examples/clean/` (fallback)
- Matt Pocock architecture improvement skill configured
- Marimo Pair installed and tested

## Requirements

- [Demo Artifacts EARS](./demo-artifacts-EARS.md)
- [Exit Reflection EARS](./exit-reflection-EARS.md)

## Related Documents

- [High-Level Design](../../high-level-design.md)
- [Part 1: Foundations & Tooling](../part-1-foundations/LLD.md)
- [Part 2: Software Standardization](../part-2-software/LLD.md)
- [Workshop Operations](../workshop-ops/LLD.md)
