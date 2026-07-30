from __future__ import annotations

from sqlalchemy import Boolean
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from models.base_model import BaseModel


class PetImage(BaseModel):
    """
    Stores uploaded pet images.
    """

    __tablename__ = "pet_images"

    pet_id: Mapped[int] = mapped_column(
        ForeignKey("pets.id"),
        nullable=False,
        index=True,
    )

    image_path: Mapped[str] = mapped_column(
        String(500),
        nullable=False,
    )

    image_type: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True,
    )

    display_order: Mapped[int] = mapped_column(
        Integer,
        default=1,
        nullable=False,
    )

    ai_analyzed: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
    )

    ai_summary: Mapped[str | None] = mapped_column(
        String(2000),
        nullable=True,
    )

    # ==========================================================
    # Relationships
    # ==========================================================

    pet = relationship(
        "Pet",
        back_populates="images",
    )

    ai_reports = relationship(
        "AIReport",
        back_populates="pet_image",
        cascade="all, delete-orphan",
    )

    def __repr__(self) -> str:
        return (
            f"<PetImage("
            f"id={self.id}, "
            f"pet_id={self.pet_id}"
            f")>"
        )