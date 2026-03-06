from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, ValidationError


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: Optional[str] = Field(default=None, max_length=200)


def main() -> None:
    print("Space Station Data Validation")
    print("=" * 40)

    time = datetime.strptime("2024-01-15T10:30:00", "%Y-%m-%dT%H:%M:%S")
    try:
        station = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=6,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=time,
            is_operational=True,
            notes="Primary orbital research station."
        )

        print("Valid station created:")
        print(f"ID: {station.station_id}")
        print(f"Name: {station.name}")
        print(f"Crew: {station.crew_size} people")
        print(f"Power: {station.power_level}%")
        print(f"Oxygen: {station.oxygen_level}%")
        print(f"Status: {'Operational' if station.is_operational else 'Not Operational'}") # noqa
        print(f"Last maintenance: {station.last_maintenance}")

    except ValidationError as e:
        print("Unexpected validation error:")
        print(e)

    print("\n" + "=" * 40)

    try:
        station = SpaceStation(
            station_id="BAD01",
            name="Broken Station",
            crew_size=50,  # invalid: must be <= 20
            power_level=120.0,  # invalid: must be <= 100
            oxygen_level=50.0,
            last_maintenance=time
        )
    except ValidationError as e:
        print("Expected validation error:")
        print(e.errors()[0]["msg"])


if __name__ == "__main__":
    main()
