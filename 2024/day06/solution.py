file_name = 'input.txt'
with open(file_name) as f:
    guard_map = [list(line) for line in f.read().splitlines()]

start = (-1, -1)
for row in range(len(guard_map)):
    for col in range(len(guard_map[0])):
        if guard_map[row][col] not in ('#', '.'):
            start = (row, col)

def walk(r, c, d, visit):
    while not(r + d[0] < 0 or r + d[0] == len(guard_map) or c + d[1] < 0 or c + d[1] == len(guard_map[0])):
        if guard_map[r + d[0]][c + d[1]] != '#':
            r, c= r + d[0], c + d[1]
        else:
            new_d = (0, -1) if d == (1, 0) else (1, 0) if d == (0, 1) else (0, 1) if d == (-1, 0) else (-1, 0)
            d = new_d
        visit.add((r, c))

def loop(r, c, d, visit):
    while not(r + d[0] < 0 or r + d[0] == len(guard_map) or c + d[1] < 0 or c + d[1] == len(guard_map[0])):
        if (r, c, d) in visit:
            return True
        visit.add((r, c, d))
        if guard_map[r + d[0]][c + d[1]] != '#':
            r, c= r + d[0], c + d[1]
        else:
            new_d = (0, -1) if d == (1, 0) else (1, 0) if d == (0, 1) else (0, 1) if d == (-1, 0) else (-1, 0)
            d = new_d
    return (r, c, d) in visit

def part_one():
    visit = set()
    row, col = start
    visit.add((row, col))
    walk(row, col, (-1, 0), visit)
    return visit

def part_two(obstacles):
    result = 0
    for row, col in obstacles:
        if guard_map[row][col] == '.':
            visit = set()
            guard_map[row][col] = '#'
            if loop(start[0], start[1], (-1, 0), visit):
                result += 1
            guard_map[row][col] = '.'
    return result

print('Lösung zu Teil 1:', len(part_one()))
print('Lösung zu Teil 2:', part_two(part_one()))