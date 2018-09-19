# -*- coding: utf-8 -*-
#封装与扩展性


class Room:
    def __init__(self,name,owner,weight,length,height):
        self.name = name
        self.owner = owner

        self.__weigth = weight
        self.__length = length
        self.__height = height

    def tell_area(self):
        return self.__weigth*self.__length


r = Room('卫生间',"ALEX",10,10,10)
print(r.tell_area())

