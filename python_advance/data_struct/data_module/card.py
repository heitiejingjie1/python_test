import collections
from random import choice
from sys import orig_argv


# 创建带有命名字段的元组子类
Card = collections.namedtuple("Card", ["rank", "suit"])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = "spades hearts diamonda clubs".split()

    """魔术方法: 初始化"""

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    """魔术方法: 获取长度"""

    def __len__(self):
        return len(self._cards)

    """魔术方法: 获取元素"""

    def __getitem__(self, position):
        return self._cards[position]


suit_values = dict(spades=3, hearts=2, diamonda=1, clubs=0)


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


def display():
    beer_card = Card("8", "clubs")
    print(beer_card)

    deck = FrenchDeck()
    print(len(deck))

    print(deck[0])
    print(deck[-1])
    print(deck[4])

    """随机选取一张牌"""
    print(choice(deck))
    print(choice(deck))

    """抽取前三张牌"""
    print(deck[:3])
    print(deck[12::13])

    for card in deck:
        print(card)


# display()
deck = FrenchDeck()
