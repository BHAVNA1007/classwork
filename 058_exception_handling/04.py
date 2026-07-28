#04

try:
   x = int(input("enter value: "))
   print(10/x)
   print("try end")

except Exception as e:
   print("some issue is there...", e)

else:
   print("try block complitly runs...")

print("rest of the code")




#case 1
'''

enter value: 2
5.0
try end
try block complitly runs...
rest of the code

'''



#case 2

'''

enter value: 0
some issue is there... division by zero
rest of the code
'''
