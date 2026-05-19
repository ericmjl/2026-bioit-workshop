# Marimo Pair Setup (Part 3 Follow-Along)

Part 3 Demo 2 shows **Marimo Pair** — an agent working inside a running Marimo
notebook kernel.

**Prerequisites**: complete [`follow-along-setup.md`](follow-along-setup.md) —
especially [uv](https://docs.astral.sh/uv/) and **`pixi global install nodejs`**
(for `npx`).

## Install npx (pixi global)

Marimo Pair's agent skill installer uses **`npx`**. Install Node.js globally with
pixi ([docs](https://pixi.sh/latest/reference/cli/pixi/global/install/)):

```bash
pixi global install nodejs
npx --version
```

This exposes `node`, `npm`, `npx`, and `corepack`. Ensure `~/.pixi/bin` is on
your `PATH`.

## Open a notebook (workshop command)

From the materials repo root:

```bash
uvx marimo edit --sandbox --no-token examples/messy/screen_hit_qc.py
```

Inside a pyds project after copying notebooks into `notebooks/`:

```bash
uvx marimo edit --sandbox --no-token notebooks/screen_hit_qc.py
```

Or use the pixi task wrapper (same command under the hood):

```bash
pixi run open-messy-notebook
```

**Flags**

- `--sandbox` — Marimo manages an isolated environment for notebook dependencies
  (pandas, numpy, etc.)
- `--no-token` — server is discoverable to Marimo Pair tooling

If your setup uses a token instead, set `MARIMO_TOKEN` before invoking Pair
scripts.

## Install the Marimo Pair skill

With a notebook running (`--no-token`), install the skill for your coding agent
([Agent Skills](https://agentskills.io) standard):

```bash
npx skills add marimo-team/marimo-pair

# upgrade later
npx skills upgrade marimo-team/marimo-pair
```

**Without npx** — if you have uv but not Node on PATH:

```bash
uvx deno -A npm:skills add marimo-team/marimo-pair
```

Projects scaffolded with `pyds project init` may already include the skill under
`.agents/skills/marimo-pair/`. Otherwise copy from the
[cookiecutter-python-project template](https://github.com/ericmjl/cookiecutter-python-project)
or use `npx skills add` above.

## What to try

Natural-language requests while Pair is connected:

- "Add a cell that plots normalized signal by well."
- "Refactor the QC step to use the shared assay_helpers module."
- "Explain what remove_outliers is doing in plain language."

## Workshop demo notebook

During the session, the presenter uses a notebook in the **live pyds project**
from Part 1 (often post-refactor from Demo 1). For follow-along after the
workshop, start with any notebook in [`examples/messy/`](../examples/messy/).

## Fallback in-room

If Marimo Pair is slow or unavailable, the presenter walks through a notebook
that was prepared beforehand — no screen recording required.
