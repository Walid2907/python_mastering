class Plant:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def grow(self):
        self.height += 1
        print(f"{self.name} grew 1cm")

    def description(self):
        return f"{self.name}: {self.height}cm"


class FloweringPlant(Plant):
    def __init__(self, name, height, color):
        super().__init__(name, height)
        self.color = color
        self.blooming = True

    def description(self):
        status = "blooming" if self.blooming else "not blooming"
        return f"{self.name}: {self.height}cm, {self.color} flowers ({status})"


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, color, prize_points):
        super().__init__(name, height, color)
        self.prize_points = prize_points

    def description(self):
        return (
            f"{self.name}: {self.height}cm, {self.color} flowers (blooming), "
            f"Prize points: {self.prize_points}"
        )


class Garden:
    def __init__(self, owner):
        self.owner = owner
        self.plants = []

    def add_plant(self, plant):
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner}'s garden")

    def grow_all(self):
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()

    def report(self):
        print(f"=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            print(f"- {plant.description()}")


class GardenManager:
    gardens_managed = 0

    def __init__(self):
        self.gardens = {}
        GardenManager.gardens_managed += 1

    def add_garden(self, garden):
        self.gardens[garden.owner] = garden

    def get_garden(self, owner):
        return self.gardens.get(owner)

    class GardenStats:
        @staticmethod
        def plant_counts(plants):
            regular = flowering = prize = 0
            for p in plants:
                if isinstance(p, PrizeFlower):
                    prize += 1
                elif isinstance(p, FloweringPlant):
                    flowering += 1
                else:
                    regular += 1
            return regular, flowering, prize

        @staticmethod
        def total_growth(plants):
            return len(plants)

    def garden_report(self, owner):
        garden = self.get_garden(owner)
        garden.report()

        stats = GardenManager.GardenStats
        regular, flowering, prize = stats.plant_counts(garden.plants)
        total_growth = stats.total_growth(garden.plants)

        print(
            f"Plants added: {len(garden.plants)}, "
            f"Total growth: {total_growth}cm"
        )
        print(
            f"Plant types: {regular} regular, "
            f"{flowering} flowering, {prize} prize flowers"
        )

    @classmethod
    def total_gardens(cls):
        return cls.gardens_managed

    @classmethod
    def create_garden_network(cls):
        return cls()

    @staticmethod
    def validate_height(plant):
        return plant.height > 0


def calculate_garden_score(garden):
    score = 0
    for plant in garden.plants:
        score += plant.height
        if isinstance(plant, PrizeFlower):
            score += plant.prize_points
    return score


print("=== Garden Management System Demo ===")

manager = GardenManager.create_garden_network()

alice_garden = Garden("Alice")
bob_garden = Garden("Bob")

manager.add_garden(alice_garden)
manager.add_garden(bob_garden)

alice_garden.add_plant(Plant("Oak Tree", 100))
alice_garden.add_plant(FloweringPlant("Rose", 25, "red"))
alice_garden.add_plant(PrizeFlower("Sunflower", 50, "yellow", 10))

alice_garden.grow_all()
manager.garden_report("Alice")

print("Height validation test:",
      GardenManager.validate_height(alice_garden.plants[0]))

print(
    f"Garden scores - Alice: {calculate_garden_score(alice_garden)}, "
    f"Bob: {calculate_garden_score(bob_garden)}"
)

print(f"Total gardens managed: {GardenManager.total_gardens()}")
