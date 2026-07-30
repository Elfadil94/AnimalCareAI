from __future__ import annotations

from database.base import Base
from database.connection import engine

# ==========================================================
# Import all models so SQLAlchemy registers every table
# ==========================================================

from models.owner import Owner
from models.species import Species
from models.breed import Breed
from models.pet import Pet
from models.pet_image import PetImage
from models.ai_report import AIReport


def create_database() -> None:
    """
    Create all database tables.
    """

    Base.metadata.create_all(bind=engine)

    print("=" * 50)
    print("AnimalCareAI Database Created Successfully")
    print("=" * 50)


if __name__ == "__main__":
    create_database()