# BioIT World 2026 — Standardizing Data Science Team Practices

Workshop materials for **BioIT World 2026** (Boston).

**In the room**: observe-along is enough — you do not need anything installed during
the session. **Follow-along** is supported if you want to run demos on your machine.

## Follow-along setup (uv + pixi)

Install **[uv](https://docs.astral.sh/uv/)** and **[pixi](https://pixi.sh)** before
the workshop. Full step-by-step guide:
[`resources/follow-along-setup.md`](resources/follow-along-setup.md).

**Quick start** (after installing uv and pixi):

```bash
pixi global install nodejs   # provides npx (Marimo Pair skill install)
git clone https://github.com/ericmjl/2026-bioit-workshop.git
cd 2026-bioit-workshop
pixi install
uv tool install pyds-cli
pyds configure
pyds system status
npx --version
```

### Try it from this repo

```bash
pixi run serve-workshop-docs      # Part 1 — MkDocs demo
pixi run open-messy-notebook     # Part 3 — uvx marimo edit --sandbox --no-token ...
pixi run test-clean-fallback      # Part 3 — refactored package tests
```

## Workshop arc

| Part | Topic | Follow-along |
|------|-------|--------------|
| 1 | Foundations & tooling | [`pyds-cli-setup.md`](resources/pyds-cli-setup.md), [`examples/pyds-init-demo/`](examples/pyds-init-demo/) |
| 2 | Software standardization | [`keystone-worksheet.md`](resources/keystone-worksheet.md) |
| 3 | Agents & automation | [`examples/messy/`](examples/messy/), [`matt-pocock-architecture-skill.md`](resources/matt-pocock-architecture-skill.md) |

Facilitator prompts: [`discussion-questions.md`](resources/discussion-questions.md)

**Presenters:** chronological runbook at [`resources/facilitator-runbook.md`](resources/facilitator-runbook.md).

## Part-specific guides

- **Environment (start here)**: [`follow-along-setup.md`](resources/follow-along-setup.md)
- **Part 1 — pyds project init**: [`pyds-cli-setup.md`](resources/pyds-cli-setup.md)
- **Part 1 — doc publishing**: [`demos/doc-publishing/`](demos/doc-publishing/) or [`examples/pyds-init-demo/`](examples/pyds-init-demo/)
- **Part 3 — coding agents**: [`matt-pocock-architecture-skill.md`](resources/matt-pocock-architecture-skill.md)
- **Part 3 — Marimo Pair**: [`marimo-pair-setup.md`](resources/marimo-pair-setup.md)

## Repo layout

```
pixi.toml               Workshop follow-along environment (uv + pixi)
examples/
  messy/                Part 3 prep staging (copy into live pyds project)
  clean/                Part 3 refactor fallback
  pyds-init-demo/       Part 1 pyds init fallback
demos/
  doc-publishing/       Part 1 docs demo (minimal MkDocs)
resources/              Setup guides, worksheets, discussion prompts
docs/                   Workshop design documents (HLD, LLDs, EARS)
```

## Depth reading

[Data Science Bootstrap Notes](https://ericmjl.github.io/data-science-bootstrap-notes/) —
companion ebook for practices covered in Parts 1–3.

## Design docs

Workshop structure and artifact specs live under [`docs/`](docs/).
