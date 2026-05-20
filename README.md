# BioIT World 2026 — Standardizing Data Science Team Practices

Workshop materials for **BioIT World 2026** (Boston).

**In the room:** observe-along is enough — you do not need anything installed during the session.

## Optional follow-along setup

Install these **before the workshop** only if you want to run demos on your own machine.

**uv** (macOS / Linux):

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**pixi** (macOS / Linux):

```bash
curl -fsSL https://pixi.sh/install.sh | sh
```

Restart your shell after each installer, then verify with `uv --version` and `pixi --version`.
Windows: see the [uv](https://docs.astral.sh/uv/getting-started/installation/) and
[pixi](https://pixi.sh/latest/installation/) installation docs.

**npm** (via pixi global — installs Node.js and exposes `npm`, `npx`, and `node`):

```bash
pixi global install nodejs
npm --version
```

## Workshop outline

**~2h 15m content + 15m break** (3-hour slot). Slide-less, discussion-first, observe-along demos.

### Part 1 — Foundations & tooling (~45 min)

Small-group discussion: what your team ships, bus factor, onboarding friction. Live demos
show the destination — frictionless project start and docs that flow from the repo — not a
hands-on install tutorial.

### Break (15 min)

### Part 2 — Software standardization (~45 min)

Discussion and mini-lecture on documentation, refactoring, and testing — the practices that
get you to the Part 1 destination. Keystone exercise: one high-pain, low-effort change to
propose to your team on Monday.

### Part 3 — Agents & automation (~45 min)

Why standards still matter in the agent age. Live demos: agent-assisted refactor of messy
notebooks and Marimo Pair. Exit reflection: one artifact, one keystone change, one tool to explore.

## Depth reading

- [Data Science Bootstrap Notes](https://ericmjl.github.io/data-science-bootstrap-notes/) —
  companion ebook for practices covered in the workshop.
- [Two years of docathons](https://ericmjl.github.io/blog/2024/6/30/two-years-of-docathons-insights-and-lessons-learned/) —
  how to run a lightweight quarterly docathon so documentation actually happens on a team.
