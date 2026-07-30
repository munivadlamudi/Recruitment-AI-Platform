"""Skill-proficiency classifications."""

from enum import StrEnum


class ProficiencyLevel(StrEnum):
    """A normalized self-reported or assessed skill level."""

    BEGINNER = "beginner"
    INTERMEDIATE = "intermediate"
    ADVANCED = "advanced"
    EXPERT = "expert"
