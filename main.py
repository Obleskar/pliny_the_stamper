from os import scandir
from marisol import Marisol


def get_input_files(input_dir='input_files'):
    """Get a list of path-like objects that represent the files to be ingested.

    Ignore all files lacking a .pdf extension.
    """
    return [file_path for file_path in scandir(input_dir) if file_path.name.endswith('.pdf')]


def apply_numbering(files, prefix='BATES_NUMBER_', backfill_zeroes=6, start_no=1):
    """Apply incrementing "bates stamps" to each provided file.

    Arguments:
        files (list): Path-like objects that point to the PDFs to be numbered.
            If cross-file numbering isn't desired, then merge the input PDFs into one PDF before executing this step.
        prefix (str): Standard prefix for each page's "bates stamp."
        backfill_zeroes (int): Maximum number of zeros that must appear after the prefix. Defaults to 6.
            Backfilled zeroes are consumed by the count number as it increments.
        start_no (int): Number to start the count on. Defaults to 1.

    Returns:
        list: Tuples with the filename and a corresponding boolean success indicator.
    """
    number_machine = Marisol(prefix=prefix, fill=backfill_zeroes, start=start_no)
    for file in files:
        number_machine.append(file)
    # Export numbered PDFs, named for their first bates number.
    status = number_machine.save()
    # Log the names of the files processed and their statuses (ex. ('file_one': True))
    print(f'Result: {status}')
    return status
