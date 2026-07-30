from __future__ import annotations

from database.session import session_scope

# Import models so SQLAlchemy registers them
from models.owner import Owner
from models.species import Species
from models.breed import Breed
from models.pet import Pet
from models.pet_image import PetImage


SPECIES = [
    "Dog",
    "Cat",
    "Horse",
    "Rabbit",
    "Bird",
    "Fish",
    "Hamster",
    "Turtle",
    "Cow",
    "Goat",
    "Sheep",
]


def seed_species() -> None:
    with session_scope() as session:
        existing = {
            species.name
            for species in session.query(Species).all()
        }

        added = 0

        for name in SPECIES:
            if name in existing:
                continue

            session.add(
                Species(
                    name=name,
                    is_active=True,
                )
            )

            added += 1

        print(f"Added {added} species.")


def main() -> None:
    print("=" * 50)
    print("AnimalCareAI Seeder")
    print("=" * 50)

    seed_species()

    print("=" * 50)
    print("Database seeding completed.")
    print("=" * 50)


if __name__ == "__main__":
    main()