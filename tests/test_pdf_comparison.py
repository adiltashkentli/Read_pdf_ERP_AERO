# tests/test_pdf_comparison.py
import unittest
from main_task.pdf_text_extractor_page import PDFTextExtractor
from main_task.pdf_barcode_extractor_page import PDFBarcodeExtractor
from main_task.pdf_comparison_page import PDFComparison

class TestPDFComparison(unittest.TestCase):
    def setUp(self):
        self.text_extractor = PDFTextExtractor()
        self.barcode_extractor = PDFBarcodeExtractor()
        self.comparison = PDFComparison()

    def test_text_comparison(self):
        reference_text = self.text_extractor.extract_text("test_task.pdf")
        comparison_text = self.text_extractor.extract_text("compare1.pdf")
        mismatches = self.comparison.compare_text_data(reference_text, comparison_text)
        self.assertEqual(len(mismatches), 0, f"Text mismatches found: {mismatches}")

    def test_barcode_comparison(self):
        reference_barcodes = self.barcode_extractor.extract_barcodes("test_task.pdf")
        comparison_barcodes = self.barcode_extractor.extract_barcodes("compare1.pdf")
        mismatches = self.comparison.compare_barcodes(reference_barcodes, comparison_barcodes)
        self.assertEqual(len(mismatches), 0, f"Barcode mismatches found: {mismatches}")

if __name__ == "__main__":
    unittest.main()