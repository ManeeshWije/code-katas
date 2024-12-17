def part1():
    with open("real_input", "r") as file:
        data = file.read().strip()
        sections = data.split("\n\n")

        regs = sections[0].split("\n")
        reg_a = int(regs[0].strip().split(":")[1])
        reg_b = int(regs[1].strip().split(":")[1])
        reg_c = int(regs[2].strip().split(":")[1])

        instructions = list(map(int, sections[1].split(":")[1].split(",")))

        ip = 0
        out = []

        def resolve_combo(op):
            if op == 0:
                return 0
            elif op == 1:
                return 1
            elif op == 2:
                return 2
            elif op == 3:
                return 3
            elif op == 4:
                return reg_a
            elif op == 5:
                return reg_b
            elif op == 6:
                return reg_c
            else:
                raise ValueError("Invalid combo operand")

        while ip < len(instructions):
            opcode = instructions[ip]
            if ip + 1 < len(instructions):
                operand = instructions[ip + 1]
            else:
                operand = 0

            if opcode == 0:  # adv
                denom = 2 ** resolve_combo(operand)
                reg_a = reg_a // denom
                ip += 2
            elif opcode == 1:  # bxl
                reg_b = reg_b ^ operand
                ip += 2
            elif opcode == 2:  # bst
                reg_b = resolve_combo(operand) % 8
                ip += 2
            elif opcode == 3:  # jnz
                if reg_a != 0:
                    ip = operand
                else:
                    ip += 2
            elif opcode == 4:  # bxc
                reg_b = reg_b ^ reg_c
                ip += 2
            elif opcode == 5:  # out
                out.append(resolve_combo(operand) % 8)
                ip += 2
            elif opcode == 6:  # bdv
                denom = 2 ** resolve_combo(operand)
                reg_b = reg_a // denom
                ip += 2
            elif opcode == 7:  # cdv
                denom = 2 ** resolve_combo(operand)
                reg_c = reg_a // denom
                ip += 2

        print(",".join(map(str, out)))


part1()
