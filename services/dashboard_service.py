from __future__ import annotations

from sqlalchemy import func
from sqlalchemy.orm import Session
from sqlalchemy.orm import joinedload

from models.owner import Owner
from models.pet import Pet
from models.species import Species


class DashboardService:
    """
    Dashboard statistics service.
    """

    @staticmethod
    def get_statistics(db: Session) -> dict:

        owners = db.query(func.count(Owner.id)).scalar() or 0

        pets = db.query(func.count(Pet.id)).scalar() or 0

        species = db.query(func.count(Species.id)).scalar() or 0

        latest_pets = (
            db.query(Pet)
            .options(
                joinedload(Pet.owner),
                joinedload(Pet.species),
            )
            .order_by(Pet.id.desc())
            .limit(5)
            .all()
        )

        return {
            "owners": owners,
            "pets": pets,
            "species": species,
            "latest_pets": latest_pets,
        }