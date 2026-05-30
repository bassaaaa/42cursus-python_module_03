import typing
import random

PLAYERS = [
    "Alice",
    "Bob",
    "Charlie",
    "Dylan",
]

ACTIONS = [
    "run",
    "eat",
    "sleep",
    "grab",
    "move",
    "climb",
    "swim",
    "release",
    "use",
]


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    while True:
        name = random.choice(PLAYERS)
        action = random.choice(ACTIONS)
        yield (name, action)


def consume_event(
    event_list: list[tuple[str, str]],
) -> typing.Generator[tuple[str, str], None, None]:
    while len(event_list):
        index = random.randrange(len(event_list))
        yield event_list.pop(index)


def main() -> None:
    print("=== Game Data Stream Processor ===")

    event_stream = gen_event()
    for i in range(1000):
        event = next(event_stream)
        print(f"Event {i}: Player {event[0]} did action {event[1]}")

    event_stream = gen_event()
    event_list = []
    for _ in range(10):
        event_list.append(next(event_stream))

    print(f"Built list of 10 events: {event_list}")
    for event in consume_event(event_list):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {event_list}")


if __name__ == "__main__":
    main()
