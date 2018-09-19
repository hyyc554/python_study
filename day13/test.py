# -*- coding: utf-8 -*-
#
# # import configparser,os
# #
# # f = configparser.ConfigParser()
# #
# # f.read('my.cnf')
# #
# # f.set('mysqld','default-time-zone','+00:00')
# # f.write(open('my.cnf','w'))
# import re
# obj = re.match('\d+', '123uuasf')
# if obj:
#     print(obj.group())
#
# data = {'132123': 2}
# import json
#
# with open('234.json','w',encoding='utf-8') as fp:
#     json.dump(data,fp)
import re
with open('index.html','r',encoding='utf-8') as fp:
    data  = fp.read()
a = re.findall('luffycity.com',data)
print(a)