# -*- coding: utf-8 -*-
import hashlib
import time
class MySQL:

    def __init__(self,*avrgs):
        self.ID = MySQL.create_ID()
        if not avrgs:
            self.host,self.port = avrgs
        else:
            self.host,self.port = (123123,23123)



    @classmethod
    def create_ID(cls):
        hash = hashlib.md5()
        hash.update(str(time.time()).encode('utf-8'))
        return hash.hexdigest()
    