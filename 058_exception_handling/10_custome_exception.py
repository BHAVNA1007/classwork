#10_custome_exception 


class AgeError(Exception):
    pass

age = int(input("enter age: "))

if age < 18:

   raise AgeError("You are not eligible")

print("Eligible")


#case 1

'''
enter age: 20
Eligible
'''
