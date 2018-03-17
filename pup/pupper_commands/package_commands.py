"""Commands for packaging up python applications."""
from pup import cli


@cli.group()
def package():
    """Packages up python applications.

    This command group can be used for packaging up a python application that
    can be used for uploading packages to the PYPI store and for distribution.
    """
    pass
