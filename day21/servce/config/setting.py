# -*- coding: utf-8 -*-
from os import path
from os.path import join

BASE_DIR = path.dirname(path.dirname(path.abspath(__file__)))


def new_path(z, x=BASE_DIR, y='db'):
    return join(x, y, z)


DATA_BASE = {
    'share_path': new_path('share')
}
