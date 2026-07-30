from __future__ import annotations

from sqlalchemy.orm import Session

from models.owner import Owner


class OwnerService:

    @staticmethod
    def create_owner(
        db: Session,
        first_name: str,
        last_name: str,
        email: str | None,
        phone: str | None,
        country: str | None,
        city: str | None,
        address: str | None,
        postal_code: str | None,
    ) -> Owner:

        owner = Owner(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            country=country,
            city=city,
            address=address,
            postal_code=postal_code,
            is_active=True,
        )

        db.add(owner)
        db.commit()
        db.refresh(owner)

        return owner

    @staticmethod
    def get_all(db: Session):

        return (
            db.query(Owner)
            .order_by(Owner.first_name)
            .all()
        )