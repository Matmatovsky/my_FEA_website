import sqlite3
from sqlite3 import Error

class myStats:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __repr__(self):
        return "I am just a class instance"
    
    def multiplication(self):
        return self.x*self.y*self.z




class_instance = myStats(2, 3.1, -1)
print(class_instance)
print(class_instance.multiplication())