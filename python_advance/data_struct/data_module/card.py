import collections
from random import choice

"""
命名元组子类：只有属性，没有方法
"""
Card = collections.namedtuple("Card", ["rank", "suit"])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = "spades diamonds clubs hearts".split()

    def __init__(self):
        self._cards = [Card(rank, suit) for rank in self.ranks for suit in self.suits]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


"""测试子类"""


def test_card():
    beer_card = Card(7, "clubs")
    print(beer_card)

    desk = FrenchDeck()
    print(len(desk))

    """获取属性子类"""
    print(desk[0])
    print(desk[51])

    """获取随机纸牌"""
    print(choice(desk))
    print(choice(desk))
    print(choice(desk))

    """抽取顶上三张牌和最后四张"""
    print(desk[:3])
    print(desk[12::13])

    """迭代可迭代元素"""
    for card in desk:
        print(card)
    for card in reversed(desk):
        print(card)

    """in运算符，检查成员是否包含某元素，如果容器没有实现__contains__方法，则会对容器做一次顺序扫描"""
    print(Card("9", "clubs") in desk)
    print(Card("9", "club") in desk)


test_card()
