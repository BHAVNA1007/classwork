#04_method_channing_return_self

class Student:

    def __init__(self, name):
       
        self.name = name
        self.marks = 0

    def set_marks(self, marks):
        self.marks = marks
        return self

    def hello(self):
        print("hyyyyy", self.name)
        return self

    def display(self):
        print("marks: ", self.marks) 
        return self

s1 = Student("deepika")

s1.hello().set_marks(80).display()