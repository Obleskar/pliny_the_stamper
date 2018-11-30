# Pliny the Stamper
A command line program for merging multiple PDFs and bates numbering their pages.

## Installation
1. Copy the project into a new directory called "pliny_the_stamper."
    ```console
    user@pc:~$ git clone https://github.com/Obleskar/pliny_the_stamper.git
    ```      
2. Navigate into the project.
    ```console
    user@pc:~$ cd pliny_the_stamper
    ```
3. Install the Pliny the Stamper.
    ```console
    user@pc:~$ pip install .
    ```
4. Test the installation.
    ```console
    user@pc:~$ pliny --help
    Usage: pliny [OPTIONS] COMMAND [ARGS]...
     
      Merge and/or bates number PDF files.
     
      Example: pliny merge
     
    Options:
      -p, --input_path TEXT    Path to the directory containing the PDFs.
      -d, --output_dir TEXT    Path to the desired output directory.
      -o, --outfile_name TEXT  Desired name for the output file.
      -v, --verbose
      --help                   Show this message and exit.

    Commands:
      merge   Combine the specified PDFs.
      number  Apply bates numbers to the top right corner of each page in the...
    ```
## Todo
- General
    - [ ] Enquote file names
    - [ ] Ensure that the output of "merge" and "number" can be piped to the other
    - [ ] Logging
    - [ ] Test: Output merged PDFs to a provided directory
- Bates Numbering
    - [ ] Put bates number in top right corner
    - [ ] Accept dynamic bates numbering prefixes
    - [ ] Keep original filenames when numbering
