#05_class_var

class Student:

    college = "IIT Delhi"

    def __init__(self, name):
        self.name = name

s1 = Student("Deepika")
s2 = Student("Virat")

print(s1.name)
print(s1.college)
print(s2.name)
print(s1.college)

Student.college = "IIT Indore"

print(s1.college)
print(s2.college)


'''
Deepika
IIT Delhi
Virat
IIT Delhi
IIT Indore
IIT Indore
'''


class Student:

   college = "IIT Delhi"

   def __init__(self, name, city):
        self.name = name
        self.city = city

s1 = Student("deepika","Chennai")
s2 = Student("Virat","Delhi")

print(s1.__dict__)
print(s2.__dict__)

s1.college = "SAIT"

print(s1.__dict__)
print(s2.__dict__)

print(s1.college)

'''
{'name': 'deepika', 'city': 'Chennai'}
{'name': 'Virat', 'city': 'Delhi'}
{'name': 'deepika', 'city': 'Chennai', 'college': 'SAIT'}
{'name': 'Virat', 'city': 'Delhi'}
SAIT
'''

