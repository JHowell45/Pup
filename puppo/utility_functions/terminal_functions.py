"""File containing functions used for executing consoel commands."""
from subprocess import check_output


def run_command(commandList):
    """Use this function to return the results of terminal commands."""
    return check_output(commandList).decode('utf-8')
