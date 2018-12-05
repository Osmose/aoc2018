import os
import sys

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    puzzle_input = f.read()


def find_diff(line1, line2):
    diff = None
    for idx, letter in enumerate(line1):
        if line2[idx] != letter:
            if diff is not None:
                return None
            diff = idx
    return idx


lines = puzzle_input.split('\n')[:-1]
for line1 in lines:
    for line2 in lines:
        if line1 == line2:
            continue

        diff_id = find_diff(line1, line2)
        if diff_id is not None:
            print(line1)
            print(line2)
            print(f'Diff at {diff_id}')
            sys.exit()
