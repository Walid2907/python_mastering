class Plants:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def grow(self):
        self.height += 1

    def ages(self):
        self.age += 1

    def get_info(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")


plant1 = Plants("Rose", 25, 30)
print("=== Day 1 ===")
plant1.get_info()
days = 8
for day in range(1, days):
    plant1.grow()
    plant1.ages()

print(f"=== Day {days} ===")
plant1.get_info()
