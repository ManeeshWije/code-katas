import re

def part1():
    file_data = open("real_input", "r")
    lines = file_data.readlines()
    res = 0
    for line in lines:
        mults = re.findall(r"mul\(\d+,\d+\)", line)
        for mult in mults:
            nums = mult.split(",")
            n1 = re.search(r"\d+", nums[0])
            n2 = re.search(r"\d+", nums[1])
            res += int(n1.group()) * int(n2.group())
    print(res)

def part2():
    file_data = open("real_input", "r")
    lines = file_data.readlines()
    res = 0
    skip = False
    for line in lines:
        donts = re.finditer(r"don't\(\)", line)
        dos = re.finditer(r"do\(\)", line)
        mults = re.finditer(r"mul\(\d+,\d+\)", line)
        dont_list = []
        do_list = []
        for dont in donts:
            dont_list.append(int(dont.start()))
        for do in dos:
            do_list.append(int(do.start()))
        for mult in mults:
            if dont_list and int(mult.start()) >= dont_list[0]:
                skip = True
                dont_list.pop(0)
            if do_list and int(mult.start()) >= do_list[0]:
                skip = False
                do_list.pop(0)
            if not skip:
                nums = mult.group().split(",")
                n1 = re.search(r"\d+", nums[0])
                n2 = re.search(r"\d+", nums[1])
                res += int(n1.group()) * int(n2.group())
        print(res)


# part1()
part2()
