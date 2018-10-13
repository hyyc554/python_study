import random


def list_builder(length):
    li = list(range(length))
    random.shuffle(li)
    return li
