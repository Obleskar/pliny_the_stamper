from os.path import join
from marisol import Marisol


def apply_numbering(prefix='BATES_NUMBER_', backfill_zeroes=6, start_no=1):
    """Apply incrementing "bates stamps" to each provided file.

    Arguments:
        prefix (str): Standard prefix for each page's "bates stamp."
        backfill_zeroes (int): Maximum number of zeros that must appear after the prefix. Defaults to 6.
            Backfilled zeroes are consumed by the count number as it increments.
        start_no (int): Number to start the count on. Defaults to 1.

    Returns:
        list: Tuples with the filename and a corresponding boolean success indicator.
    """
    number_machine = Marisol(prefix=prefix, fill=backfill_zeroes, start=start_no)
    number_machine.append(join('input_files', 'fb_target.pdf'))
    number_machine.append(join('input_files', 'fb_target.pdf'))
    # Export numbered PDFs, named for their first bates number.
    status = number_machine.save()
    # Log the names of the files processed and their statuses (ex. ('file_one': True))
    print(f'Result: {status}')
    return status
