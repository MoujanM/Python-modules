
from enum import Enum
from pydantic import BaseModel, Field, model_validator, ValidationError
from datetime import datetime
from typing import Optional, Self


class ContactType(Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: str | None = Field(max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode='after')
    def validate_alien(self) -> Self:
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC'")
        if self.contact_type == ContactType.PHYSICAL and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")
        if self.contact_type == ContactType.TELEPATHIC and self.witness_count < 3:
            raise ValueError("Telepathic contact requires at least 3 witnesses")
        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError("Strong signals (> 7.0) should include received messages")

        return self


def main() -> None:
    print("\nAlien Contact Log Validation")
    print("=" * 40)

    try:
        valid_contact = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime.now(),
            contact_type=ContactType.RADIO,
            location="Area 51, Nevada",
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received="Greetings from Zeta Reticuli"
        )
        print("Valid contact report:")
        print(f"ID: {valid_contact.contact_id}")
        print(f"Type: {valid_contact.contact_type.value}")
        print(f"Location: {valid_contact.location}")
        print(f"Signal: {valid_contact.signal_strength}/10")
        print(f"Duration: {valid_contact.duration_minutes} minutes")
        print(f"Witnesses: {valid_contact.witness_count}")
        print(f"Message: '{valid_contact.message_received}'")
        print()
    except ValidationError as e:
        for error in e.errors():
            print(error['msg'])
        
    try:
        invalid_contact = AlienContact(
            contact_id="AC_2024_005",
            timestamp=datetime.now(),
            contact_type=ContactType.TELEPATHIC,
            location="Middle of Nowhere",
            signal_strength=6.0,
            duration_minutes=20,
            witness_count=2,
            message_received="You are the chosen!"
        )
    except ValidationError as e:
        print("=" * 40)
        print("Expected validation error:")
        for error in e.errors():
            msg = error['msg'].split(', ', 1)[-1]
            print(msg)

main()
