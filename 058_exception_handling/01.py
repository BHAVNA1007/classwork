#01  without handling
'''
print("welcome")

a = 10
b = 0
c = a/b

print(c)
print("rest of the code")
'''

'''
welcome
ZeroDivisionError: division by zero
'''

#with handling
'''
print("welcome")
try:
  a = 10
  b = 0
  c = a/b
  print(c)
except:
  print("do not give zero...")
print("rest of the code...") 
'''


'''
welcome
do not give zero...
rest of the code...
'''





print("welcome")
try:
  a = 10
  b = 2
  c = a/b
  print(c)
except:
  print("do not give zero...")
print("rest of the code...") 

'''
welcome
5.0
rest of the code...
'''

