# Discussion Questions

Facilitator reference for Parts 1 and 2. Demo step-by-step scripts live in the
Part 1 and Part 3 demo artifact specs — not here.

---

## Part 1: Foundations & Tooling

### Framing (lead, ~5 min)

> This session is for **data science team leads**. We're building toward clarity
> on what your team ships and what good could look like. Turn to your neighbors
> and discuss your **team's** work — not personal side projects.

### Block A: Team Work Inventory (~15 min)

**Setup script** (read aloud):

> Inventory what your team actually delivers day-to-day. Don't solve problems
> yet — just name the outputs.

**Prompts**

1. What does your team produce in a typical month? List concrete outputs.
2. Are those outputs consistent across team members, or does everyone ship something different?
3. If a collaborator asked "what does your data science team deliver?", could every member give the same answer?
4. What fraction of work feels like a one-off analysis vs. something reused?

**Facilitator notes**

- Groups of 3–4 (neighbor seating).
- If discussion runs long at 28 minutes, cut plenary shares — do not skip demos.
- **Edge case — "Our team is fine"**: Validate, then ask: "What would break first if you doubled in size?"
- **Low energy**: "How many of you ship dashboards? How many maintain them?"

### Block B: Bus Factor & Onboarding (~10 min)

**Prompts**

1. If your most specialized team member left tomorrow, how long until someone else could continue their work?
2. How easy is it for team members to onboard onto each other's repos/notebooks?
3. Do you see silos — individuals working in bespoke ways that others can't follow?
4. Is your team growing? Does that change the urgency?

**Bridge to demos** (~1 min):

> You've surfaced the gaps — inconsistency, bus factor, onboarding pain. Before
> we talk about how to get there, let me show you what it looks like when a
> team *has* its act together. This is the destination, not the tutorial.

### Bridge out (before break, ~30 sec)

> You've seen what good looks like — frictionless starts, docs that flow from
> code. After the break, we'll talk about **how your team gets there**: the
> practices that matter, and the one change you'd make first.

---

## Part 2: Software Standardization

### Bridge in (~2 min)

> Before the break, you saw what good looks like — a team where starting a
> project is frictionless and docs flow from code. That was the **destination**.
> This segment is the **road**: the practices your team would need to get there,
> and the one change you'd make first.

### Block A: Docs / Refactor / Test (~10 min)

**Prompts**

1. Does your team write docs? Where do they live — repo, wiki, nowhere?
2. When do you refactor vs ship and move on?
3. What testing exists today — none, manual, automated, CI?
4. What would your team push back on if you introduced any of these?

**Facilitation note**

> Given what your team ships today, which of these is the biggest gap?

**Bridge to mini-lecture**:

> You don't need perfection. You need enough structure that the next person —
> or an agent — can follow the pattern. Here's what that looks like in practice.

### Facilitator notes (Part 2 edge cases)

- **"Testing is overkill for notebooks"**: Agree for one-offs; draw the line at
  "reused more than twice."
- **"We can't build — IT blocks us"**: Keystone might be process or buy, not build.
- **"We already do all of this"**: Keystone might be standardizing *what* you
  ship (Part 1), not practices.
- If Part 1 ran long: cut optional plenary share; **do not** cut the keystone exercise.
