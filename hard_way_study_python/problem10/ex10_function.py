def break_words(stuff):
    """
    拆分单词
    """
    words = stuff.split(" ")

    return words


def sort_words(words):
    """
    排序单词
    """

    return sorted(words)


def print_first_word(words):
    """
    打印第一个单词后弹出它
    """
    word = words.pop(0)
    print(word)


def print_last_word(words):
    """
    打印最后一个单词后弹出它
    """
    word = words.pop(-1)
    print(word)


def sort_sentence(sentence):
    """
    接收一个完整的句子，并返回排序后的单词列表
    """
    words = break_words(sentence)

    return sort_words(words)


def print_first_and_last(sentence):
    """
    从句子中打印第一个和最后一个单词
    """
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)


def print_first_and_last_sorted(sentence):
    """
    排序句子后打印第一个单词和最后一个单词
    """
    words = sort_words(sentence)

    print_first_word(words)
    print_last_word(words)
