from alchemy.grimoire import validate_ingredients, record_spell

def main() -> None:
    print("\n=== Circular Curse Breaking ===\n")

    print("Testing ingredient validation:")
    ings1 = validate_ingredients("fire air")
    ings2 = validate_ingredients("dragon scales")

    print(f'validate_ingredients("fire air"): {ings1}')
    print(f'validate_ingredients("dragon scales"): {ings2}')

    print("\nTesting spell recording with validation:")
    spell1 = record_spell("Fireball", "fire")
    spell2 = record_spell("Dark Magic", "shadow")
    print(f'record_spell("Fireball", "fire"): {spell1}')
    print(f'record_spell(Dark Magic", "shadow"): {spell2}')

    print("\nTesting late import technique:")
    spell3 = record_spell("Lightning", "air")
    print(f'record_spell("Lightning", "air"): {spell3}')

    print("\nCircular dependency curse avoided using late imports!")
    print("All spells processed safely!")

main()