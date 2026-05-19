"""Tests for bioit_workshop_demo.cli."""

from typer.testing import CliRunner

from bioit_workshop_demo.cli import app

runner = CliRunner()


def test_hello() -> None:
    result = runner.invoke(app, ["hello"])
    assert result.exit_code == 0
    assert "BioIT Workshop Demo" in result.stdout


def test_describe() -> None:
    result = runner.invoke(app, ["describe"])
    assert result.exit_code == 0
    assert "BioIT World 2026" in result.stdout
