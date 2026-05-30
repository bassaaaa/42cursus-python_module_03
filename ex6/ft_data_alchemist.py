import random

PLAYERS = [
    "Alice",
    "bob",
    "Charlie",
    "dylan",
    "Emma",
    "Gregory",
    "john",
    "kevin",
    "Liam",
]


def main() -> None:
    print("=== Game Data Alchemist ===\n")
    print(f"Initial list of players: {PLAYERS}")

    capitalized_players = [name.capitalize() for name in PLAYERS]
    print(f"New list with all names capitalized: {capitalized_players}")

    capitalized_only = [name for name in PLAYERS if name.istitle()]
    print(f"New list of capitalized names only: {capitalized_only}")

    score_dict = {name: random.randint(0, 999) for name in capitalized_players}
    print(f"Score dict: {score_dict}")

    average = sum(score_dict.values()) / len(score_dict)
    print(f"Score average is {round(average, 2)}")

    high_scores = {
        name: score for name, score in score_dict.items() if average < score
    }
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()
