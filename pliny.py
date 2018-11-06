from click import command, option, echo, argument, File, group, make_pass_decorator
from datetime import datetime
from os import getcwd

from main import apply_numbering, get_input_files, merge_pdfs


class Config(object):
    """Configuration object with attributes that can incorporate with commands."""
    def __init__(self):
        self.verbose = False


# Make a decorator for passing Config to commands.
pass_config = make_pass_decorator(Config, ensure=True)


@group()
@option('-p', '--input_path',
        default='.',
        help='Path to the directory containing the PDFs.',
        required=False)
@option('-d', '--output_dir',
        default='.',
        help='Path to the desired output directory.',
        required=False)
@option('-o', '--outfile_name',
        type=File('w'),
        default=f'{datetime.now()}_pliny_doc.pdf',
        help='Desired name for the output file.',
        required=False)
@option('-v', '--verbose',
        default=False,
        is_flag=True,
        required=False)
@pass_config
def pliny_global(config, input_path, output_dir, outfile_name, verbose):
    """Merge and/or bates number PDF files.

    Example: pliny merge
    """
    config.path = input_path
    config.outfile_dir = output_dir
    config.outfile_name = outfile_name
    config.verbose = verbose
    if verbose:
        echo('Verbose mode active.')
    # Get a list of input PDF files from the provided directory.
    config.files = [filename for filename in get_input_files(input_path)]


@pliny_global.command()
@pass_config
def merge(config):
    """Combine the specified PDFs."""
    config.merge = True
    if config.verbose:
       echo(f'Combining the specified PDFs from {config.input_path} into {config.outfile_name}')
    merge_pdfs(files=config.files, outfile_name=config.outfile_name, destination_path=config.outfile_dir)


@pliny_global.command()
@option('--string', default='World', help='The thing that is greeted.')
@pass_config
def number(config, string, out):
    """Apply bates numbers to the top right corner of each page in the specified PDF(s)."""
    config.number = True
    if config.verbose:
        echo(f'Numbering PDFs.')
