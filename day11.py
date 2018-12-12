SERIAL = 7139
GRID_SIZE = 300

def cell_power(x, y):
    grid_id = x + 10
    return ((grid_id * y + SERIAL) * grid_id) // 100 % 10 - 5


sum_table = [[0 for _ in range(GRID_SIZE + 1)] for _ in range(GRID_SIZE + 1)]
for x in range(299, -1, -1):
    for y in range(299, -1, -1):
        sum_table[x][y] = cell_power(x, y) + sum_table[x+1][y] + \
            sum_table[x][y+1] - sum_table[x+1][y+1]


def subgrid_power(x, y, w):
    x -= 1
    y -= 1
    return sum_table[x][y] + sum_table[x+w][y+w] - sum_table[x][y+w] - sum_table[x+w][y]


def part2():
    max_power = 0
    max_w = 0
    max_x = 0
    max_y = 0

    for w in range(1, GRID_SIZE + 1):
        for x in range(1, GRID_SIZE - w + 1):
            for y in range(1, GRID_SIZE - w + 1):
                power = subgrid_power(x, y, w)
                if power > max_power:
                    max_power, max_w, max_x, max_y = power, w, y, x

    return max_power, max_w, max_x, max_y


print(part2())
