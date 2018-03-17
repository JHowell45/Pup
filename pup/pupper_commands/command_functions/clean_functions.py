"""Functions for cleaning a directory."""
from os import remove, walk
from os.path import abspath
from shutil import rmtree

from click import echo, style

from pup.decorator_functions.display_decorators import command_handler
from tqdm import tqdm


def clean_directory(root_directory, verbose):
    """Use this function to remove '__pycache__' and '.pyc' directories and files.

    This function is used for removing all of the nested '__pycache__' and
    '.pyc' directories and files from the specified root directory.

    :param root_directory: the root directory to remove cached files from.
    :param verbose: display additional nformation or not.
    """
    full_path = abspath(str(root_directory))
    incorrect_directory = {}

    for root, directories, files in walk(full_path, topdown=False):

        # Delete '.pyc' files in directory:
        files_to_remove = \
            [python_file for python_file in files if '.pyc' in python_file]
        if files_to_remove and not verbose:
            for python_file in tqdm(files_to_remove, desc="Deleting files"):
                remove('{}/{}'.format(root, python_file))
        if files_to_remove and verbose:
            for python_file in files_to_remove:
                file_path = '{}/{}'.format(root, python_file)
                print(file_path)
                remove(file_path)

        # Delete '__pycache__' directories:
        try:
            if root.rsplit('/', 1)[1] == '__pycache__':
                if verbose:
                    print(root)
                try:
                    rmtree(root, ignore_errors=True)
                except OSError as e:
                    incorrect_directory[root] = "Failed to delete directory"
        except Exception as e:
            if root.rsplit('\\', 1)[1] == '__pycache__':
                try:
                    rmtree(root, ignore_errors=True)
                except OSError as e:
                    incorrect_directory[root] = "Failed to delete directory"
    __print_issues(incorrect_directory) if incorrect_directory else None


@command_handler('issues', colour='red')
def __print_issues(issues):
    """Use this function to display issues."""
    for key, value in issues.items():
        echo('{}: {}'.format(str(key), style(str(value), fg='yellow')))
