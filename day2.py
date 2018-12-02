from collections import Counter

with open('input/day2.txt') as f:
    inp = [r.strip() for r in f.readlines()]

def part1():
    twos = 0
    threes = 0
    for box in inp:
        counts = set(Counter(box).values())
        if 2 in counts: twos += 1
        if 3 in counts: threes += 1
    return twos * threes

def part2():
    seen = set()
    for box in inp:
        for idx in range(len(box)):
            sub = box[:idx] + box[idx+1:]
            if (idx, sub) in seen:
                return sub
            seen.add((idx, sub))

print(part1())
print(part2())
