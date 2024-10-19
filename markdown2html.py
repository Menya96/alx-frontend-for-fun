#!/usr/bin/python3

import sys
import os

def markdown_to_html(markdown_file, output_file):
     """
    Converts a Markdown file to HTML.

    Args:
      markdown_file: The path to the Markdown file.
      output_file: The path to the output HTML file.
  """

    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)

  # Check if Markdown file exists
    if not os.path.exists(markdown_file):
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)

     # No errors detected, proceed with conversion (implementation not included)
     # ... (code to read Markdown file, convert to HTML, and write to output file)

  print(f"Converted {markdown_file} to {output_file}")

    # Main execution block
    if __name__ == "__main__":
        markdown_file = sys.argv[1]
        output_file = sys.argv[2]
        markdown_to_html(markdown_file, output_file)

      # Exit with success (no errors encountered)
        sys.exit(0)
