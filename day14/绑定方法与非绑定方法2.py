# -*- coding: utf-8 -*-
import settings
import hashlib
import time


class People:
    def __init__(self,name,age,sex):
        self.id = self.create_id()
        self.name = name
        self.age = age
        self.sex = sex

    def tell_info(self):#绑定到对象的方法
        print('Name:%s Age:%s Sex:%s'%(self.name,self.age,self.sex))
    @classmethod
    def from_cof(cls):

        obj =cls(
            settings.name,
            settings.age,
            settings.sex
        )
        return obj
    @staticmethod
    def create_id():
        m = hashlib.md5(str(time.time()).encode('utf-8'))
        return m.hexdigest()


# p = People('yc',18,'male')
# p = People(settings.name,settings.age,settings.sex)

#绑定给对象，就应该由对象调用，自动将对象本身当做第一个参数传入
# p.tell_info()#tell_info(p)

#绑定给类，就应该由类调用，自动将类本身当做第一个参数传入

# p = People.from_cof()
# p.tell_info()

#非绑定方法，不与类或对象绑定，谁都可以调用，没有自动传值一说
p1 =People('yc1',18,'male')
p2 = People('yc2',19,'male')

print(p1.id)
print(p2.id)

























