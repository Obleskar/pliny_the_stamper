from click.testing import CliRunner
from pytest import fixture

from pliny import pliny_global, pagify

def test_help():
    """"Ensure that the help documentation prints correctly.

    This also serves as a reminder to update :ref:`README.md` when commands are added or changed.

    """
    intended_helptext = ['Usage: pliny-global [OPTIONS] COMMAND [ARGS]...', '',
                         '  Merge and/or bates number PDF files.', '',
                         '  Example: pliny merge', '',
                         'Options:',
                         '  -p, --input_path TEXT    Path to the directory containing the PDFs.',
                         '  -d, --output_dir TEXT    Path to the desired output directory.',
                         '  -o, --outfile_name TEXT  Desired name for the output file.',
                         '  -v, --verbose',
                         '  --help                   Show this message and exit.', '',
                         'Commands:',
                         '  merge   Combine the specified PDFs.',
                         '  number  Apply bates numbers to the top right corner of each page in the...',
                         '  pagify  Create a new PDF file for each page of the each specified PDF...']
    result = CliRunner().invoke(pliny_global, ['--help'])
    assert result.exit_code == 0
    for intended_line, actual_line in zip(result.output.split('\n'), intended_helptext):
        assert intended_line == actual_line


# def run_pagifier(*args):
#     cli_args = ["pliny"] + list(args)
#     return
