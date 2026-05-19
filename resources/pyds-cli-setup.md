# pyds-cli Setup (Part 1 Follow-Along)

Part 1 Demo 1 uses [pyds-cli](https://ericmjl.github.io/pyds-cli/) live.

**Prerequisites**: complete [`follow-along-setup.md`](follow-along-setup.md) first
(uv, pixi, git, and `pixi install` in this repo).

## Install pyds-cli with uv

```bash
uv tool install pyds-cli
pyds --version
```

The CLI command is `pyds`.

## Verify prerequisites

pyds expects `pixi`, `git`, and `uv` on your `PATH`:

```bash
pyds system status
```

## One-time configuration

```bash
pyds configure
```

You'll be prompted for name, email, and optionally your GitHub username.

## Part 1 demo command

From an empty directory where you want your follow-along project:

```bash
pyds project init --no-github
```

This scaffolds via [cookiecutter-python-project](https://github.com/ericmjl/cookiecutter-python-project):
`notebooks/`, source package, CLI stub, pre-commit hooks, pytest layout, and **pixi**
environment setup.

Then enter the new project and install its environment:

```bash
cd your-project-name
pixi install
```

## Upstream docs

- [pyds-cli documentation](https://ericmjl.github.io/pyds-cli/)
- [Creating a new project](https://ericmjl.github.io/pyds-cli/workflows/01-new-project/)

## Fallback in this repo

If live init is slow in-room, explore [`examples/pyds-init-demo/`](../examples/pyds-init-demo/):

```bash
cd examples/pyds-init-demo
pixi install
pixi run -e docs serve-docs
```
