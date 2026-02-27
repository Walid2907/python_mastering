from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.GameEngine import GameEngine


print("=== DataDeck Game Engine ===")

engine = GameEngine()
factory = FantasyCardFactory()
strategy = AggressiveStrategy()

engine.configure_engine(factory, strategy)

print("\nConfiguring Fantasy Card Game...")
print("Factory:", factory.__class__.__name__)
print("Strategy:", strategy.get_strategy_name())
print("Available types:", factory.get_supported_types())

print("\nSimulating aggressive turn...")
turn_report = engine.simulate_turn()
print("Turn execution:")
print(turn_report)

print("\nGame Report:")
print(engine.get_engine_status())

print("\nAbstract Factory + Strategy Pattern: Maximum flexibility achieved!")
