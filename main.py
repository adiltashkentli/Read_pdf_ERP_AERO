# main.py
from main_task.pdf_text_extractor_page import PDFTextExtractor
from main_task.pdf_barcode_extractor_page import PDFBarcodeExtractor
from main_task.pdf_comparison_page import PDFComparison

def main():
    file_paths = ['test_task.pdf', 'compare1.pdf', 'compare2.pdf']

    # Инициализация экстракторов и компаратора
    text_extractor = PDFTextExtractor()
    barcode_extractor = PDFBarcodeExtractor()
    comparison = PDFComparison()

    # Шаг 1: Извлечение эталонных данных
    reference_text_data = text_extractor.extract_text(file_paths[0])
    reference_barcodes = barcode_extractor.extract_barcodes(file_paths[0])

    # Шаг 2: Извлечение данных из других файлов и сравнение
    for file_path in file_paths[1:]:
        print(f"Compare: {file_path}")

        # Извлечение текстовых данных
        comparison_text_data = text_extractor.extract_text(file_path)
        text_mismatches = comparison.compare_text_data(reference_text_data, comparison_text_data)
        if text_mismatches:
            print("Mismatch(es):")
            for mismatch in text_mismatches:
                print(mismatch)
        else:
            print("All data matched.")

        # Извлечение и сравнение баркодов
        comparison_barcodes = barcode_extractor.extract_barcodes(file_path)
        barcode_mismatches = comparison.compare_barcodes(reference_barcodes, comparison_barcodes)
        if barcode_mismatches:
            print("Mismatch(es) in barcodes:")
            for mismatch in barcode_mismatches:
                print(mismatch)
        else:
            print("Barcodes all matched.")

if __name__ == "__main__":
    main()