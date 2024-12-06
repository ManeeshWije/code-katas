def visit(grid, i, j):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # up, right, down, left
    direction_idx = 0  # Start by facing up
    visited = set()

    while True:
        # Add current cell to visited
        visited.add((i, j))

        # Calculate the next position based on the current direction
        next_i = i + directions[direction_idx][0]
        next_j = j + directions[direction_idx][1]

        # Check if next step is out of bounds
        if not (0 <= next_i < len(grid) and 0 <= next_j < len(grid[0])):
            return visited

        # Check if the next cell is an obstacle
        if grid[next_i][next_j] == "#":
            # Rotate 90 degrees clockwise
            direction_idx += 1
            if (
                direction_idx == 4
            ):  # If it exceeds the last valid index, reset to 0 (COULD ALSO MOD HERE REALIZED AFTER)
                direction_idx = 0
        else:
            # Move to the next cell
            i, j = next_i, next_j


def detect_cycles(grid, i, j):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    direction_idx = 0
    visited = set()

    while True:
        # we also want to add directions to seen
        visited.add((i, j, directions[direction_idx][0], directions[direction_idx][1]))

        next_i = i + directions[direction_idx][0]
        next_j = j + directions[direction_idx][1]

        if not (0 <= next_i < len(grid) and 0 <= next_j < len(grid[0])):
            return False

        if grid[next_i][next_j] == "#":
            direction_idx += 1
            if direction_idx == 4:
                direction_idx = 0
        else:
            i, j = next_i, next_j

        # if same indices AND direction associated is detected, then it was a cycle
        if (
            i,
            j,
            directions[direction_idx][0],
            directions[direction_idx][1],
        ) in visited:
            return True


def part1():
    with open("real_input", "r") as file:
        data = list(list(line.strip()) for line in file)
    starting_i = 0
    starting_j = 0
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == "^":  # starting here
                starting_i = i
                starting_j = j
    res = visit(data, starting_i, starting_j)
    print(len(res))


def part2():
    with open("real_input", "r") as file:
        data = list(list(line.strip()) for line in file)
    starting_i = 0
    starting_j = 0
    res = 0
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == "^":
                starting_i = i
                starting_j = j
    can_visit = visit(data, starting_i, starting_j)

    # try each index in can_visit and add obstacle, if cycle detected, add 1 to res, stop when tried all visited idxs
    for i, j in can_visit:
        data[i][j] = "#"
        if detect_cycles(data, starting_i, starting_j):
            res += 1
        data[i][j] = "."  # Remove the obstacle
    print(res)


# part1()
part2()
