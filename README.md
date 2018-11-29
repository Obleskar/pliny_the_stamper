# Pliny the Stamper
A command line program for merging multiple PDFs and bates numbering their pages.

### Installation
1. Copy the project into a new directory called "pliny_the_stamper."
    ```sh
    git clone https://github.com/Obleskar/pliny_the_stamper.git
    ```      
2. Navigate into the project.
    ```sh
    cd pliny_the_stamper
    ```
3. Install the package.
    ```sh
    pip install .
    ```
### Todo
- General
    - Enquote file names
    - Ensure that the output of "merge" and "number" can be piped to the other
    - Logging
    - Test: Output merged PDFs to a provided directory
- Bates Numbering
    - Put bates number in top right corner
    - Accept dynamic bates numbering prefixes
    - Keep original filenames when numbering
