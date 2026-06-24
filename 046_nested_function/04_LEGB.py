###04

'''
#local
x = 100
def test():
  x = 10
  print("inside function", x)
test()
'''

'''
#global
x = 100
def outer():
   x = 90
   def test():
      print("inside function:",x)
   test()
outer()
print("x is: ",x)

#inside function: 90
#x is:  100
'''

'''
#builtin

def outer():
   def test():
       print("inside function")
       print(len([10,20,30]))
   test()
outer()  
'''




