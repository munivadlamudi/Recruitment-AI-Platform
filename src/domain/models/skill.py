"""Candidate skill entity."""

from pydantic import Field

from src.domain.enums import ProficiencyLevel
from src.domain.models.base import DomainModel


class Skill(DomainModel):
    """A normalized skill and its optional proficiency evidence."""

    name: str = Field(min_length=1, max_length=100)
    proficiency: ProficiencyLevel | None = None
    years_of_experience: float | None = Field(default=None, ge=0, le=80)
