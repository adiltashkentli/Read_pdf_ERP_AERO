# main_task/pdf_text_extractor_page.py
from PyPDF2 import PdfReader
from main_task.base_page import BasePage

class PDFTextExtractor(BasePage):
    def __init__(self):
        super().__init__()

    def extract_text(self, pdf_path):
        text_data = []
        reader = PdfReader(pdf_path)
        for page_num, page in enumerate(reader.pages, start=1):
            text = page.extract_text()
            if text:
                text_data.append({
                    "page": page_num,
                    "text": text
                })
        return text_data