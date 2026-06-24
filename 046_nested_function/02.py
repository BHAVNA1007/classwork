####02


def outer():
   x = 10

   def inner():
      print("value of ", x)
   inner()
outer()
# value of  10
 
'''       
def outer():
   x = 10

   def inner():
      y = 20 
      print("value of ", x)
   inner()
   print(y)#NameError: name 'y' is not defined
outer()
'''

def outer():
   x = 10
   def inner():
      x = 20
      print("inner value  of ", x)
   inner()
   print("inside outer ",x)
outer()  

'''
inner value  of  20
inside outer  10
''' 

