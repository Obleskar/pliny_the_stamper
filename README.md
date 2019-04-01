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
## Pagewise Extraction
Pagewise extraction creates a new PDF file for each page in the provided PDF files.

1. Add new directories for input and output files.
    ```console
    user@pc:~/tools/pliny_the_stamper$ mkdir input_files output_files
    ```

2. Move input files into `input_files`.
    ```console
    user@pc:~/tools/pliny_the_stamper$ mv ~/Desktop/input_file_alpha.pdf input_files
    user@pc:~/tools/pliny_the_stamper$ mv ~/Desktop/input_file_bravo.pdf input_files
    ```
    
3. Perform pagewise extraction
    ```console
    user@pc:~/tools/pliny_the_stamper$ pliny -p input_files -d output_files -v pagify
    ```

4. Find the fruits of your labor in `output_files`.
    ```console
    user@pc:~/tools/pliny_the_stamper$ ls output_files/
    input_file_alpha  input_file_bravo
    ```
    ```console
    user@pc:~/tools/pliny_the_stamper$ cd output_files/input_file_alpha
    user@pc:~/tools/pliny_the_stamper/output_files/input_file_alpha$ ls
    input_file_alpha_pagified_1.pdf  input_file_alpha_pagified_2.pdf
    ```

## Todo
- General
    - [ ] Enable user defined output directories to pagewise extraction commands
    - [ ] Enquote file names
    - [ ] Ensure that the output of "merge" and "number" can be piped to the other
    - [ ] Logging
    - [ ] Test: Output merged PDFs to a provided directory
    - [ ] Add a progress bar to each command
- Bates Numbering
    - [ ] Put bates number in top right corner
    - [ ] Accept dynamic bates numbering prefixes
    - [ ] Keep original filenames when numbering
