# Part 1 Demo Artifacts — EARS

**Parent LLD**: [Part 1 LLD](./LLD.md)

## pyds-cli Setup Guide

**Artifact**: `resources/pyds-cli-setup.md`

- [ ] **ART-P1-PYDS-001**: The setup guide shall document installing pyds-cli (`pip install pyds-cli`; CLI command is `pyds`).
- [ ] **ART-P1-PYDS-002**: The setup guide shall list prerequisites: `pixi`, `git`, and `uv` on PATH (see `pyds system status`).
- [ ] **ART-P1-PYDS-003**: The setup guide shall document one-time `pyds configure` (name, email, optional GitHub username).
- [ ] **ART-P1-PYDS-004**: The setup guide shall document the Part 1 demo command: `pyds project init --no-github`.
- [ ] **ART-P1-PYDS-005**: The setup guide shall link to upstream docs: [pyds-cli](https://ericmjl.github.io/pyds-cli/) and [Creating a new project](https://ericmjl.github.io/pyds-cli/workflows/01-new-project/).

## pyds-init Demo Fallback

**Artifact**: `examples/pyds-init-demo/`

- [ ] **ART-P1-PYDS-010**: The fallback directory shall contain a pre-built project produced by `pyds project init` (representative output of the live demo).
- [ ] **ART-P1-PYDS-011**: The fallback project shall illustrate what `pyds project init` encodes via the [cookiecutter-python-project](https://github.com/ericmjl/cookiecutter-python-project) template: `notebooks/`, a named source package, CLI stub, pre-commit hooks, and pixi-based environment setup.
- [ ] **ART-P1-PYDS-012**: Presenters shall use this directory if live `pyds project init` fails or runs too slowly in-room.

## Doc Publishing Demo

**Artifact**: `demos/doc-publishing/`

- [ ] **ART-P1-DOCS-001**: The doc publishing demo shall include a minimal MkDocs, Sphinx, or GitHub Pages configuration that builds from repo Markdown.
- [ ] **ART-P1-DOCS-002**: The demo shall include at least one sample doc page beyond the README.
- [ ] **ART-P1-DOCS-003**: Where a live publish step is used in-room, a pre-published URL or local build output shall exist as fallback (no screen recording).
- [ ] **ART-P1-DOCS-004**: Where possible, the doc publishing demo shall use a project scaffolded with pyds-cli (e.g., `examples/pyds-init-demo/`) to show docs flowing from a real project layout.

## Related Documents

- [Part 1 LLD](./LLD.md)
- [Materials Repo EARS](../workshop-ops/materials-repo-EARS.md)
