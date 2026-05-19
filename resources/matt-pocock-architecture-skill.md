# Architecture Improvement Skill (Matt Pocock)

Part 3 Demo 1 uses Matt Pocock's **improve-codebase-architecture** skill so a
coding agent finds **seams** and proposes **deepening** refactors — turning
shallow, duplicated notebook code into reusable modules.

## What to watch for in the demo

- **Seam** — where an interface lives; a place behaviour can change without
  editing every caller.
- **Deepen** — hide complexity behind a smaller interface (high leverage for
  callers, high locality for maintainers).
- **Deletion test** — if deleting a module just moves complexity to callers, it
  was too shallow; if complexity concentrates, the module was earning its keep.

## Install the skill

The skill ships in Matt's public skills repo:

- GitHub: [mattpocock/skills](https://github.com/mattpocock/skills)
- Skill path: `skills/engineering/improve-codebase-architecture/SKILL.md`

**Cursor / Claude Code** — copy or symlink the skill into your project's
`.agents/skills/` (or global skills directory). See your editor's skill
install docs.

**MCP (optional)** — Matt's skills are also available as an MCP server:
[skills over MCP — mattpocock/skills](https://skillsovermcp.com/connect/mattpocock/skills)

## Video explainer

Matt walks through seams, depth, and using one skill to de-slop AI-touched
codebases:

- [How To De-Slop A Codebase Ruined By AI (with one skill)](https://www.youtube.com/watch?v=3MP8D-mdheA)

Related talks on fundamentals and AI-ready codebases:

- [Your codebase is NOT ready for AI (here's how to fix it)](https://www.youtube.com/watch?v=uC44zFz7JSM)

## Sample prompt (Part 3 demo)

After copying messy notebooks into your live pyds project's `notebooks/`:

```
Use the improve-codebase-architecture skill on this project.

The notebooks/ directory has three Marimo notebooks with duplicated assay
helpers (load_assay_table, remove_outliers, normalize_to_control) — each
copy differs slightly. Find deepening opportunities: extract shared logic
into a deep module with a small interface, add tests, and update notebooks
to import from the package.
```

## Pre-built fallback

If the live agent refactor is slow in-room, narrate from
[`examples/clean/`](../examples/clean/) — output from running this skill against
the messy notebooks during prep.
