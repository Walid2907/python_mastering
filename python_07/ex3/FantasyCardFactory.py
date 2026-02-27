import random
from typing import Dict, Any, List
from ex3.CardFactory import CardFactory
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard


class FantasyCardFactory(CardFactory):
    def __init__(self):
        self._creatures = ["dragon", "goblin"]
        self._spells = ["fireball", "lightning"]
        self._artifacts = ["mana_ring", "crystal"]

    def get_supported_types(self) -> Dict[str, Any]:
        return {
            "creatures": list(self._creatures),
            "spells": list(self._spells),
            "artifacts": list(self._artifacts)
        }

    def create_creature(self, name_or_power: Any) -> Card:
        if (isinstance(name_or_power, str)
                and name_or_power.lower() == "goblin"):
            return CreatureCard("Goblin Warrior",
                                2, "common",
                                2, 3)
        return CreatureCard("Fire Dragon", 5,
                            "legendary", 7, 5)

    def create_spell(self, name_or_power: Any) -> Card:
        if (isinstance(name_or_power, str)
                and name_or_power.lower() == "lightning"):
            return SpellCard("Lightning Bolt", 3,
                             "rare", "damage")
        return SpellCard("Fireball", 3,
                         "rare", "damage")

    def create_artifact(self, name_or_power: Any) -> Card:
        return ArtifactCard("Mana Ring", 2,
                            "uncommon", 3,
                            "Permanent: +1 mana per turn")

    def create_themed_deck(self, size: int) -> Dict[str, Any]:
        if size <= 0:
            raise ValueError("size must be positive")

        cards: List[Card] = []
        for _ in range(size):
            kind = random.choice(["creature", "spell", "artifact"])
            if kind == "creature":
                cards.append(self.create_creature(random.choice
                                                  (self._creatures)))
            elif kind == "spell":
                cards.append(self.create_spell(random.choice
                                               (self._spells)))
            else:
                cards.append(self.create_artifact(random.choice
                                                  (self._artifacts)))

        return {"size": size, "cards": cards}
