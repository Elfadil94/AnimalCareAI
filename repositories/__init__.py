"""
AnimalCareAI Models Package

Importing this package loads all SQLAlchemy models so that
relationship() references (e.g. "Pet", "Owner") can be resolved.
"""

from .owner import Owner
from .species import Species
from .breed import Breed
from .pet import Pet
from .pet_image import PetImage

__all__ = [
    "Owner",
    "Species",
    "Breed",
    "Pet",
    "PetImage",
]