from datetime import datetime
from enum import Enum
from typing import List

from pydantic import BaseModel, Field, model_validator


class Rank(str, Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=2, max_length=50)
    rank: Rank
    age: int = Field(..., ge=18, le=80)
    specialization: str = Field(..., min_length=3, max_length=30)
    years_experience: int = Field(..., ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(..., min_length=5, max_length=15)
    mission_name: str = Field(..., min_length=3, max_length=100)
    destination: str = Field(..., min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(..., ge=1, le=3650)
    crew: List[CrewMember] = Field(..., min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(..., ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def validate_mission(self):
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")

        if not any(
            member.rank in {Rank.captain, Rank.commander}
            for member in self.crew
        ):
            raise ValueError(
                "Mission must have at least one Commander or Captain"
            )

        if self.duration_days > 365:
            experienced = [
                m for m in self.crew if m.years_experience >= 5
            ]
            if len(experienced) < len(self.crew) / 2:
                raise ValueError(
                    "Long missions require at least 50% experienced crew"
                )

        if any(not member.is_active for member in self.crew):
            raise ValueError("All crew members must be active")

        return self


def main():
    print("Space Mission Crew Validation")
    print("=" * 40)

    crew = [
        CrewMember(
            member_id="C001",
            name="Sarah Connor",
            rank=Rank.commander,
            age=45,
            specialization="Mission Command",
            years_experience=15,
        ),
        CrewMember(
            member_id="C002",
            name="John Smith",
            rank=Rank.lieutenant,
            age=34,
            specialization="Navigation",
            years_experience=6,
        ),
        CrewMember(
            member_id="C003",
            name="Alice Johnson",
            rank=Rank.officer,
            age=29,
            specialization="Engineering",
            years_experience=4,
        ),
    ]

    mission = SpaceMission(
        mission_id="M2024_MARS",
        mission_name="Mars Colony Establishment",
        destination="Mars",
        launch_date=datetime.now(),
        duration_days=900,
        crew=crew,
        budget_millions=2500.0,
    )

    print("Valid mission created:")
    print(f"Mission: {mission.mission_name}")
    print(f"ID: {mission.mission_id}")
    print(f"Destination: {mission.destination} ")
    print(f"Duration: {mission.duration_days} days")
    print(f"Budget: ${mission.budget_millions}M")
    print(f"Crew size: {len(mission.crew)}")
    print("Crew members:")
    for member in crew:
        print(f"- {member.name} ({member.rank}) - {member.specialization}")
    print()
    print("=" * 40)

    # Testing wrong crew
    crew = [
        CrewMember(
            member_id="C101",
            name="Mark Davis",
            rank=Rank.lieutenant,
            age=38,
            specialization="Navigation",
            years_experience=10,
        ),
        CrewMember(
            member_id="C102",
            name="Emma Brown",
            rank=Rank.lieutenant,
            age=32,
            specialization="Engineering",
            years_experience=7,
        ),
    ]

    try:
        mission = SpaceMission(
            mission_id="M2024_FAIL",
            mission_name="Failed Leadership Mission",
            destination="Mars",
            launch_date=datetime.now(),
            duration_days=500,
            crew=crew,  # no commander/captain
            budget_millions=1200.0,
        )
    except Exception:
        print("Expected validation error:")
        print("Mission must have at least one Commander or Captain")


if __name__ == "__main__":
    main()
