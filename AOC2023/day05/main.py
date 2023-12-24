def get_new_seed(start_idx: int, end_idx: int, lines: list[str], seed: int) -> int:
    for i in range(start_idx + 1, end_idx):
        if lines[i] == "":
            break
        nums = lines[i].split(" ")
        dest = int(nums[0])
        src = int(nums[1])
        rng = int(nums[2])

        if seed >= src and seed <= src + rng - 1:
            seed += dest - src
            return seed
    return seed


def part1():
    data = open("input", "r")
    lines = data.read().strip().split("\n")
    seeds: list[int] = []

    first = lines[0].split(" ")
    for seed in first:
        if seed.isdigit():
            seeds.append(int(seed))

    seed2soil = lines.index("seed-to-soil map:")
    soil2fert = lines.index("soil-to-fertilizer map:")
    fert2water = lines.index("fertilizer-to-water map:")
    water2light = lines.index("water-to-light map:")
    light2temp = lines.index("light-to-temperature map:")
    temp2humid = lines.index("temperature-to-humidity map:")
    humid2loc = lines.index("humidity-to-location map:")

    possible_locs = []
    for seed in seeds:
        s = get_new_seed(seed2soil, soil2fert, lines, seed)
        s = get_new_seed(soil2fert, fert2water, lines, s)
        s = get_new_seed(fert2water, water2light, lines, s)
        s = get_new_seed(water2light, light2temp, lines, s)
        s = get_new_seed(light2temp, temp2humid, lines, s)
        s = get_new_seed(temp2humid, humid2loc, lines, s)
        s = get_new_seed(humid2loc, len(lines), lines, s)
        possible_locs.append(s)

    res = sorted(possible_locs)[0]
    print(res)


def part2():
    data = open("input", "r")
    lines = data.read().strip().split("\n")
    seeds: list[int] = []

    first = lines[0].split(" ")
    for seed in first:
        if seed.isdigit():
            seeds.append(int(seed))

    seed2soil = lines.index("seed-to-soil map:")
    soil2fert = lines.index("soil-to-fertilizer map:")
    fert2water = lines.index("fertilizer-to-water map:")
    water2light = lines.index("water-to-light map:")
    light2temp = lines.index("light-to-temperature map:")
    temp2humid = lines.index("temperature-to-humidity map:")
    humid2loc = lines.index("humidity-to-location map:")

    lowest = float("inf")
    for i in range(0, len(seeds), 2):
        start = seeds[i]
        rng = seeds[i + 1]
        print(start, rng)
        for j in range(start, start + rng):
            s = get_new_seed(seed2soil, soil2fert, lines, j)
            s = get_new_seed(soil2fert, fert2water, lines, s)
            s = get_new_seed(fert2water, water2light, lines, s)
            s = get_new_seed(water2light, light2temp, lines, s)
            s = get_new_seed(light2temp, temp2humid, lines, s)
            s = get_new_seed(temp2humid, humid2loc, lines, s)
            s = get_new_seed(humid2loc, len(lines), lines, s)
            lowest = min(s, lowest)
    print(lowest)


# part1()
part2()
