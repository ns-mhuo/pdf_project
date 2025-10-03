#!/usr/bin/env python3
"""
Markdown to Confluence HTML Converter
Converts nsproxy routing automation markdown documentation to Confluence-ready HTML
"""

import re
import sys
from pathlib import Path


def convert_tables(html):
    """
    Convert markdown tables to HTML tables
    """
    lines = html.split('\n')
    result = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.strip().startswith('|') and '|' in line:
            # Start of table
            table_lines = []
            # Collect all table lines
            while i < len(lines) and lines[i].strip().startswith('|'):
                table_lines.append(lines[i])
                i += 1
            # Convert table
            table_html = convert_table_block(table_lines)
            result.append(table_html)
        else:
            result.append(line)
            i += 1
    return '\n'.join(result)


def convert_table_block(table_lines):
    """
    Convert a block of markdown table lines to HTML table
    """
    if len(table_lines) < 2:
        return '\n'.join(table_lines)  # Not a valid table
    
    # Check if second line is separator
    second_line = table_lines[1].strip()
    if not re.match(r'^\|[\s\-\|:]+\|$', second_line):
        return '\n'.join(table_lines)  # Not a valid table
    
    # Parse header
    header_cells = [cell.strip() for cell in table_lines[0].split('|')[1:-1]]
    # Parse body rows
    body_rows = []
    for line in table_lines[2:]:
        if line.strip():
            cells = [cell.strip() for cell in line.split('|')[1:-1]]
            body_rows.append(cells)
    
    # Build HTML
    html = '<table>\n'
    # Header
    html += '<tr>\n'
    for cell in header_cells:
        html += f'<th>{cell}</th>\n'
    html += '</tr>\n'
    # Body
    for row in body_rows:
        html += '<tr>\n'
        for cell in row:
            html += f'<td>{cell}</td>\n'
        html += '</tr>\n'
    html += '</table>'
    return html


def convert_markdown_to_confluence_html(md_content):
    """
    Convert markdown content to Confluence-compatible HTML
    """
    html = md_content
    
    # Convert headers
    html = re.sub(r'^# (.+)$', r'<h1>\1</h1>', html, flags=re.MULTILINE)
    html = re.sub(r'^## (.+)$', r'<h2>\1</h2>', html, flags=re.MULTILINE)
    html = re.sub(r'^### (.+)$', r'<h3>\1</h3>', html, flags=re.MULTILINE)
    html = re.sub(r'^#### (.+)$', r'<h4>\1</h4>', html, flags=re.MULTILINE)
    html = re.sub(r'^##### (.+)$', r'<h5>\1</h5>', html, flags=re.MULTILINE)
    
    # Convert code blocks
    html = re.sub(r'```([a-zA-Z]*)\n(.*?)\n```', r'<pre><code>\2</code></pre>', html, flags=re.DOTALL)
    
    # Convert inline code
    html = re.sub(r'`([^`]+)`', r'<code>\1</code>', html)
    
    # Convert bold text
    html = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', html)
    
    # Convert italic text
    html = re.sub(r'\*([^*]+)\*', r'<em>\1</em>', html)
    
    # Convert unordered lists
    html = re.sub(r'^- (.+)$', r'<li>\1</li>', html, flags=re.MULTILINE)
    html = re.sub(r'^  - (.+)$', r'  <li>\1</li>', html, flags=re.MULTILINE)
    
    # Convert ordered lists
    html = re.sub(r'^(\d+)\. (.+)$', r'<li>\2</li>', html, flags=re.MULTILINE)
    
    # Wrap consecutive list items in ul/ol tags
    html = re.sub(r'(<li>.*?</li>(?:\n<li>.*?</li>)*)', lambda m: f'<ul>\n{m.group(1)}\n</ul>', html, flags=re.DOTALL)
    
    # Convert tables
    html = convert_tables(html)
    
    # Convert links
    html = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', html)
    
    # Convert line breaks
    html = html.replace('\n\n', '</p>\n<p>')
    html = f'<p>{html}</p>'
    
    # Clean up empty paragraphs and fix nesting
    html = re.sub(r'<p></p>', '', html)
    html = re.sub(r'<p>(<h[1-6]>.*?</h[1-6]>)</p>', r'\1', html)
    html = re.sub(r'<p>(<ul>.*?</ul>)</p>', r'\1', html, flags=re.DOTALL)
    html = re.sub(r'<p>(<pre>.*?</pre>)</p>', r'\1', html, flags=re.DOTALL)
    html = re.sub(r'<p>(<table>.*?</table>)</p>', r'\1', html, flags=re.DOTALL)
    
    return html


def generate_confluence_ready_html(md_file_path, output_file_path=None):
    """
    Generate Confluence-ready HTML from markdown file
    """
    # Read markdown content
    md_path = Path(md_file_path)
    if not md_path.exists():
        raise FileNotFoundError(f"Markdown file not found: {md_file_path}")
    
    with open(md_path, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    # Convert to HTML
    html_content = convert_markdown_to_confluence_html(md_content)
    
    # Confluence-optimized CSS
    confluence_css = """
    <style>
    /* Confluence Page Styling */
    .wiki-content {
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        line-height: 1.6;
        color: #172b4d;
        max-width: 100%;
        margin: 0;
        padding: 0;
    }
    
    /* Headers */
    h1 { 
        color: #0052cc; 
        border-bottom: 2px solid #0052cc; 
        padding-bottom: 8px;
        margin-top: 0;
        font-size: 1.8em;
    }
    h2 { 
        color: #0065ff; 
        margin-top: 32px;
        margin-bottom: 16px;
        font-size: 1.4em;
        padding-left: 0;
        border-left: 3px solid #0065ff;
        padding-left: 12px;
    }
    h3 { 
        color: #0052cc; 
        margin-top: 24px;
        margin-bottom: 12px;
        font-size: 1.2em;
    }
    h4 { 
        color: #172b4d; 
        margin-top: 20px;
        margin-bottom: 10px;
        font-weight: 600;
        font-size: 1.1em;
    }
    
    /* Code styling */
    pre {
        background: #f4f5f7;
        border: 1px solid #dfe1e6;
        border-radius: 3px;
        padding: 12px;
        overflow-x: auto;
        margin: 16px 0;
        font-family: 'SFMono-Regular', Consolas, monospace;
        font-size: 0.9em;
        line-height: 1.4;
    }
    
    code {
        background: #f4f5f7;
        color: #172b4d;
        padding: 2px 4px;
        border-radius: 3px;
        font-family: 'SFMono-Regular', Consolas, monospace;
        font-size: 0.9em;
    }
    
    /* Tables */
    table {
        border-collapse: collapse;
        width: 100%;
        margin: 16px 0;
        border: 1px solid #dfe1e6;
    }
    
    th {
        background: #f4f5f7;
        color: #172b4d;
        padding: 8px 12px;
        text-align: left;
        font-weight: 600;
        border: 1px solid #dfe1e6;
    }
    
    td {
        padding: 8px 12px;
        border: 1px solid #dfe1e6;
        vertical-align: top;
    }
    
    tr:nth-child(even) {
        background: #f8f9fa;
    }
    
    /* Lists */
    ul, ol {
        margin: 12px 0;
        padding-left: 24px;
    }
    
    li {
        margin: 6px 0;
        line-height: 1.5;
    }
    
    /* Status indicators */
    li:contains('✅') {
        color: #00875a;
    }
    
    li:contains('🔄') {
        color: #ff8b00;
    }
    
    /* Links */
    a {
        color: #0052cc;
        text-decoration: none;
    }
    
    a:hover {
        color: #0065ff;
        text-decoration: underline;
    }
    
    /* Paragraphs */
    p {
        margin: 12px 0;
        line-height: 1.6;
    }
    
    /* Info panels */
    .panel {
        border: 1px solid #dfe1e6;
        border-radius: 3px;
        margin: 16px 0;
    }
    
    .panel-info {
        border-left: 3px solid #0052cc;
        background: #e6f7ff;
    }
    
    .panel-success {
        border-left: 3px solid #00875a;
        background: #e3fcef;
    }
    
    .panel-warning {
        border-left: 3px solid #ff8b00;
        background: #fffbf0;
    }
    
    .panel-body {
        padding: 12px;
    }
    </style>
    """
    
    # Create complete HTML document for Confluence
    confluence_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Confluence-Ready HTML</title>
    {confluence_css}
</head>
<body>
    <div class="wiki-content">
        {html_content}
    </div>
</body>
</html>"""
    
    # Determine output file
    if output_file_path is None:
        output_file_path = md_path.parent / f"{md_path.stem}-confluence.html"
    
    # Write HTML file
    output_path = Path(output_file_path)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(confluence_html)
    
    return output_path


def main():
    """
    Main function to handle command-line arguments and convert the file.
    """
    if len(sys.argv) != 2:
        print("Usage: python3 md2html.py <input_markdown_file>")
        sys.exit(1)
        
    input_file = sys.argv[1]

    try:
        output_file = generate_confluence_ready_html(input_file)
        
        print(f"✅ Confluence HTML generated successfully!")
        print(f"📄 Input:  {input_file}")
        print(f"📄 Output: {output_file}")
        print(f"📊 Size:   {output_file.stat().st_size // 1024}KB")
        print(f"")
        print(f"🎯 Ready for Confluence:")
        print(f"   1. Open the HTML file in a browser")
        print(f"   2. Copy the content (Ctrl+A, Ctrl+C)")
        print(f"   3. Paste into Confluence page editor")
        
    except FileNotFoundError as e:
        print(f"❌ Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
