"""Scaffolding for creating simple CLI application."""
from os import getcwd, mkdir


def create_scaffold(application_name, add_tests):
    """Use this function to create scaffolding for a simple CLI application.

    This function is used for creating the directory structure and basic files
    it will create the necessary directories and also has an option for
    creating a tests directory.

    :param application_name: the name of the CLI application.
    :type application_name: string
    :param add_tests: whether or not to add a tests directory.
    :type add_tests: boolean
    """
    application_directory = getcwd()
    print("Directory to create application in: {}".format(
        application_directory))
    mkdir('{}/{}'.format(application_directory, application_name))
