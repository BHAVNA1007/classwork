#09_abstract_method


from abc import ABC, abstractmethod

class Bank(ABC):
   @abstractmethod
   def interest(self):
       pass

class SBI(Bank):
   def interest(self):
 
      print("SBI interest 8.1")

'''

class HDFC():
    pass

obj = SBI()
obj.interest()  #SBI interest 8.1

'''
'''
obj1 = HDFC()
obj1.interest()

AttributeError: 'HDFC' object has no attribute 'interest'
'''

class HDFC():
    def add(self):
        print("added....")

obj1 = HDFC()
obj1.add()


