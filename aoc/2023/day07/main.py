from typing import Dict


class Card:
    def __init__(self, card: str, bid: int) -> None:
        self.card = card
        self.bid = bid
        self.type = 0
        self.rank = 0

    def __str__(self) -> str:
        return f"{self.card} {self.bid} {self.type} {self.rank}\n"


def read_file(file: str) -> list[str]:
    data = open(file, "r")
    return data.read().strip().split("\n")


def is_higher(card1, card2):
    card_order = {
        "A": 14,
        "K": 13,
        "Q": 12,
        "J": 11,
        "T": 10,
        "9": 9,
        "8": 8,
        "7": 7,
        "6": 6,
        "5": 5,
        "4": 4,
        "3": 3,
        "2": 2,
    }

    value1 = card_order.get(card1, 0)
    value2 = card_order.get(card2, 0)

    return value1 > value2


def part1():
    lines = read_file("input")
    cards: list[Card] = []
    for line in lines:
        section = line.split(" ")
        cards.append(Card(section[0], int(section[1])))

    freqs: list = []
    for card in cards:
        freq: Dict[str, int] = {}
        for ch in card.card:
            if ch not in freq:
                freq[ch] = 1
            else:
                freq[ch] += 1
        freqs.append(freq)

    for i, freq in enumerate(freqs):
        count = len(freq.keys())
        if count == 5:
            cards[i].type = 1
        elif count == 4:
            cards[i].type = 2
        elif count == 3:
            # can be two pair or three of a kind
            for _, v in freq.items():
                if v == 3:
                    cards[i].type = 4
                    break
                else:
                    cards[i].type = 3
        elif count == 2:
            # can be full house or four of a kind
            for _, v in freq.items():
                if v == 4:
                    cards[i].type = 6
                    break
                else:
                    cards[i].type = 5
        elif count == 1:
            cards[i].type = 7

    cards = sorted(cards, key=lambda x: (x.type))
    # do second ordering rule
    # Start by comparing the first card in each hand. If these cards are different, the hand with the stronger first card is considered stronger. If the first card in each hand have the same label, however, then move on to considering the second card in each hand. If they differ, the hand with the higher second card wins; otherwise, continue with the third card in each hand, then the fourth, then the fifth.

    count = 1
    for i in range(len(cards) - 1):
        if cards[i].type == cards[i + 1].type:
            # print(cards[i], cards[i + 1])
            for ch in cards[i].card:
                for ch2 in cards[i + 1].card:
                    if is_higher(ch, ch2):
                        print(i, ch, ch2, cards[i], cards[i + 1])
                        cards[i].rank = i + 2
                        cards[i + 1].rank = i + 1
                        break
                    else:
                        print(i, ch, ch2, cards[i], cards[i + 1])
                        break
                        # cards[i].rank = i + 1
                        # cards[i + 1].rank = i + 2
                break
        else:
            cards[i].rank = i + 1

    for card in cards:
        print(card)


part1()
