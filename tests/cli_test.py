from click.testing import CliRunner
from os import getcwd, path, scandir
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


def test_pagifier(output_file_dir=path.join(getcwd(), 'output_files')):
    """Ensure that the pagifier command performs pagewise extraction of the provided PDF file.

    The test input files `argparse.pdf` and `pocco click.pdf` should become new directories `argparse` and
    `pocco click`, respectively.

    The `argparse` directory should hold `argparse_pagified_1.pdf` to `argparse_pagified_40.pdf`.
    The `pocco click` directory should hold `pocco click_pagified_1.pdf` to `pocco click_pagified_105.pdf`.
    """
    intended_text = 'Verbose mode active.\n'# \
                    # 'Pagifying PDFs:\n'
    runner = CliRunner()
    result = runner.invoke(pliny_global, ['-p', 'input_files',
                                          '-d', 'output_files',
                                          '-v',
                                          'pagify'])
    # Ensure that the response prompt is correct.
    assert result.output.startswith(intended_text)
    # Ensure that a correctly named output directory's created for each input file.
    output_dirs = [directory.name for directory in scandir(output_file_dir) if path.isdir(directory)]
    assert 'argparse' in output_dirs
    assert 'pocoo click' in output_dirs
    assert path.isfile(path.join(output_file_dir, 'argparse', 'argparse_pagified_1.pdf'))
