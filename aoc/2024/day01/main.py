def part1():
    data = open("real_input", "r")
    lines = data.read().strip().split("\n")
    first_col = []
    second_col = []
    for line in lines:
        first_col.append(line.split("  ")[0])
        second_col.append(line.split("  ")[1])
    first_col.sort()
    second_col.sort()
    res = 0
    for i, num in enumerate(first_col):
        res += abs(int(num) - int(second_col[i]))

    print(res)


def part2():
    data = open("real_input", "r")
    lines = data.read().strip().split("\n")
    first_col = []
    second_col = {}
    for line in lines:
        first_col.append(line.split("  ")[0])
        second_num = int(line.split("  ")[1])
        if second_num in second_col:
            second_col[second_num] += 1
        else:
            second_col[second_num] = 1
    res = 0
    for _, num in enumerate(first_col):
        if int(num) in second_col:
            res += int(num) * second_col[int(num)]

    print(res)


part2()
