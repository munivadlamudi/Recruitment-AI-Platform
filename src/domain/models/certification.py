"""Candidate certification entity."""

from datetime import date

from pydantic import Field, model_validator

from src.domain.models.base import DomainModel


class Certification(DomainModel):
    """A professional certification held by a candidate."""

    name: str = Field(min_length=1, max_length=200)
    issuer: str = Field(min_length=1, max_length=200)
    issued_on: date | None = None
    expires_on: date | None = None
    credential_id: str | None = Field(default=None, max_length=150)
    credential_url: str | None = Field(default=None, max_length=500)

    @model_validator(mode="after")
    def validate_expiry(self) -> "Certification":
        """Reject a certification that expires before it was issued."""
        if self.issued_on and self.expires_on and self.expires_on < self.issued_on:
            raise ValueError("expires_on cannot be earlier than issued_on")
        return self
