#02_property_decorator

'''
#without property decorator
class Employee:

    def __init__(self, salary):

       self.__salary = salary

    def get_salary(self):
   
        return self.__salary 

    def set_salary(self, salary):
   
        self.__salary = salary

e = Employee(1000)
print(e.get_salary()) #10000
'''

#with property decorator

class Employee:

    def __init__(self, salary):
       self.__salary = salary
    
    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self):
        self.__salary = salary

e = Employee(10000)
print(e.salary)   #10000


