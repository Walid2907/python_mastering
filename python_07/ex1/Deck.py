from typing import Dict
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
import random


class Deck:
    def __init__(self):
        self.deck = []

    def add_card(self, card: Card) -> None:
        self.deck.append(card)

    def remove_card(self, card_name: str) -> bool:
        for card in self.deck:
            if card_name == card.name:
                self.deck.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.deck)

    def draw_card(self) -> Card:
        if len(self.deck) == 0:
            raise ValueError("no more cards to draw")
        return self.deck.pop(0)

    def get_deck_stats(self) -> Dict:
        stats = {"total_cards": len(self.deck),
                 "creatures": 0,
                 "spells": 0,
                 "artifacts": 0,
                 "avg_cost": 0
                 }
        total = 0
        for card in self.deck:
            total += card.cost
            if isinstance(card, CreatureCard):
                stats["creatures"] += 1
            elif isinstance(card, SpellCard):
                stats["spells"] += 1
            elif isinstance(card, ArtifactCard):
                stats["artifacts"] += 1
        stats["avg_cost"] = round(total / len(self.deck), 1) if self.deck else 0
        return stats
