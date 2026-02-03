from ex0.CreatureCard import CreatureCard


# game stats to follow the game
game_state = {"mana": 6, "battlefield": []}
# creating the card
dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 7)
# creating enemy card
Goblin_Warrior = CreatureCard("Goblin Warrior", 1, "common", 2, 4)
print("=== DataDeck Card Foundation ===\n")

print("Testing Abstract Base Class Design:\n")
# printing the card info
print("CreatureCard Info:")
print(dragon.get_card_info())

print("\nPlaying Fire Dragon with 6 mana available:")
print(f"Playable: {dragon.is_playable(game_state['mana'])}")
print(f"Play result: {dragon.play(game_state)}")

print("\nFire Dragon attacks Goblin Warrior:")
print(f"attack result: {dragon.attack_target(Goblin_Warrior)}")

# testing if we can play our dragon card
# after we already spent most of or mana
# in the last attack
print("\nTesting insufficient mana (1 available):")
print(f"Playable: {dragon.is_playable(game_state['mana'])}")
