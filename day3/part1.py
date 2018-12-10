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
        print(f'Overlap: {len([cell for cell in fabric if cell > 1])}')
        with open(os.path.join(os.path.dirname(__file__), 'fabric.txt'), 'w') as f:
            for y in range(fabric_side):
                for x in range(fabric_side):
                    f.write(str(fabric[x + (y * fabric_side)]))
                f.write('\n')
        sys.exit()

    try:
        cid, left, top, width, height = [int(chunk) for chunk in re.split(r'[@,:x]', line[1:])]
    except ValueError:
        print(line)
        raise

    for x in range(width):
        for y in range(height):
            index = left + x + ((top + y) * fabric_side)
            try:
                fabric[index] = fabric[index] + 1
            except Exception:
                print(f'Left: {left}, Top: {top}, X: {x}, Y: {y}, Width: {width}, Height: {height}')
                print(f'Index: {index}')
                raise
