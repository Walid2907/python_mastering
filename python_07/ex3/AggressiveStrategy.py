from typing import Dict, List, Any
from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    def get_strategy_name(self) -> str:
        return self.__class__.__name__

    def prioritize_targets(self, available_targets: List[Any]) -> List[Any]:
        return list(available_targets)

    def execute_turn(self, hand: List[Any],
                     battlefield: List[Any],
                     game_state: Dict[str, Any]) -> Dict[str, Any]:
        mana = game_state.get("mana", 0)
        hand.sort(key=lambda c: getattr(c, "cost", 999))

        cards_played = []
        mana_used = 0

        remaining = []
        for card in hand:
            if getattr(card, "cost", 999) <= mana:
                result = card.play(game_state)
                if result.get("card_played"):
                    cards_played.append(result["card_played"])
                    used = result.get("mana_used", 0)
                    mana_used += used
                    mana -= used
                else:
                    remaining.append(card)
            else:
                remaining.append(card)

        hand[:] = remaining

        # simple damage estimation
        damage_dealt = 0
        for unit in battlefield:
            if hasattr(unit, "attack_power"):
                damage_dealt += getattr(unit, "attack_power", 0)
            elif hasattr(unit, "attack"):
                damage_dealt += getattr(unit, "attack", 0)

        return {
            "strategy": self.get_strategy_name(),
            "actions": {
                "cards_played": cards_played,
                "mana_used": mana_used,
                "targets_attacked": ["Enemy Player"],
                "damage_dealt": damage_dealt
            }
        }
