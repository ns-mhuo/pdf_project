PDF, HTML, and Markdown Conversion Tools
A collection of simple, fast command-line tools in Python to convert between PDF, HTML, and Markdown formats.

Features
PDF to Markdown: Extracts text from all pages of a PDF and creates a structured Markdown file.

Markdown to HTML: Converts a Markdown file into a styled HTML file ready to be pasted into a Confluence page.

HTML to Markdown: Converts an HTML file into a clean Markdown file.

Lightweight and easy to use.

Project Structure
The repository contains the following files:

.
├── .gitignore
├── LICENSE
├── README.md
├── convert.py
├── md2html.py
├── html2md.py
└── requirements.txt

Setup and Installation
Follow these steps to set up the project on your local machine.

1. Clone the Repository

First, clone this repository to your desired location (e.g., inside your ~/git folder). Make sure you have SSH keys set up with your GitHub account.

git clone git@github.com:ns-mhuo/pdf_project.git
cd pdf_project

2. Create and Activate a Virtual Environment

It is highly recommended to use a virtual environment to manage project dependencies.

# Create a hidden virtual environment named .venv
python3 -m venv .venv

# Activate the environment
source .venv/bin/activate

Your terminal prompt should now be prefixed with (.venv).

3. Install Dependencies

Install the required Python packages from the requirements.txt file.

pip3 install -r requirements.txt

Usage
With your virtual environment active, you can run the scripts from the command line.

PDF to Markdown (convert.py)
Syntax:

python3 convert.py <path_to_input.pdf> <path_to_output.md>

Example:

python3 convert.py report.pdf converted_report.md

Markdown to Confluence HTML (md2html.py)
Syntax:

python3 md2html.py <path_to_input.md>

Example:
This command will generate a styled HTML file with a -confluence.html suffix.

python3 md2html.py mydoc.md

HTML to Markdown (html2md.py)
Syntax:

python3 html2md.py <path_to_input.html> <path_to_output.md>

Example:

python3 html2md.py page.html converted_page.md

License
This project is licensed under the MIT License. See the LICENSE file for details.