#03_instance_var


class Student:

   def __init__(self, name, age):
  
       self.name = name
       self.age = age
    
s1 = Student("Bhavna", 25)
s2 = Student("Shikha", 33)

print(s1.name)
print(s2.name)

s1.name = "Deepika"

print(s1.name)

'''
Bhavna
Shikha
Deepika
'''