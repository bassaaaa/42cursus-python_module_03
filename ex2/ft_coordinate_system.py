import math


def to_float(value: str) -> float:
    value = value.strip()
    try:
        return float(value)
    except ValueError as e:
        print(f"Error on parameter '{value}': {e}")
        raise


def get_player_pos() -> tuple[float, float, float]:
    while True:
        input_str = input(
            "Enter new coordinates as floats in format 'x,y,z': "
        )
        parts = input_str.split(",")

        if len(parts) != 3:
            print("Invalid syntax")
            continue

        try:
            x = to_float(parts[0])
            y = to_float(parts[1])
            z = to_float(parts[2])
            return (x, y, z)
        except ValueError:
            pass


def distance(
    first_pos: tuple[float, float, float],
    second_pos: tuple[float, float, float],
) -> float:
    return math.sqrt(
        (second_pos[0] - first_pos[0]) ** 2
        + (second_pos[1] - first_pos[1]) ** 2
        + (second_pos[2] - first_pos[2]) ** 2
    )


def main() -> None:
    center = (0.0, 0.0, 0.0)

    print("=== Game Coordinate System ===\n")
    print("Get a first set of coordinates")
    first_pos = get_player_pos()
    print(f"Got a first tuple: {first_pos}")
    print(f"It includes: X={first_pos[0]}, Y={first_pos[1]}, Z={first_pos[2]}")
    print(f"Distance to center: {distance(center, first_pos):.4f}\n")

    print("Get a second set of coordinates")
    second_pos = get_player_pos()
    print(
        "Distance between the 2 sets of coordinates: "
        f"{distance(first_pos, second_pos):.4f}"
    )


if __name__ == "__main__":
    main()
