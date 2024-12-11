"""
3267: 81 40 27

    81
  +40  *40
+27     *27
"""


def recurseP1(nums, target, current_total, index, path, matched):
    if matched[0]:  # If already matched, skip further recursion
        return 0

    if index == len(nums):  # Base case: we've used all numbers
        if current_total == target:  # Match found
            print(f"Match found! Path: {path} = {current_total}")
            matched[0] = True
            return current_total  # Return the matching total
        return 0  # No match found in this branch

    branch_sum = 0

    # Recursive case: Apply '+' and recurse
    branch_sum += recurseP1(
        nums,
        target,
        current_total + nums[index],
        index + 1,
        path + f" + {nums[index]}",
        matched,
    )

    # Recursive case: Apply '*' and recurse
    branch_sum += recurseP1(
        nums,
        target,
        current_total * nums[index],
        index + 1,
        path + f" * {nums[index]}",
        matched,
    )

    return branch_sum


def part1():
    with open("real_input", "r") as file:
        data = file.read().strip().split("\n")
    total = 0
    for line in data:
        sections = line.split(":")
        value = int(sections[0])
        nums = list(map(int, sections[1].lstrip().split(" ")))
        matched = [False]
        for i in range(len(nums)):
            total += recurseP1(nums, value, nums[i], i + 1, str(nums[i]), matched)
    print(total)


def recurseP2(nums, target, current_total, index, path, matched):
    if matched[0]:  # If already matched, skip further recursion
        return 0

    if index == len(nums):  # Base case: we've used all numbers
        if current_total == target:  # Match found
            print(f"Match found! Path: {path} = {current_total}")
            matched[0] = True
            return current_total  # Return the matching total
        return 0  # No match found in this branch

    branch_sum = 0

    # Recursive case: Apply '+' and recurse
    branch_sum += recurseP2(
        nums,
        target,
        current_total + nums[index],
        index + 1,
        path + f" + {nums[index]}",
        matched,
    )

    # Recursive case: Apply '*' and recurse
    branch_sum += recurseP2(
        nums,
        target,
        current_total * nums[index],
        index + 1,
        path + f" * {nums[index]}",
        matched,
    )

    # Recursive case: Apply '||' and recurse
    concatenated_total = int(str(current_total) + str(nums[index]))
    branch_sum += recurseP2(
        nums,
        target,
        concatenated_total,
        index + 1,
        path + f" || {nums[index]}",
        matched,
    )

    return branch_sum


def part2():
    with open("real_input", "r") as file:
        data = file.read().strip().split("\n")
    total = 0
    for line in data:
        sections = line.split(":")
        value = int(sections[0])
        nums = list(map(int, sections[1].lstrip().split(" ")))
        matched = [False]
        for i in range(len(nums)):
            total += recurseP2(nums, value, nums[i], i + 1, str(nums[i]), matched)
    print(total)


# part1()
part2()
