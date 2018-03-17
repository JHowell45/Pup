"""
"""
from functools import wraps
from shutil import get_terminal_size
import click


def command_handler(command_title, colour='green'):
    """Use this decorator for
    """
    def decorator(function):
        """
        """
        @wraps(function)
        def wrapper(*args, **kwargs):
            """
            """
            terminal_width = get_terminal_size()[0]
            banner_length = int(int(terminal_width) - (len(command_title) + 2))
            banner = '-' * int((banner_length - 2) / 2)
            click.secho('|{0} {1} {0}|'.format(
                banner, command_title.title()), fg=colour)
            function(*args, **kwargs)
        return wrapper
    return decorator
