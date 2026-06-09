#05_removing_elements
# pop()

student = {"name": "dipu", "age": 30, "city": "chennai"}
print(student)
print(student.pop('city'))
print(student)

'''
print(student.pop("address"))  #KeyError: 'address'

'''
# popitem()
student = {"name": "dipu", "age": 30, "city": "chennai"}

print(student.popitem())

print(student)

# all items pop in reverse 

student = {"name": "dipu", "age": 30, "city": "chennai"}
print(student)

while student:
    print(student.popitem()) 
    '''
    ('city', 'chennai')
    ('age', 30)
    ('name', 'dipu')
    '''
print(student)    #{}    
     
    
#  del     
student = {"name": "dipu", "age": 30, "city": "chennai"}
del student["age"]
print(student)    #{'name': 'dipu', 'city': 'chennai'}

'''
del student["address"]   #KeyError: 'address'
print(student)
'''
#safe way to delete any key in dictionary

student = {"name": "dipu", "age": 30, "city": "chennai"}

if "address" in student:
    del student["address"]
print(student)    


# delete entire dictionary

student = {"name": "dipu", "age": 30, "city": "chennai"}
del student    #delete the whole dictionary
'''print(student)  #NameError: name 'student' is not defined 
'''
# if we want to clear all keys values then:
# clear()

student = {"name": "dipu", "age": 30, "city": "chennai"}
student.clear()
print(student)    #{}











