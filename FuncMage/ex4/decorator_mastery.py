

from functools import wraps
from collections.abc import Callable
import time


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start_time = time.perf_counter()

        result = func(*args, **kwargs)

        end_time = time.perf_counter()
        print(f"Spell completed in {(end_time - start_time):.3f} seconds")
        return (result)
    
    return (wrapper)


def power_validator(min_power: int) -> Callable:
    def validator(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            power = None
            for arg in args:
                if isinstance(arg, int):
                    power = arg
                    break
            if power >= min_power:
                return func(*args, **kwargs)
            else:
                return "Insufficient power for this spell"
        return wrapper
    return validator


def retry_spell(max_attempts: int) -> Callable:
    def retry(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    func(*args, **kwargs)
                    print(f"{func.__name__} cast successfully!")
                    break
                except Exception as e:
                    if attempt == max_attempts:
                        print(f"Spell casting failed after {max_attempts} attempts")
                    else:
                        print(f"Spell failed, retrying... (attempt {attempt}/{max_attempts})")
        return wrapper
    return retry


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return (len(name) >= 3 and name.replace(" ", "").isalpha())

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


def main() -> None:
    print("\nTesting spell timer...")
    
    @spell_timer
    def fireball(target: str, power: int) -> str:
        time.sleep(1.011)
        return f"Fireball cast!"
    
    result = fireball('Goblin', 5)
    print(f"Result: {result}")
    
    print("\nTesting power validator...")
    @power_validator(min_power=10)
    def lightening_bolt(power: int, target: str) -> str:
        return f"Bolted {target} with {power} power"

    print(f"High powered spell: {lightening_bolt(35, 'Enemy')}")
    print(f"Low powered spell: {lightening_bolt(8, 'Enemy')}")

    print("\nTesting retry spell...")
    # @retry_spell(max_attempts=3)
    def excepting_bolt(power: int, target: str) -> str:
        if power > 5:
            raise Exception
        return f"Bolted {target} with {power} power"
    
    # excepting_bolt(7, 'oops')
    retrier = retry_spell(3)
    protected_bolt = retrier(excepting_bolt)
    protected_bolt(7, 'oops')
    protected_bolt(4, 'Waah')

    print("\nTesting MageGuild...")
    print(MageGuild.validate_mage_name('Phoenix'))
    print(MageGuild.validate_mage_name('Test@Name'))
    
    guild = MageGuild()
    print(guild.cast_spell("Fireball", 15))
    print(guild.cast_spell("Drizzle", 5))




main()