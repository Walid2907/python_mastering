def garden_operations():
    int("abc")
    10 / 0
    with open("missing.txt", "r") as f:
        f.read()
    garden_plants = {"rose": "red", "sunflower": "yellow"}
    garden_plants["missing_plant"]


def test_error_types():
    print("=== Garden Error Types Demo ===\n")

    try:
        print("Testing ValueError...")
        int("abc")
    except ValueError as e:
        print(f"Caught ValueError: {e}\n")

    try:
        print("Testing ZeroDivisionError...")
        10 / 0
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}\n")

    try:
        print("Testing FileNotFoundError...")
        with open("missing.txt", "r") as f:
            f.read()
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}\n")

    try:
        print("Testing KeyError...")
        garden_plants = {"rose": "red", "sunflower": "yellow"}
        garden_plants["missing_plant"]
    except KeyError as e:
        print(f"Caught KeyError: {e}\n")

    try:
        print("Testing multiple errors together...")
        int("abc")
        10 / 0
    except (ValueError, ZeroDivisionError):
        print("Caught an error, but program continues!\n")

    print("All error types tested successfully!")
test_error_types()