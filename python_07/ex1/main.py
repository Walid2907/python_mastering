from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck


print("=== DataDeck Deck Builder ===")


print("Building deck with different card types...")
# Create cards
fire_dragon = CreatureCard("Fire Dragon", cost=9,
                           rarity="Legendary", attack=7, health=5)
lightning_bolt = SpellCard("Lightning Bolt", cost=5,
                           rarity="Rare", effect_type="damage")
mana_crystal = ArtifactCard("Mana Crystal", cost=3,
                            rarity="Uncommon", durability=3,
                            effect="+1 mana per turn")

# Create a deck
my_deck = Deck()
# Add cards to deck
my_deck.add_card(fire_dragon)
my_deck.add_card(lightning_bolt)
my_deck.add_card(mana_crystal)
# Show deck stats
stats = my_deck.get_deck_stats()
print("Deck stats:", stats)
# Shuffle deck
my_deck.shuffle()

print("Drawing and playing cards:\n")
# Draw and play cards
for _ in my_deck.deck:
    card = my_deck.draw_card()
    print(f"Drew: {card.name} ({card.__class__.__name__})")
    result = card.play({"mana": 5, "battlefield": [], "artifacts": []})
    print(f"Play result: {result}\n")

