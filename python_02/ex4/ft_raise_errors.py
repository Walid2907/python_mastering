def check_plant_health(plant_name, water_level, sunlight_hours):
    if plant_name == "":
        raise ValueError("Plant name cannot be empty!\n")
    if not isinstance(plant_name, str):
        raise ValueError("Invalid plant name!\n")
    if water_level > 10:
        raise ValueError(f"Water level {water_level} is too high (max 10)\n")
    if water_level < 1:
        raise ValueError(f"Water level {water_level} is too low (min 1)\n")
    if sunlight_hours < 2:
        raise ValueError(f"Sunlight hours {sunlight_hours} "
                         f"is too low (min 2)\n")
    if sunlight_hours > 12:
        raise ValueError(f"Sunlight hours {sunlight_hours} is "
                         f"too high (max 12)\n")

    return f"Plant '{plant_name}' is healthy!\n"


def test_plant_checks():
    print("=== Garden Plant Health Checker ===\n")

    print("Testing good values...")
    try:
        message = check_plant_health("tomato", 4, 8)
        print(message)
    except ValueError as e:
        print(f"Error: {e}")

    print("Testing empty plant name...")
    try:
        message = check_plant_health("", 4, 8)
        print(message)
    except ValueError as e:
        print(f"Error: {e}")

    print("Testing bad water level...")
    try:
        message = check_plant_health("tomato", 15, 8)
        print(message)
    except ValueError as e:
        print(f"Error: {e}")

    print("Testing bad sunlight hours...")
    try:
        message = check_plant_health("tomato", 4, 1)
        print(message)
    except ValueError as e:
        print(f"Error: {e}")

    print("All error raising tests completed!")


test_plant_checks()
