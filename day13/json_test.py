# -*- coding: utf-8 -*-

import json
data = {'a': 0, 'b': 1}
with open('123.json', 'w', encoding='utf-8') as fp:
    json.dump(data, fp)
