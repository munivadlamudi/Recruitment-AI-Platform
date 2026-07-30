"""Date-range value object for education and employment periods."""

from datetime import date

from pydantic import BaseModel, ConfigDict, model_validator


class DateRange(BaseModel):
    """An inclusive start date and optional end date."""

    model_config = ConfigDict(extra="forbid", frozen=True)

    start_date: date
    end_date: date | None = None

    @model_validator(mode="after")
    def validate_chronology(self) -> "DateRange":
        """Reject a range ending before it starts."""
        if self.end_date is not None and self.end_date < self.start_date:
            raise ValueError("end_date cannot be earlier than start_date")
        return self
