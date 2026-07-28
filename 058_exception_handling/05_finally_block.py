#05_finally_block


print("welcome")

try:
   print("try start")
   x = int(input("Enter x: "))
   print(10/x)
   print("try ends...")

except Exception as e:

   print("Error occure in try", e)

else:
    print("try complitely runs no error occure")

finally:
    print("I am always in running mode...")

print("rest of the code") 



#case 1
'''
welcome
try start
Enter x: 2
5.0
try ends...
try complitely runs no error occure
I am always in running mode...
rest of the code
'''


#case 2

'''
welcome
try start
Enter x: 0
Error occure in try division by zero
I am always in running mode...
rest of the code
'''