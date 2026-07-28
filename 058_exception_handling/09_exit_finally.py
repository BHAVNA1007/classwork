#09_exit_finally


import os

try:
   print("only try block executes")

   os._exit(0)

finally:

   print("finally block")  


'''
only try block executes

'''