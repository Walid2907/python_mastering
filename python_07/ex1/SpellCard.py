from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from typing import Dict, List


class SpellCard(Card):
    valid_effect_type = ["damage", "heal", "buff", "debuff"]

    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        if effect_type not in self.valid_effect_type:
            raise ValueError("Invalid spell effect type")
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type

    def play(self, game_state: Dict) -> Dict:
        # check if u can play the card
        available_mana = game_state.get("mana", 0)
        if self.is_playable(available_mana):
            # remove the consumed mana from the game stat
            game_state["mana"] = available_mana - self.cost
            return {
                "card_played": self.name,
                "mana_used": self.cost,
                "effect": f"Spell cast: {self.effect_type}",
                "consumed": True
            }
        return {"card_played": None,
                "mana_used": 0, "effect": "Not enough mana"}

    def resolve_effect(self, targets: List[CreatureCard]) -> Dict[str, dict]:
        results = {}
        for target in targets:
            # damage effect
            if self.effect_type == "damage":
                # 1 for now but need correction
                target.health -= 1
                # to the damage delt
                defeated = target.health <= 0
                # make it nest dict for each one more
                # reasonable
                results[target.name] = {
                    "target": target.name,
                    "effect": "damage",
                    "damage_dealt": 1,
                    "target_defeated": defeated,
                    "target_remaining_health": max(target.health, 0)
                }

            # heal effect
            elif self.effect_type == "heal":
                target.health += 1  # same here 1 is for test
                results[target.name] = {
                    "target": target.name,
                    "effect": "heal",
                    "healing_done": 1,
                    "target_health": target.health
                }
            # buff effect
            elif self.effect_type == "buff":
                target.attack += 1
                results[target.name] = {
                    "target": target.name,
                    "effect": "buff",
                    "buff_done": "plus 1 in attack",
                    "target_attack": target.attack
                }
            # debuff effect
            elif self.effect_type == "debuff":
                target.attack = max(0, target.attack - 1)
                results[target.name] = {
                    "target": target.name,
                    "effect": "debuff",
                    "buff_done": "minus 1 in attack",
                    "target_attack": target.attack
                }
        return results
