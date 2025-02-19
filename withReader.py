from PyPDF2 import PdfReader

# Функция для извлечения текста
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

# Функция для сравнения текстовых данных
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

# Основной код
file_paths = ['test_task.pdf', 'compare1.pdf', 'compare2.pdf']

# Шаг 1: Извлечение эталонных данных
reference_text_data = extract_text_with_pypdf(file_paths[0])

# Шаг 2: Извлечение данных из других файлов и сравнение
for file_path in file_paths[1:]:
    print(f"Сравнение с файлом: {file_path}")
    
    # Извлечение текстовых данных
    comparison_text_data = extract_text_with_pypdf(file_path)
    text_mismatches = compare_text_data(reference_text_data, comparison_text_data)
    if text_mismatches:
        print("Несоответствия в тексте:")
        for mismatch in text_mismatches:
            print(mismatch)
    else:
        print("Текст полностью совпадает.")