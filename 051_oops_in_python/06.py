#06

class Student:
   
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        self.c = self.a + self.b 
   
    def display(self):
        return self.c 

s1 = Student(10, 20)
s1.add()
print(s1.display()) 