def part1():
    with open("real_input", "r") as file:
        data = [int(x) for x in file.read().strip().split(" ")]
    for b in range(75):
        print(b)
        output = []
        for i in range(len(data)):
            if data[i] == 0:
                output.append(1)
            elif len(str(data[i])) % 2 == 0:
                length = len(str(data[i]))
                string = str(data[i])
                left = int(string[:length // 2])
                right = int(string[length // 2:])
                output.append(left)
                output.append(right)
            else:
                output.append(data[i] * 2024)
        data = output

    print(len(data))


part1()
