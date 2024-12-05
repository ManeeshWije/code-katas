def is_page_num_valid(rules_map, nums):
    for i in range(len(nums)):
        if nums[i] in rules_map.keys():
            idx = list(rules_map).index(nums[i])
            for j in range(i + 1, len(nums)):
                if nums[j] not in list(rules_map.values())[idx]:
                    return False
        else:  # check if any values have non-key, and the key for that is NOT to the right of the num
            for k, v in rules_map.items():
                if nums[i] in v:
                    for j in range(i + 1, len(nums)):
                        if nums[j] == k:
                            return False
    return True


def part1():
    with open("real_input", "r") as file:
        data = file.read()
    section = data.strip().split("\n\n")
    rules = section[0].strip().split("\n")
    page_nums = section[1].strip().split("\n")
    rules_map = {}
    res = 0
    for rule in rules:
        r = list(map(int, rule.split("|")))
        if r[0] in rules_map:
            rules_map[r[0]].append(r[1])
        else:
            rules_map[r[0]] = [r[1]]
    for page_num in page_nums:
        nums = list(map(int, page_num.strip().split(",")))
        if is_page_num_valid(rules_map, nums):
            middle = nums[(len(nums) - 1) // 2]
            res += middle
    print(res)


def part2():
    with open("real_input", "r") as file:
        data = file.read()
    section = data.strip().split("\n\n")
    rules = section[0].strip().split("\n")
    page_nums = section[1].strip().split("\n")
    rules_map = {}
    res = 0

    for rule in rules:
        r = list(map(int, rule.split("|")))
        if r[0] in rules_map:
            rules_map[r[0]].append(r[1])
        else:
            rules_map[r[0]] = [r[1]]

    for page_num in page_nums:
        nums = list(map(int, page_num.strip().split(",")))
        # Man this is pretty ass
        if not is_page_num_valid(rules_map, nums):
            while not is_page_num_valid(rules_map, nums):
                for i in range(len(nums)):
                    for k, v in rules_map.items():
                        if nums[i] in v:  # Current number should not precede its key
                            for j in range(i + 1, len(nums)):
                                if nums[j] == k:  # Key found after the value
                                    nums[i], nums[j] = nums[j], nums[i]  # Swap
                                    break
            middle = nums[(len(nums) - 1) // 2]
            res += middle
    print(res)


# part1()
part2()
