from __future__ import annotations

from sqlalchemy.orm import Session

from models.pet_image import PetImage
from utils.file_storage import FileStorage


class ImageService:
    """
    Service for managing pet images.
    """

    @staticmethod
    def add_image(
        db: Session,
        pet_id: int,
        uploaded_file,
        image_type: str = "general",
    ) -> PetImage:

        image_path = FileStorage.save_image(uploaded_file)

        image = PetImage(
            pet_id=pet_id,
            image_path=image_path,
            image_type=image_type,
            display_order=1,
            ai_analyzed=False,
            ai_summary=None,
        )

        db.add(image)
        db.commit()
        db.refresh(image)

        return image

    @staticmethod
    def get_pet_images(
        db: Session,
        pet_id: int,
    ) -> list[PetImage]:

        return (
            db.query(PetImage)
            .filter(PetImage.pet_id == pet_id)
            .order_by(PetImage.display_order)
            .all()
        )

    @staticmethod
    def delete_image(
        db: Session,
        image_id: int,
    ) -> bool:

        image = (
            db.query(PetImage)
            .filter(PetImage.id == image_id)
            .first()
        )

        if image is None:
            return False

        FileStorage.delete_image(image.image_path)

        db.delete(image)
        db.commit()

        return True