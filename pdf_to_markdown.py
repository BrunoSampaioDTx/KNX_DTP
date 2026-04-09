import sys
import argparse
from pathlib import Path

import pymupdf4llm


def convert_pdf_to_markdown(pdf_path: str, output_path: str | None = None) -> str:
    pdf = Path(pdf_path)
    if not pdf.exists():
        raise FileNotFoundError(f"PDF not found: {pdf_path}")

    md_text = pymupdf4llm.to_markdown(str(pdf))

    if output_path is None:
        output_path = str(pdf.with_suffix(".md"))

    Path(output_path).write_text(md_text, encoding="utf-8")
    print(f"Converted: {pdf.name} -> {output_path}")
    return output_path


def main():
    parser = argparse.ArgumentParser(description="Convert PDF to Markdown")
    parser.add_argument("pdf", help="Path to the PDF file")
    parser.add_argument("-o", "--output", help="Output Markdown file path (default: same name with .md)")
    args = parser.parse_args()

    convert_pdf_to_markdown(args.pdf, args.output)


if __name__ == "__main__":
    main()


    # run as: python pdf_to_markdown.py "03_07_02 Datapoint Types v02.02.01 AS.pdf" -o "aux__aa/pdf.md"
