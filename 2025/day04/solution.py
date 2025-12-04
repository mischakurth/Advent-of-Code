from collections import defaultdict
file_name = 'input.txt'

def day_04(part):
    with open(file_name) as f:
        grid = [list(line) for line in f.read().splitlines()]
    neigh, rolls = forklifts_neighbours(grid)
    if part == 1:
        return len(list(n for n in rolls if len(neigh[n]) < 4))
    else:
        return len(rolls) - len(neigh_iter(neigh, rolls.copy()))

def update_neigh(grid, row, col, neigh):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    for d in directions:
        if row + d[0] < 0 or row + d[0] == len(grid) or col + d[1] < 0 or col + d[1] == len(grid[0]):
            continue
        if grid[row + d[0]][col + d[1]] == '@':
            neigh[(row, col)].add((row + d[0], col + d[1]))
            neigh[(row + d[0], col + d[1])].add((row, col))

def neigh_iter(neigh, rolls):
    remove_in_current_round = set(n for n in rolls if len(neigh[n]) < 4)
    while remove_in_current_round:
        rolls -= remove_in_current_round
        for r in rolls:
            neigh[r] -= remove_in_current_round
        remove_in_current_round = set(n for n in rolls if len(neigh[n]) < 4)
    return rolls

def forklifts_neighbours(grid):
    rolls = set()
    neigh = defaultdict(set)
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == '@':
                rolls.add((row, col))
                update_neigh(grid, row, col, neigh)
    return neigh, rolls

print('Lösung zu Teil 1:', day_04(1))
print('Lösung zu Teil 2:', day_04(2))