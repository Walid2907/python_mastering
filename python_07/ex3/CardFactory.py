from abc import ABC, abstractmethod
from typing import Dict, Any
from ex0.Card import Card


class CardFactory(ABC):
    @abstractmethod
    def create_creature(self, name_or_power: Any) -> Card:
        pass

    @abstractmethod
    def create_spell(self, name_or_power: Any) -> Card:
        pass

    @abstractmethod
    def create_artifact(self, name_or_power: Any) -> Card:
        pass

    @abstractmethod
    def create_themed_deck(self, size: int) -> Dict[str, Any]:
        pass

    @abstractmethod
    def get_supported_types(self) -> Dict[str, Any]:
        pass
