# Getting started

## Install the environment

```bash
pixi install
```

## Run the CLI stub

```bash
bioit-workshop-demo hello
bioit-workshop-demo describe
```

## Run tests

```bash
pixi run test
```

## Build docs locally

```bash
pixi run -e docs build-docs
```

The static site lands in `site/` — use this as the offline fallback if live
`mkdocs serve` is unavailable in-room.
