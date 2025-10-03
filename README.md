# PDF, HTML, and Markdown Conversion Tools

A collection of simple, fast command-line tools in Python to convert between PDF, HTML, and Markdown formats.

## Features

* **Multi-format Converter**: Handles conversions between PDF, Markdown, and LaTeX (`.tex`) files
* **Markdown to HTML**: Converts a Markdown file into a styled HTML file ready to be pasted into a Confluence page
* **HTML to Markdown**: Converts an HTML file into a clean Markdown file
* Lightweight and easy to use

## Project Structure

The repository contains the following files:

```
.
├── .gitignore
├── LICENSE
├── README.md
├── convert.py
├── html2md.py
├── md2html.py
├── requirements.txt
├── 1.md                    # Example Markdown file
├── 1-confluence.html       # Example HTML output
└── test/                   # Test output files
    ├── test_output.md
    ├── test_output2.md
    └── test_output3.md
```

## Setup and Installation

Follow these steps to set up the project on your local machine.

### 1. Clone the Repository

First, clone this repository to your desired location (e.g., inside your `~/git` folder). Make sure you have SSH keys set up with your GitHub account.

```bash
git clone git@github.com:ns-mhuo/pdf_project.git
cd pdf_project
```

### 2. Create and Activate a Virtual Environment

It is highly recommended to use a virtual environment to manage project dependencies.

```bash
# Create a hidden virtual environment named .venv
python3 -m venv .venv

# Activate the environment
source .venv/bin/activate
```

Your terminal prompt should now be prefixed with `(.venv)`.

### 3. Install Dependencies

Install the required Python packages from the `requirements.txt` file. If you've added a new tool, re-run this command to get the latest dependencies.

```bash
pip3 install -r requirements.txt
```

## Usage

With your virtual environment active, you can run the scripts from the command line.

### Multi-format Converter (`convert.py`)

This script handles conversions involving PDF, Markdown, and LaTeX. It automatically detects the direction based on the filenames you provide.

**Syntax (PDF to Markdown):**

```bash
python3 convert.py <input.pdf> <output.md>
```

**Syntax (Markdown to PDF):**

```bash
python3 convert.py <input.md> <output.pdf>
```

**Syntax (Markdown to TeX):**

This is useful for getting a guaranteed plain text version of your Markdown file.

```bash
python3 convert.py <input.md> <output.tex>
```

**Syntax (TeX to Markdown):**

```bash
python3 convert.py <input.tex> <output.md>
```

### Markdown to HTML Converter (`md2html.py`)

Converts Markdown files to styled HTML files optimized for Confluence pages.

**Syntax:**

```bash
python3 md2html.py <input.md> [output.html]
```

If no output file is specified, it will create `<input_filename>-confluence.html`.

**Features:**
- Converts headers, lists, code blocks, inline code, bold/italic text
- Generates proper HTML tables from Markdown tables
- Includes Confluence-optimized CSS styling
- Ready to copy-paste into Confluence pages

### HTML to Markdown Converter (`html2md.py`)

Converts HTML files back to clean Markdown format.

**Syntax:**

```bash
python3 html2md.py <input.html> <output.md>
```

**Features:**
- Extracts content from HTML pages (ignores CSS and styling)
- Converts HTML elements back to Markdown syntax
- Handles tables, lists, headers, and formatting
- Produces clean, readable Markdown output

## Examples

Try the included example files:

```bash
# Convert the example Markdown to HTML
python3 md2html.py 1.md

# Convert the generated HTML back to Markdown
python3 html2md.py 1-confluence.html clean_output.md

# Convert PDF to Markdown (if you have a PDF file)
python3 convert.py document.pdf document.md
```

## Requirements

- Python 3.6+
- Dependencies listed in `requirements.txt`:
  - PyMuPDF (for PDF processing)
  - fpdf2 (for PDF generation)
  - beautifulsoup4 (for HTML parsing)
  - markdownify (for HTML to Markdown conversion)

## Contributing

Feel free to submit issues, feature requests, or pull requests to improve these tools.

## License

See LICENSE file for details.
