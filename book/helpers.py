import uuid

class SaveMedia:
    @staticmethod
    def save_book_image_path(instance, filename):
        image_extension = filename.split('.')[-1]
        return f"book/{uuid.uuid4()}.{image_extension}"
