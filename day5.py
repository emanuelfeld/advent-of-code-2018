import string

with open('input/day5.txt') as infile:
    inp = infile.readline().strip()

# SLOW part 1

# import re

# pairs = '|'.join([f'{c}{c.upper()}|{c.upper()}{c}' for c in string.ascii_lowercase])
# pattern = re.compile(pairs)

# def part1(s):
#     l = len(s)
#     while True:
#         s = pattern.sub('', s)
#         if len(s) == l:
#             break
#         else:
#             l = len(s)
#     return l

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
    return stack

def part2(s):
    lengths = []
    for char in string.ascii_lowercase:
        s_no_char = [c for c in s if c.lower() != char]
        lengths.append(len(part1(s_no_char)))
    return min(lengths)

reduced = part1(inp)
print(len(reduced))
print(part2(reduced))
