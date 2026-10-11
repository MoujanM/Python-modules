
from pydantic import BaseModel, Field, ValidationError
from typing import Optional
from datetime import datetime

class SpaceStation(BaseModel):
    # strings
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    
    # numbers
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    
    # others
    last_maintenance: datetime
    is_operational: bool = Field(default=True)
    notes: str | None = Field(default=None, max_length=200)

def main() -> None:
    print("\nSpace Station Data Validation")
    print("=" * 40)

    try:
        valid_station = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=6,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime.now()
        )
        print("Valid station creatied:")
        print(f"ID: {valid_station.station_id}")
        print(f"Name: {valid_station.name}")
        print(f"Crew: {valid_station.crew_size} people")
        print(f"Power: {valid_station.power_level}%")
        print(f"Oxygen: {valid_station.oxygen_level}%")
        print(f"Status: {'Operational' if valid_station.is_operational else 'Non-Operational'}")
        print()
    except ValidationError as e:
        print("Validation Errors detected:")
        print(e.errors()[0]['msg'])
    
    print("=" * 40)

    try:
        broke_station = SpaceStation(
            station_id="OSS001",
            name="Overcrowded Space Station",
            crew_size=35,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime.now()
        )
    except ValidationError as e:
        print("Expected validation error:")
        for error in e.errors():
            print(error['msg'])

main()