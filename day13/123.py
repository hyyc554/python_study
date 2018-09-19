# -*- coding: utf-8 -*-
# print('\n'.join([''.join([('zyx-Love'[(x-y)%8]if((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3<=0 else' ')for x in range(-30,30)])for y in range(15,-15,-1)]))

# 作者：地球的外星人君
# 链接：https://zhuanlan.zhihu.com/p/28726375
# 来源：知乎
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
def cal(n):
   res= 1
   for i in range(n,0,-1):
       print(i)
       res = res*i
       print(res)
   return res

print(cal(7))