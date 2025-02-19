import os

class BasePage:
    def __init__(self):
        pass

    @staticmethod
    def save_temp_image(image, file_path):
        """Сохраняет временное изображение."""
        image.save(file_path)

    @staticmethod
    def remove_temp_file(file_path):
        """Удаляет временный файл."""
        if os.path.exists(file_path):
            os.remove(file_path)