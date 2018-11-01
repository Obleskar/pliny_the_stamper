from click import command, option, echo, argument, File, group, make_pass_decorator
from os import getcwd

from main import apply_numbering, merge_pdfs


class Config(object):
    """Configuration object with attributes that can incorporate with commands."""
    def __init__(self):
        self.verbose = False


# Make a decorator for passing Config to commands.
pass_config = make_pass_decorator(Config, ensure=True)


@group()
@option('-v', '--verbose', is_flag=True)
@pass_config
def pliny_global(config, verbose):
    """Merge and/or bates number PDF files.

    Example: pliny merge
    """
    config.verbose = verbose
    if verbose:
        echo('Verbose mode active.')


@pliny_global.command()
@option('p', '--path', default=None, help='Source directory containing the PDFs.')
@argument('name', type=File('w'), default='merged_file.pdf', required=False, help='Name for the output file.')
@pass_config
def merge(config, path, name):
    """Combine the specified PDFs."""
    if config.verbose:
       echo(f'Combining the specified PDFs from {path} into {name}')


@pliny_global.command()
@option('--string', default='World', help='The thing that is greeted.')
@argument('out', type=File('w'), default='-', required=False)
@pass_config
def number(config, string, out):
    """Apply bates numbers to the top right corner of each page in the specified PDF(s).


    """
    if config.verbose:
        echo(f'Doubly verbose me lord')
