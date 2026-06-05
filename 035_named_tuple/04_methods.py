from collections import namedtuple


#_fields

Student = namedtuple("Student",['rollno','name','marks'])
s1 = Student('121','deepika',99)
print(Student._fields)
print(s1._fields)

#_asdict()

Student = namedtuple("Student",['rollno','name','marks'])
s1 = Student('121','deepika',99)
print(s1._asdict())

#_replace()

Student = namedtuple("Student",['rollno','name','marks'])
s1 = Student('121','deepika',99)
print(s1)

s2 = s1._replace(marks = 30)

print(s1)
print(s2)

print(id(s1))
print(id(s2))


#_make()
Student = namedtuple("Student",['rollno','name','marks'])
data = [101,'deepika',77]
s1 = Student._make(data)
print(s1.rollno)
print(s1.name)
print(s1.marks)










