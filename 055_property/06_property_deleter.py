#06_property_deleter


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
   
   @name.deleter
   def name(self):
       del self.__name 

   @property
   def marks(self):
       return self.__marks
   
   @marks.setter
   def marks(self, marks):
       self.__marks = marks

   @marks.deleter
   def marks(self):
       del self.__marks

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


del s.name

'''
print(s.name)
now this line throw erorr:
AttributeError: 'Student' object has no attribute '_Student__name'. Did you mean: '_Student__marks'?

'''

del s.marks

'''
print(s.marks)

AttributeError: 'Student' object has no attribute '_Student__marks'
'''


