import os
import re


with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    puzzle_input = f.read()


guards = {}


class Guard:
    def __init__(self, id):
        self.id = id
        self.sleep_data = [0 for x in range(60)]
        self.sleep_start = None  # stateful because we can

    def sleep(self, time):
        self.sleep_start = time

    def wake(self, time):
        for k in range(self.sleep_start, time):
            self.sleep_data[k] += 1

    @property
    def total_sleep(self):
        return sum(self.sleep_data)

    @property
    def most_sleep_minute(self):
        max_amount = max(self.sleep_data)
        return self.sleep_data.index(max_amount), max_amount


active_guard = None
for line in list(sorted(puzzle_input.split('\n'))):
    if not line:
        continue

    match = re.match(r'\[([\d-]+) \d\d:(\d\d)\] (.+)', line)
    date = match[1]
    minute = match[2]
    action = match[3]

    if action.startswith('Guard'):
        match = re.match(r'Guard #(\d+) begins shift', action)
        guard_id = int(match[1])
        if guard_id in guards:
            active_guard = guards[guard_id]
        else:
            guards[guard_id] = Guard(guard_id)
            active_guard = guards[guard_id]
    elif action.startswith('falls'):
        active_guard.sleep(int(minute))
    else:
        active_guard.wake(int(minute))

max_guard = max(guards.values(), key=lambda guard: guard.most_sleep_minute[1])
print(f'Guard: {max_guard.id}, Most Sleep: {max_guard.most_sleep_minute[0]}')
print(f'{max_guard.id * max_guard.most_sleep_minute[0]}')
