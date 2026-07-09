#03_property_and_setter


class Employee:

    def __init__(self, salary):

        self.__salary = salary

    @property
    def salary(self):
        return self.__salary
  
    @salary.setter
    def salary(self, salary):
        self.__salary = salary


e = Employee(10000)
print(e.salary)      #10000

e.salary = 5555
print(e.salary)   #5555 (changes in salary)
   