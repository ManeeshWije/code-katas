def part1():
    data = open("input", "r")
    lines = data.read().strip().split("\n")
    total = 0
    for line in lines:
        parts = line.split(":")
        game = line.split(";")
        valid = True

        id = int(parts[0].strip().split(" ")[-1])

        for c in game:
            r = c.find("red")
            g = c.find("green")
            b = c.find("blue")
            if r != -1:
                num_start = r - 2
                while num_start >= 0 and c[num_start].isdigit():
                    num_start -= 1
                num = c[num_start + 1 : r]
                if int(num) > 12:
                    valid = False
            if g != -1:
                num_start = g - 2
                while num_start >= 0 and c[num_start].isdigit():
                    num_start -= 1
                num = c[num_start + 1 : g]
                if int(num) > 13:
                    valid = False
            if b != -1:
                num_start = b - 2
                while num_start >= 0 and c[num_start].isdigit():
                    num_start -= 1
                num = c[num_start + 1 : b]
                if int(num) > 14:
                    valid = False
        if valid:
            total += id
    print(f'Part 1: {total}')

def part2():
    data = open("input", "r")
    lines = data.read().strip().split("\n")
    total = 0
    for line in lines:
        game = line.split(";")

        max_r = float('-inf')
        max_g = float('-inf')
        max_b = float('-inf')
        for c in game:
            r = c.find("red")
            g = c.find("green")
            b = c.find("blue")
            if r != -1:
                num_start = r - 2
                while num_start >= 0 and c[num_start].isdigit():
                    num_start -= 1
                num = int(c[num_start + 1 : r])
                max_r = max(num, max_r)
            if g != -1:
                num_start = g - 2
                while num_start >= 0 and c[num_start].isdigit():
                    num_start -= 1
                num = int(c[num_start + 1 : g])
                max_g = max(num, max_g)
            if b != -1:
                num_start = b - 2
                while num_start >= 0 and c[num_start].isdigit():
                    num_start -= 1
                num = int(c[num_start + 1 : b])
                max_b = max(num, max_b)
        total += (int(max_r) * int(max_g) * int(max_b))

    print(f'Part 2: {total}')


part1()
part2()
