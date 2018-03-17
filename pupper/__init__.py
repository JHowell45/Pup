"""Use this file to house the root CLI command.

This file is used for creating the root command used for housing the nested
commands and scripts.
"""
import click


@click.group()
def cli():
    """Scripts and commands for making Python easier.

    Pupper is a list of commands and scripts designed to making python
    packages, applications, webpages and anything else you can think of easier.
    """
    pass
