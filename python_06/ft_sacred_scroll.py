import alchemy.elements


print("\n=== Sacred Scroll Mastery ===\n")
print("Testing direct module access:")
print(f"alchemy.elements.create_fire(): {alchemy.elements.create_fire()}")
print(f"alchemy.elements.create_water(): {alchemy.elements.create_water()}")
print(f"alchemy.elements.create_earth(): {alchemy.elements.create_earth()}")
print(f"alchemy.elements.create_air(): {alchemy.elements.create_air()}")

print("\nTesting package-level access (controlled by __init__.py):")
print(f"alchemy.create_fire(): {alchemy.create_fire()}")
print(f"alchemy.create_water(): {alchemy.create_water()}")
try:
    alchemy.elements.create_earth()
except AttributeError:
    print("alchemy.elements.create_earth(): AttributeError - not exposed")

try:
    alchemy.elements.create_air()
except AttributeError:
    print("alchemy.create_air(): AttributeError - not exposed")

print("Package metadata:")
print(alchemy.__version__)
print(alchemy.__author__)
