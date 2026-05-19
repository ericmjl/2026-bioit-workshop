# Follow-Along Setup

Install this **before the workshop** if you want to follow along live. Observe-along
in the room is still fine — you do not need any of this installed during the session.

**Python**: 3.11+ (the workshop `pixi.toml` uses 3.12).

## Overview

| Tool | Role in this workshop |
|------|------------------------|
| **[uv](https://docs.astral.sh/uv/)** | Install CLI tools (`pyds-cli`) and run Marimo via `uvx` |
| **[pixi](https://pixi.sh)** | Project environments, global CLI tools (`nodejs` → `npx`) |
| **git** | Clone the repo; required by pyds and project templates |
| **npx** | Install Marimo Pair agent skill (`npx skills add …`); via `pixi global install nodejs` |

Part 1 scaffolds **new projects with pixi**. Part 3 notebooks open with
**`uvx marimo edit --sandbox --no-token`**. This repo's root `pixi.toml` covers
docs and tests follow-along.

---

## 1. Install git

Most macOS and Linux systems already have git. Verify:

```bash
git --version
```

---

## 2. Install uv

**macOS / Linux**

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Restart your shell, then verify:

```bash
uv --version
```

**Windows** — see [uv installation docs](https://docs.astral.sh/uv/getting-started/installation/).

---

## 3. Install pixi

**macOS / Linux**

```bash
curl -fsSL https://pixi.sh/install.sh | sh
```

Restart your shell, then verify:

```bash
pixi --version
```

**Windows** — see [pixi installation docs](https://pixi.sh/latest/#installation).

Ensure `~/.pixi/bin` is on your `PATH` (the pixi installer usually adds this).

---

## 4. Install Node.js globally (for npx)

Marimo Pair skill install uses **`npx`**. Install Node.js via [pixi global](https://pixi.sh/latest/reference/cli/pixi/global/install/):

```bash
pixi global install nodejs
npx --version
node --version
```

This exposes `node`, `npm`, `npx`, and `corepack` from conda-forge. To pin a major
version: `pixi global install "nodejs=22.*"`.

---

## 5. Clone this repo

```bash
git clone https://github.com/ericmjl/2026-bioit-workshop.git
cd 2026-bioit-workshop
```

---

## 6. Install the workshop follow-along environment

From the repo root:

```bash
pixi install
```

This provisions Python plus MkDocs and pytest for exploring materials in this
repo. Marimo notebooks use **`uvx`** (see Part 3 below) — not the pixi env.

### Handy pixi tasks

```bash
pixi run open-messy-notebook    # Part 3 — uvx marimo edit --sandbox --no-token ...
pixi run serve-workshop-docs     # Part 1 — doc publishing demo
pixi run test-clean-fallback     # Part 3 — tests on refactored fallback
```

---

## 7. Install pyds-cli (Part 1 follow-along)

pyds-cli is installed as a **global tool** via uv (not into the pixi env):

```bash
uv tool install pyds-cli
pyds --version
```

One-time configuration:

```bash
pyds configure
```

Verify pyds prerequisites (pixi, git, uv on PATH):

```bash
pyds system status
```

Part 1-specific steps: [`pyds-cli-setup.md`](pyds-cli-setup.md).

---

## 8. Verify everything

Run from the repo root:

```bash
uv --version
pixi --version
git --version
npx --version
pyds system status
uvx marimo --version
pixi run test-clean-fallback
```

If all commands succeed, you are ready to follow along.

---

## Follow-along by workshop part

### Part 1 — Foundations & tooling

| Demo | What to run |
|------|-------------|
| Project init | `pyds project init --no-github` (see [`pyds-cli-setup.md`](pyds-cli-setup.md)) |
| Docs from code | `cd examples/pyds-init-demo && pixi install && pixi run -e docs serve-docs` |
| Minimal docs demo | `pixi run serve-workshop-docs` (from repo root) |

If live init is slow in-room, explore the pre-built fallback:
`examples/pyds-init-demo/`.

### Part 2 — Software standardization

Discussion and keystone worksheet — no extra setup. Print or open
[`keystone-worksheet.md`](keystone-worksheet.md).

### Part 3 — Agents & automation

| Demo | What to run |
|------|-------------|
| Messy notebooks | `uvx marimo edit --sandbox --no-token examples/messy/screen_hit_qc.py` (or `pixi run open-messy-notebook`). After Part 1, copy into your pyds project and use `notebooks/screen_hit_qc.py` in the path. |
| Architecture skill | [`matt-pocock-architecture-skill.md`](matt-pocock-architecture-skill.md) |
| Marimo Pair | [`marimo-pair-setup.md`](marimo-pair-setup.md) — `npx skills add marimo-team/marimo-pair` |
| Clean fallback | `pixi run test-clean-fallback` or explore `examples/clean/` |

---

## Optional: coding agent

Part 3 demos assume a coding agent (Cursor, Claude Code, etc.) with Matt Pocock's
architecture improvement skill. Not required for Parts 1–2.

- Skill setup: [`matt-pocock-architecture-skill.md`](matt-pocock-architecture-skill.md)

---

## Troubleshooting

**`pyds` not found after `uv tool install`** — ensure `~/.local/bin` (or uv's tool
bin directory) is on your `PATH`. Run `uv tool dir` to find the install location.

**`pixi install` fails on your platform** — check `platforms` in the root
`pixi.toml`. Open an issue on the repo if your platform is missing.

**`npx` not found after `pixi global install nodejs`** — ensure `~/.pixi/bin` is on
your `PATH`. Run `pixi global list` and confirm the `nodejs` environment exposes
`npx`.

**Marimo browser does not open** — copy the URL from the terminal into your browser.

---

## Related guides

- [`pyds-cli-setup.md`](pyds-cli-setup.md) — Part 1 project init details
- [`marimo-pair-setup.md`](marimo-pair-setup.md) — Part 3 Marimo Pair
- [Data Science Bootstrap Notes](https://ericmjl.github.io/data-science-bootstrap-notes/) — depth reading
