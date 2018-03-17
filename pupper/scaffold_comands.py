"""Scaffolding commands for creating and setting up projects."""
import click
from pupper import cli


@cli.group()
def scaffold():
    """Create and setup projects.

    This command group is used for creating and setting up python application
    and projects. It can even be used for creating Click CLI applications like
    this one!
    """
    pass
