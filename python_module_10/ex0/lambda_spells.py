

def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda a: a['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda m: m['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda s: f"* {s} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    powers = list(map(lambda m: m['power'], mages))
    return {
        "min_power": min(powers),
        "max_power": max(powers),
        "avg_power": sum(powers)/len(powers)
    }


"""
def main() -> None:
    artifacts = [{'name': 'Ice Wand', 'power': 72, 'type': 'armor'},
                 {'name': 'Crystal Orb', 'power': 100, 'type': 'weapon'},
                 {'name': 'Crystal Orb', 'power': 118, 'type': 'focus'},
                 {'name': 'Wind Cloak', 'power': 112, 'type': 'relic'}]

    mages = [{'name': 'Luna', 'power': 58, 'element': 'lightning'},
             {'name': 'Phoenix', 'power': 90, 'element': 'wind'},
             {'name': 'Zara', 'power': 80, 'element': 'ice'},
             {'name': 'Casey', 'power': 71, 'element': 'earth'},
             {'name': 'Alex', 'power': 79, 'element': 'lightning'}]

    spells = ['fireball', 'darkness', 'blizzard', 'flash']
    sorted_artifacts = artifact_sorter(artifacts)
    for i in sorted_artifacts:
        print(f"{i['name']} ({i['power']}power) comes before ", end="")
    print(mage_stats(mages))
    print(spell_transformer(spells))


if __name__ == "__main__":
    main()
"""
