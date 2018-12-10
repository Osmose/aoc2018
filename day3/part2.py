import os
import sys
import re

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    puzzle_input = f.read()


fabric = []
fabric_side = 1100
for k in range(fabric_side * fabric_side):
    fabric.append(0)

for line in puzzle_input.split('\n'):
    if not line:
        break

    cid, left, top, width, height = [int(chunk) for chunk in re.split(r'[@,:x]', line[1:])]
    for x in range(width):
        for y in range(height):
            index = left + x + ((top + y) * fabric_side)
            fabric[index] = fabric[index] + 1

for line in puzzle_input.split('\n'):
    if not line:
        print('Could not find square')
        sys.exit()

    cid, left, top, width, height = [int(chunk) for chunk in re.split(r'[@,:x]', line[1:])]
    area = width * height
    for x in range(width):
        for y in range(height):
            index = left + x + ((top + y) * fabric_side)
            area -= fabric[index]

    if area == 0:
        print(f'Found match: {cid}')
        sys.exit()
