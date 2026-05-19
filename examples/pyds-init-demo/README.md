# BioIT Workshop Demo

Representative output of `pyds project init --no-github` — used as the Part 1
fallback if live scaffolding fails or runs too slowly in-room.

Scaffolded from the [cookiecutter-python-project](https://github.com/ericmjl/cookiecutter-python-project)
template that pyds-cli wraps.

## Layout (what pyds encodes)

```
bioit-workshop-demo/
├── bioit_workshop_demo/   # source package + CLI stub
├── notebooks/             # Marimo / analysis notebooks
├── docs/                  # MkDocs source (Demo 2)
├── tests/                 # pytest layout
├── pixi.toml              # pixi environment
├── mkdocs.yaml            # doc publishing config
└── .pre-commit-config.yaml
```

## Get started

```bash
cd examples/pyds-init-demo
pixi install
pixi run -e docs serve-docs   # doc publishing demo
pixi run test                 # pytest
bioit-workshop-demo hello     # CLI stub (after pixi install)
```

## Part 3 connection

Copy messy notebooks from [`../messy/`](../messy/) into `notebooks/` during the
Part 3 live demo.
