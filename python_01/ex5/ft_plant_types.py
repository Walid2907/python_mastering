class Plants:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age


class Flower(Plants):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        print(f"{self.name} is blooming beautifully!")

    def __str__(self):
        return (f"{self.name} (Flower): {self.height}cm, "
                f"{self.age} days, {self.color} color")


class Tree(Plants):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        shade = int(3.14 * (self.height / 100) ** 2)
        print(f"{self.name} provides {shade} square meters of shade")

    def __str__(self):
        return (f"{self.name} (Tree): {self.height}cm, "
                f"{self.age} days, {self.trunk_diameter}cm diameter")


class Vegetable(Plants):
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def nutritional_value_info(self):
        print(f"{self.name} is rich in vitamin {self.nutritional_value}")

    def __str__(self):
        return (f"{self.name} (Vegetable): {self.height}cm, "
                f"{self.age} days, {self.harvest_season} harvest")


print("=== Garden Plant Types ===")
flower = Flower("Rose", 3, 5, "red")
print(flower)
flower.bloom()
tree = Tree("oak", 500, 128, 50)
print(tree)
tree.produce_shade()
vegetable = Vegetable("tomato", 30, 19, "summer", "C")
print(vegetable)
vegetable.nutritional_value_info()
