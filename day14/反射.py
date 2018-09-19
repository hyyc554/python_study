# -*- coding: utf-8 -*-
#反射：通过字符串映射到属性
# class People:
#     country = 'China'
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def talk(self):
#         print('%s is talking'%self.name)
#
# obj = People('yc',18)
# print(obj.name)#obj.__dict__('name')
# print(obj.talk)
# choice = input('>>>:')#choice = 'name'
# print(obj.choice)#print(obj.'name')

# print(hasattr(obj,'name'))  #obj.name#obj.__dic__['name']
# print(hasattr(obj,'talk'))  #obj.talk#obj.__dic__['talk']

# print(getattr(obj,'namexxxx',None))
# print(getattr(obj,'talk',None))
#
# setattr(obj,'sex','male')#obj.sex= 'male'
# print(obj.sex)
#
# delattr(obj,'age')  #del obj.age
# print(obj.__dict__)

# print(getattr(People,'country'))#People.country



#反射的应用
class Service:
    def run(self):
        while True:
            inp = input('>>>:').strip()  #cmd= get a.txt
            cmds = inp.split()  #cmds = ['get','a.txt]

            print(cmds)
            if hasattr(self,cmds[0]):
                func = getattr(self,cmds[0])
                func(cmds)

    def get(self,cmds):
        print('get....',cmds)

    def put(self,cmds):
        print('put...',cmds)

obj = Service()
obj.run()








