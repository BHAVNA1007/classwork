#03_overridding

'''
class Parent:
   def calculation(self):
      print("Parent claculation called")

class Child(Parent):
   def calculation(self):
      print("Child calculation called") 

obj1 = Child()
obj1.calculation()   #Child calculation called

'''



class Parent:
   def calculation(self):
      print("Parent claculation called")

class Child(Parent):
   def calculation(self):
      super().calculation()
      print("Child calculation called") 

obj1 = Child()
obj1.calculation()

'''
Parent claculation called
Child calculation called
'''

'''
obj2 = Parent()
obj2.calculation()
#Parent claculation called
'''