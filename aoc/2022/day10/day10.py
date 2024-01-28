from collections import defaultdict


def p1():
    signal = []
    cycles = defaultdict(int)
    sigStrength = {}

    X = 1
    cycle = 1
    realCycles = [20, 60, 100, 140, 180, 220]
    total = 0

    with open("input.txt", "r") as file:
        for line in file:
            signal.append(line.strip())

    for command in signal:
        cycles[cycle] = X
        if command == "noop":
            cycle += 1
            cycles[cycle] = X

        elif command.startswith("addx"):
            V = int(command.split(" ")[-1])
            for i in range(2):
                cycle += 1
                cycles[cycle] = X
            X += V
            cycles[cycle] = X

    for cycle, X in cycles.items():
        sigStrength[cycle] = cycle * X

    for cycle in realCycles:
        total += sigStrength[cycle]

    print(total)


p1()
