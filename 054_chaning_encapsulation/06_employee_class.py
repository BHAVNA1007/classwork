#06_employee_class

"""
wap to create employee class which have id, name, and salary make it properly encapsulated.
"""

class Employee:

    def __init__(self, id, name, salary):
        self.__id = id
        self.__name = name
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        if salary > 1000:
           self.__salary = salary
        else:
           print("Invalid salary") 

    def get_name(self):
        return self.__name

    def set_name(self, name):
        if name.stip() != "":
           self.__name = name
        else:
           print("Invalid name")

    def get_id(self):
        return self.__id
    def set_id(self, id):
        self.__id = id

s1 = Employee(101, "Bhavna", 90000000)

print(s1.get_salary())
print(s1.get_id())
print(s1.get_name())

s1.set_salary(1000000000)   
print(s1.get_salary())      