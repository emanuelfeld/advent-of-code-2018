import re
from collections import defaultdict, deque

with open('input/day9.txt') as f:
    num_p, num_m = map(int, re.findall(r'\d+', f.read()))  

def solve(players, marbles):
    scores = defaultdict(int)
    circle = deque([0])
    
    for m in range(1, marbles + 1):
        if m % 23:
            circle.rotate(-1)
            circle.append(m)
        else:
            circle.rotate(7)
            scores[m % players] += m + circle.pop()
            circle.rotate(-1)
    return max(scores.values())

print('part 1:', solve(num_p, num_m))
print('part 2:', solve(num_p, num_m * 100))
