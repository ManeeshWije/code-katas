def part1():
    with open("real_input", "r") as file:
        data = [list(line.strip()) for line in file]

    find = "XMAS"
    res = 0
    directions = [  # (row_offset, col_offset)
        (0, 1),  # right
        (0, -1),  # left
        (1, 0),  # down
        (-1, 0),  # up
        (1, 1),  # diagonal down-right
        (1, -1),  # diagonal down-left
        (-1, 1),  # diagonal up-right
        (-1, -1),  # diagonal up-left
    ]
    for i in range(len(data)):
        for j in range(len(data[0])):
            # once we found X, check all dirs for XMAS
            if data[i][j] == "X":
                for dx, dy in directions:
                    is_valid = True
                    for k in range(len(find)):
                        new_i, new_j = i + k * dx, j + k * dy
                        if not (
                            0 <= new_i < len(data)
                            and 0 <= new_j < len(data[0])
                            and data[new_i][new_j] == find[k]
                        ):
                            is_valid = False
                            break
                    if is_valid:
                        res += 1
    print(res)


def part2():
    with open("real_input", "r") as file:
        data = [list(line.strip()) for line in file]

    res = 0
    for i in range(len(data)):
        for j in range(len(data[0])):
            # M and S (mas, sam), M and M (mas, mas)
            # S and S (sam, sam), S and M (sam, mas)
            if data[i][j] == "M" and i + 2 < len(data) and j + 2 < len(data[0]):
                if data[i + 1][j + 1] == "A" and data[i + 2][j + 2] == "S":
                    if (
                        data[i][j + 2] == "S"
                        and data[i + 1][j + 1] == "A"
                        and data[i + 2][j] == "M"
                    ):
                        res += 1
                    if (
                        data[i][j + 2] == "M"
                        and data[i + 1][j + 1] == "A"
                        and data[i + 2][j] == "S"
                    ):
                        res += 1
            if data[i][j] == "S" and i + 2 < len(data) and j + 2 < len(data[0]):
                if data[i + 1][j + 1] == "A" and data[i + 2][j + 2] == "M":
                    if (
                        data[i][j + 2] == "S"
                        and data[i + 1][j + 1] == "A"
                        and data[i + 2][j] == "M"
                    ):
                        res += 1
                    if (
                        data[i][j + 2] == "M"
                        and data[i + 1][j + 1] == "A"
                        and data[i + 2][j] == "S"
                    ):
                        res += 1

    print(res)

# part1()
part2()
