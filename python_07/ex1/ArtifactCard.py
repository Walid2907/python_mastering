from ex0.Card import Card
from typing import Dict


class ArtifactCard(Card):
    def __init__(self, name: str, cost: int,
                 rarity: str, durability: int, effect: str):
        if durability <= 0:
            raise ValueError("your artifact is broken!!!")
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect

    def play(self, game_state: Dict) -> Dict:
        available_mana = game_state.get("mana", 0)
        if self in game_state.get("artifacts", []):
            return {
                "card_played": None,
                "mana_used": 0,
                "effect": f"{self.name} is already active"
            }
        if self.is_playable(available_mana):
            # remove the consumed mana from the game stat
            game_state["mana"] = available_mana - self.cost
            game_state.setdefault("artifacts", []).append(self)
            return {
                "card_played": self.name,
                "mana_used": self.cost,
                "effect": self.effect
            }
        return {"card_played": None,
                "mana_used": 0, "effect": "Not enough mana"}

    def activate_ability(self) -> Dict:
        if self.durability <= 0:
            return {
                "artifact": self.name,
                "effect": "Artifact is destroyed"
            }
        self.durability -= 1
        return {
            "artifact": self.name,
            "effect": self.effect,
            "durability_left": self.durability
        }
