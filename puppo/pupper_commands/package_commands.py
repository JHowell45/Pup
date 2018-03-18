"""Commands for packaging up python applications."""
import click

from puppo import cli
from puppo.decorator_functions.display_decorators import command_handler
from puppo.pupper_commands.command_functions.package_functions import \
    pypi_fuctions


@cli.group()
def package():
    """Packages up python applications.

    This command group can be used for packaging up a python application that
    can be used for uploading packages to the PYPI store and for distribution.
    """
    pass


@package.command()
@click.option('--testpypi', is_flag=True,
              help="Whether to send to the test PYPI instead of the production"
              " version.")
@click.option('-v', '--verbose', is_flag=True,
              help="Display additional information.")
@command_handler('package PYPI')
def pypi(testpypi, verbose):
    """packaging and uploading to PYPI.

    This command is used for creating a 'sdist' for the curernt directory using
    the 'setup.py' file and then uploading it to the PYPI python package store.

    :param testpypi: boolean value saying whether or not to send to test PYPI.
    :param verbose: used to decide whether or not to print additional
                    information.
    """
    pypi_fuctions.package_application(testpypi, verbose)
