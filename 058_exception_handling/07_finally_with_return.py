#07_finally_with_return


def test():

   try:
     
       return "from try"

   finally:
 
       print("from finally")

print(test())

'''
from finally
from try
'''



def test1():

   try:
     
       return "from try"

   finally:
 
       return "from finally"

print(test1())
'''
from finally
'''



'''
print("welcome")
try:
   print("try")
print("rest of code")


#SyntaxError: expected 'except' or 'finally' block
'''
