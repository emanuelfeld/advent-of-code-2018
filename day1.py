from itertools import cycle

with open('input/day1.txt') as f:
    inp = [int(r) for r in f.readlines()]

def part1():
    return sum(inp)

def part2():
    freq = 0
    seen = set([0])
    for change in cycle(inp):
        freq += change
        if freq in seen:
            return freq
        seen.add(freq)

print(part1())
print(part2())
