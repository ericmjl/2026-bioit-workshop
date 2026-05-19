# Doc Publishing Demo (Part 1)

Part 1 Demo 2 shows **docs from code** — documentation that lives in the repo
and rebuilds when you edit Markdown.

## Primary demo path (pyds layout)

The live demo runs against a pyds-scaffolded project:

```bash
cd examples/pyds-init-demo
pixi install
pixi run -e docs serve-docs
```

Edit `docs/getting-started.md`, save, and refresh the browser — that's the
edit → publish cycle narrated in-room.

**Pre-built fallback**: build static HTML offline:

```bash
cd examples/pyds-init-demo
pixi run -e docs build-docs
# open site/index.html
```

## Minimal standalone config (this directory)

This folder also contains a **minimal MkDocs setup** for workshops where you
want doc publishing isolated from the full pyds tree. Same pattern, smaller
surface area.

```bash
cd demos/doc-publishing
pip install mkdocs mkdocs-material
mkdocs serve
```

Pre-built fallback in this directory:

```bash
mkdocs build
# open site/index.html
```

## What to narrate

> When docs live in the repo, they're always current. Collaborators — and
> later, agents — can find what they need.
