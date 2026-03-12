import re

MULTIPLIERS = {
    "k": 1e3,
    "m": 1e-3,
    "u": 1e-6,
    "n": 1e-9,
    "meg": 1e6
}

def parse_value(text, name):
    pattern = rf"{name}\s*=\s*([\d\.]+)\s*([a-zA-Z]*)"
    match = re.search(pattern, text, re.IGNORECASE)

    if not match:
        return None

    value = float(match.group(1))
    unit = match.group(2).lower()

    for key, mult in MULTIPLIERS.items():
        if unit.startswith(key):
            value *= mult
            break

    return value