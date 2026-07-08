#04_class_methods

class Student:

   college = "NIT"

   def __init__(self, name):

      self.name = name

   @classmethod

   def change_college(cls, new):

      cls.college = new

s1 = Student("deepika")

print(s1.name)

print(s1.college)

Student.change_college("IIT") 

print(s1.college)


'''

deepika
NIT
IIT

'''