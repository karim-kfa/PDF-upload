import argparse
import csv
from pathlib import Path
from typing import List

from .parser import extract_text_from_pdf, parse_gross_written_premium


def parse_files(paths: List[Path], output: Path):
    with output.open("w", newline="") as csvfile:
        fieldnames = ["file", "medical", "motor", "p_and_c", "p_and_s"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for pdf_path in paths:
            text = extract_text_from_pdf(str(pdf_path))
            values = parse_gross_written_premium(text)
            values["file"] = str(pdf_path)
            writer.writerow(values)


def main(argv=None):
    parser = argparse.ArgumentParser(description="Extract Gross Written Premium values from PDFs")
    parser.add_argument("pdfs", nargs="+", type=Path, help="PDF files to parse")
    parser.add_argument("-o", "--output", type=Path, default=Path("output.csv"), help="CSV output path")
    args = parser.parse_args(argv)

    parse_files(args.pdfs, args.output)


if __name__ == "__main__":
    main()
