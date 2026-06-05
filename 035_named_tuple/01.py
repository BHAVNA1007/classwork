#syntax 
#tuplename=namedtuple("Tuplenmae",['field1','field1',...])

from collections import namedtuple
student = namedtuple("student",['name','age','city'])
s1 = student("abc",24,"mumbai")
print(s1.name)
print(s1.age)
print(s1.city)

s2 = student("abcde",25,"dubai")
print(s2.name)
print(s2.age)
print(s2.city)