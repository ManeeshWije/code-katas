def mix(given_value, secret_num):
    return given_value ^ secret_num


def prune(secret_num):
    return secret_num % 16777216


def part1():
    with open("ex_input", "r") as file:
        data = map(int, file.read().strip().split("\n"))
    total = 0
    for num in data:
        res = num
        for _ in range(2000):
            res = prune(mix(res * 64, res))
            res = prune(mix(res // 32, res))
            res = prune(mix(res * 2048, res))
            print(f"part1 = {res} with num = {num}")
        total += res
    print(total)


changes = {}
prices = []


# def part2():
#     with open("ex_input", "r") as file:
#         data = map(int, file.read().strip().split("\n"))
#     for num in data:
#         res = num
#         for i in range(2000):
#             last_price = int(str(res)[-1])
#             res = prune(mix(res * 64, res))
#             res = prune(mix(res // 32, res))
#             res = prune(mix(res * 2048, res))
#             new_price = int(str(res)[-1])
#             change = new_price - last_price
#             changes[res] = (new_price, change)
#             prices.append(new_price)
#     print(changes)

# part1()
# part2()
