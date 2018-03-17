"""Utility commands."""
import click
from pupper import cli

@cli.command()
@click.argument('root_directories', nargs=-1)
def clean(root_directories):
    """Remove all cached files and directories.

    This command is used for deleting all of the '__pycache__' directories and
    '.pyc' files. Useful if you're getting errors do to with a mismatch between
    the python file and it's cached counterpart.

    :argument: root_directories -- the directories to search for '__pycache__'
                                   directories and '.pyc' files and remove.
    """
    pass
