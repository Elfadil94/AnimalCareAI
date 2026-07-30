from __future__ import annotations

from sqlalchemy.orm import Session

from models.ai_report import AIReport


class AIReportService:
    """
    Service responsible for managing AI reports.
    """

    @staticmethod
    def create_report(
        db: Session,
        pet_id: int,
        pet_image_id: int,
        model_name: str,
        report: str,
        symptoms: str | None = None,
        confidence: str | None = None,
    ) -> AIReport:

        ai_report = AIReport(
            pet_id=pet_id,
            pet_image_id=pet_image_id,
            model_name=model_name,
            symptoms=symptoms,
            report=report,
            confidence=confidence,
        )

        db.add(ai_report)
        db.commit()
        db.refresh(ai_report)

        return ai_report

    @staticmethod
    def get_report(
        db: Session,
        report_id: int,
    ) -> AIReport | None:

        return (
            db.query(AIReport)
            .filter(AIReport.id == report_id)
            .first()
        )

    @staticmethod
    def get_reports_for_pet(
        db: Session,
        pet_id: int,
    ) -> list[AIReport]:

        return (
            db.query(AIReport)
            .filter(AIReport.pet_id == pet_id)
            .order_by(AIReport.created_at.desc())
            .all()
        )

    @staticmethod
    def get_latest_reports(
        db: Session,
        limit: int = 10,
    ) -> list[AIReport]:

        return (
            db.query(AIReport)
            .order_by(AIReport.created_at.desc())
            .limit(limit)
            .all()
        )

    @staticmethod
    def delete_report(
        db: Session,
        report_id: int,
    ) -> bool:

        report = (
            db.query(AIReport)
            .filter(AIReport.id == report_id)
            .first()
        )

        if report is None:
            return False

        db.delete(report)
        db.commit()

        return True