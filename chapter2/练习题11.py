# -*- coding: utf-8 -*-
import re
with open('retest.txt', 'r', encoding='utf-8') as re_file:
    f = re_file.read()
target = re.search('luffycity.com', f).group()
if target:
    print(target)
else:
    print('not found')
