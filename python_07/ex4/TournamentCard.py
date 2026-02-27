from typing import Dict, Any
from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    def __init__(self, name: str, cost: int,
                 rarity: str, attack_power: int,
                 health: int, defense: int = 0):
        super().__init__(name, cost, rarity)

        if attack_power <= 0:
            raise ValueError("attack_power must be positive")
        if health <= 0:
            raise ValueError("health must be positive")
        if defense < 0:
            raise ValueError("defense must be non-negative")

        self.attack_power = attack_power
        self.health = health
        self.defense = defense

        self._wins = 0
        self._losses = 0
        self._rating = 1200

    def play(self, game_state: Dict[str, Any]) -> Dict[str, Any]:
        available_mana = game_state.get("mana", 0)
        game_state.setdefault("battlefield", [])

        if not self.is_playable(available_mana):
            return {"card_played": None, "mana_used": 0,
                    "effect": "Not enough mana"}

        game_state["mana"] = available_mana - self.cost
        game_state["battlefield"].append(self)
        return {"card_played": self.name,
                "mana_used": self.cost, "effect": "Tournament card deployed"}

    def attack(self, target: Any) -> Dict[str, Any]:
        target_name = getattr(target, "name", str(target))
        return {"attacker": self.name, "target": target_name,
                "damage": self.attack_power, "combat_type": "tournament"}

    def defend(self, incoming_damage: int) -> Dict[str, Any]:
        blocked = min(max(incoming_damage, 0), self.defense)
        taken = max(0, incoming_damage - blocked)
        self.health -= taken
        return {"defender": self.name, "damage_taken": taken,
                "damage_blocked": blocked, "still_alive": self.health > 0}

    def get_combat_stats(self) -> Dict[str, Any]:
        return {"attack_power": self.attack_power,
                "defense": self.defense, "health": self.health}

    def calculate_rating(self) -> int:
        return int(self._rating)

    def update_wins(self, wins: int) -> None:
        if wins < 0:
            raise ValueError("wins must be non-negative")
        self._wins += wins
        self._rating += 16 * wins

    def update_losses(self, losses: int) -> None:
        if losses < 0:
            raise ValueError("losses must be non-negative")
        self._losses += losses
        self._rating -= 16 * losses

    def get_rank_info(self) -> Dict[str, Any]:
        return {"rating": self.calculate_rating(),
                "wins": self._wins, "losses": self._losses}

    def get_tournament_stats(self) -> Dict[str, Any]:
        stats = self.get_card_info()
        stats.update(self.get_combat_stats())
        stats.update(self.get_rank_info())
        return stats
