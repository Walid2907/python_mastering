import alchemy.elements


def healing_potion():
    return (f"Healing potion brewed with {alchemy.elements.create_fire()} "
            f"and {alchemy.elements.create_water()}")


def strength_potion():
    return (f"Strength potion brewed with {alchemy.elements.create_earth()} "
            f"and {alchemy.elements.create_fire()}")


def invisibility_potion():
    return (f"Invisibility potion brewed with {alchemy.elements.create_air()} "
            f"and {alchemy.elements.create_water()}")


def wisdom_potion():
    return (f"Wisdom potion brewed with all elements: "
            f"{alchemy.elements.create_fire()},"
            f"{alchemy.elements.create_water()}, "
            f"{alchemy.elements.create_earth()}, "
            f"{alchemy.elements.create_air()} ")
