import re
from collections import defaultdict


def part1():
    with open("real_input", "r") as file:
        data = file.read().strip()
        sections = data.split("\n")
        res = 0
        quadrants = [0, 0, 0, 0]  # 4 entries for 4 quadrants
        for section in sections:
            px, py = [
                int(x)
                for match in re.findall(r"p=(-?\d+),(-?\d+)", section)
                for x in match
            ]
            vx, vy = [
                int(x)
                for match in re.findall(r"v=(-?\d+),(-?\d+)", section)
                for x in match
            ]
            # need to mod so we can wrap around if went out of bounds
            new_px = (px + vx * 100) % 101
            new_py = (py + vy * 100) % 103
            if new_px < 50 and new_py < 51:
                quadrants[0] += 1
            elif new_px > 50 and new_py < 51:
                quadrants[1] += 1
            elif new_px < 50 and new_py > 51:
                quadrants[2] += 1
            elif new_px > 50 and new_py > 51:
                quadrants[3] += 1
        res += quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3]
    print(res)


def has_vertical_streak(seen_points):
    # Checks if there is a vertical streak of 10 or more continuous points along the y-axis.
    # Group points by their x-coordinates
    x_groups = defaultdict(list)
    for x, y in seen_points:
        x_groups[x].append(y)

    # Check each group for vertical streaks
    for x, y_list in x_groups.items():
        y_list.sort()  # Sort y-coordinates to find continuous streaks
        streak = 1
        for i in range(1, len(y_list)):
            if y_list[i] == y_list[i - 1] + 1:  # Continuous along y-axis
                streak += 1
                if streak >= 10:
                    return True
            else:
                streak = 1
    return False


def part2():
    with open("real_input", "r") as file:
        data = file.read().strip()
        sections = data.split("\n")
        t = 1

        while True:
            seen = set()
            for section in sections:
                px, py = [
                    int(x)
                    for match in re.findall(r"p=(-?\d+),(-?\d+)", section)
                    for x in match
                ]
                vx, vy = [
                    int(x)
                    for match in re.findall(r"v=(-?\d+),(-?\d+)", section)
                    for x in match
                ]
                new_px = (px + vx * t) % 101
                new_py = (py + vy * t) % 103
                seen.add((new_px, new_py))

            # Check if there's a vertical streak
            if has_vertical_streak(seen):
                # visualize
                for i in range(103):
                    row = ""
                    for j in range(101):
                        if (i, j) in seen:
                            row += "#"
                        else:
                            row += "."
                    print(row)
                print(t)
                break

            t += 1


# part1()
part2()
