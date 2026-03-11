def mage_counter() -> callable:
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> callable:
    total = initial_power

    def accumulate(amount: int) -> int:
        nonlocal total
        total += amount
        return total

    return accumulate


def enchantment_factory(enchantment_type: str) -> callable:
    def enchant(item: str) -> str:
        return f"{enchantment_type} {item}"
    return enchant


def memory_vault() -> dict[str, callable]:
    storage = {}

    def store(key: str, value) -> None:
        storage[key] = value

    def recall(key: str):
        return storage.get(key, "Memory not found")

    return {'store': store, 'recall': recall}


if __name__ == "__main__":
    initial_powers = [55, 77, 56]
    power_additions = [18, 9, 5, 8, 10]
    enchantment_types = ['Flaming', 'Frozen', 'Flowing']
    items_to_enchant = ['Shield', 'Staff', 'Armor', 'Wand']

    print("Testing mage counter...")
    counter = mage_counter()
    for i in range(3):
        print(f"Call {i + 1}: {counter()}")

    print("\nTesting enchantment factory...")
    for e_type in enchantment_types:
        enchant = enchantment_factory(e_type)
        for item in items_to_enchant:
            print(enchant(item))
