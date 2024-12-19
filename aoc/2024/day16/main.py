import heapq


def part1():
    with open("real_input", "r") as file:
        grid = list(list(file.read().strip().split("\n")))

    start_i = start_j = -1
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "S":
                start_i = i
                start_j = j
                break
    # start at start and face east
    seen = {(start_i, start_j, 0, 1)}
    pq = [(0, start_i, start_j, 0, 1)]
    res = 0
    while pq:
        cost, curr_i, curr_j, dx, dy = heapq.heappop(pq)
        seen.add((curr_i, curr_j, dx, dy))
        if grid[curr_i][curr_j] == "E":
            res = cost
            break
        for next_cost, next_i, next_j, next_dx, next_dy in [
            (cost + 1, curr_i + dx, curr_j + dy, dx, dy),  # same dir so cost + 1
            (cost + 1000, curr_i, curr_j, dy, -dx),  # turn counter-clockwise
            (cost + 1000, curr_i, curr_j, -dy, dx),  # turn clockwise
        ]:
            if grid[next_i][next_j] == "#":
                continue
            if (next_i, next_j, next_dx, next_dy) in seen:
                continue
            heapq.heappush(pq, (next_cost, next_i, next_j, next_dx, next_dy))

    print(res)


part1()
