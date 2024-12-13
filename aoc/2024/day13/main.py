import re


def part1():
    with open("real_input", "r") as file:
        data = file.read().strip()
        section = data.split("\n\n")
    res = 0
    for s in section:
        button_a = [
            int(x)
            for match in re.findall(r"Button A: X\+(\d+), Y\+(\d+)", s)
            for x in match
        ]
        button_b = [
            int(x)
            for match in re.findall(r"Button B: X\+(\d+), Y\+(\d+)", s)
            for x in match
        ]
        prize = [
            int(x) for match in re.findall(r"Prize: X=(\d+), Y=(\d+)", s) for x in match
        ]
        attempts = 1000000000000
        for i in range(101):
            for j in range(101):
                new_i, new_j = (
                    button_a[0] * i + button_b[0] * j,
                    button_a[1] * i + button_b[1] * j,
                )
                if new_i == prize[0] and new_j == prize[1]:
                    attempts = min(attempts, 3 * i + j)
        if attempts < 1000000000000:
            res += attempts

    print(res)


part1()
