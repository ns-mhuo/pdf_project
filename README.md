# PDF, HTML, and Markdown Conversion Tools

A collection of simple, fast command-line tools in Python to convert between PDF, HTML, and Markdown formats.

## Features

* **Multi-format Converter**: Handles conversions between PDF, Markdown, and LaTeX (`.tex`) files.

* **Markdown to HTML**: Converts a Markdown file into a styled HTML file ready to be pasted into a Confluence page.

* **HTML to Markdown**: Converts an HTML file into a clean Markdown file.

* Lightweight and easy to use.

## Project Structure

The repository contains the following files:

.
├── .gitignore
├── LICENSE
├── README.md
├── convert.py
├── html2md.py
├── md2html.py
└── requirements.txt

## Setup and Installation

Follow these steps to set up the project on your local machine.

**1.** Clone the **Repository**

First, clone this repository to your desired location (e.g., inside your `~/git` folder). Make sure you have SSH keys set up with your GitHub account.

git clone git@github.com:ns-mhuo/pdf_project.git
cd pdf_project

**2. Create and Activate a Virtual Environment**

It is highly recommended to use a virtual environment to manage project dependencies.

# Create a hidden virtual environment named .venv
python3 -m venv .venv

# Activate the environment
source .venv/bin/activate

Your terminal prompt should now be prefixed with `(.venv)`.

**3. Install Dependencies**

Install the required Python packages from the `requirements.txt` file. If you've added a new tool, re-run this command to get the latest dependencies.

pip3 install -r requirements.txt

## Usage

With your virtual environment active, you can run the scripts from the command line.

### Multi-format Converter (`convert.py`)

This script handles conversions involving PDF, Markdown, and LaTeX. It automatically detects the direction based on the filenames you provide.

**Syntax (PDF to Markdown):**

python3 convert.py <input.pdf> <output.md>

**Syntax (Markdown to PDF):**

python3 convert.py <input.md> <output.pdf>

**Syntax (Markdown to TeX):**

This is useful for getting a guaranteed plain text version of your Markdown file.

python3 convert.py <input.md> <output.tex>
