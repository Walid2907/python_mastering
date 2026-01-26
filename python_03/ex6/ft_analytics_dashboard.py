# ==============================
# Data Alchemist – Analytics Dashboard
# ==============================

print("=== Game Analytics Dashboard ===")

# ------------------------------
# Sample Data (hardcoded, simple)
# ------------------------------

players = ["alice", "bob", "charlie", "diana"]

scores = {
    "alice": 2300,
    "bob": 1800,
    "charlie": 2150,
    "diana": 1950
}

achievements = [
    ("alice", "first_kill"),
    ("alice", "level_10"),
    ("alice", "boss_slayer"),
    ("bob", "first_kill"),
    ("bob", "level_10"),
    ("charlie", "first_kill"),
    ("charlie", "level_10"),
    ("charlie", "boss_slayer"),
    ("charlie", "master"),
    ("diana", "first_kill")
]

active_players = {"alice", "bob", "charlie"}

regions = {
    "alice": "north",
    "bob": "east",
    "charlie": "central",
    "diana": "north"
}

# ==============================
# List Comprehension Examples
# ==============================

print("\n=== List Comprehension Examples ===")

# Filter players with high scores
high_scorers = [player for player, score in scores.items() if score > 2000]
print("High scorers (>2000):", high_scorers)

# Transform scores (double them)
doubled_scores = [score * 2 for score in scores.values()]
print("Scores doubled:", doubled_scores)

# Active players list
active_list = [player for player in players if player in active_players]
print("Active players:", active_list)

# ==============================
# Dict Comprehension Examples
# ==============================

print("\n=== Dict Comprehension Examples ===")

# Player to score mapping
player_scores = {player: scores[player] for player in players}
print("Player scores:", player_scores)

# Score categories
score_categories = {
    "high": len([s for s in scores.values() if s >= 2200]),
    "medium": len([s for s in scores.values() if 1800 <= s < 2200]),
    "low": len([s for s in scores.values() if s < 1800])
}
print("Score categories:", score_categories)

# Achievement count per player
achievement_counts = {
    player: len([a for p, a in achievements if p == player])
    for player in players
}
print("Achievement counts:", achievement_counts)

# ==============================
# Set Comprehension Examples
# ==============================

print("\n=== Set Comprehension Examples ===")

# Unique players
unique_players = {player for player in players}
print("Unique players:", unique_players)

# Unique achievements
unique_achievements = {achievement for _, achievement in achievements}
print("Unique achievements:", unique_achievements)

# Active regions
active_regions = {regions[player] for player in active_players}
print("Active regions:", active_regions)

# ==============================
# Combined Analysis
# ==============================

print("\n=== Combined Analysis ===")

total_players = len(unique_players)
total_unique_achievements = len(unique_achievements)
average_score = sum(scores.values()) / len(scores)
top_player = max(scores, key=scores.get)

print("Total players:", total_players)
print("Total unique achievements:", total_unique_achievements)
print("Average score:", average_score)
print(
    f"Top performer: {top_player} "
    f"({scores[top_player]} points, "
    f"{achievement_counts[top_player]} achievements)"
)
