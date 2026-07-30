from __future__ import annotations

from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from models.base_model import BaseModel


class Breed(BaseModel):
    """
    Animal breed (Golden Retriever, Persian Cat, etc.)
    """

    __tablename__ = "breeds"

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        index=True,
    )

    species_id: Mapped[int] = mapped_column(
        ForeignKey("species.id"),
        nullable=False,
    )

    description: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True,
    )

    is_active: Mapped[bool] = mapped_column(
        default=True,
        nullable=False,
    )

    # Relationships
    species = relationship(
        "Species",
        back_populates="breeds",
    )

    pets = relationship(
        "Pet",
        back_populates="breed",
    )

    def __repr__(self) -> str:
        return f"<Breed(name='{self.name}')>"