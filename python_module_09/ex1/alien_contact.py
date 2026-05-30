from enum import Enum
from pydantic import BaseModel, Field, model_validator, ValidationError
from datetime import datetime


class ContactType(Enum):
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: str | None = Field(default=None, max_length=500)
    is_verified: bool = False

    @model_validator(mode='after')
    def validate_rules(self) -> 'AlienContact':
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC' (Alien Contact)")
        if self.contact_type is ContactType.physical and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")
        if (self.contact_type is ContactType.telepathic and
                self.witness_count < 3):
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses")
        if (self.signal_strength > 7 and not
                isinstance(self.message_received, str)):
            raise ValueError(
                "Strong signals (> 7.0) should include received messages")
        return self


def main() -> None:
    valid = AlienContact(contact_id="AC6767",
                         timestamp=datetime(2024, 1, 15, 10, 30, 0),
                         location="Ohio",
                         contact_type=ContactType.telepathic,
                         signal_strength=7.8, duration_minutes=20,
                         witness_count=20, message_received="WE COME IN PEACE",
                         is_verified=True)
    print("Alien Contact Log Validation\n"
          "======================================")
    print("Valid contact report:")
    print(f"ID: {valid.contact_id}\nType: {valid.contact_type.value}\n"
          f"Location: {valid.location}\nSignal: {valid.signal_strength}/10\n"
          f"Duration: {valid.duration_minutes} minutes\n"
          f"Witnesses: {valid.witness_count}\n"
          f"Message: '{valid.message_received}'")
    print("\n======================================")
    print("Expected validation error:")
    try:
        invalid = AlienContact(contact_id="AC6767",
                               timestamp=datetime(2024, 1, 15, 10, 30, 0),
                               location="Ohio",
                               contact_type=ContactType.telepathic,
                               signal_strength=7.8, duration_minutes=20,
                               witness_count=2,
                               message_received="WE COME IN PEACE",
                               is_verified=True)
        print(invalid)
    except ValidationError as e:
        print(e.errors()[0]["msg"].split(", ", 1)[1])


if __name__ == "__main__":
    main()
