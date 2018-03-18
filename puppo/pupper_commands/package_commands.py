"""Commands for packaging up python applications."""
from puppo import cli


@cli.group()
def package():
    """Packages up python applications.

    This command group can be used for packaging up a python application that
    can be used for uploading packages to the PYPI store and for distribution.
    """
    pass


@package.command()
def pypi():
    """packaging and uploading to PYPI.

    This command is used for creating a 'sdist' for the curernt directory using
    the 'setup.py' file and then uploading it to the PYPI python package store.
    """
    pass
