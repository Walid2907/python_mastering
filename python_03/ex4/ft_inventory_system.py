
# Inventory calculation function

def calculate_details(name, dictionary: dict):
    """
    Calculates total value and total item count for a given player.
    Uses the passed dictionary instead of global variables.
    """
    total_value = 0
    total_items = 0
    for item in dictionary.get(name).keys():
        details = dictionary.get(name).get(item)
        quantity = details.get("quantity")
        value = details.get("value")
        total = quantity * value
        total_value = total_value + total
        total_items = total_items + quantity

    return total_value, total_items


print("=== Player Inventory System ===\n")


# Players database

players = {
    "Alice": {
        "sword": {"quantity": 1, "category": "weapon",
                  "rarity": "rare", "value": 500},
        "potions": {"quantity": 5, "category": "consumable",
                    "rarity": "common", "value": 50},
        "shield": {"quantity": 1, "category": "armor",
                   "rarity": "uncommon", "value": 200}
    },
    "Bob": {
        "magic_ring": {"quantity": 1, "category": "ring",
                       "rarity": "rare", "value": 600},
        "sword": {"quantity": 0, "category": "weapon",
                  "rarity": "rare", "value": 500},
        "potions": {"quantity": 0, "category": "consumable",
                    "rarity": "common", "value": 50},
        "shield": {"quantity": 0, "category": "armor",
                   "rarity": "uncommon", "value": 200}
    }
}

print("=== Alice's Inventory ===")

total_value_alice = 0
total_items_alice = 0

# Printing Alice inventory
for item in players.get("Alice").keys():
    details = players.get("Alice").get(item)
    quantity = details.get("quantity")
    category = details.get("category")
    rarity = details.get("rarity")
    value = details.get("value")
    total = quantity * value
    total_value_alice = total_value_alice + total
    total_items_alice = total_items_alice + quantity
    print(f"{item} ({category}, {rarity}): {quantity}x @ "
          f"{value} gold each = {total} gold")


# Printing inventory summary
print(f"\nInventory value: {total_value_alice} gold")
print(f"Item count: {total_items_alice} items")

# NOTE: This prints item names with quantities (not categories)
print("Categories: ", end="")
for item in players.get("Alice").keys():
    details = players.get("Alice").get(item)
    print(f"{item}({details.get('quantity')}), ", end="")
print("\n")


# Transaction

print("=== Transaction: Alice gives Bob 2 potions ===")

# Manual quantity update (logic preserved)
players.get("Alice").get("potions").update({"quantity": 3})
players.get("Bob").get("potions").update({"quantity": 2})

print("Transaction successful!\n")


# Updated inventories

print("=== Updated Inventories ===")
print(f"Alice potions: {players.get('Alice').get('potions').get('quantity')}")
print(f"Bob potions: {players.get('Bob').get('potions').get('quantity')}\n")

# Inventory analytics

# Bob
total_value_bob, total_items_bob = calculate_details("Bob", players)

# Alice
total_value_alice, total_items_alice = calculate_details("Alice", players)

# Compare inventory value
if total_value_bob > total_value_alice:
    biggest = total_value_bob
    player = "Bob"
else:
    biggest = total_value_alice
    player = "Alice"

print("=== Inventory Analytics ===")
print(f"Most valuable player: {player} ({biggest} gold)")

# Compare item count
if total_items_bob > total_items_alice:
    biggest = total_items_bob
    player = "Bob"
else:
    biggest = total_items_alice
    player = "Alice"

print(f"Most items: {player} ({biggest} items)")

# Rarest items detection (clean dict version)
# Rarity ranking
rarity_rank = {
    "common": 1,
    "uncommon": 2,
    "rare": 3
}
rarest_items = {}
max_rank = 0

for player in players.keys():
    for item in players.get(player).keys():
        details = players.get(player).get(item)
        rarity = details.get("rarity")
        rank = rarity_rank.get(rarity)
        if rank > max_rank:
            max_rank = rank
            rarest_items = {}
            rarest_items.update({item: rarity})
        elif rank == max_rank:
            rarest_items.update({item: rarity})
first = True
print("Rarest items: ", end="")
for item in rarest_items.keys():
    if not first:
        print(", ", end="")
    print(item, end="")
    first = False
