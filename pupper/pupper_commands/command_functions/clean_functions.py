"""
"""
from os.path import abspath


def clean_directory(root_directory):
    """Use this function to remove '__pycache__' and '.pyc' directories and files.

    This function is used for removing all of the nested '__pycache__' and
    '.pyc' directories and files from the specified root directory.

    :param root_directory: the root directory to remove cached files from.
    """
    full_path = abspath(root_directory)
    # print(full_path)
