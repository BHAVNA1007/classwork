#12_abs_class_with_abs_methods

from abc import ABC, abstractmethod

class Parent(ABC):
   def __init__(self, name, salary):
      self.name = name
      self.salary = salary

   @abstractmethod
   def display(self):
       pass

   @abstractmethod
   def display1(self):
       pass

class Child(Parent):
   def display(self):
       print("child.......")

class Child1(Child):
   def display1(self):
       print("child1.......")



c = Child1("abc", 123)
c.display()
c.display1()


  