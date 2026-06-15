#05 keyword argument
'''
def hello(name, age):
    print("Name is ", name)
    print("age is ", age)
    
hello(age = 30, name="deepika")    
'''
'''
Name is  deepika
age is  30
'''
'''
def hello(name, age):
    print("Name is ", name)
    print("age is ", age)
    
hello(age = 30, "deepika")   
SyntaxError: positional argument follows keyword argument 
'''
def hello(name, age,address, salary):
    print("Name is ", name)
    print("age is ", age)
    print("address is", address)
    print("salary: ", salary)
    
hello( "deepika",30,address="chennai", salary=40000)    
'''
Name is  deepika
age is  30
Name is  deepika
age is  30
address is chennai
salary:  40000
'''

