"""Optional CLI stub — plausible output from an agent refactor."""

import typer

app = typer.Typer(help="QC utilities for assay tables.")


@app.command()
def version() -> None:
    """Print package version."""
    typer.echo("assay-helpers 0.1.0")


if __name__ == "__main__":
    app()
