class Card:
    def __init__(self, winning, mine):
        self.winning = winning
        self.mine = mine
        self.win_count = 0
        self.card_num = 0
        self.real_win = 0

    def __str__(self):
        return f"CARD_NUM: {self.card_num}\nWinning: {self.winning}\nMine: {self.mine}\nWin Count: {self.win_count}\nReal Win: {self.real_win}\n"


def part1():
    data = open("input", "r")
    lines = data.read().strip().split("\n")
    cards = []
    for line in lines:
        card = line.split("|")

        start = card[0].index(":")
        # winning and mine
        cards.append(
            Card(
                card[0][start + 1 : :].replace("  ", " ").strip().split(" "),
                card[1].replace("  ", " ").strip().split(" "),
            )
        )

    total = 0
    for _, card in enumerate(cards):
        count = 0
        for _, win in enumerate(card.winning):
            for _, mine in enumerate(card.mine):
                if mine == win:
                    count += 1
        if count > 0:
            total += (2**count) - (2 ** (count - 1))

    print(f"Part 1 = {total}")


def part2():
    data = open("input", "r")
    lines = data.read().strip().split("\n")
    cards = []
    for line in lines:
        card = line.split("|")

        start = card[0].index(":")
        # winning and mine
        cards.append(
            Card(
                card[0][start + 1 : :].replace("  ", " ").strip().split(" "),
                card[1].replace("  ", " ").strip().split(" "),
            )
        )

    total = 0
    for i, card in enumerate(cards):
        card.card_num = i + 1
        card.real_win += 1
        count = 0
        for _, win in enumerate(card.winning):
            for _, mine in enumerate(card.mine):
                if mine == win:
                    count += 1
        card.win_count += count

    for i, card in enumerate(cards):
        for j in range(card.win_count):
            cards[i + j + 1].real_win += card.real_win
        total += card.real_win

    print(f"Part 2 = {total}")

part1()
part2()
