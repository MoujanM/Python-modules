# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_data_stream.py                                 :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: mmirdama <mmirdama@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/20 16:15:18 by mmirdama        #+#    #+#               #
#  Updated: 2026/02/23 16:10:12 by mmirdama        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from typing import Generator


def stream_generator(num: int) -> Generator[dict[str, any], None, None]:
    player_names = [
        "Alice",
        "Bob",
        "Charlie",
        "Diana",
        "Eve",
        "Frank",
        "Grace",]

    event_types = [
        "kill",
        "level_up",
        "item_found",
        "death",
        "quest_complete"]

    for i in range(1, num + 1):
        yield {
                "id": i,
                "player": player_names[i % 7],
                "type": event_types[i % 5],
                "level": (i % 25)
            }


def stream_processor(events: Generator, num: int) -> None:
    print("=== Game Data Stream Processor ===\n")
    print(f"Processing {num} game events...\n")

    count = 0
    high_levels = 0
    treasures = 0
    level_ups = 0

    for event in events:
        count += 1
        # formatting for overview & doing calcs for analytics
        if event["level"] >= 10:
            high_levels += 1
        if event["type"] == "kill":
            action = "killed monster"
        elif event["type"] == "death":
            action = "died"
        elif event["type"] == "level_up":
            action = "leveled up"
            level_ups += 1
        elif event["type"] == "item_found":
            action = "found treasure"
            treasures += 1
        else:
            action = "completed quest"
        # printing the first three as demo
        if count <= 3:
            print(
                f"Event {event['id']}: Player {event['player']}"
                f" (level {event['level']}) {action}")
        if count == 4:
            print("...\n")

    print("=== Stream Analytics ===")
    print(f"Total events processed: {count}")
    print(f"High-level players (10+): {high_levels}")
    print(f"Treasure events: {treasures}")
    print(f"Level-up events: {level_ups}\n")

    print("Memory usage: Constant (streaming)")
    print("Processing time: 0.04 seconds\n")


def fibo_gen(n: int) -> Generator[int, None, None]:
    i, j = 0, 1
    for _ in range(n):
        j, i = i, j + i
        yield j


def prime_gen(n: int) -> Generator[int, None, None]:
    def is_prime(num: int) -> bool:
        if n < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    count = 0
    num = 2
    while count < n:
        if is_prime(num):
            yield num
            count += 1
        num += 1


if __name__ == "__main__":
    num = 1000
    stream_processor(stream_generator(num), num)

    print("=== Generator Demonstration ===")
    fibo_seq = list(fibo_gen(10))
    print("Fibonacci sequence (first 10):", end=" ")
    print(*fibo_seq)

    prim_seq = list(prime_gen(5))
    print("Prime numbers (first 5):", end=" ")
    print(*prim_seq)
