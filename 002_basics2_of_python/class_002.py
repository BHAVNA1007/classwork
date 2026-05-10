# Output in python: --means display the data to the user

print("hello")
print(123)
print(15.1)
print(True)


#we can print multiple values using , (comma)

name = "bhavna"
age = 25
print(name,age)

# separator : (sep) used to change or sepator between values

print(name,age,sep="->")
print(name,age,sep=",")

print("a","b","c", sep="\n")

# end : keyword argument of the print function. it tells          #  python what to print at the end of the output after all 
#  values are printed

print("helow", end="")
print("guys")

print("helow", end=" ")
print("guys")

print("hello\tguys")

name = "bhaa"
print("Name of a person is", name)

# (f or F) we can use both before the string is means this is # formated string evaluate the expression inside {}

print(f"name of a person is {name}")

age=25
print(f"age is {age + 1}")

name="Bhavna"
age=25

print(f"hello {name +' welcome '} your age is {age} ")

print(f"hello {name +" welcome "} your age is {age} ")

print(f"hello {name +''' welcome '''} your age is {age} ")

# print(f"hello {name} and {address}")
'''it will throw the
NameError:  name 'address' is not defined'''

# print(f"hello {name} and {}")
'''
    SyntaxError:   f-string: valid expression required before '}'   '''


# format mathod : replace the {} with the value of variable
age = 30
print("your age is {} your name is {}".format(age, name))





