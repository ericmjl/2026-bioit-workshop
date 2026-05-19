# Facilitator Runbook

**BioIT World 2026** — one document to lead from in the room.

Audience: **data science team leads**. Mode: discussion-first, observe-along demos.
Repo: https://github.com/ericmjl/2026-bioit-workshop

**Default roles** (swap at break):

| Segment | Lead | Support |
|---------|------|---------|
| Part 1 | Eric | Jackie |
| Part 2 | Jackie | Eric |
| Part 3 | Eric | Jackie |

Attendee handouts: [`keystone-worksheet.md`](keystone-worksheet.md), [`exit-reflection.md`](exit-reflection.md).
Expanded discussion prompts: [`discussion-questions.md`](discussion-questions.md).

---

## Support playbook

**During discussion:** circulate, listen for plenary-worthy comments, help stuck groups
(repeat the prompt), answer 1:1 without derailing.

**Mic routing:** triage → repeat question for back row → or brief offline answer.

**During demos:** watch lead's screen for errors; have fallback paths ready (see below).

**Popcorn:** either presenter may add an example — one voice at a time.

**Timeboxing:** if discussion runs long, cut plenary shares before demos (Part 1) or
optional plenary (Part 2). Do not cut Part 1 demos, Part 2 keystone, or Part 3 exit reflection.

---

## Part 1: Foundations & Tooling

**Goal:** inventory what teams ship; show what good looks like (not how to install).

### Framing (lead)

**Say:**

> This session is for **data science team leads**. We're building toward clarity on
> what your team ships and what good could look like. Turn to your neighbors and
> discuss your **team's** work — not personal side projects.

### Discussion: team inventory (lead facilitates)

**Say (setup):**

> Inventory what your team actually delivers day-to-day. Don't solve problems yet —
> just name the outputs.

**Prompts** (groups of 3–4):

1. What does your team produce in a typical month?
2. Are outputs consistent across members?
3. Could every member answer "what does DS deliver?" the same way?
4. What fraction is one-off vs reused?

**Support:** listen for plenary candidates.

### Discussion: bus factor & onboarding (lead facilitates)

**Prompts:**

1. If your most specialized member left tomorrow, how long until someone else could continue?
2. How easy is onboarding onto each other's repos/notebooks?
3. Silos — bespoke ways others can't follow?
4. Team growing — does that change urgency?

### Plenary debrief (support runs mic)

2–3 group shares (or 1 if time is tight). Optional story (one max): standardizing
shipping format — clarity for collaborators.

**Edge cases:**

- *"Our team is fine"* → "What would break first if you doubled in size?"
- *Low energy* → "How many ship dashboards? How many maintain them?"

### Bridge to demos (lead)

**Say:**

> You've surfaced gaps — inconsistency, bus factor, onboarding pain. Before we talk
> about how to get there, let me show you what it looks like when a team *has* its
> act together. This is the **destination**, not the tutorial.

### Demo 1: frictionless project start (lead)

**Show:** `pyds project init --no-github` (or narrate from `examples/pyds-init-demo/`).

**Say (narration):**

> On a team that has its act together, the first commit is already aligned with team
> standards — `notebooks/`, package, CLI stub, tests, pixi, pre-commit. No folder-structure
> debate on day one.

**Highlight:** cookiecutter-python-project template — what pyds encodes.

**Fallback:** `examples/pyds-init-demo/` if live init fails or is slow.

### Demo 2: docs from code (lead)

**Show:** MkDocs serve on pyds project (or `pixi run serve-workshop-docs` / pre-built
`demos/doc-publishing/site/`). Edit a doc page → refresh browser.

**Say:**

> When docs live in the repo, they're always current. Collaborators — and later,
> agents — can find what they need.

### Bridge out + break (lead)

**Say:**

> You've seen what good looks like — frictionless starts, docs that flow from code.
> After the break, we'll talk about **how your team gets there**: the practices that
> matter, and the one change you'd make first.

**Swap lead/support** if planned. Keep live pyds project open for Part 3.

---

## Part 2: Software Standardization

**Goal:** practices (doc, refactor, test) + one keystone change for Monday.

### Bridge in (lead)

**Say:**

> Before the break, you saw the **destination**. This segment is the **road**: the
> practices your team would need to get there, and the one change you'd make first.

### Discussion: docs / refactor / test (lead facilitates)

**Prompts:**

1. Does your team write docs? Repo, wiki, nowhere?
2. When do you refactor vs ship and move on?
3. What testing exists — none, manual, automated, CI?
4. What would your team push back on?

**Say:**

> Given what your team ships today, which of these is the biggest gap?

**Bridge to lecture:**

> You don't need perfection. You need enough structure that the next person — or an
> agent — can follow the pattern.

### Mini-lecture: doc, refactor, test (either presenter)

**Doc:** what the next person needs — install, run, I/O, assumptions. README beats wiki.

**Refactor:** duplicate code is the signal → modules, CLI, package. Not elegance — reuse.

**Test:** smoke tests on core logic; CI on push; trust for refactors and agent changes.

*Optional:* flash a test file or doc page from workshop repo.

### Formality aside (within lecture)

| Context | Stance |
|---------|--------|
| Regulated (GxP, clinical) | **Buy** validated tools |
| Research / exploratory | **Build** for yourself |
| Shared internal platform | **Build** with docs + tests |

**Say:** "In research, build is cool — your audience is yourself. In regulated contexts, buy."

Take build-vs-buy deep dives offline.

### Keystone exercise (lead) — do not cut

**Individual** — distribute or point to [`keystone-worksheet.md`](keystone-worksheet.md):

**Say:**

> Write one change that is **high pain relief, low effort**. Examples: standardize
> artifact type, adopt `pyds project init` for new repos, migrate off conda, require
> docs in repo.

**Pair share:** compare with neighbor — would their team buy in?

**Optional plenary:** one volunteer. If quiet, offer anchor stories (pixi migration;
standardizing shipping format) from worksheet.

### Monday script (lead)

**Say:**

> "I attended a workshop on how DS teams standardize their practices. I'd like us to
> start by agreeing on one or two technical artifacts we always ship. Can we discuss
> what those should be?"

### Bridge to Part 3 (lead)

**Say:**

> You've named one practice your team could adopt. Part 3 is about the tool that
> **compresses the cost** — coding agents. Agents can help enforce those practices —
> if you have the fundamentals in place.

**Edge cases:** *"Testing overkill for notebooks"* → reused more than twice; *"IT blocks
build"* → keystone might be process or buy.

---

## Part 3: Agents & Automation

**Goal:** agents amplify standards; two demos; exit reflection.

### Bridge in + mini-lecture (lead)

**Say (Part 2 callback):**

> In Part 2 you wrote down one keystone change. Now imagine an agent that helps you
> enforce it. Agents don't replace standards; they **amplify** them.

**Core points:**

- Agents = half an employee — productive, need direction
- Without Part 2 practices, agents can't set patterns for you
- Agents follow patterns — Part 1 + Part 2 pay off here
- Agents compress build/refactor time → lowers keystone ROI threshold

**Memorable line:**

> "If you didn't do your fundamentals right — no standard structure, no good
> documentation — your agents are going to struggle."

### Pulse check (support runs mic)

Show of hands: who has access to a coding agent at work? (No shaming if few.)

### Demo 1: messy notebooks → architecture skill → refactor (lead)

**Narrative arc:** mess → skill → refactor → tie to keystone.

**Show (step by step):**

1. Open live pyds project from Part 1 (or re-init).
2. Copy: `cp examples/messy/*.py /path/to/project/notebooks/`
   - **Say:** "Even with a good scaffold, analysis debt still lands here."
3. Open 2–3 notebooks — point at duplicated `load_assay_table`, `remove_outliers`,
   `normalize_to_control` with different implementations.
4. **Say:** "Analysis treadmill — duplicated code, no shared modules."
5. Explain **seams** and **deepen** — [`matt-pocock-architecture-skill.md`](matt-pocock-architecture-skill.md).
6. Prompt agent with architecture improvement skill on `notebooks/`.
7. Walk through proposed extractions (live project if possible).
8. **Fallback if slow:** `examples/clean/` — narrate intended refactor.
9. **Say:** "Part 2 said refactor when you duplicate — here's an agent doing that work."

### Demo 2: Marimo Pair (lead)

**Show:** `uvx marimo edit --sandbox --no-token notebooks/screen_hit_qc.py` + Pair session.

Natural-language actions: add cell, refactor, explain. Contrast with copy-paste to ChatGPT.

**Fallback:** shorten or skip; walk prepared notebook. Point to
[`marimo-pair-setup.md`](marimo-pair-setup.md).

### Exit reflection (lead)

**Say** — individual, paper or notes app ([`exit-reflection.md`](exit-reflection.md)):

1. One **technical artifact** my team should standardize on: ___
2. One **keystone change** I'll propose next week: ___
3. One **tool** I'll explore: ___

### Close (lead)

- Repo URL: https://github.com/ericmjl/2026-bioit-workshop
- Bootstrap ebook: https://ericmjl.github.io/data-science-bootstrap-notes/
- **Say:** "If nothing is broken, don't fix it. If clarity is missing, start with what you ship."

Optional buffer for Q&A if the slot allows.

---

## Fallback cheat sheet

| If this fails… | Do this |
|----------------|---------|
| `pyds project init` | `examples/pyds-init-demo/` |
| Doc publish live | `demos/doc-publishing/site/` or pyds-init `build-docs` |
| Agent refactor slow | `examples/clean/` + narrate |
| Marimo Pair slow | Shorten or skip; marimo-pair-setup for later |
| Discussion overrun Part 1 | Cut plenary; keep demos |
| Discussion overrun Part 2 | Cut optional plenary; keep keystone |
| Part 3 running long | Cut Marimo Pair; keep exit reflection |

---

## Presenter prep (day before)

- [ ] `pyds configure`; `pyds system status`; init tested
- [ ] Doc demo works; fallback site opens
- [ ] Copy `examples/messy/` → live project rehearsed
- [ ] Architecture skill + prompt ready; `examples/clean/` verified
- [ ] Marimo Pair + `pixi global install nodejs` / `npx --version`
- [ ] Terminal font readable from back row; HDMI tested
- [ ] Confirm role swap with co-presenter

---

## Related documents

- [`docs/designs/workshop-ops/LLD.md`](../docs/designs/workshop-ops/LLD.md) — dry-run checklist, repo layout
- Part LLDs: [`part-1`](../docs/designs/part-1-foundations/LLD.md), [`part-2`](../docs/designs/part-2-software/LLD.md), [`part-3`](../docs/designs/part-3-agents/LLD.md)
