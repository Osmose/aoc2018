import os


with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    puzzle_input = f.read()


def react(polymer):
    new_polymer = ''
    prev = None
    for unit in polymer:
        if prev is None:
            prev = unit
        elif prev.upper() == unit.upper() and prev != unit:
            prev = None
        else:
            new_polymer += prev
            prev = unit
    if prev:
        new_polymer += prev
    return new_polymer


def fully_react(polymer):
    while True:
        new_polymer = react(polymer)
        print(f'New Polymer ({len(new_polymer)})')
        if new_polymer == polymer:
            break
        else:
            polymer = new_polymer
    return polymer


def types(polymer):
    return set(polymer.lower())


def remove_type(polymer, type):
    return ''.join(char for char in polymer if char.lower() != type)


polymer = puzzle_input.strip()
polymer_types = types(polymer)
removed_polymers = [remove_type(polymer, type) for type in polymer_types]
best = min([fully_react(polymer) for polymer in removed_polymers], key=lambda p: len(p))

print(best)
print(f'Length: {len(best)}')
