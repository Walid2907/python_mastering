from typing import Dict, List, Any
from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):
    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        attack_power: int,
        health: int,
        defense: int,
        mana: int,
    ):
        super().__init__(name, cost, rarity)

        if attack_power <= 0:
            raise ValueError("attack_power must be a positive integer")
        if health <= 0:
            raise ValueError("health must be a positive integer")
        if defense < 0:
            raise ValueError("defense must be a non-negative integer")
        if mana < 0:
            raise ValueError("mana must be a non-negative integer")

        self.attack_power = attack_power
        self.health = health
        self.defense = defense
        self.mana = mana

    def play(self, game_state: Dict[str, Any]) -> Dict[str, Any]:
        available_mana = game_state.get("mana", 0)
        game_state.setdefault("battlefield", [])

        if not self.is_playable(available_mana):
            return {"card_played": None, "mana_used": 0,
                    "effect": "Not enough mana"}

        game_state["mana"] = available_mana - self.cost
        game_state["battlefield"].append(self)
        return {"card_played": self.name, "mana_used": self.cost,
                "effect": "Elite card deployed"}

    def attack(self, target: Any) -> Dict[str, Any]:
        target_name = getattr(target, "name", str(target))
        return {"attacker": self.name, "target": target_name,
                "damage": self.attack_power, "combat_type": "melee"}

    def defend(self, incoming_damage: int) -> Dict[str, Any]:
        blocked = min(max(incoming_damage, 0), self.defense)
        taken = max(0, incoming_damage - blocked)
        self.health -= taken
        return {
            "defender": self.name,
            "damage_taken": taken,
            "damage_blocked": blocked,
            "still_alive": self.health > 0
        }

    def get_combat_stats(self) -> Dict[str, Any]:
        return {"attack_power": self.attack_power,
                "defense": self.defense, "health": self.health}

    def cast_spell(self, spell_name: str,
                   targets: List[Any]) -> Dict[str, Any]:
        mana_cost = 4
        if self.mana < mana_cost:
            return {
                "caster": self.name,
                "spell": spell_name,
                "targets": [getattr(t, "name", str(t)) for t in targets],
                "mana_used": 0,
                "effect": "Not enough mana"
            }

        self.mana -= mana_cost
        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": [getattr(t, "name", str(t)) for t in targets],
            "mana_used": mana_cost
        }

    def channel_mana(self, amount: int) -> Dict[str, Any]:
        if amount < 0:
            raise ValueError("amount must be non-negative")
        self.mana += amount
        return {"channeled": amount, "total_mana": self.mana}

    def get_magic_stats(self) -> Dict[str, Any]:
        return {"mana": self.mana}
