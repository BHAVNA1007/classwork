#10_abs_exp

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
         pass

class Circul(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14*self.r*self.r

class Rectangle(Shape):
    def __init__(self, r):
        self.r = r

  
obj = Circul(5)
print(obj.area())   #78.5

#obj1 = Rectangle(6)
'''
TypeError: Can't instantiate abstract class Rectangle without an implementation for abstract method 'area'
'''


