import re
from collections import Counter, defaultdict

with open('input/day4.txt') as f:
    inp = f.readlines()
    inp.sort()

detail = defaultdict(list)
total = defaultdict(int)

for line in inp:
    data = re.findall('([0-9]+)', line)
    if 'Guard' in line:
        guard = int(data[-1])
    elif 'falls asleep' in line:
        time_sleep = int(data[-1])
    else:
        time_wake = int(data[-1])
        detail[guard].extend(list(range(time_sleep, time_wake)))
        total[guard] += (time_wake - time_sleep)

def part1():
    out_time = 0

    for key, val in total.items():
        if val > out_time:
            out_time = val
            out_id = key

    out_minute, _ = Counter(detail[out_id]).most_common(1)[0]
    return out_id * out_minute

def part2():
    out_count = 0

    for key, val in detail.items():
        minute, count = Counter(val).most_common(1)[0]
        if count > out_count:
            out_count = count
            out_id = key
            out_minute = minute

    return out_id * out_minute

print(part1())
print(part2())
