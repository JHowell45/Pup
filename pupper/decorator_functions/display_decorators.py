"""Decorator unctions for displaying commands."""
from functools import wraps
from shutil import get_terminal_size

import click


def command_handler(command_title, colour='green'):
    """Use this decorator for surrounding the functions with banners."""
    def decorator(function):
        """Nested decorator function."""
        terminal_width = int(get_terminal_size()[0])
        title = ' {} '.format(command_title)
        banner_length = int((terminal_width - len(title)) / 2)
        banner = '-' * banner_length
        command_banner = '|{0}{1}{0}|'.format(
            banner, title.title())
        lower_banner = '|{}|'.format('-' * int(len(command_banner) - 2))

        @wraps(function)
        def wrapper(*args, **kwargs):
            """Nested wrapper function."""
            click.secho(command_banner, fg=colour)
            result = function(*args, **kwargs)
            click.secho(lower_banner, fg=colour)
            return result
        return wrapper
    return decorator
