from pydantic import BaseModel, Field


class PetAnalysis(BaseModel):
    possible_causes: list[str] = Field(
        description="Three possible causes."
    )

    risk_level: str = Field(
        description="Low, Medium or High."
    )

    recommendations: list[str] = Field(
        description="Three recommendations."
    )

    visit_vet: str = Field(
        description="Advice about visiting a veterinarian."
    )

    emergency: bool = Field(
        description="Whether the case is an emergency."
    )

    disclaimer: str = Field(
        description="Educational disclaimer."
    )