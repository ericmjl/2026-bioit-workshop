# Part 3 Demo Artifacts — EARS

**Parent LLD**: [Part 3 LLD](./LLD.md)

## Messy Notebooks (prep staging)

**Artifact**: `examples/messy/`

Messy notebooks are **authored and versioned in the workshop materials repo**. During the Part 3 live demo, the presenter copies them into the **live pyds project** scaffolded in Part 1 (typically `notebooks/`). That copy step is part of the run of show — it shows how real analysis debt lands inside an otherwise well-structured project.

- [x] **ART-P3-MESSY-001**: The messy examples directory shall contain 2–3 Marimo notebooks.
- [x] **ART-P3-MESSY-002**: The notebooks shall contain duplicated functions with slight modifications across files (realistic, not toy one-liners).
- [x] **ART-P3-MESSY-003**: The messy notebooks shall be openable with `uvx marimo edit --sandbox --no-token` per follow-along setup (no manual Marimo install).
- [x] **ART-P3-MESSY-004**: The messy notebooks shall be copy-ready into a pyds-scaffolded project's `notebooks/` directory (no paths or imports that assume they live only at repo root).
- [x] **ART-P3-MESSY-005**: Part 3 demo materials shall document the copy command or step used to move notebooks from `examples/messy/` into the live demo project before the agent refactor.

## Clean Refactor Output

**Artifact**: `examples/clean/`

- [x] **ART-P3-CLEAN-001**: The clean examples directory shall contain a pre-built refactored output (shared module, package, or CLI) derived from the messy notebooks.
- [x] **ART-P3-CLEAN-002**: The clean output shall demonstrate extracted reusable code that an agent refactor would plausibly produce.
- [x] **ART-P3-CLEAN-003**: The clean output shall serve as the live-demo fallback if the agent refactor fails or is slow in-room.

## Architecture Improvement Skill Doc

**Artifact**: `resources/matt-pocock-architecture-skill.md`

- [x] **ART-P3-SKILL-001**: The architecture skill doc shall explain how to install or invoke Matt Pocock's codebase architecture improvement skill.
- [x] **ART-P3-SKILL-002**: The doc shall link to the YouTube explainer on "seams" and "deepen."
- [x] **ART-P3-SKILL-003**: The doc shall include a sample prompt for pointing the skill at the messy notebook collection.

## Marimo Pair Setup Doc

**Artifact**: `resources/marimo-pair-setup.md`

- [x] **ART-P3-MARIMO-001**: The Marimo Pair setup doc shall document opening notebooks with `uvx marimo edit --sandbox --no-token <path>` and Pair skill install.
- [x] **ART-P3-MARIMO-002**: The doc shall reference which notebook in the repo to use for follow-along practice.
- [x] **ART-P3-MARIMO-003**: The doc shall document installing the Marimo Pair agent skill via `npx skills add marimo-team/marimo-pair`, with `npx` provided by `pixi global install nodejs`.

## Related Documents

- [Part 3 LLD](./LLD.md)
- [Materials Repo EARS](../workshop-ops/materials-repo-EARS.md)
