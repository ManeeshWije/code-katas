def get_adjacent_idx(i, j):
    return [
        [i - 1, j],
        [i + 1, j],
        [i, j - 1],
        [i, j + 1],
        [i - 1, j - 1],
        [i - 1, j + 1],
        [i + 1, j - 1],
        [i + 1, j + 1],
    ]


def add_dot_to_end_of_rows(input_file):
    with open(input_file, "r") as file:
        rows = file.read().strip().split("\n")

    # Add a dot at the end of each row
    rows = [row + "." for row in rows]

    with open(input_file, "w") as file:
        file.write("\n".join(rows))


def part1():
    add_dot_to_end_of_rows("input")
    data = open("input", "r")
    rows = data.read().strip().split("\n")
    width = len(rows)
    height = len(rows[0])

    total = 0
    valid = False
    temp = ""
    for i in range(width):
        for j in range(height):
            curr = rows[i][j]
            directions = get_adjacent_idx(i, j)
            if curr.isdigit():
                if j == 0:
                    temp = ""
                    valid = False
                temp += curr
                # go through all 8 dirs if its a digit
                for x, y in directions:
                    if 0 <= x < width and 0 <= y < height:
                        adj = rows[x][y]
                        if not adj.isalnum() and adj != "." and not adj.isdigit():
                            valid = True
            elif valid:
                total += int(temp)
                temp = ""
                valid = False
            else:
                temp = ""
                valid = False
    # cover edge case
    if valid:
        print(temp)
        total += int(temp)
    print(f"Part 1 = {total}")


def find_full_number(grid, row, col):
    def is_valid_char(char):
        return char.isdigit()

    left_index = col
    right_index = col

    while left_index >= 0 and is_valid_char(grid[row][left_index]):
        left_index -= 1

    while right_index < len(grid[0]) and is_valid_char(grid[row][right_index]):
        right_index += 1

    full_number = grid[row][left_index + 1 : right_index]
    return full_number, (row, right_index)


def part2():
    data = open("input", "r")
    rows = data.read().strip().split("\n")
    width = len(rows)
    height = len(rows[0])

    num_collected_coords = []
    d = {}
    total = 0
    for i in range(width):
        for j in range(height):
            curr = rows[i][j]
            directions = get_adjacent_idx(i, j)
            if curr == "*":
                nums = []
                for x, y in directions:
                    if 0 <= x < width and 0 <= y < height:
                        adj = rows[x][y]
                        if adj.isdigit():
                            # we want the coords of num so we can check if we are simply adding the same number again
                            number, (start, end) = find_full_number(rows, x, y)
                            num_collected_coords.append((start,end))
                            count = 0
                            for v in num_collected_coords:
                                if v == (start, end):
                                    count += 1
                            if count < 2:
                                nums.append(number)
                d[(i, j)] = nums

    for _, v in d.items():
        if len(v) == 2:
            total += int(v[0]) * int(v[1])
    print(f"Part 2 = {total}")

part1()
part2()
