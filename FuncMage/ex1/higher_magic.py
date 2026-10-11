
from collections.abc import Callable


# first-class citizens/functions - can be:
# assigned to variables
# passed as args to other functs
# returned from other functs
def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target}, -{power} DP"


def heal(target: str, power: int) -> str:
    return f"Heal restores {target}, +{power} HP"


# higher-order functs can:
# take one/more functs as args
# return a funct as result
def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combiner(target: str, power: int) -> tuple[str, str]:
        res1 = spell1(target, power).split(', ')[0]
        res2 = spell2(target, power).split(', ')[0]
        return (res1, res2)
    return combiner


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified_spell(target: str, power: int) -> str:
        amplified_power = power * multiplier
        return base_spell(target, amplified_power)
    return amplified_spell


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def conditioned_spell(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        else:
            return "Spell fizzled"
    return conditioned_spell


def spell_sequence(spells: list[Callable]) -> Callable:
    def cast_list(target: str, power: int) -> str:
        results: list[str] = []
        for spell in spells:
            results.append(spell(target, power))
        return results
    return cast_list


def main() -> None:

    test_values = [5, 9, 9]
    test_targets = ['Dragon', 'Goblin', 'Wizard', 'Knight']
    
    print("\nTesting spell combiner...")
    combined = spell_combiner(fireball, heal)
    res1, res2 = combined(test_targets[0], test_values[0])
    print(f"Combined spell result: {res1}, {res2}")
        
    print("\nTesting power amplifier...")
    multiplier = 3
    ampfed = power_amplifier(fireball, 3)
    result = ampfed(test_targets[1], test_values[1])
    print(f"Original: {test_values[1]}, Amplified: {test_values[1] * multiplier}")
    # print(result)
    
    print("\nTesting conditional caster...")
    cond = conditional_caster(lambda target, power: power > 10, fireball)
    print(cond(test_targets[1], test_values[1]))

    print("\nTesting spell sequence...")
    seq = spell_sequence([fireball, heal])
    print(*seq(test_targets[2], test_values[2]), sep='\n')


main()