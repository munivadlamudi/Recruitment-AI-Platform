"""Candidate work-experience entity."""

from pydantic import Field

from src.domain.enums import EmploymentType
from src.domain.models.base import DomainModel
from src.domain.value_objects import DateRange


class Experience(DomainModel):
    """A role held by a candidate at an organization."""

    company: str = Field(min_length=1, max_length=200)
    designation: str = Field(min_length=1, max_length=150)
    period: DateRange
    employment_type: EmploymentType | None = None
    location: str | None = Field(default=None, max_length=150)
    responsibilities: list[str] = Field(default_factory=list)
