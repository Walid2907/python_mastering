import math


def create_position(x, y, z):
    """insert the 3d coordinates"""
    return x, y, z


def distance(p1, p2):
    """calculate the distance between the two coordinates"""
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)


def parse_coordinates(coord_str):
    """parse the coordinate into a tuple of ints"""
    try:
        parts = coord_str.split(",")
        if len(parts) != 3:
            raise ValueError("Coordinates must have exactly 3 values")
        x, y, z = (int(part) for part in parts)
        return x, y, z
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: ValueError, Args: {e.args}")
        return None


def main():
    print("=== Game Coordinate System ===")

    # Create a position
    pos1 = create_position(10, 20, 5)
    print(f"Position created: {pos1}")

    # Distance from origin (0,0,0)
    origin = (0, 0, 0)
    dist = distance(origin, pos1)
    print(f"Distance between {origin} and {pos1}: {dist:.2f}\n")

    # Parse a valid coordinate string
    coord_str = "3,4,0"
    print(f'Parsing coordinates: "{coord_str}"')
    pos2 = parse_coordinates(coord_str)
    if pos2:
        print(f"Parsed position: {pos2}")
        dist2 = distance(origin, pos2)
        print(f"Distance between {origin} and {pos2}: {dist2}\n")

    # Parse an invalid coordinate string
    invalid_str = "abc,def,ghi"
    print(f'Parsing invalid coordinates: "{invalid_str}"')
    parse_coordinates(invalid_str)

    # Unpacking demonstration
    if pos2:
        x, y, z = pos2
        print("\nUnpacking demonstration:")
        print(f"Player at x={x}, y={y}, z={z}")
        print(f"Coordinates: X={x}, Y={y}, Z={z}")


main()
