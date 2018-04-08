"""Scaffolding commands for creating and setting up projects."""
import click
from puppo import cli
from puppo.puppo_commands.command_functions.scaffold_functions.cli_scaffolds \
    import simple_scaffold


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
def simple(add_unittests, name):
    """Create basic CLI application.

    This function is used for creating a basic CLI application using the
    Click package.

    :param add_unittests: whether or not to create a unittests directory.
    :type add_unittests: boolean
    :param name: the name of the CLI application to create.
    :type name: string
    """
    simple_scaffold.create_scaffold(name)
