#08_abstract_class

from abc import ABC, abstractmethod

class Bank(ABC):
    @abstractmethod
    def interest(self):
        pass

obj = Bank()
obj.interest()

'''
TypeError: Can't instantiate abstract class Bank without an implementation for abstract method 'interest'
'''