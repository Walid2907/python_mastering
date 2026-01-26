# === Achievement Tracker System ===

alice = {"first_kill", "level_10", "treasure_hunter", "speed_demon"}

bob = {"first_kill", "level_10", "boss_slayer", "collector"}

charlie = {"level_10", "treasure_hunter",
           "boss_slayer", "speed_demon", "perfectionist"}

print("=== Achievement Tracker System ===\n")
print(f"Player alice achievements: {alice}")
print(f"Player bob achievements: {bob}")
print(f"Player charlie achievements: {charlie}")

# === Achievement Analytics ===

all_achievements = alice.union(bob).union(charlie)

print("\n=== Achievement Analytics ===")
print(f"All unique achievements: {all_achievements}")
print(f"Total unique achievements: {len(all_achievements)}\n")

common_all = alice.intersection(bob).intersection(charlie)
print(f"Common to all players: {common_all}")

# Rare achievements (appear in only one player)
alice_only = alice.difference(bob).difference(charlie)
bob_only = bob.difference(alice).difference(charlie)
charlie_only = charlie.difference(alice).difference(bob)
rare = alice_only.union(bob_only).union(charlie_only)
print(f"Rare achievements (1 player): {rare}\n")

# Player comparisons
print(f"Alice vs Bob common: {alice.intersection(bob)}")
print(f"Alice unique: {alice.difference(bob)}")
print(f"Bob unique: {bob.difference(alice)}")
