def spell_combiner(spell1: callable, spell2: callable) -> callable:
    def combined(target):
        result1 = spell1(target)
        result2 = spell2(target)
        return (result1, result2)
    return combined


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    def amplified(value):
        result = base_spell(value)
        return result * multiplier
    return amplified


def conditional_caster(condition: callable, spell: callable) -> callable:
    def conditional(target):
        if condition(target):
            return spell(target)
        else:
            return "Spell fizzled"
    return conditional


def spell_sequence(spells: list[callable]) -> callable:
    def sequence(target):
        results = []
        for spell in spells:
            results.append(spell(target))
        return results
    return sequence


def fireball(target):
    return f"Fireball hits {target}"


def heal(target):
    return f"Heals {target}"


def lightning(target):
    return f"Lightning strikes {target}"


def is_enemy(target):
    return target in ["Dragon", "Goblin", "'Wizard", "Knight"]


def damage_spell(value):
    return value


if __name__ == "__main__":
    print("Testing spell combiner...")
    combined_spell = spell_combiner(fireball, heal)
    result = combined_spell("Dragon")
    print("Combined spell result:", result[0], ",", result[1])

    print("\nTesting power amplifier...")
    original = damage_spell(10)
    amplified_spell = power_amplifier(damage_spell, 3)
    amplified = amplified_spell(10)
    print(f"Original: {original}, Amplified: {amplified}")
