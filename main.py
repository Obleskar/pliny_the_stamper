from marisol import Marisol
from os import getcwd, mkdir, scandir
from os.path import join, splitext
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


def pagify_pdfs(files, destination_path):
    """Iterate through each provided PDF file and create a new PDF file from each of its pages.

    Arguments:
        destination_path (str, optional): Output directory path.
    """
    for file in files:
        # Create the output directory name by removing the file's extension.
        out_dir_name = splitext(file.name)[0]
        out_dir_path = join(destination_path, out_dir_name)
        try:
            mkdir(path=out_dir_path)
        except FileExistsError as e:
            print(f'The output directory {out_dir_name} for {file.name} already exists in {destination_path}.\n'
                  f'Please delete the existing output directory or choose a different output destination.\n{e}')
        # opened_file = PdfFileReader(file)
        # for page_number in range(opened_file.getNumPages()):
        #     new_file = PdfFileWriter()
        #     new_file.addPage(opened_file.getPage(page_number))
        #     # Reuse the extensionless destination directory name to name the output file.
        #     new_filename = out_dir_name + '_pagified_' + page_number + 1 + '.pdf'
        #     # Add the singular PDF page as a new file in the output directory.
        #     with open(out_dir_path) as single_page_file:
        #         new_file.write(single_page_file)
