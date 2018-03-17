"""Utility commands."""
import click

from pupper import cli
from pupper.decorator_functions.display_decorators import command_handler
from pupper.pupper_commands.command_functions.clean_functions import \
    clean_directory
from tqdm import tqdm


@cli.command()
@click.argument('root_directories', nargs=-1)
@command_handler('clean directories')
def clean(root_directories):
    """Remove all cached files and directories.

    This command is used for deleting all of the '__pycache__' directories and
    '.pyc' files. Useful if you're getting errors do to with a mismatch between
    the python file and it's cached counterpart.

    :argument: root_directories -- the directories to search for '__pycache__'
                                   directories and '.pyc' files and remove.
    """
    for root_directory in tqdm(root_directories, desc="Directories cleaned"):
        clean_directory(root_directory)
