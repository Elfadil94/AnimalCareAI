from __future__ import annotations

from typing import Generic, Type, TypeVar

from sqlalchemy import select
from sqlalchemy.orm import Session

ModelType = TypeVar("ModelType")


class BaseRepository(Generic[ModelType]):
    """
    Base repository that provides common CRUD operations.
    """

    def __init__(self, session: Session, model: Type[ModelType]):
        self.session = session
        self.model = model

    # ======================================================
    # CREATE
    # ======================================================

    def create(self, obj: ModelType) -> ModelType:
        self.session.add(obj)
        self.session.commit()
        self.session.refresh(obj)
        return obj

    # ======================================================
    # READ
    # ======================================================

    def get_by_id(self, obj_id: int) -> ModelType | None:
        return self.session.get(self.model, obj_id)

    def get_all(self) -> list[ModelType]:
        statement = select(self.model)
        return list(self.session.scalars(statement).all())

    # ======================================================
    # UPDATE
    # ======================================================

    def update(self, obj: ModelType) -> ModelType:
        self.session.add(obj)
        self.session.commit()
        self.session.refresh(obj)
        return obj

    # ======================================================
    # DELETE
    # ======================================================

    def delete(self, obj: ModelType) -> None:
        self.session.delete(obj)
        self.session.commit()

    # ======================================================
    # EXISTS
    # ======================================================

    def exists(self, obj_id: int) -> bool:
        return self.get_by_id(obj_id) is not None