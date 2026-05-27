#006_multiple_ele_updation
'''
#using slicing   list[start:end] = iterable

a = [10,20,30,40,50]
a[1:3] = [200,300]
print(a)

a=[1,2,3,4,5]
a[1:4]=[10,20]
print(a)
'''

'''
#updating list using slicing

a=[1,2,3,4,5,6]
print(id(a))
print(a)
a[:] =[10,20,30,40]
print(id(a))
print(a)
'''

'''
#updating list using loop

a=[1,2,3,4,5,8,9]
for i in range(len(a)):
    a[i] = a[i]*2
print(a)

#updating element based on user input

marks =[80,90,70]
index = int(input("enter the index:  "))
value = int(input("enter the value: "))
marks[index] = value
print(marks)
'''

'''
student =['deepika','rashmika','katappa']
marks =[40,50,60]
name =input('Enter the name: ')

if name in student:
   index = student.index(name)
   new_marks = int(input('Enter new marks: '))
   marks[index] = new_marks
   print(marks)

else:
   print('student not found')   

'''

'''
friend =['tina','kiya','siya','priya']
name=input("enter the name: ")
if name in friend:
   updated_n = name.capitalize()
   print(updated_n)

   updated_n = name.upper()
   print(updated_n)

else:
    print('name not found')
'''














