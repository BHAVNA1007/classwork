#09_direct_parent_call

class Person:

   def __init__(self, name):

      self.name = name

      print("person's constructor")

class Employee:

   def __init__(self, name, salary):
 
       Person.__init__(self, name)
  
       self.salary = salary

       print("Emp constructor is called")

obj = Employee("Bhavna", 900000) 
print(obj.name)
print(obj.salary)

'''

person's constructor
Emp constructor is called

'''
   