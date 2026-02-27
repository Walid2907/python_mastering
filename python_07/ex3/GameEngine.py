from typing import Dict, Any, List
from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:
    def __init__(self):
        self.factory = None
        self.strategy = None
        self.turns_simulated = 0
        self.total_damage = 0
        self.cards_created = 0

        self.battlefield: List[Any] = []
        self.hand: List[Any] = []
        self.game_state: Dict[str, Any] = {"mana": 6,
                                           "battlefield": self.battlefield,
                                           "artifacts": []}

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        self.factory = factory
        self.strategy = strategy

    def simulate_turn(self) -> Dict[str, Any]:
        if self.factory is None or self.strategy is None:
            raise RuntimeError("Engine not configured")

        if not self.hand:
            self.hand = [
                self.factory.create_creature("dragon"),
                self.factory.create_creature("goblin"),
                self.factory.create_spell("lightning")
            ]
            self.cards_created += len(self.hand)

        report = self.strategy.execute_turn(self.hand,
                                            self.battlefield, self.game_state)

        self.turns_simulated += 1
        self.total_damage += report.get("actions", {}).get("damage_dealt", 0)

        return report

    def get_engine_status(self) -> Dict[str, Any]:
        return {
            "turns_simulated": self.turns_simulated,
            "strategy_used": self.strategy.get_strategy_name()
            if self.strategy else None,
            "total_damage": self.total_damage,
            "cards_created": self.cards_created
        }
