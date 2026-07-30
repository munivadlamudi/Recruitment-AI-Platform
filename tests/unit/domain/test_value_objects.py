"""Tests for immutable domain value objects."""

from datetime import date

import pytest
from pydantic import ValidationError

from src.domain.value_objects import ContactInfo, DateRange


def test_contact_info_accepts_valid_contact_channels() -> None:
    """A candidate can provide validated optional social links."""
    contact = ContactInfo(
        email="candidate@example.com",
        phone="+91 98765 43210",
        linkedin_url="https://linkedin.com/in/candidate",
    )

    assert str(contact.email) == "candidate@example.com"
    assert str(contact.linkedin_url) == "https://linkedin.com/in/candidate"


def test_contact_info_rejects_phone_without_enough_digits() -> None:
    """A non-actionable phone number should not be accepted."""
    with pytest.raises(ValidationError, match="at least five digits"):
        ContactInfo(email="candidate@example.com", phone="abc")


def test_date_range_rejects_reverse_chronology() -> None:
    """An end date cannot precede the start date."""
    with pytest.raises(ValidationError, match="cannot be earlier"):
        DateRange(start_date=date(2024, 1, 1), end_date=date(2023, 12, 31))
