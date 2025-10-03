#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A multi-format converter for PDF, Markdown, and LaTeX files.

Detects the conversion direction based on file extensions.
- .pdf -> .md : Extracts text from a PDF and saves it as Markdown.
- .md -> .pdf : Converts a Markdown file into a PDF document.
- .md -> .tex : Saves a Markdown file as a plain text LaTeX (.tex) file.
- .tex -> .md : Saves a LaTeX file as a plain text Markdown (.md) file.
"""

import sys
import fitz  # PyMuPDF
from fpdf import FPDF

def pdf_to_markdown(pdf_path, md_path):
    """
    Converts a PDF file to a Markdown file using PyMuPDF.

    Args:
        pdf_path (str): The file path of the input PDF.
        md_path (str): The file path for the output Markdown file.
    """
    try:
        doc = fitz.open(pdf_path)
        markdown_content = ""
        
        # Iterate through each page of the PDF
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            
            # Add a page break for clarity
            if page_num > 0:
                markdown_content += "\n---\n\n"
            
            # Extract text from the page
            markdown_content += page.get_text("text")

        # Write the content to the Markdown file
        with open(md_path, "w", encoding="utf-8") as md_file:
            md_file.write(markdown_content)
            
        print(f"Conversion complete! Markdown file saved as '{md_path}'")

    except Exception as e:
        print(f"An error occurred during PDF to Markdown conversion: {e}")
        sys.exit(1)

def markdown_to_pdf(md_path, pdf_path):
    """
    Converts a Markdown file to a PDF file using fpdf2.

    Args:
        md_path (str): The file path of the input Markdown file.
        pdf_path (str): The file path for the output PDF.
    """
    try:
        with open(md_path, "r", encoding="utf-8") as md_file:
            markdown_content = md_file.read()

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        
        # Use the multi_cell method for basic markdown support
        pdf.multi_cell(0, 5, markdown_content, markdown=True)
        
        pdf.output(pdf_path)
        
        print(f"Conversion complete! PDF file saved as '{pdf_path}'")

    except Exception as e:
        print(f"An error occurred during Markdown to PDF conversion: {e}")
        print("Please ensure you have run 'pip install fpdf2'")
        sys.exit(1)

def markdown_to_tex(md_path, tex_path):
    """
    Saves a Markdown file as a plain text .tex file.

    Args:
        md_path (str): The file path of the input Markdown file.
        tex_path (str): The file path for the output LaTeX file.
    """
    try:
        with open(md_path, 'r', encoding='utf-8') as infile:
            content = infile.read()
        with open(tex_path, 'w', encoding='utf-8') as outfile:
            outfile.write(content)
        print(f"Conversion complete! LaTeX file saved as '{tex_path}'")
    except Exception as e:
        print(f"An error occurred during Markdown to TeX conversion: {e}")
        sys.exit(1)

def tex_to_markdown(tex_path, md_path):
    """
    Saves a .tex file as a plain text .md file.

    Args:
        tex_path (str): The file path of the input LaTeX file.
        md_path (str): The file path for the output Markdown file.
    """
    try:
        with open(tex_path, 'r', encoding='utf-8') as infile:
            content = infile.read()
        with open(md_path, 'w', encoding='utf-8') as outfile:
            outfile.write(content)
        print(f"Conversion complete! Markdown file saved as '{md_path}'")
    except Exception as e:
        print(f"An error occurred during TeX to Markdown conversion: {e}")
        sys.exit(1)


def main():
    """
    Main function to parse arguments and run the correct converter.
    """
    if len(sys.argv) != 3:
        print("Usage: python3 convert.py <input_file> <output_file>")
        print("Example (PDF -> MD): python3 convert.py my_doc.pdf my_doc.md")
        print("Example (MD -> PDF): python3 convert.py my_doc.md my_doc.pdf")
        print("Example (MD -> TeX): python3 convert.py my_doc.md my_doc.tex")
        print("Example (TeX -> MD): python3 convert.py my_doc.tex my_doc.md")
        sys.exit(1)
        
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Detect conversion direction based on file extensions
    if input_file.lower().endswith('.pdf') and output_file.lower().endswith('.md'):
        print("Direction: PDF -> Markdown")
        pdf_to_markdown(input_file, output_file)
    elif input_file.lower().endswith('.md') and output_file.lower().endswith('.pdf'):
        print("Direction: Markdown -> PDF")
        markdown_to_pdf(input_file, output_file)
    elif input_file.lower().endswith('.md') and output_file.lower().endswith('.tex'):
        print("Direction: Markdown -> TeX")
        markdown_to_tex(input_file, output_file)
    elif input_file.lower().endswith('.tex') and output_file.lower().endswith('.md'):
        print("Direction: TeX -> Markdown")
        tex_to_markdown(input_file, output_file)
    else:
        print("Error: Unsupported file conversion.")
        print("   Supported conversions are: .pdf -> .md, .md -> .pdf, .md -> .tex, and .tex -> .md")
        sys.exit(1)

if __name__ == "__main__":
    main()

