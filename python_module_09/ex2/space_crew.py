from pydantic import BaseModel, Field, ValidationError, model_validator
from datetime import datetime
from enum import Enum


class Rank(Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def mission_validator(self) -> 'SpaceMission':
        count = 0
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")
        if (not any(m.rank in (Rank.captain, Rank.commander)
                    for m in self.crew)):
            raise ValueError("Must have at least one Commander or Captain")
        for m in self.crew:
            if m.years_experience >= 5:
                count += 1
        if self.duration_days > 365:
            if count/len(self.crew) < 0.5:
                raise ValueError(
                    "Long missions (> 365 days) need 50%"
                    " experienced crew (5+ years)")
        if not all(m.is_active for m in self.crew):
            raise ValueError("All crew members must be active")
        return self


def main() -> None:
    commander = CrewMember(member_id="CM001", name="Sarah Connor",
                           rank=Rank.commander, age=35,
                           specialization="Mission Command",
                           years_experience=15)
    officer = CrewMember(member_id="CM002", name="John Smith",
                         rank=Rank.officer, age=28,
                         specialization="Navigation",
                         years_experience=3)
    lieutenant = CrewMember(member_id="CM003", name="Alice Johnson",
                            rank=Rank.lieutenant, age=80,
                            specialization="Engineering",
                            years_experience=35, is_active=False)
    mission = SpaceMission(mission_id="M2024_MARS",
                           mission_name="Mars Colony Establishment",
                           destination="Mars",
                           launch_date=datetime(2024, 6, 1),
                           duration_days=900,
                           crew=[commander, officer],
                           budget_millions=2500.0)

    print("Space Mission Crew Validation")
    print("=========================================")
    print("Valid mission created:")
    print(f"Mission: {mission.mission_name}")
    print(f"ID: {mission.mission_id}")
    print(f"Destination: {mission.destination}")
    print(f"Duration: {mission.duration_days} days")
    print(f"Budget: ${mission.budget_millions}M")
    print(f"Crew size: {len(mission.crew)}")
    print("Crew members:")
    for m in mission.crew:
        print(f"  - {m.name} ({m.rank.value}) - {m.specialization}")

    try:
        print("=========================================")
        print("Expected validation error:")
        SpaceMission(mission_id="M0001",
                     mission_name="Doomed Mission",
                     destination="Moon",
                     launch_date=datetime(2024, 6, 1),
                     duration_days=10,
                     crew=[officer],
                     budget_millions=100.0)
    except ValidationError as e:
        print(e.errors()[0]["msg"].split(", ", 1)[1])
    try:
        print("=========================================")
        print("Expected validation error:")
        SpaceMission(mission_id="M0001",
                     mission_name="Doomed Mission",
                     destination="Moon",
                     launch_date=datetime(2024, 6, 1),
                     duration_days=10,
                     crew=[lieutenant, commander, officer],
                     budget_millions=100.0)
    except ValidationError as e:
        print(e.errors()[0]["msg"].split(", ", 1)[1])


if __name__ == "__main__":
    main()
