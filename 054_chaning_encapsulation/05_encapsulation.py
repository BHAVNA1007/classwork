#05_encapsulation
'''
#public specifiers

class Student:

   def __init__(self, name):
    
       self.name = name 

s1 = Student("bhavna")
print(s1.name)
'''




'''
#protected (_variablename)

class Student:

    def __init__(self, name):
       
       self._name = name

s1 = Student("shikha")
print(s1._name)
'''



'''
#private

class Student:

    def __init__(self, name, salary):

        self.name = name
        self.__salary = salary

s1 = Student("deepika", 900000)
print(s1.name)
 

#print(s1.__salary)

AttributeError: 'Student' object has no attribute '__salary'

'''



# getter and setter


class Student:
    def __init__(self, name, salary):

        self.name = name
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary

s1 = Student("deep", 50000)

print(s1.name)

print(s1.get_salary())

s1.set_salary(10)# here salary not updated create new salary

print(s1.get_salary())


   
  



  

