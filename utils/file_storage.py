from __future__ import annotations

from pathlib import Path
from uuid import uuid4

from streamlit.runtime.uploaded_file_manager import UploadedFile


UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)


class FileStorage:
    """
    Handles saving uploaded files to disk.
    """

    @staticmethod
    def save_image(file: UploadedFile) -> str:
        """
        Save an uploaded image and return its relative path.
        """

        extension = Path(file.name).suffix.lower()

        filename = f"{uuid4()}{extension}"

        destination = UPLOAD_DIR / filename

        with open(destination, "wb") as output:
            output.write(file.getbuffer())

        return str(destination)

    @staticmethod
    def delete_image(path: str) -> None:

        image = Path(path)

        if image.exists():
            image.unlink()

    @staticmethod
    def image_exists(path: str) -> bool:

        return Path(path).exists()