from os.path import join
from marisol import Marisol


number_machine = Marisol(prefix='BATES_NUMBER_', fill=6, start=1)  # Begin numbering with BATES_NUMBER_000001
number_machine.append(join('input_files', 'fb_target.pdf'))
number_machine.append(join('input_files', 'fb_target.pdf'))
result = number_machine.save()  # Export numbered PDFs, named for the bates number.
# Log the names of the files processed and their statuses (ex. ('file_one': True))
print(f'Result: {result}')
