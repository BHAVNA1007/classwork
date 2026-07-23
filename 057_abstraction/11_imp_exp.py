#11_imp_exp


from abc import ABC, abstractmethod

class Employee(ABC):
   def __init__(self, name, salary):
       self.name = name
       self.salary = salary

   @abstractmethod
   def calculatebonus(self):
       pass

 
   def display(self):
       print("Emp Name: ", self.name)
       print("Emp Salary: ", self.salary)

class Manager(Employee):
    def calculatebonus(self):
        bonus = self.salary*0.20
        print("Manager Bonus: ", bonus)

class Developer(Employee):
    def calculatebonus(self):
        bonus = self.salary *0.10
        print("Developer bonus: ", bonus)

obj1 = Manager("abc", 80000)
obj1.calculatebonus()
obj1.display()

obj2 = Developer("xyz", 50000)
obj2.calculatebonus()
obj2.display() 
        
   