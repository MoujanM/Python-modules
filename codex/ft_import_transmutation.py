
def full_imp() -> str:
    import alchemy

    return f"alchemy.elements.create_fire(): {alchemy.elements.create_fire()}"


def spec_imp() -> str:
    from alchemy.elements import create_water

    return f"create_water(): {create_water()}"


def ali_imp() -> str:
    from alchemy.potions import healing_potion as heal

    return f"heal(): {heal()}"


def multi_imp() -> str:
    from alchemy.elements import create_earth, create_fire
    from alchemy.potions import strength_potion

    earth = create_earth()
    fire = create_fire()

    strength = strength_potion()
    
    return f"create_earth(): {earth}\ncreate_fire(): {fire}\nstrength_potion(): {strength}"

def main() -> None:
    print("\n=== Import Transmutation Mastery ===\n")

    print("Method 1 - Full module import:")
    print(f"{full_imp()}\n")

    print("Method 2 - Specific function import:")
    print(f"{spec_imp()}\n")

    print("Method 3 - Aliased import:")
    print(f"{ali_imp()}\n")

    print("Method 4 - Multiple imports:")
    print(f"{multi_imp()}\n")

    print("All import transmutation methods mastered!")

main()