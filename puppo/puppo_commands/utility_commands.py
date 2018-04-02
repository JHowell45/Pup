"""Utility commands."""
import click
from click import Path
from puppo import cli
from puppo.decorator_functions.display_decorators import command_handler
from puppo.puppo_commands.command_functions.utility_functions.clean import \
    clean_directory
from tqdm import tqdm


@cli.command()
@click.argument('directories', nargs=-1, required=True, type=Path(exists=True))
@click.option('-v', '--verbose', is_flag=True,
              help="Display additional information.")
@command_handler('clean')
def clean(directories, verbose):
    """Remove all cached files and directories.

    This command is used for deleting all of the '__pycache__' directories and
    '.pyc' files. Useful if you're getting errors do to with a mismatch between
    the python file and it's cached counterpart.

    :param: directories -- the directories to search for '__pycache__'
                           directories and '.pyc' files and remove.
    :param verbose: used to decide whether or not to print additional
                    information.
    """
    for root_directory in tqdm(directories, desc="Directories cleaned"):
        clean_directory(root_directory, verbose)
