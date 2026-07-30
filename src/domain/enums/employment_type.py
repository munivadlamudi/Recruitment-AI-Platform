"""Employment-type classifications used by job and employment records."""

from enum import StrEnum


class EmploymentType(StrEnum):
    """The contractual arrangement for a role."""

    FULL_TIME = "full_time"
    PART_TIME = "part_time"
    CONTRACT = "contract"
    INTERNSHIP = "internship"
    FREELANCE = "freelance"
    TEMPORARY = "temporary"
