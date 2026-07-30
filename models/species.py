from __future__ import annotations

from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from models.base_model import BaseModel


class Species(BaseModel):
    """
    Animal species (Dog, Cat, Horse, Bird...)
    """

    __tablename__ = "species"

    name: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False,
        index=True,
    )

    scientific_name: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
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
    pets = relationship(
        "Pet",
        back_populates="species",
    )

    breeds = relationship(
        "Breed",
        back_populates="species",
        cascade="all, delete-orphan",
    )

    def __repr__(self) -> str:
        return f"<Species(name='{self.name}')>"