from __future__ import annotations

from datetime import date

from sqlalchemy import Boolean
from sqlalchemy import Date
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from models.base_model import BaseModel


class Pet(BaseModel):
    """
    Main Pet model.
    """

    __tablename__ = "pets"

    # ==========================================================
    # Basic Information
    # ==========================================================

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        index=True,
    )

    owner_id: Mapped[int] = mapped_column(
        ForeignKey("owners.id"),
        nullable=False,
    )

    species_id: Mapped[int] = mapped_column(
        ForeignKey("species.id"),
        nullable=False,
    )

    breed_id: Mapped[int | None] = mapped_column(
        ForeignKey("breeds.id"),
        nullable=True,
    )

    # ==========================================================
    # Birth Information
    # ==========================================================

    birth_date: Mapped[date | None] = mapped_column(
        Date,
        nullable=True,
    )

    estimated_age: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    # ==========================================================
    # Gender
    # ==========================================================

    gender: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
    )

    neutered: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
    )

    # ==========================================================
    # Physical Information
    # ==========================================================

    weight_kg: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    color: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    mixed_breed: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
    )

    # ==========================================================
    # Identification
    # ==========================================================

    microchip_number: Mapped[str | None] = mapped_column(
        String(100),
        unique=True,
        nullable=True,
    )

    passport_number: Mapped[str | None] = mapped_column(
        String(100),
        unique=True,
        nullable=True,
    )

    blood_type: Mapped[str | None] = mapped_column(
        String(10),
        nullable=True,
    )

    # ==========================================================
    # Status
    # ==========================================================

    is_alive: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )

    # ==========================================================
    # Medical Notes
    # ==========================================================

    allergies: Mapped[str | None] = mapped_column(
        String(1000),
        nullable=True,
    )

    chronic_conditions: Mapped[str | None] = mapped_column(
        String(1000),
        nullable=True,
    )

    notes: Mapped[str | None] = mapped_column(
        String(2000),
        nullable=True,
    )

    # ==========================================================
    # Relationships
    # ==========================================================

    owner = relationship(
        "Owner",
        back_populates="pets",
    )

    species = relationship(
        "Species",
        back_populates="pets",
    )

    breed = relationship(
        "Breed",
        back_populates="pets",
    )

    images = relationship(
        "PetImage",
        back_populates="pet",
        cascade="all, delete-orphan",
    )

    ai_reports = relationship(
        "AIReport",
        back_populates="pet",
        cascade="all, delete-orphan",
    )

    def __repr__(self) -> str:
        return (
            f"<Pet("
            f"id={self.id}, "
            f"name='{self.name}'"
            f")>"
        )