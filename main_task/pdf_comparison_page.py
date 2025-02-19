# main_task/pdf_comparison_page.py
class PDFComparison:
    def __init__(self):
        pass

    @staticmethod
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

    @staticmethod
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