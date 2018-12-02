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
    for box_a in inp:
        for box_b in inp:
            diff_idx = None
            diff_count = 0
            for idx in range(len(box_a)):
                if box_a[idx] != box_b[idx]:
                    diff_idx = idx
                    diff_count += 1
                    if diff_count > 1:
                        break
            if diff_count == 1:
                return box_a[:diff_idx] + box_a[diff_idx+1:]

print(part1())
print(part2())
