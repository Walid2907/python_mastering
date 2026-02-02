from .Card import Card

class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, attack: int, health: int):
        super().__init__(name, cost, rarity)
        self.attack = attack
        self.health = health

    def play(self, game_state: dict) -> dict:
        pass

    def attack_target(self, target) -> dict:
        pass

    def get_card_info(self) -> dict:
        info= self.get_card_info()
        info.update({"attack": self.attack, "health": self.health})
        return info