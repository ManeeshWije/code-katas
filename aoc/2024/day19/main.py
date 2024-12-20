def construct(target, available, cache):
    if target in cache:
        return cache[target]
    if target == "":
        cache[target] = True
        return True
    for avail in available:
        if target.startswith(avail):
            if construct(target[len(avail):], available, cache):
                cache[target] = True
                return True
    cache[target] = False
    return False

def construct2(target, available, cache):
    if target in cache:
        return cache[target]
    if target == "":
        return 1 # base case can only create 1 way
    total = 0
    for avail in available:
        if target.startswith(avail):
            total += construct2(target[len(avail):], available, cache)
    cache[target] = total
    return total

def part1():
    with open("real_input", "r") as file:
        sections = file.read().strip().split("\n\n")
        available = sections[0].split(", ")
        patterns = sections[1].split("\n")
    res = 0
    cache = {}
    for pattern in patterns:
        print(f"pattern {pattern}")
        if construct(pattern, available, cache):
            res += 1

    print(res)

def part2():
    with open("real_input", "r") as file:
        sections = file.read().strip().split("\n\n")
        available = sections[0].split(", ")
        patterns = sections[1].split("\n")
    res = 0
    cache = {}
    for pattern in patterns:
        print(f"pattern {pattern}")
        res += construct2(pattern, available, cache)

    print(res)

# part1()
part2()
