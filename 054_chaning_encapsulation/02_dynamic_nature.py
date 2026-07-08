#02_dynamic_nature

class Student:
 
     name = "deepika"

Student.age = 30

s1 = Student()

print(s1.name)

print(s1.age)

del  Student.age
'''
print(s1.age) 
AttributeError: 'Student' object has no attribute 'age'
'''

'''
del s1

print(s1.age)

NameError: name 's1' is not defined
'''
