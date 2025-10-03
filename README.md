PDF to Markdown Converter
A simple, fast command-line tool written in Python to convert the text content of PDF files into clean Markdown format. This script uses the PyMuPDF library for efficient text extraction.

Features
Extracts text from all pages of a PDF.

Creates a structured Markdown file with headings for each page.

Adds a horizontal rule (---) to separate content from different pages.

Lightweight and easy to use.

Project Structure
The repository contains the following files:

.
├── .gitignore
├── LICENSE
├── README.md
├── convert.py
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
With your virtual environment active, you can run the script from the command line.

Syntax:

python3 convert.py <path_to_input.pdf> <path_to_output.md>

Example:

Place a PDF file (e.g., report.pdf) in the project directory and run:

python3 convert.py report.pdf converted_report.md

A new file named converted_report.md will be created in the same directory.

License
This project is licensed under the MIT License. See the LICENSE file for details.