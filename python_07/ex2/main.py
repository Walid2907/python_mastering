from ex2.EliteCard import EliteCard


print("=== DataDeck Ability System ===")

elite = EliteCard(
    name="Arcane Warrior",
    cost=3,
    rarity="epic",
    attack_power=5,
    health=10,
    defense=3,
    mana=7
)

print("EliteCard capabilities:")
print("- Card: ['play', 'get_card_info', 'is_playable']")
print("- Combatable: ['attack', 'defend', 'get_combat_stats']")
print("- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']")

print("\nPlaying Arcane Warrior (Elite Card):")
print(elite.play({"mana": 10, "battlefield": []}))

print("\nCombat phase:")
print("Attack result:", elite.attack("Enemy"))
print("Defense result:", elite.defend(5))

print("\nMagic phase:")
print("Spell cast:", elite.cast_spell("Fireball", ["Enemy1", "Enemy2"]))
print("Mana channel:", elite.channel_mana(3))

print("\nMultiple interface implementation successful!")
