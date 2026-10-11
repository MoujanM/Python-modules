
from collections.abc import Callable
from typing import Any
import functools
import operator

def spell_reducer(spells: list[int], operation: str) -> int:
    allowed_ops = {'add': operator.add,
                   'multiply': operator.mul,
                   'max': max,
                   'min': min}
    if not spells[0]:
        return 0
    
    if operation in allowed_ops.keys():
        op = allowed_ops.get(operation)
        return functools.reduce(op, spells)
    else:
        raise Exception("Invalid operation.")


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    fire_enchantment = functools.partial(base_enchantment, power=50, element='fire')
    water_enchantment = functools.partial(base_enchantment, power=50, element='water')
    ice_enchantment = functools.partial(base_enchantment, power=50, element='ice')
    return {'fire': fire_enchantment,
            'water': water_enchantment,
            'ice': ice_enchantment}

@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return (memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2))


def spell_dispatcher() -> Callable[[Any], str]:
    @functools.singledispatch
    def dispatcher(arg: Any) -> str:
        return "Unknown spell type"

    @dispatcher.register
    def _(arg: int) -> str:
        return (f"Damage spell: {arg} damage")
    
    @dispatcher.register
    def _(arg: str) -> str:
        return (f"Enchantment: {arg}")

    @dispatcher.register
    def _(arg: list) -> str:
        return (f"Multi-cast: {len(arg)} spells")
    
    return dispatcher
    


def magic(power: int, element: str, target: str) -> str:
    return f"Enchanted {target} with {power} {element}"

def main() -> None:
    print("\nTesting spell reducer...")
    spells = [15, 10, 40, 35]
    print(f"Sum: {spell_reducer(spells, 'add')}")
    print(f"Product: {spell_reducer(spells, 'multiply')}")
    print(f"Max: {spell_reducer(spells, 'max')}")

    print("\nTesting partial enchanter...")
    enchants = partial_enchanter(magic)
    target = "Enemy"
    for element in enchants.keys():
        print(f"{element.title()} partial: {enchants[element](target=target)}")
    

    print("\nTesting memoized fibonacci...")
    fib_tests = [0, 1, 10, 15]
    for test in fib_tests:
        print(f"Fib({test}): {memoized_fibonacci(test)}")

    print("\nTesting spell dispatcher...")
    tests = [42, "fireball", ['blizzard', 'lightening', 'heal'], {}]
    for test in tests:
        dispatcher = spell_dispatcher()
        print(f"{dispatcher(test)}")

main()