from typing import Dict, Any
from ex0.Card import Card


class CreatureCard(Card):
    def __init__(self, name: str, cost: int,
                 rarity: str, attack: int, health: int):
        # check logic of input before constructing
        if attack <= 0:
            raise ValueError("Attack must be a positive integer")
        if health <= 0:
            raise ValueError("Health must be a positive integer")
        super().__init__(name, cost, rarity)
        self.attack = attack
        self.health = health

    def play(self, game_state: Dict[str, Any]) -> Dict[str, Any]:
        # check if u can play the card
        if self in game_state["battlefield"]:
            return {
                "card_played": None,
                "mana_used": 0,
                "effect": f"{self.name} is already on the battlefield"
            }
        if self.is_playable(game_state["mana"]):
            # remove the consumed mana from the game stat
            # append the new card
            game_state["mana"] -= self.cost
            game_state["battlefield"].append(self)
            return {
                "card_played": self.name,
                "mana_used": self.cost,
                "effect": "Creature "
                          "summoned to battlefield"
            }
        return {"card_played": None,
                "mana_used": 0, "effect": "Not enough mana"}

# you should attack a card !!
    def attack_target(self, target: "CreatureCard") -> Dict:
        # remove the damage from the health
        target.health -= self.attack
        target_defeated = target.health <= 0
        return {
            "attacker": self.name,
            "target": target.name,
            "damage_dealt": self.attack,
            "target_defeated": target_defeated,
            "target_remaining_health": max(target.health, 0)
        }

    def get_card_info(self) -> Dict:
        info = super().get_card_info()
        info.update({"attack": self.attack, "health": self.health})
        return info
