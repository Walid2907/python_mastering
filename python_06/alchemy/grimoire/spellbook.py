from .validator import validate_ingredients


def record_spell(spell_name: str, ingredients: str) -> str:
    result = validate_ingredients(ingredients)
    if "valid" in result.lower():
        return f"Spell recorded: {spell_name} ({result})"
    return f"Spell rejected: {spell_name} ({result})"
