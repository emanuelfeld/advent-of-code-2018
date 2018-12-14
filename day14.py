INPUT = '633601'

def part1():
    num_recipes = int(INPUT)
    scores = [3, 7]
    elf1 = 0
    elf2 = 1

    while len(scores) < num_recipes + 10:
        new_scores = [int(d) for d in str(scores[elf1] + scores[elf2])]
        scores.extend(new_scores)
        elf1 = (elf1 + 1 + scores[elf1]) % len(scores)
        elf2 = (elf2 + 1 + scores[elf2]) % len(scores)
    
    return scores[num_recipes:num_recipes+10]

def array_ends_with(arr, sub):
    for i in range(1, len(sub) + 1):
        if arr[len(arr) - i] != sub[len(sub) - i]:
            return False
    return True

def part2():
    target = [int(d) for d in INPUT]
    scores = [3, 7]
    elf1 = 0
    elf2 = 1

    while True:
        new_scores = [int(d) for d in str(scores[elf1] + scores[elf2])]
        for d in new_scores:
            scores.append(d)
            if array_ends_with(scores, target):
                return len(scores) - len(target)
        elf1 = (elf1 + 1 + scores[elf1]) % len(scores)
        elf2 = (elf2 + 1 + scores[elf2]) % len(scores)


print(part1())
print(part2())
