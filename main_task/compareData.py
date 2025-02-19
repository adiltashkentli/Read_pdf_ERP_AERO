from PyPDF2 import PdfReader
import pdfplumber
from PIL import Image
import os
import cv2

def extract_text_with_pypdf(pdf_path):
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


def extract_barcodes(pdf_path):
    barcodes = []
    with pdfplumber.open(pdf_path) as pdf:
        for page_num, page in enumerate(pdf.pages, start=1):
            # Преобразуем страницу PDF в изображение
            im = page.to_image(resolution=300).original
            temp_image_path = f"page_{page_num}.png"
            im.save(temp_image_path)
            
            # Загружаем изображение с помощью OpenCV
            img = cv2.imread(temp_image_path)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            
            # Декодируем баркоды
            barcode_detector = cv2.barcode.BarcodeDetector()
            retval, decoded_info, decoded_type = barcode_detector.detectAndDecode(gray)
            
            if retval:
                for info, barcode_type in zip(decoded_info, decoded_type):
                    barcodes.append({
                        "page": page_num,
                        "data": info,
                        "type": barcode_type
                    })
            
            # Удаляем временное изображение
            os.remove(temp_image_path)
    
    return barcodes

def compare_text_data(reference_data, comparison_data):
    mismatches = []
    for ref_entry in reference_data:
        match_found = False
        for comp_entry in comparison_data:
            if ref_entry["page"] == comp_entry["page"] and ref_entry["text"] == comp_entry["text"]:
                match_found = True
                break
        if not match_found:
            mismatches.append(ref_entry)
    return mismatches

def compare_barcodes(reference_barcodes, comparison_barcodes):
    mismatches = []
    for ref_barcode in reference_barcodes:
        match_found = False
        for comp_barcode in comparison_barcodes:
            if ref_barcode["data"] == comp_barcode["data"]:
                match_found = True
                break
        if not match_found:
            mismatches.append(ref_barcode)
    return mismatches

# main script
file_paths = ['test_task.pdf', 'compare1.pdf', 'compare2.pdf']

# Шаг 1: Извлечение эталонных данных
reference_text_data = extract_text_with_pypdf(file_paths[0])
reference_barcodes = extract_barcodes(file_paths[0])

# Шаг 2: Извлечение данных из других файлов и сравнение
for file_path in file_paths[1:]:
    print(f"Compare: {file_path}")
    
    # Извлечение текстовых данных
    comparison_text_data = extract_text_with_pypdf(file_path)
    text_mismatches = compare_text_data(reference_text_data, comparison_text_data)
    if text_mismatches:
        print("Mismatch(es):")
        for mismatch in text_mismatches:
            print(mismatch)
    else:
        print("All data mathched.")
    
    # Извлечение и сравнение баркодов
    comparison_barcodes = extract_barcodes(file_path)
    barcode_mismatches = compare_barcodes(reference_barcodes, comparison_barcodes)
    if barcode_mismatches:
        print("Mismatch(es) in barcodes:")
        for mismatch in barcode_mismatches:
            print(mismatch)
    else:
        print("Barcodes all matched.")