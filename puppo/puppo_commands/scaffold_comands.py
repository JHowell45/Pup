"""Scaffolding commands for creating and setting up projects."""
import click
from puppo import cli
from puppo.puppo_commands.command_functions.scaffold_functions.cli_scaffolds import \
    simple_scaffold


@cli.group()
def scaffold():
    """Create and setup projects.

    This command group is used for creating and setting up python application
    and projects. It can even be used for creating Click CLI applications like
    this one!
    """
    pass


@scaffold.group()
def cli_applications():
    """Create a CLI application.

    This command is used for scaffolding a new CLI application using click. It
    will create the basic structure for creating a Click application.
    """
    pass


@cli_applications.command()
@click.option('-aut', '--add-unittests', is_flag=True,
              help="Add Unittests directory for project.")
@click.argument('name')
def simple(add_unittests):
    """Create basic CLI application."""
    simple_scaffold.create_scaffold()
