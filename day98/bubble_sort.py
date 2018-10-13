# -*- coding: utf-8 -*-
from .list_build import list_builder
from .timer import timer


@timer
def bubble_sort(li):
    n = len(li)
    for i in range(n - 1):
        flag = True
        for j in range(n - i - 1):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
                flag = False
        if flag:
            return li
    return li


if __name__ == "__main__":
    li = list_builder(100)
    bubble_sort(li)
    print(li)
