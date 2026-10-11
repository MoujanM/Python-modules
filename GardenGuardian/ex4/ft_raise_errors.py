
def check_plant_health(plant_name: str, water_level: int, sunlight_hours: int):
    if plant_name == "":
        msg = "Plant name cannot be empty!"
        raise ValueError(msg)
    elif water_level < 1:
        msg = f"Water level {water_level} is too low (min 1)"
        raise ValueError(msg)
    elif water_level > 10:
        msg = f"Water level {water_level} is too high (max 10)"
        raise ValueError(msg)
    elif sunlight_hours < 2:
        msg = f"Sunlight hours {sunlight_hours} is too low (min 2)"
        raise ValueError(msg)
    elif sunlight_hours > 12:
        msg = f"Sunlight hours {sunlight_hours} is too high (max 12)"
        raise ValueError(msg)
    else:
        print(f"Plant '{plant_name}' is healthy!")


def test_plant_checks():
    print("=== Garden Plant Health Checker ===", end='\n\n')
    tests = [
        ("good values", ("tomato", 3, 5)),
        ("empty plant name", ("", 3, 5)),
        ("bad water level", ("tomato", 15, 5)),
        ("bad sunlight hours", ("tomato", 3, 0))
    ]
    for test in tests:
        print(f"Testing {test[0]}...")
        try:
            check_plant_health(*test[1])
            print()
        except ValueError as e:
            print(f"Error: {e}", end='\n\n')

    print("\nAll error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
