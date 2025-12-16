class Song(object):
    cheese = "fengmuxai"

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)


happy_bday = Song(
    [
        "Happy birthday to you",
        "I don't want to get sued",
        "So I'll stop right there",
    ]
)

bulls_on_parade = Song(
    [
        "They rally around the family",
        "With pockets full of shells",
    ]
)

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()

double_tigers = [
    "两只老虎",
    "两只老虎",
    "跑得快",
    "跑得快",
    "一只没有耳朵",
    "一只没有尾巴",
    "真奇怪",
    "真奇怪",
]

tiger = Song(double_tigers)
tiger.sing_me_a_song()
Song.cheese
