import re
import numpy as np

with open('input/day3.txt') as f:
    inp = []
    for r in f.readlines():
        r = re.findall('([0-9]+)', r)
        inp.append([int(d) for d in r])

fabric = np.zeros((1000, 1000))

def part1():
    for n, x, y, dx, dy in inp:
        fabric[x:x+dx, y:y+dy] += 1
    return np.sum(fabric > 1)

def part2():
    for n, x, y, dx, dy in inp:
        if np.max(fabric[x:x+dx, y:y+dy]) == 1:
            return n

print(part1())
print(part2())
