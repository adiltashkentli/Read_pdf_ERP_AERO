# main_task/pdf_barcode_extractor_page.py
import pdfplumber
import cv2
from PIL import Image
from main_task.base_page import BasePage

class PDFBarcodeExtractor(BasePage):
    def __init__(self):
        super().__init__()

    def extract_barcodes(self, pdf_path):
        barcodes = []
        with pdfplumber.open(pdf_path) as pdf:
            for page_num, page in enumerate(pdf.pages, start=1):
                # Преобразуем страницу PDF в изображение
                im = page.to_image(resolution=300).original
                temp_image_path = f"page_{page_num}.png"
                self.save_temp_image(im, temp_image_path)

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
                self.remove_temp_file(temp_image_path)

        return barcodes