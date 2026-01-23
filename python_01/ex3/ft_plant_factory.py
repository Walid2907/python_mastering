class Plants:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def __str__(self):
        return f"Created: {self.name} ({self.height}cm, {self.age} days)"


plants_data = [
    ("Rose", 25, 30),
    ("Oak", 200, 365),
    ("Cactus", 5, 90),
    ("Sunflower", 80, 45),
    ("Fern", 15, 120),
    ("bamboos", 10, 50)
]
plants_storage = []
for data in plants_data:
    plant = Plants(data[0], data[1], data[2])
    plants_storage.append(plant)
    print(plant)
