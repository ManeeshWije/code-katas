def in_bounds(i, j, grid):
    return 0 <= i < len(grid) and 0 <= j < len(grid[0])

def dfs(i, j, grid, val, visited, group, num):
    if (i, j) in visited:
        return
    if grid[i][j] == val:
        visited.add((i, j))
        group.append((i, j))
        for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            new_i, new_j = i + dx, j + dy
            if in_bounds(new_i, new_j, grid):
                dfs(new_i, new_j, grid, val, visited, group, num)

def part1():
    with open("real_input", "r") as file:
        data = list(map(list, file.read().strip().split("\n")))
    
    comps = {}
    visited = set()
    
    num = 0
    for i in range(len(data)):
        for j in range(len(data[0])):
            if (i, j) not in visited:
                val = data[i][j]
                group = []
                dfs(i, j, data, val, visited, group, num)
                if num not in comps:
                    comps[num] = []
                comps[num] += group
                num += 1
    
    res = 0
    for _, v in comps.items():
        area = len(v)
        perimeter = 0
        for x, y in v:
            for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                new_x, new_y = x + dx, y + dy
                if not in_bounds(new_x, new_y, data) or data[new_x][new_y] != data[x][y]:
                    perimeter += 1
        res += area * perimeter

    print(res)

# def part2():
#     with open("ex_input", "r") as file:
#         data = list(map(list, file.read().strip().split("\n")))
#     
#     comps = {}
#     visited = set()
#     
#     num = 0
#     for i in range(len(data)):
#         for j in range(len(data[0])):
#             if (i, j) not in visited:
#                 val = data[i][j]
#                 group = []
#                 dfs(i, j, data, val, visited, group, num)
#                 if num not in comps:
#                     comps[num] = []
#                 comps[num] += group
#                 num += 1
#     
#     res = 0
#     print(comps)
#     for _, v in comps.items():
#         area = len(v)
#         for x, y in v:
#             for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
#                 new_x, new_y = x + dx, y + dy
#                 if not in_bounds(new_x, new_y, data) or data[new_x][new_y] != data[x][y]:
#                     pass
#
#     print(res)

# part1()
# part2()
