#07_constructors_in_multiple_inheritance

class Father:

   def __init__(self):

       print("Father constructor called")

class Mother:

   def __init__(self):
 
       print("Mother constructor called")


class Child(Father, Mother):

   def __init__(self):

      super().__init__()

      print("Child constructor...")

c = Child()

'''
Father constructor called
Child constructor...
'''