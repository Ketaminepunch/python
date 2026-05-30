from pydantic import BaseModel, Field, ValidationError
from datetime import datetime


class SpaceStation(BaseModel):
    name: str = Field(min_length=1, max_length=50)
    station_id: str = Field(min_length=3, max_length=10)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    is_operational: bool = Field(default=True)
    notes: str | None = Field(default=None, max_length=200)
    last_maintenance: datetime


def main() -> None:

    iss = SpaceStation(name="ISS", station_id="ISS123", crew_size=12,
                       power_level=88.12, oxygen_level=67.41,
                       is_operational=False, notes="MYNOTE",
                       last_maintenance=datetime(2024, 1, 15, 10, 30, 0))
    isop: str = "Operational"
    if not iss.is_operational:
        isop = "Not operational"
    print("Space Station Data Validation\n"
          "========================================")
    print("Valid station Created:")
    print(f"ID: {iss.station_id}\nName: {iss.name}\n"
          f"Crew: {iss.crew_size} People\nPower: {iss.power_level}%\n"
          f"Oxygen: {iss.oxygen_level}%\nStatus: {isop}\n"
          f"Notes: {iss.notes}")
    try:
        print("========================================\n"
              "Expected validation error:")
        invalid = SpaceStation(name="invalid", station_id="ASDASD",
                               crew_size=400, power_level=67.67,
                               oxygen_level=67.67,
                               last_maintenance=datetime(2024, 1,
                                                         15, 10, 30, 0))

        print(invalid)
    except ValidationError as e:
        print(e.errors()[0]["msg"])
        print(e.errors())


if __name__ == "__main__":
    main()
