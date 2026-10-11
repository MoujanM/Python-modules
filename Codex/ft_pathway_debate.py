
def abs_imp() -> str:
    from alchemy.transmutation.basic import lead_to_gold, stone_to_gem

    return f"lead_to_gold(): {lead_to_gold()}\nstone_to_gem(): {stone_to_gem()}"


def rel_imp() -> str:
    from alchemy.transmutation.advanced import philosophers_stone, elixir_of_life

    return f"philosophers_stone(): {philosophers_stone()}\nelixir_of_life(): {elixir_of_life()}"

def pack_imp() -> str:
    import alchemy

    return (f"alchemy.transmutation.lead_to_gold(): {alchemy.transmutation.lead_to_gold()}\n"
            f"alchemy.transmutation.philosophers_stone(): {alchemy.transmutation.philosophers_stone()}")
def main() -> None:
    print("\n=== Pathway Debate Mastery ===")

    print("\nTesting Absolute Imports (from basic.py):")
    print(abs_imp())

    print("\nTesting Relative Imports (from advanced.py):")
    print(rel_imp())

    print("\nTesting Package Access:")
    print(pack_imp())

    print("\nBoth pathways work! clear, Relative: concise")


main()

