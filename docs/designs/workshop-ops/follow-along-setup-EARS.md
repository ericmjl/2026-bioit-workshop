# Follow-Along Setup — EARS

**Parent LLD**: [Workshop Operations LLD](./LLD.md)  
**Artifact**: `resources/follow-along-setup.md` and root `pixi.toml`

## Setup Guide

**Artifact**: `resources/follow-along-setup.md`

- [x] **ART-SETUP-001**: The follow-along setup guide shall document installing [uv](https://docs.astral.sh/uv/) as the primary Python tool installer.
- [x] **ART-SETUP-002**: The follow-along setup guide shall document installing [pixi](https://pixi.sh) as the primary project environment manager.
- [x] **ART-SETUP-003**: The setup guide shall list git as a prerequisite and document cloning the materials repo.
- [x] **ART-SETUP-004**: The setup guide shall document `pixi install` at the repo root to provision the workshop follow-along environment.
- [x] **ART-SETUP-005**: The setup guide shall include a verification section (commands to confirm uv, pixi, and the workshop environment work).
- [x] **ART-SETUP-006**: The setup guide shall map setup steps to workshop parts (Part 1 pyds, Part 1 docs, Part 3 notebooks/agents).
- [x] **ART-SETUP-007**: The setup guide shall state that observe-along is sufficient in-room but follow-along is supported.
- [x] **ART-SETUP-008**: The setup guide shall document installing Node.js globally via pixi (`pixi global install nodejs`) so `npx` is available for Marimo Pair skill install.
- [x] **ART-SETUP-009**: The verification section shall include `npx --version` (or equivalent) after pixi global Node.js install.

## Workshop Pixi Environment

**Artifact**: root `pixi.toml`

- [x] **ART-SETUP-010**: The repo root shall include a `pixi.toml` for participant follow-along (doc demo, clean-example tests); Marimo via `uvx`.
- [x] **ART-SETUP-011**: The root `pixi.toml` shall expose named tasks for common follow-along actions; the messy-notebook task shall use `uvx marimo edit --sandbox --no-token`.

## README Integration

- [x] **ART-SETUP-020**: The top-level README shall include a **Follow-along setup** section summarizing uv + pixi install and linking to `resources/follow-along-setup.md`.
- [x] **ART-SETUP-021**: The README shall list the quick-start commands (`pixi global install nodejs`, `pixi install`, verification) before the workshop arc table.

## Related Documents

- [Workshop Operations LLD](./LLD.md)
- [Materials Repo EARS](./materials-repo-EARS.md)
- [Part 1 Demo Artifacts](../part-1-foundations/demo-artifacts-EARS.md)
