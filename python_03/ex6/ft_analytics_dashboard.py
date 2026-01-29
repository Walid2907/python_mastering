print("=== Game Analytics Dashboard ===")

# input data

data = {
    "players": {
        "alice": {"level": 41, "total_score": 2824, "sessions_played": 13,
                  "favorite_mode": "ranked", "achievements_count": 5},
        "bob": {"level": 16, "total_score": 4657, "sessions_played": 27,
                "favorite_mode": "ranked", "achievements_count": 2},
        "charlie": {"level": 44, "total_score": 9935, "sessions_played": 21,
                    "favorite_mode": "ranked", "achievements_count": 7},
        "diana": {"level": 3, "total_score": 1488, "sessions_played": 21,
                  "favorite_mode": "casual", "achievements_count": 4},
        "eve": {"level": 33, "total_score": 1434, "sessions_played": 81,
                "favorite_mode": "casual", "achievements_count": 7},
        "frank": {"level": 15, "total_score": 8359, "sessions_played": 85,
                  "favorite_mode": "competitive", "achievements_count": 1},
    },
    "sessions": [
        {"player": "bob", "duration_minutes": 94, "score": 1831,
         "mode": "competitive", "completed": False},
        {"player": "bob", "duration_minutes": 32, "score": 1478,
         "mode": "casual", "completed": True},
        {"player": "diana", "duration_minutes": 17, "score": 1570,
         "mode": "competitive", "completed": False},
        {"player": "alice", "duration_minutes": 98, "score": 1981,
         "mode": "ranked", "completed": True},
        {"player": "diana", "duration_minutes": 15, "score": 2361,
         "mode": "competitive", "completed": False},
        {"player": "eve", "duration_minutes": 29, "score": 2985,
         "mode": "casual", "completed": True},
        {"player": "frank", "duration_minutes": 34, "score": 1285,
         "mode": "casual", "completed": True},
    ],
    "achievements": [
        "first_blood", "level_master", "speed_runner",
        "treasure_seeker", "boss_hunter", "pixel_perfect",
        "combo_king", "explorer"
    ]
}
players = data["players"]
sessions = data["sessions"]
achievements = data["achievements"]

# List Comprehension

print("\n=== List Comprehension Examples ===")

high_scorers = [
    name for name, info in players.items()
    if info["total_score"] > 2000
]
print("High scorers (>2000):", high_scorers)

scores_doubled = [
    info["total_score"] * 2 for info in players.values()
]
print("Scores doubled:", scores_doubled)

active_players = list({s["player"] for s in sessions})
print("Active players:", active_players)

# Dict Comprehension

print("\n=== Dict Comprehension Examples ===")

player_scores = {
    name: info["total_score"]
    for name, info in players.items()
}
print("Player scores:", player_scores)

score_categories = {
    "high": len([p for p in players.values() if p["total_score"] >= 5000]),
    "medium": len([p for p in players.values()
                   if 2000 <= p["total_score"] < 5000]),
    "low": len([p for p in players.values() if p["total_score"] < 2000]),
}
print("Score categories:", score_categories)

achievement_counts = {
    name: info["achievements_count"]
    for name, info in players.items()
}
print("Achievement counts:", achievement_counts)

# Set Comprehension

print("\n=== Set Comprehension Examples ===")

unique_players = set(players.keys())
print("Unique players:", unique_players)

unique_achievements = set(achievements)
print("Unique achievements:", unique_achievements)

players_with_completed_sessions = {
    s["player"] for s in sessions if s["completed"]
}
print("Players with completed sessions:", players_with_completed_sessions)

# Combined Analysis

print("\n=== Combined Analysis ===")

total_players = len(players)
total_unique_achievements = len(unique_achievements)
average_score = sum(
    info["total_score"] for info in players.values()
) / total_players

top_player = max(
    players,
    key=lambda p: players[p]["total_score"]
)

print("Total players:", total_players)
print("Total unique achievements:", total_unique_achievements)
print("Average score:", average_score)
print(
    f"Top performer: {top_player} "
    f"({players[top_player]['total_score']} points, "
    f"{players[top_player]['achievements_count']} achievements)"
)
