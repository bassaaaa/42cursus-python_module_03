import sys


def main() -> None:
    scores = []

    print("=== Player Score Analytics ===")

    index = 1
    while index < len(sys.argv):
        arg = sys.argv[index]
        try:
            scores += [int(arg)]
        except ValueError:
            print(f"Invalid parameter: '{arg}'")
        index += 1

    if len(scores) == 0:
        print(
            "No scores provided. "
            "Usage: python3 ft_score_analytics.py <score1> <score2> ..."
        )
        return

    players = len(scores)
    total = sum(scores)
    max_score = max(scores)
    min_score = min(scores)
    print(f"Scores processed: {scores}")
    print(f"Total players: {players}")
    print(f"Total score: {total}")
    print(f"Average score: {total / players}")
    print(f"High score: {max_score}")
    print(f"Low score: {min_score}")
    print(f"Score range: {max_score - min_score}")


if __name__ == "__main__":
    main()
