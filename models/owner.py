from __future__ import annotations

from sqlalchemy import Boolean
from sqlalchemy import Index
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from models.base_model import BaseModel


class Owner(BaseModel):
    """
    Pet owner.
    """

    __tablename__ = "owners"

    __table_args__ = (
        Index("idx_owner_email", "email"),
        Index("idx_owner_phone", "phone"),
    )

    # ======================================================
    # Personal Information
    # ======================================================

    first_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    last_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    email: Mapped[str | None] = mapped_column(
        String(255),
        unique=True,
    )

    phone: Mapped[str | None] = mapped_column(
        String(50),
    )

    # ======================================================
    # Address
    # ======================================================

    country: Mapped[str | None] = mapped_column(
        String(100),
    )

    city: Mapped[str | None] = mapped_column(
        String(100),
    )

    address: Mapped[str | None] = mapped_column(
        String(255),
    )

    postal_code: Mapped[str | None] = mapped_column(
        String(30),
    )

    # ======================================================
    # Status
    # ======================================================

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )

    # ======================================================
    # Relationships
    # ======================================================

    pets = relationship(
        "Pet",
        back_populates="owner",
        cascade="all, delete-orphan",
    )

    def __repr__(self) -> str:
        return (
            f"<Owner("
            f"id={self.id}, "
            f"name='{self.first_name} {self.last_name}'"
            f")>"
        )