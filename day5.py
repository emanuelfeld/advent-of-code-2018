import re
import string

with open(f'input/day5.txt') as infile:
    inp = infile.readline().strip()

toggle_case = {}
for lower in string.ascii_lowercase:
    upper = lower.upper()
    toggle_case[lower] = upper
    toggle_case[upper] = lower

def part1(s):
    stack = []
    for char in s:
        if stack and char == toggle_case[stack[-1]]:
            stack.pop()
        else:
            stack.append(char)
    return len(stack)

def part2(s):
    lengths = []
    for char in string.ascii_lowercase:
        s_no_char = re.sub(char, '', s, flags=re.IGNORECASE)
        lengths.append(part1(s_no_char))
    return min(lengths)

print(part1(inp))
print(part2(inp))
