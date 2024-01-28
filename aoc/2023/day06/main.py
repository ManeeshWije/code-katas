def read_file(file):
    data = open(file, "r")
    return data.read().strip().split("\n")

def part1():
    lines = read_file('input')
    times = []
    distances = []
    res = 1
    for i, line in enumerate(lines):
        section = line.split(" ")
        if i == 0:
            for s in section:
                if s.isdigit():
                    times.append(int(s))
        else:
            for s in section:
                if s.isdigit():
                    distances.append(int(s))
    for i, t in enumerate(times):
        valid_distance_traveled = []
        duration = 0
        velocity = 0
        # dont hold the button down at all
        valid_distance_traveled.append(duration * velocity)
        while velocity < t:
            velocity += 1
            duration = (t - velocity)
            valid_distance_traveled.append(duration * velocity)

        count = 0
        for _, v in enumerate(valid_distance_traveled):
            if v > distances[i]:
                count += 1
        res *= count
    print(res)


# takes 10 seconds, M1 macbook
def part2():
    lines = read_file('input')
    time = ""
    distance = ""
    res = 1
    for i, line in enumerate(lines):
        section = line.split(" ")
        if i == 0:
            for s in section:
                if s.isdigit():
                    time += s
        else:
            for s in section:
                if s.isdigit():
                    distance += s
    duration = 0
    velocity = 0
    count = 0
    while velocity < int(time):
        velocity += 1
        duration = (int(time) - velocity)
        if duration * velocity > int(distance):
            count += 1
    res *= count
    print(res)

part1()
# part2()
