
class Animals:
    def __init__(self, name):
        self.name = name

    class Male:
        def hunt(self):
            print("hunting")

    class Female:
        def cook(self):
            print("cooking")


lion = Animals.Male("male")