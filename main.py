from os.path import join
from marisol import Marisol


def apply_numbering(prefix='BATES_NUMBER_', backfill_zeroes=6, start_no=1):
    number_machine = Marisol(prefix=prefix, fill=backfill_zeroes, start=start_no)
    number_machine.append(join('input_files', 'fb_target.pdf'))
    number_machine.append(join('input_files', 'fb_target.pdf'))
    # Export numbered PDFs, named for their first bates number.
    result = number_machine.save()
    # Log the names of the files processed and their statuses (ex. ('file_one': True))
    print(f'Result: {result}')
