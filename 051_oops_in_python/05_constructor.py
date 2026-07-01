#05_constructor

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
      
     
    def display(self):
        print(f"name is {self.name} and age is {self.age}")
    
s1 = Student("bhavna", 25)

s1.display()

