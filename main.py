from marisol import Marisol
from os import getcwd, scandir
from os.path import join
from PyPDF2 import PdfFileMerger, PdfFileReader, PdfFileWriter


def get_input_files(input_dir=getcwd()):
    """Get a list of path-like objects that represent the files to be ingested.

    Ignores all files lacking a .pdf extension.

    Arguments:
        input_dir (str): Path to the directory containing the PDFs. Defaults to the current working directory.
    """
    return [file_path for file_path in scandir(input_dir) if file_path.name.endswith('.pdf')]


def merge_pdfs(files, outfile_name, destination_path):
    """Combine the provided PDFs in the order that they appear.

    Arguments:
        files (list, required): Path-like objects that point to PDFs to be merged.
            Use :func:`~main.get_input_files` to make requests.
        outfile_name (str, optional): Name for the resulting output file.
        destination_path (str, optional): Output directory path.

    Returns:
        (str): Path to the created file.
    """
    pdf_merger = PdfFileMerger()
    outfile_path = join(destination_path, outfile_name)
    with open(outfile_path, 'wb')as outfile:
        # Add each PDF onto the end of the preceding one.
        for file in files:
            # Files have to remain open until the pdf_merger writes the output file.
            pdf_merger.append(open(file.path, 'rb'))
            print(f'Appended {file.name}.')
        pdf_merger.write(outfile)
        print(f'Created {outfile_name} at {destination_path}.')
    return outfile_path


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
        (list) Tuples with the filename and a corresponding boolean success indicator.
    """
    number_machine = Marisol(prefix=prefix, fill=backfill_zeroes, start=start_no)
    for file in files:
        number_machine.append(file.path)
    # Export numbered PDFs, named for their first bates number.
    status = number_machine.save()
    # Log the names of the files processed and their statuses (ex. ('file_one': True))
    print(f'Result: {status}')
    return status


def pagify_pdfs(files):
    """Iterate through each provided PDF file and create a new PDF file from each of its pages."""
    for pdf_file_path in files:
        pdf_file = PdfFileReader(stream=pdf_file_path)
        print(pdf_file.getNumPages())
