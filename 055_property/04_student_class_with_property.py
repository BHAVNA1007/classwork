#04_student_class_with_property

'''
wap to create student class with rollno, name, and marks

'''

class Student:

   def __init__(self, rollno, name, marks):
      
       self.__rollno = rollno
       self.__name = name
       self.__marks = marks

   @property
   def rollno(self):
       return self.__rollno

   @rollno.setter
   def rollno(self, rollno):
       self.__rollno = rollno

   
   @property
   def name(self):
       return self.__name

   @name.setter
   def name(self, name):
       self.__name = name

   @property
   def marks(self):
       return self.__marks
   
   @marks.setter
   def marks(self, marks):
       self.__marks = marks

s = Student(101, "Bhavna", 90)

print(s.rollno)
print(s.name)
print(s.marks)

'''
output:
101
Bhavna
90
'''

#here we can modifies the data using setter

s.rollno = 102
s.name = "shikha"
s.marks = 100

print(s.rollno)
print(s.name)
print(s.marks)

'''
output:

102
shikha
100
'''


    
