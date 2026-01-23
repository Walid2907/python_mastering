class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class HealthError(GardenError):
    pass


class GardenManager:
    def __init__(self):
        self.plants = {}
        self.water_tank = 10

    def add_plant(self, name, water, sun):
        if not name:
            raise PlantError("Plant name cannot be empty!\n")
        if name in self.plants:
            raise PlantError("Plant already exists!\n")

        self.plants[name] = {
            "water": water,
            "sun": sun
        }
        print(f"Added {name} successfully")

    def water_plants(self):
        print("Opening watering system")
        try:
            if self.water_tank <= 0:
                raise WaterError("Not enough water in tank")

            for name in self.plants:
                self.plants[name]["water"] += 1
                self.water_tank -= 1
                print(f"Watering {name} - success")

        finally:
            print("Closing watering system (cleanup)")

    def check_health(self, name):
        if name not in self.plants:
            raise PlantError("Plant does not exist\n")

        water = self.plants[name]["water"]
        sun = self.plants[name]["sun"]

        if water > 10:
            raise HealthError(f"Water level {water} is too high (max 10)\n")
        if water < 1:
            raise HealthError(f"Water level {water} is too low (min 1)\n")
        if sun < 2:
            raise HealthError(f"Sunlight hours {sun} "
                              f"is too low (min 2)\n")
        if sun > 12:
            raise HealthError(f"Sunlight hours {sun} is "
                              f"too high (max 12)\n")

        print(f"{name}: healthy (water: {water}, sun: {sun})")


def test_manager():
    print("=== Garden Management System ===")
    manager = GardenManager()

    print("Adding plants to garden...")
    try:
        manager.add_plant("tomato", 4, 8)
        manager.add_plant("lettuce", 14, 6)
        manager.add_plant("", 3, 5)
    except GardenError as e:
        print(f"Error adding plant: {e}")

    print("Watering plants...")
    try:
        manager.water_plants()
    except GardenError as e:
        print(f"Watering error: {e}")

    print("Checking plant health...")
    for plant in manager.plants:
        try:
            manager.check_health(plant)
        except GardenError as e:
            print(f"Error checking {plant}: {e}")

    print("Testing error recovery...")
    try:
        manager.water_tank = 0
        manager.water_plants()
    except GardenError as e:
        print(f"Caught GardenError: {e}")
        print("System recovered and continuing...")

    print("Garden management system test complete!")
