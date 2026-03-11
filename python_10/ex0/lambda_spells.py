def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    #  sort by ’power’ level (descending)
    return sorted(artifacts, key=lambda x: x['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    #  find mages with power >= min_power
    return list(filter(lambda x: x['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    #  add "* " prefix and " *" suffix to spell name
    return list(map(lambda spell: f"* {spell} *", spells))  # noqa: C417


def mage_stats(mages: list[dict]) -> dict:
    return {
        'max_power': max(mages, key=lambda x: x['power'])['power'],
        'min_power': min(mages, key=lambda x: x['power'])['power'],
        'avg_power': round(
            sum(map(lambda x: x['power'], mages)) / len(mages), 2  # noqa: C417
        )
    }


if __name__ == "__main__":
    artifacts = [
        {'name': 'Ice Wand', 'power': 85, 'type': 'relic'},
        {'name': 'Lightning Rod', 'power': 76, 'type': 'focus'},
        {'name': 'Storm Crown', 'power': 80, 'type': 'armor'},
        {'name': 'Crystal Orb', 'power': 102, 'type': 'armor'}
    ]

    mages = [
        {'name': 'Casey', 'power': 79, 'element': 'wind'},
        {'name': 'Luna', 'power': 92, 'element': 'ice'},
        {'name': 'Jordan', 'power': 51, 'element': 'light'},
        {'name': 'River', 'power': 65, 'element': 'water'},
        {'name': 'Alex', 'power': 85, 'element': 'light'}
    ]

    spells = ['heal', 'earthquake', 'lightning', 'tornado']

    print("Testing artifact sorter...")
    artifacts_sorted = artifact_sorter(artifacts)
    print(artifacts_sorted[0]["name"], end=" ")
    print(f"({artifacts_sorted[0]['power']} power)", end=" comes before ")
    print(artifacts_sorted[1]["name"], end=" ")
    print(f"({artifacts_sorted[1]['power']} power)")

    print("\nTesting spell transformer...")
    for spell in spell_transformer(spells):
        print(spell, end=" ")
