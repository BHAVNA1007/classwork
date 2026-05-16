'''
08_example_for_methods
'''

password = input("Enter the password: ")

upr = 0
lwr = 0
digit = 0
space = 0
s_ch = 0

i = 0

while i < len(password):
   ch = password[i]
   if ch>='A' and ch<='Z':
       upr = 1
   elif ch>='a' and ch<='z':
       lwr = 1 
   elif ch>='0' and ch<='9':
       digit = 1
   elif ch == " ":
       space = 1
   else:
       s_ch = 1
   i += 1

if len(password)>=8 and len(password)<=15 and upr==1 and lwr==1 and digit==1 and s_ch==1 and space==0:
   print("Valid password")

else:
   print("Invalid password") 