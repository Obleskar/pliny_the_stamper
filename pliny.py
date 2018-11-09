from click import File, Path, echo, group, make_pass_decorator, option
from datetime import datetime

from main import apply_numbering, get_input_files, merge_pdfs


class Config(object):
    """Configuration object with attributes that are accessible by commands."""
    def __init__(self):
        self.verbose = False


# Make a decorator for passing Config to commands.
pass_config = make_pass_decorator(Config, ensure=True)


@group()
@option('-p', '--input_path',
        default='.',
        help='Path to the directory containing the PDFs.',
        required=False)
# todo: Use type=click.Path()
@option('-d', '--output_dir',
        default='.',
        help='Path to the desired output directory.',
        required=False)
@option('-o', '--outfile_name',
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
        echo(f'Combining the specified PDFs:\n{", ".join([file.name for file in config.files])} '
             f'into {config.outfile_name}.')
    result = merge_pdfs(files=config.files,
                        outfile_name=config.outfile_name,
                        destination_path=config.outfile_dir)
    if config.verbose:
        echo(f'Done merging PDFs: {", ".join([file.name for file in config.files])}.')


@pliny_global.command()
@option('--prefix', default='BATES_NUMBER_', help='The thing that is greeted.')
@pass_config
def number(config, prefix):
    """Apply bates numbers to the top right corner of each page in the specified PDF(s)."""
    config.number = True
    if config.verbose:
        echo(f'Numbering PDFs:\n{", ".join([file.name for file in config.files])}.')
    result = apply_numbering(files=config.files)
    if config.verbose:
        echo('Done numbering PDFs:\n' +
             '\n'.join([f'{file_name}->{status}' for file_name, status in result]))
