
from collections.abc import Callable

def mage_counter() -> Callable:
    count = 0
    def counter() -> int:
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> Callable:
    total_power = initial_power
    def accumulate(amount: int) -> int:
        nonlocal total_power
        total_power += amount
        return total_power
    return accumulate


def enchantment_factory(enchantment_type: str) -> Callable:
    def enchanted(item: str) -> str:
        return " ".join([enchantment_type, item])
    return enchanted


def memory_vault() -> dict[str, Callable]:
    vault: dict = {}
    def store(key: str, value: str) -> None:
        return vault.update({key: value})
    def recall(key: str):
        return vault.get(key, "Memory not found")
    return {"store": store,
            "recall": recall}




def main() -> None:
    print("\nTesting mage counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()
    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    print(f"counter_b call 1: {counter_b()}")

    print("\nTesting spell accumulator...")
    base = 100
    accumulator = spell_accumulator(base)
    print(f"Base {base}, add 20: {accumulator(20)}")
    print(f"Base {base}, add 30: {accumulator(30)}")

    print("\nTesting enchantment factory...")
    flaming = enchantment_factory("Flaming")
    frozen = enchantment_factory("Frozen")
    print(flaming("Sword"))
    print(frozen("Shield"))

    print("\nTesting memory vault...")
    vault = memory_vault()
    secret = ['secret', 42]
    vault['store'](*secret)
    print(f"Store '{secret[0]}' = {secret[1]}")
    print(f"Recall '{secret[0]}': {vault['recall']('secret')}")
    print(f"Recall 'unknown': {vault['recall']('unknown')}")


main()