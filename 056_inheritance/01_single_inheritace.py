#01_single_inheritace

class Parent:

    def fun1(self):
   
       print("this is parent")

class Child(Parent):

    def fun2(self):
    
        print("this is child")

obj = Child() 
obj.fun1()
obj.fun2()

'''
output:

this is parent
this is child
'''


class Person:
   def __init__(self, name):
      self.name = name

class Employee(Person):
   def showrole(self):
       print(self.name, "is a employee")

obj = Employee("Bhvan")
obj.showrole()

'''
output:

Bhvan is a employee
'''

        
        