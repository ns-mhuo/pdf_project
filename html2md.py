#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HTML to Markdown Converter
Converts an HTML file into Markdown format using the markdownify library.
"""

import sys
from pathlib import Path
from markdownify import markdownify as md

def html_to_markdown(html_path, md_path):
    """
    Converts an HTML file to a Markdown file.

    Args:
        html_path (str): The file path of the input HTML.
        md_path (str): The file path for the output Markdown file.
    """
    try:
        # Ensure the input file exists
        input_file = Path(html_path)
        if not input_file.is_file():
            print(f"❌ Error: Input file not found at '{html_path}'")
            return

        # Read the HTML content
        html_content = input_file.read_text(encoding="utf-8")
        
        # Convert HTML to Markdown
        markdown_content = md(html_content)

        # Write the content to the Markdown file
        with open(md_path, "w", encoding="utf-8") as md_file:
            md_file.write(markdown_content)
            
        print(f"✅ Conversion complete! Markdown file saved as '{md_path}'")

    except Exception as e:
        print(f"❌ An error occurred: {e}")

def main():
    """ Main entry point of the script """
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 3:
        print("Usage: python3 html2md.py <input_html_file> <output_markdown_file>")
        sys.exit(1)
        
    input_html = sys.argv[1]
    output_md = sys.argv[2]
    
    html_to_markdown(input_html, output_md)

if __name__ == "__main__":
    main()
