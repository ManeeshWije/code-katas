from collections import deque


def in_bounds(i, j, grid):
    return 0 <= i < len(grid) and 0 <= j < len(grid[0])


def part1():
    with open("real_input", "r") as file:
        data = file.read().strip().split("\n")
    n = 71
    bytes_fallen = 1024
    grid = []
    for _ in range(n):
        row = []
        for _ in range(n):
            row.append(".")
        grid.append(row)

    num = 0
    for coord in data:
        x, y = map(int, coord.split(","))
        if num == bytes_fallen:
            break
        for i in range(n):
            for j in range(n):
                if i == x and j == y:
                    grid[i][j] = "#"  # corrupted
        num += 1

    # start at (0, 0, 0 steps taken) and need to go to (n - 1, n - 1, steps taken)
    q = deque([(0, 0, 0)])
    seen = {(0, 0)}
    res = -1
    while q:
        curr_i, curr_j, steps_taken = q.popleft()
        # Check if we've reached the bottom-right corner
        if curr_i == n - 1 and curr_j == n - 1:
            res = steps_taken
            break

        for new_i, new_j in [
            (curr_i + 1, curr_j),
            (curr_i - 1, curr_j),
            (curr_i, curr_j + 1),
            (curr_i, curr_j - 1),
        ]:
            if (
                in_bounds(new_i, new_j, grid)
                and grid[new_i][new_j] != "#"
                and (new_i, new_j) not in seen
            ):
                seen.add((new_i, new_j))
                q.append((new_i, new_j, steps_taken + 1))
    print(res)


def has_path(grid):
    # start at (0, 0, 0 steps taken) and need to go to (n - 1, n - 1, steps taken)
    q = deque([(0, 0, 0)])
    seen = {(0, 0)}
    while q:
        curr_i, curr_j, steps_taken = q.popleft()
        # Check if we've reached the bottom-right corner
        if curr_i == len(grid) - 1 and curr_j == len(grid[0]) - 1:
            return True

        for new_i, new_j in [
            (curr_i + 1, curr_j),
            (curr_i - 1, curr_j),
            (curr_i, curr_j + 1),
            (curr_i, curr_j - 1),
        ]:
            if (
                in_bounds(new_i, new_j, grid)
                and grid[new_i][new_j] != "#"
                and (new_i, new_j) not in seen
            ):
                seen.add((new_i, new_j))
                q.append((new_i, new_j, steps_taken + 1))
    return False


# I used pypy and it only took 3 secs
def part2():
    with open("real_input", "r") as file:
        data = file.read().strip().split("\n")
    n = 71
    grid = []
    for _ in range(n):
        row = []
        for _ in range(n):
            row.append(".")
        grid.append(row)

    res = None
    for coord in data:
        x, y = map(int, coord.split(","))
        print(f"checking {x},{y}")
        for i in range(n):
            for j in range(n):
                if i == x and j == y:
                    grid[i][j] = "#"  # corrupted
        if not has_path(grid):
            res = (x, y)
            break
    print(res)


# part1()
part2()
