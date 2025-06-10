# PDF Upload Utility

This project provides simple scripts to parse PDF documents for "Gross Written Premium" figures from several insurance categories. It is designed as a lightweight tool that can be used from the command line to extract those values and output them to CSV.

## Setup

1. Ensure Python 3.8+ is installed.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Use the command-line interface to parse one or more PDF files:
   ```bash
   python -m src.cli path/to/document.pdf another.pdf
   ```
   This will produce a CSV file (`output.csv` by default) containing the extracted values.

## Project Structure

- `src/parser.py` – utilities for reading PDF files and locating the required values.
- `src/cli.py` – simple CLI wrapper that calls the parser and writes output to CSV.
- `requirements.txt` – Python dependencies for the project.

The repository currently contains an `index.html` placeholder file.
