#03


print("welcome")

try: 
   print("try start")
   print(10/2)
   print("zero issue")
   x = int("xyz")
   print("try end")

except ZeroDivisionError:
   print("do not provide zero")

except ValueError:
   print("plz check integer value")
print("rest of the code...")

'''
welcome
try start
5.0
zero issue
plz check integer value
rest of the code...
'''


print("\n\n")




print("hiiiiii")
try: 
   print("try start")
   print(10/0)
   print("zero issue")
   x = int("10")
   print("try end")

except ZeroDivisionError:
   print("do not provide zero")

except ValueError:
   print("plz check integer value")

print("rest of the code...")

'''
hiiiiii
try start
do not provide zero
rest of the code...
'''


print("\n\n")



try:
  print("try...")
  print("hi"+5)
except TypeError:
  print("wrong operation...")
print("out of body")

'''
try...
wrong operation...
out of body
'''

print("\n\n")



try:
  l = [1,2,3,4]
  print(l[4])
except:
  print("plz check index...")
print('rest of code')

'''
plz check index...
rest of code
'''




print("\n\n")



try:
  d = {"a": 1}
  print("value: ", d["a"])
except:
  print("wrong plz check key existence")

#value:  1

print("\n\n")



try:
  d = {"a": 1}
  print("value: ", d["b"])
except:
  print("wrong plz check key existence")

#wrong plz check key existence


print("\n\n")



try:
   print(y)
except NameError:
   print("plz create variable ")

#plz create variable


print("\n\n")



try:
   import xyz
except ModuleNotFoundError:
   print("module name check")

#module name check


print("\n\n")



try:
   import math
   print("math module found")
except ModuleNotFoundError:
   print("module name check")

#math module found


print("\n\n")


import math
try:
   print(math.exp(1000000))

except  OverflowError:
   print("use small value...")

#use small value...



import math
try:
   print(math.exp(10))

except  OverflowError:
   print("use small value...")

 #22026.465794806718 


print("\n\n")

print("welcome")  
try:
   x = int(input("enter value: "))
   print(10/x)
   print("try end")

except Exception:  #parent
   print("some issue is there...")

except ValueError:   #child
   print("plz give me integer valuse...")

'''
welcome
enter value: 2
5.0
try end
'''

'''
welcome
enter value: 0
some issue is there...
'''

print("\n\n")

print("wel")
try:
   x = int(input("enter value: "))
   print(10/x)
   print("try end")

except ValueError:  #child
   print("plz give me integer valuse...")

except Exception:   #parent
   print("some issue is there...")

'''
wel
enter value: abc
plz give me integer valuse...
'''

print("\n\n")

 
print("welcome")
try:
   x = int(input("enter value: "))
   print(10/x)
   print("hi" + 5)
   print("try end")

except (ValueError, TypeError):
   print("plz give me integer valuse...")

except Exception:
   print("some issue is there...")

'''
welcome
enter value: 2
5.0
plz give me integer valuse...
'''


print("\n\n")


try:
   x = int(input("enter value: "))
   print(10/x)    #abc -> valueError
   print("hi" + 5)     
   print("try end")

except ValueError as v:
   print("plz give me integer valuse...", v)

'''
enter value: abc
plz give me integer valuse... invalid literal for int() with base 10: 'abc'
'''

try:
   x = int(input("enter value: "))
   print(10/x)    #0 -> valueError     
   print("try end")

except ZeroDivisionError as z:
   print("plz give me integer valuse...", z)

'''
plz give me integer valuse... division by zero
'''

try:
   print("hi" + 5)     #type error 
   print("try end")

except TypeError as t:
   print("plz give me integer valuse...", t)

'''
plz give me integer valuse... can only concatenate str (not "int") to str
'''


try:
   x = int(input("enter value: "))
   print(10/x)
   print("hi" + 5)
   print("try end")

except Exception as e:
   print("some issue is there...", e)

'''
enter value: 2
5.0
some issue is there... can only concatenate str (not "int") to str
'''

