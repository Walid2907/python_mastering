class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def print_plants(self):
        print(f"{self.name}: {self.height}cm {self.age}years old")


plant1 = Plant("Rose", 25, 30)
plant2 = Plant("Sunflower", 80, 45)
plant3 = Plant("Cactus", 15, 120)
print("=== Garden Plant Registry ===")
plant1.print_plants()
plant2.print_plants()
plant3.print_plants()
