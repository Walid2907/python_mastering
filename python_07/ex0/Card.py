from typing import Dict, Any
from abc import ABC


class Card(ABC):
    # global var for the valid rarity
    __rarity_var = ["common", "uncommon", "rare",
                    "epic", "legendary", "eternal"]

    def __init__(self, name: str, cost: int, rarity: str):
        # check that the inpt is right and logical before constructing
        if cost < 0:
            raise ValueError("Cost must be a positive integer")
        if rarity.lower() not in self.__rarity_var:
            raise ValueError(f"Rarity must be one of {self.__rarity_var}")
        self.name = name
        self.cost = cost
        self.rarity = rarity.lower()

    def play(self, game_state: Dict[str, Any]) -> Dict[str, Any]:
        pass
    play.__isabstractmethod__ = True

# method returns infos about the card name cost rarity and type
    def get_card_info(self) -> Dict:
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity,
            "type": self.__class__.__name__.replace("Card", "")
        }

# check if the mana is enough to play
    def is_playable(self, available_mana: int) -> bool:
        return available_mana >= self.cost
