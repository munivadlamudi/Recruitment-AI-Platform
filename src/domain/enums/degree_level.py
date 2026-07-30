"""Education-level classifications."""

from enum import StrEnum


class DegreeLevel(StrEnum):
    """The highest normalized level associated with an education record."""

    HIGH_SCHOOL = "high_school"
    DIPLOMA = "diploma"
    ASSOCIATE = "associate"
    BACHELOR = "bachelor"
    MASTER = "master"
    DOCTORATE = "doctorate"
    OTHER = "other"
