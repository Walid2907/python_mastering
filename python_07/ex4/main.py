from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


print("=== DataDeck Tournament Platform ===")

platform = TournamentPlatform()

dragon = TournamentCard("Fire Dragon", 5,
                        "legendary", attack_power=7,
                        health=10, defense=1)
wizard = TournamentCard("Ice Wizard", 4,
                        "rare", attack_power=5,
                        health=8, defense=2)

print("\nRegistering Tournament Cards...")
dragon_id = platform.register_card(dragon)
wizard_id = platform.register_card(wizard)

print(f"{dragon.name} (ID: {dragon_id}):")
print("- Interfaces: [Card, Combatable, Rankable]")
print(f"- Rating: {dragon.calculate_rating()}")
print(f"- Record: {dragon.get_rank_info()['wins']}-"
      f"{dragon.get_rank_info()['losses']}")

print(f"\n{wizard.name} (ID: {wizard_id}):")
print("- Interfaces: [Card, Combatable, Rankable]")
print("- Rating:", wizard.calculate_rating())
print("- Record:", f"{wizard.get_rank_info()['wins']}-"
                   f"{wizard.get_rank_info()['losses']}")

print("\nCreating tournament match...")
match = platform.create_match(dragon_id, wizard_id)
print("Match result:", match)

print("\nTournament Leaderboard:")
leaderboard = platform.get_leaderboard()
for i, entry in enumerate(leaderboard, start=1):
    print(f"{i}. {entry['name']} - Rating: "
          f"{entry['rating']} ({entry['wins']}-{entry['losses']})")

print("\nPlatform Report:")
print(platform.generate_tournament_report())

print("\n=== Tournament Platform Successfully Deployed! ===")
