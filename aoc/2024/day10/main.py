def in_bounds(i, j, grid):
    return 0 <= i < len(grid) and 0 <= j < len(grid[0])

def dfs_p1(i, j, grid, seen):
    if (i, j) in seen:
        return 0
    seen.add((i, j))

    if int(grid[i][j]) == 9:
        return 1

    result = 0
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        new_i, new_j = i + dx, j + dy
        if in_bounds(new_i, new_j, grid):
            if int(grid[new_i][new_j]) == 1 + int(grid[i][j]):
                result += dfs_p1(new_i, new_j, grid, seen)
    return result

def dfs_p2(i, j, grid):
    if int(grid[i][j]) == 9:
        return 1

    result = 0
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        new_i, new_j = i + dx, j + dy
        if in_bounds(new_i, new_j, grid):
            if int(grid[new_i][new_j]) == 1 + int(grid[i][j]):
                result += dfs_p2(new_i, new_j, grid)
    return result



def part1():
    with open("real_input", "r") as file:
        data = list(map(list, file.read().strip().split("\n")))
    res = 0
    for i in range(len(data)):
        for j in range(len(data[0])):
            seen = set()
            if data[i][j] == "0":
                res += dfs_p1(i, j, data, seen)
    print(res)

def part2():
    with open("real_input", "r") as file:
        data = list(map(list, file.read().strip().split("\n")))
    res = 0
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == "0":
                res += dfs_p2(i, j, data)
    print(res)

# part1()
part2()
