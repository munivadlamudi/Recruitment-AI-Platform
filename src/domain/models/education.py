"""Candidate education entity."""

from pydantic import Field

from src.domain.enums import DegreeLevel
from src.domain.models.base import DomainModel
from src.domain.value_objects import DateRange


class Education(DomainModel):
    """A completed or in-progress education credential."""

    institution: str = Field(min_length=1, max_length=200)
    degree: str = Field(min_length=1, max_length=150)
    level: DegreeLevel = DegreeLevel.OTHER
    field_of_study: str | None = Field(default=None, max_length=150)
    period: DateRange | None = None
    grade: str | None = Field(default=None, max_length=50)
