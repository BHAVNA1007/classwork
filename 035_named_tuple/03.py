from collections import namedtuple

Student = namedtuple("Student",['rollno','name','marks'])

n = int(input("Enter number of students: "))

students = []

for i in range(n):
   print("Enter details")
   r = int(input("Enter roll no: "))
   n = input("Enter name: ")
   m = int(input("Enter marks: "))
   students.append(Student(r,n,m)) 

print(students)


for s in students:
    print(s)

for s in students:
    print("roll: ",s.rollno)
    print("name: ",s.name)
    print("marks: ",s.marks)