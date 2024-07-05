from functools import cache
from pathlib import Path

import PyPDF2


class PdfConverter:

    def __init__(self, pdf_path: Path):
        self.pdf_path = pdf_path

    @cache
    def convert_to_text(self) -> str:
        with open(self.pdf_path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            text = ""
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text += page.extract_text()
        return text
