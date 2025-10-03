#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
A command-line tool to convert the text content of a PDF file into Markdown.

This script uses the PyMuPDF library (fitz) to extract text from each page
of a specified PDF and saves it to a structured Markdown file.
"""

import fitz  # PyMuPDF
import sys
import os

def pdf_to_markdown(pdf_path, md_path):
    """
    Extracts text from a PDF file and saves it as a Markdown file.

    Args:
        pdf_path (str): The full path to the input PDF file.
        md_path (str): The full path for the output Markdown file.
    """
    # Check if the source file exists
    if not os.path.exists(pdf_path):
        print(f"❌ Error: The file '{pdf_path}' was not found.")
        sys.exit(1)

    try:
        # Open the PDF file using a context manager
        with fitz.open(pdf_path) as doc:
            print(f"✅ Successfully opened '{pdf_path}'.")
            print(f"📄 Processing {len(doc)} pages...")

            markdown_content = []
            
            # Add a title to the Markdown file based on the PDF's filename
            pdf_filename = os.path.basename(pdf_path)
            markdown_content.append(f"# {pdf_filename}\n\n")
            
            # Iterate through each page of the PDF
            for page_num, page in enumerate(doc):
                # Add a separator and heading for each page
                if page_num > 0:
                    markdown_content.append("\n---\n") # Horizontal rule as page break
                
                markdown_content.append(f"## Page {page_num + 1}\n\n")
                
                # Extract raw text from the page
                text = page.get_text("text")
                if text.strip(): # Only add content if the page is not blank
                    markdown_content.append(text)

        # Write the collected content to the Markdown file
        with open(md_path, "w", encoding="utf-8") as md_file:
            md_file.write("".join(markdown_content))
            
        print(f"✅ Conversion complete! Markdown file saved as '{md_path}'")

    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")
        sys.exit(1)

def main():
    """
    Main function to handle command-line arguments and run the conversion.
    """
    # Ensure correct number of command-line arguments are provided
    if len(sys.argv) != 3:
        print("Usage: python3 convert.py <input_pdf_file> <output_markdown_file>")
        print("Example: python3 convert.py 'My Report.pdf' 'report_output.md'")
        sys.exit(1)
        
    input_pdf = sys.argv[1]
    output_md = sys.argv[2]
    
    pdf_to_markdown(input_pdf, output_md)

if __name__ == "__main__":
    main()

