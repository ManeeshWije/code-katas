def part1():
    data = open("real_input", "r")
    lines = data.readlines()
    res = 0
    for line in lines:
        nums = list(map(int, line.split()))
        n = len(nums)
        is_safe = True
        check_increasing = False
        check_decreasing = False
        if nums[1] > nums[0]:
            check_increasing = True
        else:
            check_decreasing = True

        for i in range(1, n):
            adj = abs(nums[i] - nums[i - 1])
            if check_decreasing and nums[i] > nums[i - 1]:
                is_safe = False
                break
            if check_increasing and nums[i] < nums[i - 1]:
                is_safe = False
                break
            if adj < 1 or adj > 3:
                is_safe = False
                break
        if is_safe:
            res += 1
    print(res)


def part2():
    data = open("real_input", "r")
    lines = data.readlines()
    res = 0

    for line in lines:
        nums = list(map(int, line.split()))
        n = len(nums)
        is_safe = True

        # Check if the original sequence is valid
        if nums[1] > nums[0]:
            check_increasing = True
        else:
            check_increasing = False

        for i in range(1, n):
            adj = abs(nums[i] - nums[i - 1])
            if adj < 1 or adj > 3:  # Safety condition
                is_safe = False
                break
            if check_increasing and nums[i] < nums[i - 1]:  # Monotonicity broken
                is_safe = False
                break
            if not check_increasing and nums[i] > nums[i - 1]:  # Monotonicity broken
                is_safe = False
                break

        if is_safe:
            res += 1
            continue

        # Check if the sequence can be made safe by removing one number
        can_be_safe = False
        for i in range(n):
            # Simulate removing nums[i]
            modified_nums = nums[:i] + nums[i + 1 :]

            # Re-evaluate safety and monotonicity for the modified sequence
            is_safe_after_removal = True
            if modified_nums[1] > modified_nums[0]:
                check_increasing = True
            else:
                check_increasing = False

            for j in range(1, len(modified_nums)):
                adj = abs(modified_nums[j] - modified_nums[j - 1])
                if adj < 1 or adj > 3:
                    is_safe_after_removal = False
                    break
                if check_increasing and modified_nums[j] < modified_nums[j - 1]:
                    is_safe_after_removal = False
                    break
                if not check_increasing and modified_nums[j] > modified_nums[j - 1]:
                    is_safe_after_removal = False
                    break

            if is_safe_after_removal:
                can_be_safe = True
                break

        if can_be_safe:
            res += 1

    print(res)


part1()
part2()
