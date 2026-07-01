#02

class Student:
   
   def set(self):
       print("set is called...")
       self.id = 101
       self.name = "deepika"
       self.address = "chennai"

   def display(self):
       print("display is called...")
       print("Id is: ", self.id)
       print("Name is: ", self.name)
       print("Address is: ", self.address)


s1 = Student()  #s1 is object of class Student
s1.set()
s1.display()


s2 = Student()  #s2 is object of class Student
s2.set()
s2.display()


'''
set is called...
display is called...
Id is:  101
Name is:  deepika
Address is:  chennai
set is called...
display is called...
Id is:  101
Name is:  deepika
Address is:  chennai
'''
 