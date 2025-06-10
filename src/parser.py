import re
from typing import Dict
from pdfminer.high_level import extract_text


def extract_text_from_pdf(pdf_path: str) -> str:
    """Return all text from the given PDF file."""
    return extract_text(pdf_path)


GWP_CATEGORIES = {
    "medical": re.compile(r"Medical.*?([0-9,\.]+)", re.IGNORECASE),
    "motor": re.compile(r"Motor.*?([0-9,\.]+)", re.IGNORECASE),
    "p_and_c": re.compile(r"P\s*&\s*C.*?([0-9,\.]+)", re.IGNORECASE),
    "p_and_s": re.compile(r"P\s*&\s*S.*?([0-9,\.]+)", re.IGNORECASE),
}


def parse_gross_written_premium(text: str) -> Dict[str, str]:
    """Search the provided text for Gross Written Premium figures.

    Returns a dictionary mapping categories to the captured numeric strings.
    """
    results: Dict[str, str] = {}
    # Attempt to limit search around a heading containing 'Gross Written Premium'
    # but fallback to full text search if not found
    gwp_section_match = re.search(r"Gross\s+Written\s+Premium(.+)", text, re.IGNORECASE | re.DOTALL)
    section = gwp_section_match.group(1) if gwp_section_match else text

    for name, pattern in GWP_CATEGORIES.items():
        m = pattern.search(section)
        if m:
            results[name] = m.group(1)
        else:
            results[name] = ""
    return results


def extract_gwp_from_pdf(pdf_path: str, sub_category: str) -> str:
    """Extract the numeric GWP value for a given sub-category from a PDF.

    ``sub_category`` should be one of: 'medical', 'motor', 'p_and_c', 'p_and_s'.
    """
    text = extract_text(pdf_path)
    results = parse_gross_written_premium(text)

    key = sub_category.lower().strip()
    if key in results:
        return results[key]
    raise ValueError(f"Sub-category '{sub_category}' not recognized.")
