from alchemy.grimoire.spellbook import validate_ingredients, record_spell


def late_import():
    from alchemy.grimoire.spellbook import record_spell
    print("\nTesting late import technique:")
    print(f"record_spell(\"Lightning\", \"air\"): "
          f"{record_spell('Lightning', 'air')}")


print("\n=== Circular Curse Breaking ===\n")
print("Testing ingredient validation:")
print(f"validate_ingredients(\"fire air\"): "
      f"{validate_ingredients('fire air')}")
print(f"validate_ingredients(\"dragon scales\"): "
      f"{validate_ingredients('dragon scales')}")

print("\nTesting spell recording with validation:")
print(f"record_spell(\"Fireball\", \"fire air\"):  "
      f"{record_spell('Fireball', 'fire air')}")
print(f"record_spell(\"Dark Magic\", \"shadow\"): "
      f"{record_spell('Dark Magic', 'shadow')}")

late_import()
print("\nCircular dependency curse avoided using late imports!")
print("All spells processed safely!")
