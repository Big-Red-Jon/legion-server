
UNITS = [
    {
        "id": 1,
        "name": "Stormtroopers",
        "unitTypeId": 3,
        "amount": 4,
        "speed": 2,
        "factionId": 1,
        "pointCost": 44,
        "ownedAmount": 4,
        "health": 1,
        "courage": 1,
        "defenseDice": 2,
        "surgeToHit": True,
        "surgeToCrit": False,
        "surgeToDefend": False,
        "weaponId": [1, 2],
        "keyWorkId": 1,
        "upgradeId": [1, 2, 3],
    },
    {
        "id": 2,
        "name": "Shoretroopers",
        "unitTypeId": 3,
        "amount": 4,
        "speed": 2,
        "factionId": 1,
        "pointCost": 52,
        "ownedAmount": 2,
        "health": 1,
        "courage": 1,
        "defenseDice": 2,
        "surgeToHit": False,
        "surgeToCrit": False,
        "surgeToDefend": False,
        "keyWorkId": [3, 4],
        "weaponId": [1, 2],
        "upgradeId": [1, 2, 3],
    },
    {
        "id": 2,
        "name": "Snowtroopers",
        "unitTypeId": 3,
        "amount": 4,
        "speed": 1,
        "factionId": 1,
        "pointCost": 52,
        "ownedAmount": 2,
        "health": 1,
        "courage": 1,
        "defenseDice": 2,
        "surgeToHit": False,
        "surgeToCrit": False,
        "surgeToDefend": False,
        "keyWorkId": 2,
        "weaponId": [1, 2],
        "upgradeId": [1, 2, 3],
    }
]


def get_all_units():
    return UNITS


def get_single_unit(id):
    request_unit = None

    for unit in UNITS:
        if unit["id"] == id:
            requested_unit = unit
    return requested_unit
