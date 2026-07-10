#06_multiple_inheritance

class Father:

   def house(self):
 
       print("father has house")

   def laptop(self):
  
       print("Father has laptop") 

class Mother:

   def laptop(self):
  
       print("Mother has laptop") 



class Child(Father, Mother):

    def nothing(self):
  
       print("Child has nothing")
'''
father has house
Father has laptop
Child has nothing
'''



'''

class Child(Mother, Father):

    def nothing(self):
  
       print("Child has nothing")
'''

'''
father has house
Mother has laptop
Child has nothing
'''


c = Child()
c.house()
c.laptop()
c.nothing() 



