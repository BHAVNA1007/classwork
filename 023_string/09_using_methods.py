'''
09_using_methods

'''

pwd = input("Enter the password: ")

upr = 0
lwr = 0
digit = 0
space = 0
s_char = 0

i = 0

l = len(pwd)

while i < len(pwd) :
   ch = pwd[i]
   if ch.isupper():
      upr = 1
   elif ch.islower(): 
      lwr = 1
   elif ch.isdigit():
      digit = 1
   elif ch.isspace():
      space = 1
   else:
      s_char = 1

   i += 1

if l>=8 and l<=15 and lwr==1 and upr==1 and digit==1 and space==0 and s_char==1: 
    print("Valid Password")

else:
    print("Invalid password")
