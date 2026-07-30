from __future__ import annotations

from sqlalchemy.orm import Session
from sqlalchemy.orm import joinedload

from models.owner import Owner
from models.pet import Pet
from models.species import Species


class PetService:
    """
    Business logic for Pet operations.
    """

    @staticmethod
    def create_pet(
        db: Session,
        name: str,
        owner_id: int,
        species_id: int,
        gender: str,
        weight_kg: float | None = None,
        color: str | None = None,
    ) -> Pet:

        pet = Pet(
            name=name,
            owner_id=owner_id,
            species_id=species_id,
            gender=gender,
            weight_kg=weight_kg,
            color=color,
            is_alive=True,
            is_active=True,
        )

        db.add(pet)
        db.commit()
        db.refresh(pet)

        return pet

    @staticmethod
    def get_all_pets(db: Session) -> list[Pet]:
        """
        Return all pets with Owner and Species loaded.
        """

        return (
            db.query(Pet)
            .options(
                joinedload(Pet.owner),
                joinedload(Pet.species),
            )
            .order_by(Pet.name.asc())
            .all()
        )

    @staticmethod
    def get_pet_by_id(
        db: Session,
        pet_id: int,
    ) -> Pet | None:

        return (
            db.query(Pet)
            .options(
                joinedload(Pet.owner),
                joinedload(Pet.species),
            )
            .filter(Pet.id == pet_id)
            .first()
        )

    @staticmethod
    def get_all_owners(db: Session) -> list[Owner]:

        return (
            db.query(Owner)
            .order_by(
                Owner.first_name.asc(),
                Owner.last_name.asc(),
            )
            .all()
        )

    @staticmethod
    def get_all_species(db: Session) -> list[Species]:

        return (
            db.query(Species)
            .order_by(Species.name.asc())
            .all()
        )