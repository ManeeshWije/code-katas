def part1():
    with open("real_input", "r") as file:
        data = file.read().strip()
    disk = []
    id = 0
    for i in range(len(data)):
        digit = int(data[i])
        # Block
        if i % 2 == 0:
            disk += [id] * digit
            id += 1
        else: # Free space length as -1
            disk += [-1] * digit
    # Now simulate moving from end of disk to leftmost -1
    while True:
        moved = False
        # Traverse right to left
        for j in range(len(disk) - 1, -1, -1):
            if disk[j] != -1:  # If it's a block
                leftmost_free = disk.index(-1)  # Find the leftmost free space
                if leftmost_free < j:  # Only move if the free space is to the left
                    disk[leftmost_free] = disk[j]  # Move block to the free space
                    disk[j] = -1  # Mark the current position as free
                    moved = True
        if not moved:  # Stop if no blocks were moved in this pass
            break
    # Do calculation
    res = 0
    for k in range(len(disk)):
        if disk[k] == -1:
            break
        prod = disk[k] * k
        res += prod
    print(res)

def part2():
    with open("ex_input", "r") as file:
        data = file.read().strip()
    disk = []
    id = 0
    for i in range(len(data)):
        digit = int(data[i])
        # Block
        if i % 2 == 0:
            disk += [id] * digit
            id += 1
        else: # Free space length as -1
            disk += [-1] * digit
    # Now simulate moving from end of disk to leftmost -1
    while True:
        moved = False
        # Traverse right to left
        for j in range(len(disk) - 1, -1, -1):
            if disk[j] != -1:  # If it's a block
                leftmost_free = disk.index(-1)  # Find the leftmost free space
                if leftmost_free < j:  # Only move if the free space is to the left
                    disk[leftmost_free] = disk[j]  # Move block to the free space
                    disk[j] = -1  # Mark the current position as free
                    moved = True
        if not moved:  # Stop if no blocks were moved in this pass
            break
    # Do calculation
    res = 0
    for k in range(len(disk)):
        if disk[k] == -1:
            break
        prod = disk[k] * k
        res += prod
    print(res)

# part1()
part2()
