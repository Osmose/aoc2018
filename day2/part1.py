import os
from collections import Counter

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    puzzle_input = f.read()

twos = 0
threes = 0
for line in puzzle_input.split('\n'):
    if not line:
        break

    counts = Counter(line)
    if 3 in counts.values():
        threes += 1
    if 2 in counts.values():
        twos += 1

print(f'Checksum: {twos * threes}')
