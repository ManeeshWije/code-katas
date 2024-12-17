def move_robot(i, j, move):
    if move == "<":
        j -= 1
    elif move == ">":
        j += 1
    elif move == "^":
        i -= 1
    elif move == "v":
        i += 1
    return (i, j)


def part1():
    with open("real_input", "r") as file:
        data = file.read().strip()
        grid, moves = data.split("\n\n")
        grid = list(map(list, grid.split("\n")))
    starting_i = starting_j = 0
    boxes = set()
    walls = set()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "@":
                starting_i = i
                starting_j = j
            if grid[i][j] == "O":
                boxes.add((i, j))
            if grid[i][j] == "#":
                walls.add((i, j))

    # Process each move
    for move in moves:
        next_i, next_j = move_robot(starting_i, starting_j, move)

        chain = []
        current_pos = (next_i, next_j)

        # Follow the chain of boxes in the move direction
        while current_pos in boxes:
            chain.append(current_pos)
            current_pos = move_robot(current_pos[0], current_pos[1], move)

        # Check if the last position in the chain is valid (not a wall)
        if current_pos not in walls and current_pos not in boxes:
            # Move the robot
            starting_i, starting_j = next_i, next_j

            # Move all boxes in the chain
            for box in reversed(chain):
                boxes.remove(box)
                next_box_pos = move_robot(box[0], box[1], move)
                boxes.add(next_box_pos)
        # If invalid move (wall), the robot does not move

    # Output the resulting grid
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i, j) == (starting_i, starting_j):
                print("@", end="")
            elif (i, j) in boxes:
                print("O", end="")
            elif (i, j) in walls:
                print("#", end="")
            else:
                print(".", end="")
        print()
    res = 0
    for (box_i, box_j) in boxes:
        res += (100 * box_i) + box_j
    print(res)


part1()
