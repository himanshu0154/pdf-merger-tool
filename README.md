# PDF Merger Tool

A simple command-line tool written in Python that merges multiple PDF files into a single file using the `pypdf` library.

## Author

Developed by [himanshu0154](https://github.com/himanshu0154)

## Features

- Merge any number of PDF files
- File existence validation
- Easy command-line interface
- Custom path configuration

## Requirements

- Python 3.7+
- [`pypdf`](https://pypi.org/project/pypdf/)

Install the required package using:

```bash
pip install pypdf

# Usage

1. clone the repository:

```bash
git clone https://github.com/himanshu0154/pdf-merger-tool.git
cd pdf-merger-tool
```

2. Organise your PDF files inside the PDF_merger\data directory

3. Run the script:

```bash
python main.py
```

4. Enter the number of PDF files and their names without the .pdf extension when prompted.


5. The script will merge them and create a new file named merged-pdf.pdf in the same directory.

# Example 

```bash
how many pdfs do you want to merge?
3
enter the name of your pdf
1. file1
2. file2
3. file3
pdf merged successfully
```

# Directory Structure

```bash
pdf-merger-tool/
├── PDF_merger/
│   └── data/
│       ├── file1.pdf
│       ├── file2.pdf
│       ├── file3.pdf
│       └── merged-pdf.pdf
└── main.py
```

# License

This project is licensed under MIT License. See the LICENSE file for details.
