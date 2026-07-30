"""Tests for candidate domain entities and aggregate validation."""

from datetime import date

import pytest
from pydantic import ValidationError

from src.domain.enums import DegreeLevel, EmploymentType, ProficiencyLevel
from src.domain.models import Candidate, Certification, Education, Experience, Skill
from src.domain.value_objects import ContactInfo, DateRange


def make_contact() -> ContactInfo:
    """Create valid contact data shared by aggregate tests."""
    return ContactInfo(email="ada@example.com", github_url="https://github.com/ada")


def test_candidate_models_a_complete_profile() -> None:
    """Candidate preserves structured resume information across entities."""
    candidate = Candidate(
        full_name="Ada Lovelace",
        contact_info=make_contact(),
        skills=[Skill(name="Python", proficiency=ProficiencyLevel.EXPERT, years_of_experience=5)],
        education=[
            Education(
                institution="Example University",
                degree="B.Tech",
                level=DegreeLevel.BACHELOR,
            )
        ],
        experience=[
            Experience(
                company="Analytical Engines Ltd.",
                designation="Software Engineer",
                employment_type=EmploymentType.FULL_TIME,
                period=DateRange(start_date=date(2020, 1, 1)),
            )
        ],
    )

    assert candidate.full_name == "Ada Lovelace"
    assert candidate.skills[0].proficiency is ProficiencyLevel.EXPERT
    assert candidate.experience[0].employment_type is EmploymentType.FULL_TIME


def test_candidate_rejects_duplicate_skills_case_insensitively() -> None:
    """Repeated skills create ambiguous matching input and are rejected."""
    with pytest.raises(ValidationError, match="must not contain duplicates"):
        Candidate(
            full_name="Ada Lovelace",
            contact_info=make_contact(),
            skills=[Skill(name="Python"), Skill(name="python")],
        )


def test_certification_rejects_expiry_before_issue_date() -> None:
    """Certification dates must be chronological."""
    with pytest.raises(ValidationError, match="cannot be earlier"):
        Certification(
            name="Cloud Certificate",
            issuer="Cloud Provider",
            issued_on=date(2025, 1, 1),
            expires_on=date(2024, 12, 31),
        )
