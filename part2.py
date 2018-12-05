import sys

with open('part2.txt') as f:
    puzzle_input = f.read()

seen = set()
puzzle_sum = 0
while True:
    for line in puzzle_input.split('\n'):
        if not line:
            break
        if line.startswith('+'):
            puzzle_sum += int(line[1:])
        else:
            puzzle_sum -= int(line[1:])
        if puzzle_sum in seen:
            print(f'Found: {puzzle_sum}')
            sys.exit()
        else:
            seen.add(puzzle_sum)
