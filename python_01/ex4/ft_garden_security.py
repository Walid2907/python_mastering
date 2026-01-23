class SecurePlant:
    def __init__(self, name):
        self.name = name
        self.__height = 0
        self.__age = 0
        print(f"Plant created: {self.name}")

    def set_height(self, height):
        if height >= 0:
            self.__height = height
            print(f"Height updated: {height}cm [OK]")
        else:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")

    def set_age(self, age):
        if age >= 0:
            self.__age = age
            print(f"Age updated: {age} days [OK]")
        else:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")

    def get_height(self):
        return self.__height

    def get_age(self):
        return self.__age

    def __str__(self):
        return (f"Current plant: {self.name} ({self.__height}cm, "
                f"{self.__age} days)")


print("=== Garden Security System ===")
plant = SecurePlant("Rose")
plant.set_height(25)
plant.set_age(30)
age = plant.get_age()
print(plant)


plant.hiegth = -10