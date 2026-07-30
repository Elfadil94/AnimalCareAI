from __future__ import annotations

import mimetypes
from pathlib import Path

from google.genai import types
from sqlalchemy.orm import Session

from ai.gemini_client import GeminiClient
from ai.prompts import build_prompt
from services.ai_report_service import AIReportService


class AIService:
    """
    AI service responsible for analyzing pet images using Gemini.
    """

    @staticmethod
    def analyze_image(
        db: Session,
        pet_id: int,
        pet_image_id: int,
        image_path: str,
        symptoms: str | None = None,
    ) -> str:

        path = Path(image_path)

        if not path.exists():
            raise FileNotFoundError(
                f"Image not found: {image_path}"
            )

        mime_type, _ = mimetypes.guess_type(path)

        if mime_type is None:
            mime_type = "image/jpeg"

        with open(path, "rb") as f:
            image_bytes = f.read()

        prompt = build_prompt(symptoms)

        response = GeminiClient.client().models.generate_content(
            model=GeminiClient.model(),
            contents=[
                prompt,
                types.Part.from_bytes(
                    data=image_bytes,
                    mime_type=mime_type,
                ),
            ],
        )

        report = (
            response.text.strip()
            if response.text
            else "No response returned from Gemini."
        )

        confidence = None

        report_lower = report.lower()

        if "high" in report_lower:
            confidence = "High"
        elif "medium" in report_lower:
            confidence = "Medium"
        elif "low" in report_lower:
            confidence = "Low"

        AIReportService.create_report(
            db=db,
            pet_id=pet_id,
            pet_image_id=pet_image_id,
            model_name=GeminiClient.model(),
            report=report,
            symptoms=symptoms,
            confidence=confidence,
        )

        return report