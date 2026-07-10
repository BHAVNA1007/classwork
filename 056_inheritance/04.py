#04

class Person:

    def __init__(self, name, age, address):

        self.name = name
        self.age = age
        self.address = address
        print("Person con.. is called")

class Employee(Person):

    def __init__(self, name, age, address, salary):

        super().__init__(name, age, address)

        self.salary = salary
        
        print("Employee con.. is called")

emp = Employee("Bhavna", 25, "mumbai", 900000)

print(emp.name)
print(emp.age)
print(emp.address)
print(emp.salary)

'''
Person con.. is called
Employee con.. is called
Bhavna
25
mumbai
900000
'''

     