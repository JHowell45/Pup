"""Decorators for handling packaging functions."""
from os import getcwd
from os.path import exists


def packaging_handler(function):
    """Use this function to handle packaging up the application for distribution.

    Thi function is used for decorating the function used for packaging up the
    application and handling any errors thrown.
    """
    def wrapper(*args, **kwargs):
        """Nested wrapper function."""
        result = None
        try:
            result = function(*args, **kwargs)
        except Exception as e:
            print("Failed to package application!")
            if exists('{}/setup.py'.format(getcwd())):
                print('Error: {}'.format(e))
            else:
                print("Could not find 'setup.py' in the root "
                      "directory: {}".format(getcwd()))
        return result
    return wrapper
