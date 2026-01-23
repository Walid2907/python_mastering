def water_plants(plant_list):
    try:
        print("Opening watering system")
        for plant in plant_list:
            if plant is None or type(plant) is not str or plant == "":
                raise ValueError(f"Cannot water {plant} - invalid plant!")
            print(f"Watering {plant}")
    except ValueError as e:
        print(f"Error: {e}")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system():
    print("=== Garden Watering System ===\n")

    print("Testing normal watering...")
    good_plants = ["tomato", "lettuce", "carrots"]
    water_plants(good_plants)
    print("Watering completed successfully!\n")

    print("Testing with error...")
    bad_plants = ["tomato", None, "carrots"]
    water_plants(bad_plants)
    print("\nCleanup always happens, even with errors!")
