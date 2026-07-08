#03_method_channing

#internal method calls

class Student:
   def __init__(self, name, marks):

      self.name = name
      self.marks = marks

   def displayname(self):
      print("Name: ",self.name)

   def displaymarks(self):
      print("Marks: ", self.marks)

   def displayall(self):
       self.displayname()
       self.displaymarks()

s1 = Student("deepika", 90)

s1.displayall()  
   