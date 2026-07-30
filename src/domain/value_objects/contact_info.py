"""Candidate contact information value object."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, EmailStr, Field, HttpUrl, field_validator


class ContactInfo(BaseModel):
    """Validated contact channels belonging to a candidate."""

    model_config = ConfigDict(extra="forbid", frozen=True, str_strip_whitespace=True)

    email: EmailStr
    phone: str | None = Field(default=None, min_length=5, max_length=30)
    linkedin_url: HttpUrl | None = None
    github_url: HttpUrl | None = None

    @field_validator("phone")
    @classmethod
    def validate_phone(cls, value: str | None) -> str | None:
        """Ensure a phone number contains enough numeric characters to be useful."""
        if value is None:
            return None
        digit_count = sum(character.isdigit() for character in value)
        if digit_count < 5:
            raise ValueError("phone must contain at least five digits")
        return value
