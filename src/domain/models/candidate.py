"""Candidate aggregate root."""

from pydantic import Field, model_validator

from src.domain.models.base import DomainModel
from src.domain.models.certification import Certification
from src.domain.models.education import Education
from src.domain.models.experience import Experience
from src.domain.models.skill import Skill
from src.domain.value_objects import ContactInfo


class Candidate(DomainModel):
    """A candidate's structured profile extracted from their resume."""

    full_name: str = Field(min_length=1, max_length=200)
    contact_info: ContactInfo
    location: str | None = Field(default=None, max_length=150)
    skills: list[Skill] = Field(default_factory=list)
    education: list[Education] = Field(default_factory=list)
    experience: list[Experience] = Field(default_factory=list)
    certifications: list[Certification] = Field(default_factory=list)
    projects: list[str] = Field(default_factory=list)

    @model_validator(mode="after")
    def ensure_unique_skills(self) -> "Candidate":
        """Prevent duplicate skills differing only by letter case."""
        names = [skill.name.casefold() for skill in self.skills]
        if len(names) != len(set(names)):
            raise ValueError("skills must not contain duplicates")
        return self
