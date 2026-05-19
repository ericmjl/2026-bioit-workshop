"""CLI stub scaffolded by pyds project init."""

import typer

app = typer.Typer()


@app.command()
def hello() -> None:
    """Echo the project name."""
    typer.echo("This project's name is BioIT Workshop Demo")


@app.command()
def describe() -> None:
    """Describe the project."""
    typer.echo("Representative pyds project init output for BioIT World 2026.")


if __name__ == "__main__":
    app()
