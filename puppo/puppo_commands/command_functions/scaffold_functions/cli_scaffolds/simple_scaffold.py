"""Scaffolding for creating simple CLI application."""
from os import getcwd, mkdir


def create_scaffold(application_name):
    """Use this function to create scaffolding for a simple CLI application.

    This function is used for creating the directory structure and basic files.
    """
    application_directory = getcwd()
    print("Directory to create application in: {}".format(
        application_directory))
    mkdir('{}/{}'.format(application_directory, application_name))
