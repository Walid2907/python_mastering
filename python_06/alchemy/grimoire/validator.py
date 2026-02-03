def validate_ingredients(ingredients: str) -> str:
    valid_ingredients = {"fire", "water", "earth", "air"}
    items = ingredients.lower().split()
    invalid = [item for item in items if item not in valid_ingredients]
    if invalid:
        return f"{', '.join(invalid)} - INVALID"
    return f"{', '.join(items)} - VALID"
