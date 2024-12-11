def in_bounds(i, j, grid):
    return 0 <= i < len(grid) and 0 <= j < len(grid[0])


def part1():
    with open("real_input", "r") as file:
        data = list(map(list, file.read().strip().split("\n")))

    antennas = {}
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] != ".":
                if data[i][j] not in antennas:
                    antennas[data[i][j]] = [(i, j)]
                else:
                    antennas[data[i][j]].append((i, j))
    antinodes = set()
    # every pair of coords, calculate the diff
    # add this diff into 8 directions
    # if the resultant coord with that diff is the same node type (ex "a") check two things:
    # 1. original + opposite diff is within bounds
    # 2. resultant coord + diff is within bounds
    # if 1. is true, add original + opposite diff coords to antinodes set
    # if 2. is true, add resultant coord + diff coords to antinodes set
    # return len(antinode_set)
    for k, v in antennas.items():
        for m in range(len(v)):
            for l in range(m + 1, len(v)):
                diff_coords = (abs(v[l][0] - v[m][0])), abs((v[l][1] - v[m][1]))
                for dx, dy in [
                    (1, 1),
                    (-1, -1),
                    (1, -1),
                    (-1, 1),
                    (0, -1),
                    (-1, 0),
                    (0, 1),
                    (1, 0),
                ]:
                    new_i = v[m][0] + diff_coords[0] * dx
                    new_j = v[m][1] + diff_coords[1] * dy
                    if in_bounds(new_i, new_j, data) and data[new_i][new_j] == k:
                        # grab coord opposite dir of original after adding diff
                        orig_opposite_i = v[m][0] + diff_coords[0] * -dx
                        orig_opposite_j = v[m][1] + diff_coords[1] * -dy
                        # grab coord of the matching char after adding diff
                        resultant_new_i = new_i + diff_coords[0] * dx
                        resultant_new_j = new_j + diff_coords[1] * dy
                        # these two are our antinodes

                        if (orig_opposite_i, orig_opposite_j) not in antinodes:
                            if in_bounds(orig_opposite_i, orig_opposite_j, data):
                                antinodes.add((orig_opposite_i, orig_opposite_j))

                        if (resultant_new_i, resultant_new_j) not in antinodes:
                            if in_bounds(resultant_new_i, resultant_new_j, data):
                                antinodes.add((resultant_new_i, resultant_new_j))
    print(len(antinodes))


def part2():
    with open("real_input", "r") as file:
        data = list(map(list, file.read().strip().split("\n")))

    antennas = {}
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] != ".":
                if data[i][j] not in antennas:
                    antennas[data[i][j]] = [(i, j)]
                else:
                    antennas[data[i][j]].append((i, j))

    print(antennas)
    antinodes = set()
    for k, v in antennas.items():
        for m in range(len(v)):
            for l in range(m + 1, len(v)):
                diff_coords = (abs(v[l][0] - v[m][0])), abs((v[l][1] - v[m][1]))
                for dx, dy in [
                    (1, 1),
                    (-1, -1),
                    (1, -1),
                    (-1, 1),
                    (0, -1),
                    (-1, 0),
                    (0, 1),
                    (1, 0),
                ]:
                    new_i = v[m][0] + diff_coords[0] * dx
                    new_j = v[m][1] + diff_coords[1] * dy
                    if in_bounds(new_i, new_j, data) and data[new_i][new_j] == k:
                        antinodes.add((v[m][0], v[m][1]))
                        antinodes.add((new_i, new_j))
                        orig_opposite_i = v[m][0] + diff_coords[0] * -dx
                        orig_opposite_j = v[m][1] + diff_coords[1] * -dy
                        resultant_new_i = new_i + diff_coords[0] * dx
                        resultant_new_j = new_j + diff_coords[1] * dy

                        while in_bounds(orig_opposite_i, orig_opposite_j, data):
                            antinodes.add((orig_opposite_i, orig_opposite_j))
                            orig_opposite_i += diff_coords[0] * -dx
                            orig_opposite_j += diff_coords[1] * -dy

                        while in_bounds(resultant_new_i, resultant_new_j, data):
                            antinodes.add((resultant_new_i, resultant_new_j))
                            resultant_new_i += diff_coords[0] * dx
                            resultant_new_j += diff_coords[1] * dy
    n = len(data)
    m = len(data[0])
    print(
        "\n".join(
            "".join("#" if (i, j) in antinodes else "." for j in range(m))
            for i in range(n)
        )
    )
    print(len(antinodes))


# part1()
part2()
