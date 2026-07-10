#03_super_keyword

'''
syntax1 : super().methodname(arguments)

syntax2 : super().__init__(arguments)

'''

class Person:

   def __init__(self):

       print("Parent constructor is called")
'''
class Employee(Person):

   def __init__(self):

       print("Employee constructor is called")

emp = Employee() 

#Employee constructor is called
'''

class Employee(Person):

    def __init__(self):

        super().__init__()
        print("employee cons...")

emp = Employee()

'''
Parent constructor is called
employee cons...
'''

