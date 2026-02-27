from typing import Dict, List
from ex4.TournamentCard import TournamentCard


class TournamentPlatform:
    def __init__(self):
        self._cards: Dict[str, TournamentCard] = {}
        self._matches_played = 0

    def register_card(self, card: TournamentCard) -> str:
        base_id = card.name.lower().replace(" ", "_")
        card_id = base_id
        i = 1
        while card_id in self._cards:
            i += 1
            card_id = f"{base_id}_{i}"
        self._cards[card_id] = card
        return card_id

    def create_match(self, card1_id: str, card2_id: str) -> Dict[str, int]:
        c1 = self._cards[card1_id]
        c2 = self._cards[card2_id]

        if c1.attack_power > c2.attack_power:
            winner_id, loser_id = card1_id, card2_id
        elif c2.attack_power > c1.attack_power:
            winner_id, loser_id = card2_id, card1_id
        else:
            winner_id, loser_id = (card1_id, card2_id) \
                if c1.calculate_rating() >= c2.calculate_rating() \
                else (card2_id, card1_id)

        winner = self._cards[winner_id]
        loser = self._cards[loser_id]

        winner.update_wins(1)
        loser.update_losses(1)

        self._matches_played += 1
        return {
            "winner": winner_id,
            "loser": loser_id,
            "winner_rating": winner.calculate_rating(),
            "loser_rating": loser.calculate_rating()
        }

    def get_leaderboard(self) -> List[Dict[str, int]]:
        board = []
        for card_id, card in self._cards.items():
            info = card.get_rank_info()
            board.append({"id": card_id, "name": card.name,
                          "rating": info["rating"], "wins": info["wins"],
                          "losses": info["losses"]})
        board.sort(key=lambda x: x["rating"], reverse=True)
        return board

    def generate_tournament_report(self) -> Dict[str, int]:
        ratings = [c.calculate_rating() for c in self._cards.values()]
        avg_rating = int(sum(ratings) / len(ratings)) if ratings else 0
        return {
            "total_cards": len(self._cards),
            "matches_played": self._matches_played,
            "avg_rating": avg_rating,
            "platform_status": "active"
        }
