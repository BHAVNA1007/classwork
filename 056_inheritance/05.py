#05

class Person:

   def show(self):
 
      print("Person's show method")

class Child(Person):

   def show(self):

      super().show()    # Calls Person.show()

      print("Child's show method")

c = Child()
c.show()

'''
Person's show method
Child's show method

'''