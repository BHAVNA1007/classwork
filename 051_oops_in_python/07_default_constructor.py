#07_default_constructor

class Student:

    def __init__(self):
        
        print("default parameter...")

        self.name = "bhavna"

        self.age = 25 

    def display(self):

        print(f"name is {self.name} age is {self.age}")

s1 = Student()

s1.display()