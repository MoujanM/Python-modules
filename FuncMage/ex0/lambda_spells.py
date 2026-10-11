
def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return (sorted(artifacts, key=lambda item: item['power'], reverse=True))


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda item: item['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spell: f'*{spell}*', spells))


def mage_stats(mages: list[dict]) -> dict:
    get_power = lambda mage: mage['power']
    return {'max_power': max(mages, key=get_power)['power'],
            'min_power': min(mages, key=get_power)['power'],
            'avg_power': float(sum(map(get_power, mages))/len(mages))}



def main() -> None:
    artifacts = [
        {'name': 'Earth Shield', 'power': 90, 'type': 'weapon'},
        {'name': 'Ice Wand', 'power': 86, 'type': 'weapon'},
        {'name': 'Ice Wand', 'power': 103, 'type': 'weapon'},
        {'name': 'Lightning Rod', 'power': 100, 'type': 'accessory'}]
    mages = [
        {'name': 'Riley', 'power': 61, 'element': 'earth'},
        {'name': 'Ember', 'power': 88, 'element': 'earth'},
        {'name': 'Nova', 'power': 59, 'element': 'water'},
        {'name': 'Luna', 'power': 62, 'element': 'earth'},
        {'name': 'Alex', 'power': 50, 'element': 'earth'}]
    spells = ['blizzard', 'lightning', 'tsunami', 'heal']

    print("\nTesting artifact sorter...")
    sorted_art = artifact_sorter(artifacts)
    print(f"{sorted_art[0]['name']} ({sorted_art[0]['power']} power) comes before "
          f"{sorted_art[1]['name']} ({sorted_art[1]['power']} power)")

    # print("\nTesting power filter...")
    # print(*(x['name'] for x in power_filter(mages, 60)))
    
    print("\nTesting spell transformer...")
    print(*spell_transformer(spells))

    # print("\nTesting stats generator...")
    # stats = mage_stats(mages)
    # print(*stats.items())

main()