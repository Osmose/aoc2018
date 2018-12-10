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


polymer = puzzle_input.strip()
while True:
    new_polymer = react(polymer)
    print(f'New Polymer ({len(new_polymer)})')
    if new_polymer == polymer:
        break
    else:
        polymer = new_polymer

print(polymer)
print(f'Length: {len(polymer)}')
